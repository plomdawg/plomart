import flask
import plomart
import io
import os
import redis


app = flask.Flask(__name__)

# Get app IP and port from env vars, default to http://localhost:5000
APP_IP = os.environ.get("APP_IP", "127.0.0.1")
PORT = os.environ.get("PORT", 5000)

# Connect to the Redis server running in heroku
rd = redis.from_url(os.environ.get("REDIS_URL"))


@app.route('/favicon.ico')
def favicon():
    image_dir = os.path.join(app.root_path, 'static')
    return flask.send_from_directory(image_dir, 'favicon.ico', mimetype='image/x-icon')


@app.route('/')
def index():
    return flask.render_template("./index.html", count=rd.get("faces_generated"))


@app.route('/faces_generated')
def faces_generated():
    return int(rd.get("faces_generated"))


@app.route('/character.png')
def character():
    # Generate a random character
    image = plomart.create_random_character()

    # Create file-object in memory
    file_object = io.BytesIO()

    # Write PNG in file-object
    image.save(file_object, 'PNG')

    # Move to beginning of file so `send_file()` it will read from start
    file_object.seek(0)

    # Increment counter of faces generated
    faces_generated = rd.incr("faces_generated")

    return flask.send_file(file_object, mimetype='image/PNG')


if __name__ == "__main__":
    # Use waitress to serve the flask app so it's secure.
    from waitress import serve
    print(f"Running web app on http://{APP_IP}:{PORT}")
    serve(app, host="0.0.0.0", port=PORT)
