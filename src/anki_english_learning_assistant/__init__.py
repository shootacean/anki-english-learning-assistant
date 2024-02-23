import json
import urllib.request
import traceback

# Anki Connect
# https://ankiweb.net/shared/info/2055492159
# ANKI_CONNECT_URL = 'http://localhost:8765'
ANKI_CONNECT_URL = "http://host.docker.internal:8765"


class Anki:
    def __request(self, action, **params):
        return {"action": action, "params": params, "version": 6}

    def __invoke(self, action, **params):
        requestJson = json.dumps(self.__request(action, **params)).encode("utf-8")
        response = json.load(
            urllib.request.urlopen(
                urllib.request.Request(ANKI_CONNECT_URL, requestJson)
            )
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

    def create_deck(self, **params):
        return self.__invoke("createDeck", **params)

    def deck_names(self, **params):
        return self.__invoke("deckNames", **params)

    def add_note(self, **params):
        try:
            result = self.__invoke("addNote", **params)
        except Exception as e:
            if e.args == ("cannot create note because it is a duplicate",):
                print("WARNING: ノートが重複しています。")
            else:
                print(type(e.args))
                print(e.args)
                traceback.print_exc()
                raise e
        else:
            return result
