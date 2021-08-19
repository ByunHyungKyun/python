#두번째 문제
#첫숫자를 입력하시오
#끝숫자를 입력하시오
#첫숫자부터 끝수까지의 합은 x입니다

num1 = input("첫번째 숫자를 입력하시오")
num2 = input("두번째 숫자를 입력하시오")
result = 0

for i in range(int(num1),int(num2)+1):
    result += i

print(num1,"부터",num2,"까지의 합은 : ",result,"입니다")