from anki_english_learning_assistant import Anki
from pandas import read_csv

# TODO : Anki Connectが起動しているかのチェック

anki = Anki()

DECK_NAME = "anki-english-learning-assistant"

# Create deck
anki.create_deck(deck=DECK_NAME)

# Add note
result = anki.add_note(
    note={
        "deckName": DECK_NAME,
        "modelName": "Basic",
        "fields": {
            # English
            "Front": "apple",
            # Japanese
            "Back": "りんご",
        },
        "tags": [DECK_NAME],
    }
)

# Bulk insert by CSV
csv = read_csv("fruits.csv")
for i, row in csv.iterrows():
    result = anki.add_note(
        note={
            "deckName": DECK_NAME,
            "modelName": "Basic",
            "fields": {
                # English
                "Front": row["english"],
                # Japanese
                "Back": row["japanese"],
            },
            "tags": [DECK_NAME],
        }
    )
    print(result)
