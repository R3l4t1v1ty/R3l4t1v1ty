import typing
from typing import List
from typing import Optional
import math
import functools


class Trie:

    def __init__(self):
        self.value = None
        self.branches = [None]*27

    def insert(self, word: str) -> None:
        root = self
        for i in range(len(word)):
            ind = int(ord(word[i])-ord("a"))
            if root.branches[ind]:
                root = root.branches[ind]
            else:
                for j in range(i,len(word)):
                    ind = int(ord(word[j])-ord("a"))
                    root.branches[ind] = Trie()
                    root = root.branches[ind]
                break

        root.branches[26] = Trie()


    def search(self, word: str) -> bool:
        root = self
        for i in range(len(word)):
            root = root.branches[int(ord(word[i])-ord("a"))]
            if not root:
                return False
        if root.branches[26]:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        root = self
        for i in range(len(prefix)):
            root = root.branches[int(ord(prefix[i])-ord("a"))]
            if not root:
                return False
        return True


def main():
    obj = Trie()

    obj.insert("banana")
    print(obj.search("bana"))
    print(obj.startsWith("bana"))
    obj.insert("bandana")
    obj.insert("anaban")
    print(obj.search("bandana"))
    print(obj.startsWith("anana"))


    exit()

if __name__ == "__main__":
    main()