import flask
import plomart
import io
import os
import redis


app = flask.Flask(__name__)

# Get app IP and port from env vars, default to http://localhost:5000
APP_IP = os.environ.get("APP_IP", "127.0.0.1")
PORT = os.environ.get("PORT", 5000)

# Redis hostname is redis in the container.
redis_cache = redis.Redis(host='redis', port=6379)


@app.route('/favicon.ico')
def favicon():
    image_dir = os.path.join(app.root_path, 'static')
    return flask.send_from_directory(image_dir, 'favicon.ico', mimetype='image/x-icon')


@app.route('/faces_generated')
def faces_generated():
    if redis_cache is None:
        count = 0
    else:
        count = redis_cache.get("faces_generated")
        if count is None:
            count = 0
        else:
            count = count.decode('ascii')
    return count


@app.route('/')
def index():
    return flask.render_template("./index.html", count=faces_generated())


@app.route('/random_character.png')
def random_character():
    # Generate a random character
    image = plomart.create_random_character()

    # Create file-object in memory
    file_object = io.BytesIO()

    # Write PNG in file-object
    image.save(file_object, 'PNG')

    # Move to beginning of file so `send_file()` it will read from start
    file_object.seek(0)

    # Increment counter of faces generated
    redis_cache.incr("faces_generated")
    return flask.send_file(file_object, mimetype='image/PNG')


if __name__ == "__main__":
    # Use waitress to serve the flask app so it's secure.
    from waitress import serve
    print(f"Running web app on http://{APP_IP}:{PORT}")
    serve(app, host="0.0.0.0", port=PORT)
