# -*- coding: utf-8 -*-
"""Public forms."""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import BooleanField


class UploadForm(FlaskForm):
    file = FileField("File", validators=[FileRequired()])
    pos = BooleanField("Get PoS")
    lemmas = BooleanField("Lemmatization")
    deps = BooleanField("Dependency parsing")
    ner = BooleanField("NER")

    punct = BooleanField("Remove punctuation")
    spaces = BooleanField("Remove spaces")
    stop = BooleanField("Remove stopwords")
