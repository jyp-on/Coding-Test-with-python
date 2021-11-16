from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
    #queue 구현을 위해 deque 라이브러리 사용
    queue = deque([start]) #시작노드 설정
    visited[start] = True   #현재노드 방문처리
    while queue:            #큐가 빌 때까지 반복
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)

