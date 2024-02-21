import anki_english_learning_assistant as anki

# TODO : Anki Connectが起動しているかのチェック

# Create deck
anki.create_deck(deck="anki-english-learning-assistant")

# List decks
result = anki.deck_names()
print("got list of decks: {}".format(result))
