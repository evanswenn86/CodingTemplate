# 二叉树层次遍历

from collections import deque


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        if root is None:
            return []

        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

# 层次便利总模板
queue = deque()
seen = set()
# start 可以为任意数据结构，其为需要进行遍历的数据的头部数据
queue.append(start)
seen.add(start)
while len(queue):
    size = len(queue)

    for _ in range(size):
        head = queue.popleft()
        for neighbor in head.neighbors:
            if neighbor not in seen:
                seen.add(head.neighbor)
                queue.append(neighbor)

# 不分层遍历的总模板
queue = deque()
seen = set()

seen.add(start)
queue.append(start)

while queue:
    node = queue.popleft()
    for neighbor in node.neighbors:
        if neighbor not in seen:
            seen.add(neighbor)
            queue.append(neighbor)

# topology sort 模板
# 对于图中的任意两个结点u和v，若存在一条有向边从u指向v，则在拓扑排序中u一定出现在v前面。
#
# 拓扑排序主要用来解决有向图中的依赖解析（dependency resolution）问题。

class Solution:

    def topoSort(self, graph):
        node_to_indegree = self.getIndegree(graph)
        order = []
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        queue = deque(start_nodes)

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order


    def getIndegree(self, graph):
        node_to_indegree = {x: 0 for x in graph}

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1
        return node_to_indegree




