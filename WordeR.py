import itertools
import random
from sys import argv


def get_words(new_s, word_list, n=3):
    if not new_s:
        return word_list
    else:
        possibilities = [i for i in dictionary if all(new_s.count(b) >= i.count(b) for b in i)]
        y = 0
        x = len(possibilities)
        f = open('.\%s.txt' % new_s, 'w+')
        while x > y:
            w = possibilities[y]
            if len(w) >= n:
                print w
                f.write(str(y) + '. ' + w + '\n')
            y += 1
        f.close()
        if not possibilities:
            return get_words([], word_list)
        else:
            word = random.choice(possibilities)
            word_list.append(word)
            word_dict = {i: word.count(i) for i in word}
            new_final_word = list(
                itertools.chain.from_iterable([[a for i in range(abs(s.count(a) - b))] for a, b in word_dict.items()]))
            return get_words(new_final_word, word_list)


# final_words = get_words(s, [])
# print(final_words)


if __name__ == '__main__':
    dictionary = [i.strip('\n') for i in open('dictionary.txt')]
    # s = "EMASSE"
    s = (argv[1]).upper()
    n = int(argv[2])
    # print n
    final_words = get_words(s, [], n)
