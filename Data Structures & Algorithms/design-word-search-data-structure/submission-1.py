class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isWord = True

    def searchWildCard(self, word, index, curr):

        if index == len(word):
            return curr.isWord

        ch = word[index]

        if ch == ".":
            for child in curr.children.values():
                if self.searchWildCard(word, index + 1, child):
                    return True
            return False

        if ch not in curr.children:
            return False

        return self.searchWildCard(word, index + 1, curr.children[ch])

    def search(self, word: str) -> bool:
        return self.searchWildCard(word, 0, self.root)