# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

#     Trie() Initializes the trie object.
#     void insert(String word) Inserts the string word into the trie.
#     boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#     boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True

 

# Constraints:

#     1 <= word.length, prefix.length <= 2000
#     word and prefix consist only of lowercase English letters.
#     At most 3 * 104 calls in total will be made to insert, search, and startsWith.

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# i think maintaining 2 hashes is sloppy, but it makes membership checking faster
# the sheer amount of dictionaries this creates has to be a memory overhead nightmare
# i thought about an implementation with linked lists but a hashmap tree is really
# the only data structure that supports cheap accesses
class Trie:

    def __init__(self):
        self.prefixes = {}
        self.words = set()

    def insert(self, word: str) -> None:
        self.words.add(word)
        
        letter_dict = self.prefixes
        for char in word:
            letter_dict = letter_dict.setdefault(char,{})

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        letter_dict = self.prefixes

        for char in prefix:
            if char not in letter_dict:
                return False
            letter_dict = letter_dict[char]
        return True

a = Trie()
a.insert('test')
a.insert('two')
print(a.search('test'),a.startsWith('t'))
