class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False
    
    def __repr__(self) -> str:
        return f"children = {self.children} - is_end? {self.isEnd}"

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def __repr__(self) -> str:
        return f"{self.root}"
    
    def insert(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEnd = True 
    
    def contains(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isEnd
    
    def startsWith(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
    
    def printWordsR(self, curr=None, word='', words=[]):
        if curr is None: curr = self.root

        for char, children in curr.children.items():
            new_word = word + char
            if children.isEnd:
                words.append(new_word)
            self.printWordsR(children, new_word, words)

        return words
    
    def printWords(self):
        print(self.printWordsR())

    def find_substr(self, substr, curr=None):
        if curr is None: curr = self.root

        for char in substr:
            if char in curr.children:
                curr = curr.children[char]
            else:
                for child in curr.children.values():
                    if self.find_substr(substr, child): return True
                return False
        return True
    
    def find_sufix(self, sufix, curr):

        for i in range(len(sufix)):
            char = sufix[i]  
                
            if char in curr.children:
                curr = curr.children[char]
                if i == len(sufix)-1:
                    return curr.isEnd 
            else:
                for child in curr.children.values():
                    if self.find_sufix(sufix, child): return True
        return False
    
    def prefix_sufix(self, prefix, sufix):
        curr = self.root

        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else: return False
        return self.find_sufix(sufix, curr)
    
        
    



trie = Trie()
trie.insert("apple")
'''print(f"trie contains apple? {trie.contains("apple")}")
print(f"trie contains app? {trie.contains("app")}")
print(f"trie starts with app? {trie.startsWith("app")}")
print(f"trie starts with pp? {trie.startsWith("pp")}")'''
trie.insert("app")
#trie.insert("bye")
'''print(f"trie contains bye? {trie.contains("bye")}")
trie.printWords()
print(f"trie has substring pp? {trie.find_substr("pp")}")'''
trie.insert("agogo")
prefix = "a"
sufix = "gogo"
print(f"trie has prefix {prefix} and sufix {sufix}? {trie.prefix_sufix(prefix, sufix)}")
