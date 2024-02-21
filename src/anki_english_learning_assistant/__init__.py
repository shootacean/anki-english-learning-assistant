import json
import urllib.request

# Anki Connect
# https://ankiweb.net/shared/info/2055492159
# ANKI_CONNECT_URL = 'http://localhost:8765'
ANKI_CONNECT_URL = "http://host.docker.internal:8765"


def request(action, **params):
    return {"action": action, "params": params, "version": 6}


def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode("utf-8")
    response = json.load(
        urllib.request.urlopen(urllib.request.Request(ANKI_CONNECT_URL, requestJson))
    )
    if len(response) != 2:
        raise Exception("response has an unexpected number of fields")
    if "error" not in response:
        raise Exception("response is missing required error field")
    if "result" not in response:
        raise Exception("response is missing required result field")
    if response["error"] is not None:
        raise Exception(response["error"])
    return response["result"]
