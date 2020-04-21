# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node_map = {}
        def helper(node: 'Node')-> 'Node':
            if node:
                if node in node_map:
                    return node_map[node]
                else:
                    curr = Node(node.val,None,None)
                    node_map[node] = curr
                    curr.next = helper(node.next)
                    curr.random = helper(node.random)
                    return curr

            else:
                return None
        ans = helper(head)
        return ans