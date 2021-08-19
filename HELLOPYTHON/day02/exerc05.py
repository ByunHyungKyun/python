
#다섯번째 문제
#첫글자를 입력
#끝글자를 입력
# 홀수의 합은 ?입니다

num1 = input("첫번째 숫자를 입력하시오")
num2 = input("두번째 숫자를 입력하시오")
result = 0

for i in range(int(num1),int(num2)+1):
    if i%2 == 1:
        result += i
    elif i == 1:
        result += i
        
print(num1,"부터",num2,"까지의 합은 :",result,"입니다")


