class Trie:

    def __init__(self):
        self.words = {}

    def insert(self, word: str) -> None:
        letter_dict = self.words
        for char in word:
            letter_dict = letter_dict.setdefault(char,{})

    def search(self, word: str) -> bool:
        letter_dict = self.words
        for char in word:
            if char not in letter_dict:
                return false
            letter_dict = letter_dict[char]
        return True

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix)


a = Trie()
a.insert('test')
a.insert('two')
print(a.search('test'),a.startsWith('t'))