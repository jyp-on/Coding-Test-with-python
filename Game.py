#캐릭터가 방문한 칸의 수 출력
n, m = map(int, input().split())

d = [[0] * m for _ in range(n)] #캐릭터가 맵을 방문했는지 확인하는 용도로 0으로 초기화한 맵 생성(방문 할 경우 1로 변경)

x, y, direction = map(int, input().split())
d[x][y] = 1 #현재좌표 방문처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

    # 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

#시뮬레이션 시작
count = 1 #캐릭터 생성위치 방문처리 했으므로 1부터 시작
turn_time = 0 
while True:
    #왼쪽회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0: #d[nx][ny] == 0 > 육지이고 array[nx][ny] == 0 > 안 가본 장소
        d[nx][ny] = 1 
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction] 
        if array[nx][ny] == 0: #뒤로 갈 수 있는 경우
            x = nx
            y = ny
        else:
            break #뒤가 막혀있는 경우 종료

        turn_time = 0 #뒤로 갈 경우 턴타임 0으로 초기화

print(count)

            
        




