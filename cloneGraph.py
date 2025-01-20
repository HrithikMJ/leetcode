# I couldn't wrap my head around this, initially i couldn't traverse it, then used dfs.
# i was stuck with using hashset and adding the node to it.
# I tried appending to the the neighbors but couldnt figure how to return the cloned node, then
# got a little help and used a dict instead, added new as value to old as key, then returned
# the new if it was available. else created a new Node and returned it

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        visited = {}

        def dfs(node):
            if not node:
                return
            if node in visited:
                return visited[node]
            temp = Node(node.val)
            visited[node] = temp
            for neighbor in node.neighbors:
                temp.neighbors.append(dfs(neighbor))
            return temp

        clone = dfs(node)
        return clone
