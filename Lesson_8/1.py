"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

import collections


class Node:
    __slots__ = 'left', 'right'
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

def make_haffman_tree(node, code=""):
    if type(node) is str:
        return {
            node: code
        }

    l, r = node.children()

    result = {}
    # 0 - налево, 1 - направо
    result.update(make_haffman_tree(l, code + "0"))
    result.update(make_haffman_tree(r, code + "1"))

    return result


string = "beep boop beer!"
print("Исходная строка: " + string)

tree = collections.Counter()
for letter in string:
    tree[letter] += 1

while len(tree) > 1:
    char1, count1 = tree.most_common()[-1]
    char2, count2 = tree.most_common()[-2]
    tree[char1] -= count1
    tree[char2] -= count2
    tree += collections.Counter()
    tree[Node(char1, char2)] += count1 + count2


code_table = make_haffman_tree(list(tree)[0])

coded = []
for char in string:
    coded.append(code_table[char])

print("Закодированная строка: %s" % "".join(coded))









