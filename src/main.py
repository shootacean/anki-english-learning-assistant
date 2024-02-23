from anki_english_learning_assistant import Anki

# TODO : Anki Connectが起動しているかのチェック

anki = Anki()

DECK_NAME = "anki-english-learning-assistant"

# Create deck
anki.create_deck(deck=DECK_NAME)

# List decks
result = anki.deck_names()
print("got list of decks: {}".format(result))

# Add note
result = anki.add_note(
    note={
        "deckName": DECK_NAME,
        "modelName": "Basic",
        "fields": {
            "Front": "Front content",
            "Back": "Back content",
        },
        "tags": [DECK_NAME],
    }
)
