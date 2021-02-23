#!/usr/bin/python
# (C) 2015 Muthiah Annamalai, <ezhillang@gmail.com>
#     Ezhil Language Foundation
#

import codecs
import operator
import sys

from ngram.LetterModels import Unigram, Bigram, Trigram

sys.stdout = codecs.getwriter("utf-8")(sys.stdout)


class TamilVUNgram:
    def __init__(self):
        self.filename = "tamilvu_dictionary_words.txt"
        self.unigram = Unigram(self.filename)
        self.unigram.frequency_model()
        print("--- completed Unigram model ---")
        self.bigram = Bigram(self.filename)
        self.bigram.language_model(verbose=False)
        self.trigram = Trigram(self.filename)
        self.trigram.language_model(verbose=False)

        print("--- completed Bigram,Trigram model ---")

    def save(self):
        # save letter2 of bigram
        # save letter of unigram
        with codecs.open("tvu_bigram.txt", "w", "utf-8") as fp:
            d = {}
            for k, v in list(self.bigram.letter2.items()):
                for k2, v2 in list(v.items()):
                    if v2 == 0:
                        continue
                    d[k + k2] = v2
            for k, v in sorted(
                list(d.items()), key=operator.itemgetter(1), reverse=True
            ):
                fp.write("%s - %d\n" % (k, v))

        with codecs.open("tvu_unigram.txt", "w", "utf-8") as fp:
            for k, v in sorted(
                list(self.unigram.letter.items()),
                key=operator.itemgetter(1),
                reverse=True,
            ):
                if v == 0:
                    continue
                fp.write("%s - %d\n" % (k, v))
        self.trigram.save("tvu_trigram.txt")
        print("SAVED tvu_unigram.txt, tvu_bigram.txt")


if __name__ == "__main__":
    tamildict = TamilVUNgram()
    tamildict.save()
