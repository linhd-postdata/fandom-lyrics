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
