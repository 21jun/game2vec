from data import db
import pandas as pd
import numpy as np
import re


def clean_text(text):
    t = re.sub('[^a-zA-Z0-9]', ' ', text).strip()
    t = re.sub(' +', ' ', t)
    return t


def load_comments_SQL():
    SQL = "SELECT gameName ,text FROM steam.yt_comment where filter=1;"
    df = db.to_df(SQL)

    comments = df['text'].apply(clean_text).str.split().to_numpy()
    gameName = df['gameName'].to_numpy()

    corpus = []
    for g, c in zip(gameName, comments):
        text = [g] + c
        corpus.append(text)

    return corpus
