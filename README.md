# Fandom lyrics Corpus (Spanish)


This corpus is a subset in JSON format of the available songs in [Fandom](https://lyrics.fandom.com/wiki/Category:Language/Spanish) (accessed on July 1st, 2020).

It containes more than 100 000 unannotated songs from over 6000 authors.

## Statistics

- Authors: 6178
- Works: 103585
- Stanzas: 701212
- Verses: 3451697
- Words: 20735344
- Characters: 120830774

The file [`fandom-lyrics.json`](./fandom-lyrics.json) contains the corpus. The format of each entry is as follows:

```json
{
    "author": "Amaral",
        "title": "¿Qué Será?",
        "text": [
            [
                "Yo soy la bala perdida",
                "Esta noche me voy a bailar",
                "Yo soy una viva la vida",
                "Pero siempre digo la verdad",
                "Si tú eres mi amigo",
                "Que más da ser chica o chico",
                "Si tú eres mi hermana",
                "Que más da ser negra o blanca"
            ],
            [
                "Chiqui chiqui chiquibum chiquibum"
            ],
        ...
    ]
},
```

Folder [`json`](./json) contains the works by author.

This repo is a dump of the website www.lyrics.fandom.com, we do not own the rights of any of the works pulished here.

For any violations or infringement of copyright, take proper action within the scope of the original website.