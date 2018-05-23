from Stack.linkedstack import LinkedStack


class PolindromADT:
    "Polindrom ADT read set of words, able to distinquish only polindroms and write them into the path-file."
    def __init__(self):
        self.words = []
        self.polindroms = []

    def process(self):
        "Filter only polindroms"
        self.polindroms = list(filter(PolindromADT._is_polindrom, self.words))

    def read(self, path, format=lambda x: x.strip()):
        "Read words to analyze from the path-file and take the format argument as function to format file string"
        with open(path, encoding='utf-8') as file:
            self.words = list(map(format, file.readlines()))

    def write(self, path):
        "Write polindroms into the path-file"
        with open(path, 'w', encoding='utf-8') as file:
            new_words = list(map(lambda x: x + '\n', self.polindroms))
            for i in new_words:
                file.write(i)

    @staticmethod
    def _is_polindrom(word):
        "Check if word is polindrom"
        stack = LinkedStack()
        iter = 0
        while iter != len(word) // 2:
            stack.push(word[iter].lower())
            iter += 1
        if (len(word) % 2):
            iter += 1
        while iter != len(word):
            if stack.pop() != word[iter]:
                return False
            iter += 1
        return True


if __name__ == '__main__':
    s = PolindromADT()
    s.read("base.lst", format=lambda x: x.split()[0])
    s.process()
    s.write('danylo.txt')
