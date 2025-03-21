"""
Functions for dealing with filepaths
"""

from collections import defaultdict
from pathlib import Path


def filetree_string(paths: list[Path]) -> str:
    """
    Returns a visual representation of the paths provided
    (very similar to linux package `tree`

    TODO: ChatGPT wrote this function and I haven't audited it properly yet
    """

    def build_tree(paths):
        tree = defaultdict(dict)
        for path in paths:
            parts = path.parts
            node = tree
            for part in parts[:-1]:
                node = node.setdefault(part, {})
            node[parts[-1]] = None  # Mark file nodes with None
        return tree

    def tree_to_string(node, prefix=""):
        result = ""
        for key, sub_node in sorted(node.items()):
            result += prefix + "├── " + key + "\n"
            if isinstance(sub_node, dict):
                result += tree_to_string(sub_node, prefix + "│   ")
        return result

    filetree = build_tree(paths)
    return tree_to_string(filetree)
