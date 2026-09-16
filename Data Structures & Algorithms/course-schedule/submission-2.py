class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # 0 = unvisited, 1 = visiting (in current DFS path), 2 = fully processed
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False  # cycle detected
            if state[course] == 2:
                return True   # already confirmed safe

            state[course] = 1
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True