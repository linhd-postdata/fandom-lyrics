# About the corpora

Some of the corpora files are in the Apache Parquet format due to Github file size limit. To read these files from pandas just write:

```python
import pandas as pd

dataset = pd.read_parquet("path_to_file.parquet")
```

Some files are split into several chunks. In order to read all of them you must use the following code:

```python
import pandas as pd
from pathlib import Path

file_list = []
for path in Path("path_to_folder").glob("*.parquet"):
    df = pd.read_parquet(path)
    file_list.append(df)
total = pd.concat(file_list)
```

# Fandom lyrics Corpus (Spanish)

This corpus is a subset in JSON format of the available songs in [Fandom](https://lyrics.fandom.com/wiki/Category:Language/Spanish) (accessed on July 1st, 2020).

It containes more than 100 000 unannotated songs from over 6000 authors.

## Statistics

- Authors: 6178
- Works: 103585
- Stanzas: 701212
- Verses: 3451697
- Words: 19756294
- Characters: 99602951


The file [`fandom-lyrics.zip`](./fandom-lyrics.zip) contains the corpus. The format of each entry is as follows:

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

# Fandom lyrics Corpus (Spanish) + Spotify features

[`spotify_corpus.parquet`](./spotify_corpus.parquet)

This corpus is a subset of the Fandom lyrics corpus enriched with metadata obtained with the Spotify API.

It contains 76600 songs with different features annotated by Spotify. The complete list of features can be found at https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-audio-features/.

The features included are:

- **acousticness**

	A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
- **analysis_url**

	An HTTP URL to access the full audio analysis of this track. An access token is required to access this data.
- **danceability**

	Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
- **duration_ms**

	The duration of the track in milliseconds.
- **energy**

	Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
- **id**

	The Spotify ID for the track.
- **instrumentalness**

	Predicts whether a track contains no vocals. “Ooh” and “aah” sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly “vocal”. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
- **key**

	The key the track is in. Integers map to pitches using standard Pitch Class notation . E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on.
- **liveness**

	Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
- **loudness**

	The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.
- **mode**

	Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
- **speechiness**

	Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
- **tempo**

	The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
- **time_signature**

	An estimated overall time signature of a track. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure).
- **track_href**

	A link to the Web API endpoint providing full details of the track.
- **type**

	The object type: “audio_features”
- **uri**

	The Spotify URI for the track.
- **valence**

	A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).
- **genres**

	A list with the genres associated with the artist, retrieved from the spotify API. Some artists couldn't be found on the Spotify database.
- **n_verses**

	Number of verses of the song.
- **lengths**

	A list with the number of syllables each verse of the song has.

# Fandom lyrics Corpus (Spanish) + Spotify + Last.fm features

[`lastfm_corpus.parquet`](./lastfm_corpus.parquet)

This corpus is a subset of the Fandom lyrics + Spotify corpus enriched with metadata obtained with the LastFM API.

It contains 74838 songs with different features annotated by LastFM. The Lastfm annotations include:

- **top_tags**

	A list of the most common tags for each song (Some songs don't have any)
- **similar_songs_ids**

	A list of similar songs (according to LastFM) that are also on this dataset. 
- **similar_songs_scores**

	A list of the similarity scores (from 0 to 1) fro eacxh similar song. The order of the scores is the same as the order of the similar_songs_ids.
	

# Fandom lyrics Corpus (Spanish) + Rantanplan scansion

All previous corpora with scansion information obtained from [Rantanplan](https://github.com/linhd-postdata/rantanplan) can be found in [`rantanplan-data folder`](./rantanplan-data).

The features included are:

- **author**
- **title**
- **text**
- **scansion**
  
  First, Rantanplan will show a list of lines. Each line is then shown as two separate lists. 
  A list of tokens, and a list of "phonological groups" i.e., the phonological units that form a verse after synalephas and sinaereris are taken into account.
  
  At the verse level we find information about the verse itself, e.g.:
	
  + rhythm: Pattern of the unstressed (-) and stressed (+) syllable.
  + length: Proposed length for the verse.
  + rhyme: A letter code to match rhyming verses. 
	
  The complete list of features can be found at [rantanplan docs](https://github.com/linhd-postdata/rantanplan#output-example)

# LDA topics corpus

[`10topic-song.csv`](./10topic-song.csv)
- **topic**

	The topic id.
- **gamma**

	 topicmodels score for the document.
- **id**

	The song ID.

Through the many possible LDA implementations, we decided to use the package 
[topicmodels][topicmodels] (Grün and Hornik, 2011). This set of tools has several advantages: 
it is well documented, allows us to work inside tidyverse packages, specifically
developed for fast and efficient text mining in R, and counts with accompanying 
packages for creating graphs and evaluating the coherence of the resulting topics.

[topicmodels]: https://cran.r-project.org/web/packages/topicmodels/index.html

# Lyrics digital fingerprint


This corpus is the Sportify + LastFM dataset enriqued with rantaplan rhyme and stress, 
and columns calculated with [3-rhyme-groups](./notebooks/3-rhyme-groups.ipynb) and 
[4-lenght-groups](./notebooks/4-lenght-groups.ipynb) notebooks:
- **monorhyme**: 100 if poem is monorhyme, else 0
- **crossed_rhyme**: percentage of verses which ryhme is enclosed (abab)
- **enclosed_rhyme**: percentage of verses which ryhme is crossed (abba)
- **couplet**: percentage of verses which are couplets (aabbcc)
- **no_rhyme**: percentage of no rhyming verses
