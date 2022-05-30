import flask
import plomart
import io
import os

app = flask.Flask(__name__)

# Get app IP and port from env vars, default to http://localhost:5000
APP_IP = os.environ.get("APP_IP", "127.0.0.1")
PORT = os.environ.get("PORT", 5000)


@app.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/x-icon')


@app.route('/')
def index():
    return flask.render_template("./index.html")


@app.route('/image.png')
def character():
    # Generate a random character
    image = plomart.create_character()

    # Create file-object in memory
    file_object = io.BytesIO()

    # Write PNG in file-object
    image.save(file_object, 'PNG')

    # Move to beginning of file so `send_file()` it will read from start
    file_object.seek(0)

    return flask.send_file(file_object, mimetype='image/PNG')


if __name__ == "__main__":
    app.host = "0.0.0.0"
    app.port = PORT
    print(f"Running on port {PORT}")
    app.run()
