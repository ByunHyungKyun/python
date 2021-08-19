import random
mine = input("홀/짝을 선택하세요")

"""내가 한거 
print(mine)

a = random.random()


if a >= 0.5 and mine=='홀':
     print("컴퓨터는 홀 정답입니다.")
elif a >= 0.5 and mine=='짝':
    print("컴퓨터는 홀 오답입니다.")
elif a < 0.5 and mine=='홀':
    print("컴퓨터는 짝 오답입니다.")
elif a < 0.5 and mine=='짝':
    print("컴퓨터는 짝 정답입니다.")
"""

#선생님이랑 한거
com = ""
result = ""
rand = random.random()

if rand < 0.5:
    com = "홀"
else :
    com = "짝"

if mine == com:
    result = "이김"
else:
    result = "짐"

print("com: ",com)
print("mine: ",mine)
print("result: ",result)
































