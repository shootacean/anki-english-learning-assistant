# MEMO

## Anki Connectの疎通確認

```shell
$ curl localhost:8765 -X POST -d '{"action": "deckNames", "version": 6}'
```

## Anki Connect API

- [x] カードの追加方法

## Anki Data Structure

- Deck
    - Card
        - Due
- Note -> Card
    - Note Type
    - Field
    - ...

