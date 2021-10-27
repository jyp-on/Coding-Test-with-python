input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
 #아스키코드 > 숫자 변환 함수를 이용하여 알파벳 입렵값 변환


steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

result = 0
for step in steps:
    next_row = row + step[0]    
    next_column = column + step[1]
    if next_row<=8 and next_column<=8 and next_row>=1 and next_column>=1:
        result += 1

print(result)
