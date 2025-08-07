class TrieNode:
    def __init__(self):
        self.childen={}
        self.isEnd=False

class Trie:

    def __init__(self):
        self.root=TrieNode()
    def insert(self, word: str) -> None:
        node=self.root
        for ch in word:
            if ch not in node.childen:
                node.childen[ch]=TrieNode()
            node=node.childen[ch]
        node.isEnd=True
    def search(self, word: str) -> bool:
        node=self._findNode(word)
        return node is not None and node.isEnd
    def startsWith(self, prefix: str) -> bool:
        return self._findNode(prefix) is not None

    def _findNode(self,prefix:str)->TrieNode:
        node= self.root
        for ch in prefix:
            if ch not in node.childen:
                return None
            node=node.childen[ch]
        return node

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)