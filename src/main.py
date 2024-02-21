import anki_english_learning_assistant as anki

anki.invoke("createDeck", deck="anki-english-learning-assistant")
result = anki.invoke("deckNames")
print("got list of decks: {}".format(result))
