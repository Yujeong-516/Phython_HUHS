from random import *
chicken = sample(id, 1)

id = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
#tip, 정수 여러개인 경우 range 사용이 편함
#id = range(1,21) 
#id = list(id) 변환 필요
id. remove(chicken)

id = list(id)
shuffle(id)
coffee = sample(id, 3)

print("-- 당첨자 발표 --")
print(f"치킨 당첨자: {chicken} ")
print(f"커피 당첨자: {coffee} ")
print("-- 축하합니다 --")

'''답안
form random inport *
id = range(1, 21)
id = list(id)

winners = sample(id, 4)
print("-- 당첨자 발표 --")
print(" 치킨 당첨자 : {0}". format(winners[0]))
print(" 치킨 당첨자 : {0}". format(winners[1:]))
print("-- 축하합니다 --")
'''