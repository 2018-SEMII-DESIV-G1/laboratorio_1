class LetterCounter:
    alphabet = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0,
        'e': 0, 'f': 0, 'g': 0, 'h': 0,
        'i': 0, 'j': 0, 'k': 0, 'l': 0,
        'm': 0, 'n': 0, 'o': 0, 'p': 0,
        'q': 0, 'r': 0, 's': 0, 't': 0,
        'u': 0, 'v': 0, 'w': 0, 'x': 0,
        'y': 0, 'z': 0,
    }

    def __init__(self, s, *args, **kwargs):
        self.s = s

    def count_letters(self, *args, **kwargs):
        for c in self.s:
            self.alphabet[c] += 1
        return self.alphabet

    def print_counter(self, *args, **kwargs):
        for c in self.alphabet:
            if self.alphabet[c] > 0:
                print('La letra {} tiene {} apariciones.'.format(c, self.alphabet[c]))


def main():
    s = input('Introduzca la cadena a analizar: ')
    lc = LetterCounter(s)
    count_letters = lc.count_letters()
    lc.print_counter(count_letters)


if __name__ == '__main__':
    main()
