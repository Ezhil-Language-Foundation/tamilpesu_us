import random
import sys
from pathlib import Path

from gensim.models import KeyedVectors

BASEDIR = Path(__file__).parent


def realign_array(arr, fixed_length):
    diff = fixed_length - len(arr)
    if diff > 0:
        arr += [''] * diff
    elif diff < 0:
        arr = arr[:fixed_length]

    gap_size = fixed_length - 1

    aligned = [elem for pair in zip(arr, [''] * gap_size) for elem in pair]
    for i in range(1, len(aligned)):
        if aligned[i] == '' or len(aligned) == 0:
            aligned[i] = aligned[i - 1]
    return aligned

english_embedding = KeyedVectors.load(str(BASEDIR / 'models/english_embedding.kvmodel'))
kural_vocab_embedding = KeyedVectors.load(str(BASEDIR / 'models/kural_vocab_embedding.kvmodel'))

english_embeddings_keys_to_index = english_embedding.key_to_index
english_embedding_vector_values = english_embedding.vectors

def get_matching_kural( input_sentence ):
    sen = get_sentence_tokens_after_stopword_removal(input_sentence)

    generated = []

    loop = 0

    while len(generated) < 7:
        for s in sen:
            if s in english_embeddings_keys_to_index:
                your_word_vector = english_embedding_vector_values[english_embeddings_keys_to_index[s]]

                if len(generated) == 6:
                    g_arr = kural_vocab_embedding.most_similar(positive=[your_word_vector], topn=100)
                    for g in g_arr:
                        if len(g[0]) < 7 and g[0] not in generated:
                            generated.append(g[0])
                            break
                    break

                g = kural_vocab_embedding.most_similar(positive=[your_word_vector], topn=3)
                if g[0][0] in generated:
                    choosed = random.choice(g)[0]
                    count = 0
                    while choosed in generated:
                        if count > len(g): break
                        count += 1
                        choosed = random.choice(g)[0]
                    generated.append(choosed)
                else:
                    generated.append(g[0][0])
                if len(generated) == 7:
                    break
        random.shuffle(sen)
        loop += 1
        if loop > 100:
            print("Please try to avoid invalid words, and use less stop words")
            break

    return [" ".join(generated[0:4]), " ".join(generated[4:])]

def main():
    if len(sys.argv) < 2:
        print("Given input english sentence as argument")
        exit(-1)

    input_sentence = sys.argv[1]
    result_kural = get_matching_kural( input_sentence )
    print(result_kural[0])
    print(result_kural[1])

def get_sentence_tokens_after_stopword_removal(input_sentence):
    stop_words_replacements = {
        "is": "same",
        "and": "other",
        "i": "self",
        "i am": "self",
        "will": "future",
        "you": "person",
        "some": "few",
        "my": "own",
        "me": "self",
        "in": "from"
    }
    given_sentence = input_sentence.lower()
    sen = []
    for word in given_sentence.split(" "):
        if word in stop_words_replacements:
            sen.append(stop_words_replacements[word])
        else:
            sen.append(word)
    sen = [ii for n, ii in enumerate(sen) if ii not in sen[:n]]
    if len(sen) < 7:
        sen = realign_array(sen, 7)
    return sen


if __name__ == '__main__':
    main()
