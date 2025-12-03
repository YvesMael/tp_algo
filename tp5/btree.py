from __future__ import annotations
from dataclasses import dataclass
from collections.abc import Iterator


@dataclass
class BinaryTree:
    """
    A binary tree is a tree data structure in which each node has at most two children,
    which are referred to as the left child and the right child.

    The BinaryTree class is a dataclass with a single field, root, which is a reference to the root node of the tree.

    The Node class is a nested dataclass with three fields: key, left, and right.
    The key field is an integer that stores the value of the node.
    The left and right fields are references to the left and right children of the node, respectively.

    Example:
        >>> bt = BinaryTree(Node(2, Node(1, Node(0)), Node(4, Node(3), Node(5))))
    """
    root: Node | None = None


@dataclass
class Node:
    key: int
    left: Node | None = None       # "Or None" for terminal nodes
    right: Node | None = None


def bt_is_empty(bt: BinaryTree) -> bool:
    if bt.root: return False
    else: return True

def bt_root(bt: BinaryTree) -> Node:
    if bt_is_empty(bt): raise ValueError
    else: return bt.root

def bt_iter_dfs(n: Node) -> Iterator[Node]:
    if n:
        for ng in bt_iter_dfs(n.left): yield ng
        yield n
        for nd in bt_iter_dfs(n.right): yield nd
    else: pass

def bt_iter_bfs(n: Node) -> Iterator[Node]:    
    liste = [n] if n else []
    while len(liste)>0:
        n= liste.pop(0)
        yield n
        if n.left: liste.append(n.left)
        if n.right: liste.append(n.right)

def bt_height(bt: BinaryTree) -> int:
    def rec(noeud:Node)->int:
        if noeud is None: return -1
        return 1 + max(rec(noeud.left),rec(noeud.right))
    return rec(bt.root) 

def bt_size(bt: BinaryTree) -> int:
    def rec(noeud:Node)->int:
        if noeud is None: return 0
        return 1 + rec(noeud.left),rec(noeud.right)
    return rec(bt.root) 

def bt_str(bt: BinaryTree) -> str:
    raise NotImplementedError("bt_str function not implemented yet")


def bt_new(nodes: list[int | None] | None = None) -> BinaryTree:
    raise NotImplementedError("bt_new function not implemented yet")


def bt_is_bst(bt: BinaryTree) -> bool:
    raise NotImplementedError("bt_is_bst function not implemented yet")


def bt_is_heap(bt: BinaryTree) -> bool:
    raise NotImplementedError("bt_is_heap function not implemented yet")


def bt_lca(bt: BinaryTree, a: int, b: int) -> int:
    raise NotImplementedError("bt_lca function not implemented yet")


def bt_prettystr(bt: BinaryTree) -> str:
    raise NotImplementedError("bt_prettystr function not implemented yet")


if __name__ == '__main__':
    a = BinaryTree(Node(0, Node(1, Node(3), Node(4)), Node(2, Node(5), Node(6))))