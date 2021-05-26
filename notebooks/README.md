# Notebooks

This folder contains Jupyter notebooks. Naming convention is a number(for ordering) 
and a short `-` delimited description, e.g. `0-initial-data-exploration`.

*  [1-add-rantanplan-scansion](./1-add-rantanplan-scansion.ipynb) adds a new `scansion` column to [plain_lyrics_dataset.csv.zip](../plain_lyrics_dataset.csv.zip)
   and saves it into [rantanplan-data](../rantanplan-data) folder. 
   The scansion information has been obtained using the [rantanplan](https://github.com/linhd-postdata/rantanplan) library.
   Result dataframe is divided into several files due to Github file size limits.
   

*  [2-filter-scansion-info](./2-filter-scansion-info.ipynb) reads all files from [rantanplan-data](../rantanplan-data) folder
   and adds `rhyme` and `stress` keys to columns. Result is saved into [rhyme-stress](../rantanplan-data/rhyme-stress)
   folder. 
   

*  [3-rhyme-groups](./3-rhyme-groups.ipynb) reads `rhyme` column and generate five new columns: 
      - **monorhyme**: 100 if poem is monorhyme, else 0
      - **crossed_rhyme**: percentage of verses which ryhme is enclosed (abab)
      - **enclosed_rhyme**: percentage of verses which ryhme is crossed (abba)
      - **couplet**: percentage of verses which are couplets (aabbcc)
      - **no_rhyme**: percentage of no rhyming verses
   Result is saved into [spotify-rhyme-groups.parquet](../../spotify-rhyme-groups.parquet)
   folder.


*  [4-lenght-groups](./4-lenght-groups.ipynb) reads `stress` column and generate five new columns: 
      - **arte_menor**: verses with less than 8 syllables
      - **octosílabo**: verses with 8 syllables
      - **enea_decasílabo**: verses with 8 or 9 syllables
      - **endecasílabo**: percentage of verses which are couplets (aabbcc)
      - **arte_mayor**: percentage of no rhyming verses

*  [5-merge](./5-merge.ipynb) creates [`lyrics_digital_fingerprint.parquet`](../lyrics_digital_fingerprint.parquet) file
   by merging lyrics, spotify, rantanplan and topics information.
   
*  [6-subset](./6-subset.ipynb) generates a random subset for ElasticSearch experiments.

*  [7-LDA_no_stopwords_no_lemmas](7-LDA_no_stopwords_no_lemmas.ipynb) applies [Latent Dirichlet Allocation (LDA)](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) 
   from [gensim library](https://radimrehurek.com/gensim/models/ldamodel.html#module-gensim.models.ldamodel) to the corpus and saves the model into [`ldamodels`](../ldamodels) folder.
   Text preprocessing: 
      - Remove stopwords
      - Remove punctuation
      - Remove spaces
   