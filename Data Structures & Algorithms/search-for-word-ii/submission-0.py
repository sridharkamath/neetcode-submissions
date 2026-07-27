class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None


class Solution:

    def __init__(self):
        self.root = TrieNode()
        self.result = []

    def addWord(self, word):

        curr = self.root

        for ch in word:

            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]

        curr.isWord = True
        curr.word = word

    def dfs(self, r, c, node):

        # Out of bounds
        if (
            r < 0 or
            c < 0 or
            r >= self.rows or
            c >= self.cols
        ):
            return

        ch = self.board[r][c]

        # Already visited
        if ch == "#":
            return

        # Current path is not a valid prefix
        if ch not in node.children:
            return

        # Move one level down the Trie
        node = node.children[ch]

        # Found a complete word
        if node.isWord:
            self.result.append(node.word)

            # Prevent duplicates
            node.isWord = False

        # Mark current cell as visited
        self.board[r][c] = "#"

        # Explore all four directions
        self.dfs(r + 1, c, node)
        self.dfs(r - 1, c, node)
        self.dfs(r, c + 1, node)
        self.dfs(r, c - 1, node)

        # Backtrack
        self.board[r][c] = ch

    def findWords(self, board, words):

        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

        self.result = []

        # Build Trie
        for word in words:
            self.addWord(word)

        # Start DFS from every cell
        for r in range(self.rows):
            for c in range(self.cols):
                self.dfs(r, c, self.root)

        return self.result