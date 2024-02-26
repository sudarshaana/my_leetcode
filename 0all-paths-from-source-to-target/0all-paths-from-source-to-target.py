class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph)-1
        result = []

        def path_finder(current, path):
            if current == target:
                result.append(path[:])
                return

            for node in graph[current]:
                path.append(node)
                path_finder(node, path)
                path.pop()

        path = [0]
        path_finder(0, path)
        return result