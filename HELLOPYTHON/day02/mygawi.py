import random
mine = input("가위,바위,보를 입력하시오");
com = ""
result = ""
rand = random.random()

if 0.3>=rand :
    com="가위"
elif 0.3<rand and rand <=0.6 :
    com="바위"
else :
    com="보"
    
if com == mine:
    result = "비김"
elif com == "가위" and mine == '보':
    result ="짐"
elif com == "가위" and mine == '바위':
    result ="이김"
elif com == "바위" and mine == '보':
    result ="이김"
elif com == "바위" and mine == '가위':
    result ="짐"
elif com == "보" and mine == '바위':
    result ="짐"
elif com == "보" and mine == '가위':
    result ="이김"
else :
    result ="입력값이 이상합니다."
    
print("com: ",com)
print("mine: ",mine)
print("result: ",result)    


















