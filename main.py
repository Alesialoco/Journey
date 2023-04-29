import flask

app = flask.Flask(__name__)


@app.route('/')
def render_map():
    return flask.render_template("map.html")


@app.route('/help')
def render_help():
    return flask.render_template("help.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')