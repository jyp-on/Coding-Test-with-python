from random import randint
import time

array = []
for _ in range(10000):
    array.append(randint(1, 100))

#선택정렬 프로그램 성능 측정
start_time = time.time()

#선택정령 프로그램 소스코드
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #스와핑

end_time = time.time()
print("선택 정렬 성능 측정:", end_time-start_time)

#배열 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    array.append(randint(1, 100))

start_time = time.time()

array.sort()

end_time = time.time()

print("기본 정렬 라이브러리의 성능 측정:", end_time-start_time)



