import string


class WordsFinder:
    def __init__(self, *files):
        self.file_names = files
        self.all_words = None

    def get_all_words(self):
        if self.all_words is not None:
            return self.all_words

        all_words = {}
        for filename in self.file_names:
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                punctuation_chars = string.punctuation + '«»—'
                for punctuation in punctuation_chars:
                    text = text.replace(punctuation, ' ')
                words = text.split()
                all_words[filename] = words

        self.all_words = all_words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        results = {}
        word = word.lower()
        for filename, words in all_words.items():
            try:
                index = words.index(word)
            except ValueError:
                index = None
            results[filename] = index
        return results

    def count(self, word):
        all_words = self.get_all_words()
        results = {}
        word = word.lower()
        for filename, words in all_words.items():
            cnt = words.count(word)
            results[filename] = cnt
        return results


# Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
