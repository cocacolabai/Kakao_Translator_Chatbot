import flask
from papago import papago

app = flask.Flask(__name__)


@app.route("/param", methods=["POST"])
def param():

    req = flask.request.get_json()
    global lang_from
    lang_from = req['value']['origin']
    global lang_to
    lang_to = req['value']['origin']
    print(req)


@app.route("/translate", methods=["POST"])
def translate():

    req = flask.request.get_json()

    txt = req['userRequest']['utterance']
    req['contexts'][0]['lifespan'] = 1
    lang_from = req['contexts'][0]['params']['대상언어']['value']
    lang_to = req['contexts'][0]['params']['번역언어']['value']

    ret = papago(txt, lang_from, lang_to)

    print(req)
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": ret
                    }
                }
            ]
        }
    }
    print(res)
    return flask.jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

