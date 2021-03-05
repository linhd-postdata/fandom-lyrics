# -*- coding: utf-8 -*-
"""Spacy utilities and decorators."""
import spacy
from spacy_affixes import AffixesMatcher
from spacy_affixes.utils import AFFIXES_SUFFIX
from spacy_affixes.utils import load_affixes

nlp = spacy.load("es_core_news_md")
suffixes = {k: v for k, v in load_affixes().items() if
            k.startswith(AFFIXES_SUFFIX)}
affixes_matcher = AffixesMatcher(nlp, split_on=["VERB", "AUX"],
                                 rules=suffixes)
nlp.add_pipe(affixes_matcher, name="affixes", first=True)


def clear_pipeline(pipe_names: list) -> None:
    global nlp
    for pipe in pipe_names:
        if nlp.has_pipe(pipe):
            nlp.remove_pipe(pipe)


def remove_stopwords(doc):
    """English stopwords from: https://gist.github.com/sebleier/554280
    Spanish stopwords from spacy"""
    # comentario eleccion stopwords nltk, spacy o las que cargue el user
    doc = [token for token in doc if not token.is_stop]
    return doc


def remove_punct(doc):
    # print lista punct
    doc = [token for token in doc if not token.is_punct]
    return doc


def filter_pos(doc, allowed_pos):
    """Available PoS categories: https://universaldependencies.org/docs/u/pos/"""
    doc = [token for token in doc if token.pos_ in allowed_pos]
    return doc


def remove_spaces(doc):
    doc = [token for token in doc if not token.is_space]
    return doc


def clean_df(df=None, pos_output=False, rm_stopwords=False,
             get_lemmas=False, rm_punct=False, rm_spaces=False,
             allowed_pos=None, get_deps=False, get_ner=False):
    global nlp
    df['ner'] = [[(ent.text, ent.label_) for ent in doc.ents] for
                 doc in list(nlp.pipe(df["text"]))] if get_ner else None
    nlp.add_pipe(remove_stopwords, name="stopwords") if rm_stopwords else None
    nlp.add_pipe(remove_punct, name="punct") if rm_punct else None
    nlp.add_pipe(remove_spaces, name="spaces") if rm_spaces else None
    nlp.add_pipe(filter_pos, name="filter_pos") if allowed_pos else None
    df['tokens'] = list(nlp.pipe(df["text"]))
    df['pos'] = [[token.pos_ for token in doc] for doc in
                 df['tokens']] if pos_output else None
    df['deps'] = [[token.dep_ for token in doc] for doc in
                  df['tokens']] if get_deps else None
    df['lemmas'] = [[token.lemma_ for token in doc] for doc in
                    df['tokens']] if get_lemmas else None
    clear_pipeline(['stopwords', 'punct', 'spaces', 'filter_pos'])
    return df
