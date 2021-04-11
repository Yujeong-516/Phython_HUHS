from random import *
passenger = range(1, 51)
all_board = 0
for order in passenger:
    time = randint(5, 50)
    if 5 <= time <= 15:
        print(f"[O] {order}번째 손님 (소요시간: {time}분)") 
        all_board += 1 
    else:
        print(f"[ ] {order}번째 손님 (소요시간: {time}분)") 
print(f"총 탑승 승객: {all_board} 분")