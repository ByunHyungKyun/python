
#세번째 문제
#출력할 구구단을 입력하시오

num1 = input("출력할 구구단을 입력하시오")
result = 0

for i in range(1,10):
    print(num1 +' * '+str(i)+' = '+str(int(num1)*i))

