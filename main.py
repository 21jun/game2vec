from data import loader
from model.word2vec import Game2Vec


if __name__ == "__main__":

    corpus = loader.load_comments_SQL()
    game2vec = Game2Vec(corpus=corpus, size=100, window=5, min_count=5,
                        workers=16, iter=3, sg=1)

    print(game2vec.model["Good"])
