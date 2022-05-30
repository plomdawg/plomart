import flask
import plomart
import io
import os


app = flask.Flask(__name__)

# Get app IP and port from env vars, default to http://localhost:5000
APP_IP = os.environ.get("APP_IP", "127.0.0.1")
PORT = os.environ.get("PORT", 5000)

# Check if we have a Redis server to run (heroku runs Redis app)
rd = None
redis_url = os.environ.get("REDIS_URL")
if redis_url is not None:
    import redis
    rd = redis.from_url(redis_url)


@app.route('/favicon.ico')
def favicon():
    image_dir = os.path.join(app.root_path, 'static')
    return flask.send_from_directory(image_dir, 'favicon.ico', mimetype='image/x-icon')


@app.route('/')
def index():
    if rd is None:
        count = "0"
    else:
        count = rd.get("faces_generated").decode('ascii')
    return flask.render_template("./index.html", count=count)


@app.route('/faces_generated')
def faces_generated():
    if rd is None:
        return 0
    else:
        return rd.get("faces_generated").decode('ascii')


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
    if rd is None:
        faces_generated = 0
    else:
        faces_generated = rd.incr("faces_generated")

    return flask.send_file(file_object, mimetype='image/PNG')


if __name__ == "__main__":
    # Use waitress to serve the flask app so it's secure.
    from waitress import serve
    print(f"Running web app on http://{APP_IP}:{PORT}")
    serve(app, host="0.0.0.0", port=PORT)
