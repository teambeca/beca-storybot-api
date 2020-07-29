import json
from gevent.pywsgi import WSGIServer
from flask import Flask, request, abort, make_response, jsonify

# ----------------------------------------------------------------------------------------------------------------------
app = Flask(__name__)

# Pass : >\qP.%hcB:{ZP;wD+JJ;5@+B
TOKEN = "$2y$12$aTLjWAe7XUIZC8jFNoytQuATo4MfZH9iM2LjDDhle7ZJlWIspBvYG"


# ----------------------------------------------------------------------------------------------------------------------
def _check_token():
    token = request.headers.get("token")
    if token is None:
        return False

    if token.__eq__("Token " + TOKEN):
        return True
    else:
        return False


def _get_json():
    try:
        json_data = request.get_json()
    except:
        return None

    if json_data is None:
        return None
    elif not "message" in json_data:
        return None
    elif not "size" in json_data:
        json_data["size"] = 500
    return json_data


def _predict(message, size=500):
    print("")


@app.route('/', methods=["POST"])
def matching():
    if not _check_token():
        abort(make_response(jsonify(message="Authentication error"), 401))

    json_data = _get_json()
    if json_data is None:
        abort(make_response(jsonify(message="The body is not valid"), 404))

    # TODO: call _predict
    # TODO: return


if __name__ == '__main__':
    app_server = WSGIServer(('', 5041), app)
    app_server.serve_forever()
