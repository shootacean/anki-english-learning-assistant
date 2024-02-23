from anki_english_learning_assistant import Anki

# TODO : Anki Connectが起動しているかのチェック

anki = Anki()

# Create deck
anki.create_deck(deck="anki-english-learning-assistant")

# List decks
result = anki.deck_names()
print("got list of decks: {}".format(result))

# TODO : add note
