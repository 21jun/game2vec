from gensim.models import Word2Vec


class Game2Vec:
    def __init__(self, corpus, size, window, min_count, workers, iter, sg):
        self.model = Word2Vec(corpus, size=size,
                              window=window, min_count=min_count, workers=workers, iter=iter, sg=sg)

    def save(self, path="word2vec.model"):
        self.model.save(path)
