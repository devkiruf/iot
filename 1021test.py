"""
ja = int(input("분자 값을 입력하시오: "))
mo = int(input("분모 값을 입력하시오: "))

mok = ja // mo
na = ja % mo 
print(f"나눗셈 몫= {mok}")
print(f"나눗셈 나머지= {na}")

hwa = int(input("화씨온도를 입력하시오")) 
sub = float((hwa - 32.0) / 1.8)
print(f"입력하신 화씨온도 {hwa:,.2f}도는 섭씨온도로 {sub:,.2f}도 이다.")
"""
'''
won = int(input("환전하고 싶은 원화를 입력하시오:"))
dal = won / 1196.00
print(f"환전하고 싶은 원화 {won:,}원은 US 달러로 $ {dal:,.2f} 이다")
'''
"""
up = int(input("윗변(cm) : "))
down = int(input("밑변(cm) : "))
height = int(input("높이(cm) : "))
ada = (up + down) * height / 2
print(f"사다리꼴의 넓이 : {ada}")
"""
"""
a = int(input("수 넣어 ㅅㅂ: "))

print("%x" %a)

print(13^8)
"""


"""
a = int(input("어떤 수 : "))

#print(f"2진수:{bin(a)}, 8진수:{oct(a)}, 10진수:{a}, 16진수:{hex(a)}")

print(format("{:#b}" .format(a)))
print(format(a,'o'))
print(format(a))
print(format(a,'x')) 

"""

"""

a = int(input("어떤 수 : "))
print(format(a,'b'))

#print(format("{:#b}" .format(a))) 

print("%o" %a)
print(a)
print("%x" %a)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
"""
"""
a = int(input("어떤 수: "))
b = int(input("왼쪽 쉬프트 값"))
print(f"왼쪽 쉬프트 {a} << {b} = {a * 2**3}")
"""
"""
a = int(input("판별 할 숫자를 입력하시오 : "))
if a % 2 == 0:
    print("당신이 입력한 숫자는 짝수입니다")
else:
    print("당신이 입력한 숫자는 홀수입니다")
"""
"""
a = float(input("학점을 입력하시오 : "))

if a >= 4:
    if a <= 4.5:
        print("장학금 신청 가능")
    else:
        print("제대로 된 값을 입력하세요")
elif a < 1:
    print("제대로 된 값을 입력하시오")
else:
    print("장학금 신청 불가능")
"""
"""
hwal = input("컴퓨터 활용 자격증 유뮤 (Y/N)")
grade = input("몇학년")

if hwal == "Y":
    if grade == "4":
        print("응시 지원 대상자임")
    else:
        print("응시 지원 대상자가 아님")
else:
    print("응시 지원 대상자가 아님")
"""
"""
name = input("이름을 입력하시오")
kg = float(input("체중을 입력하시오..: "))
cm = float(input("키를 입력하시오..: "))
m = cm / 100
bmi = kg / m **2
bmi_name = []
if bmi > 20:
    if bmi > 29:
        bmi_name = "비만"
    elif bmi >= 25:
        bmi_name = "과체중"
    else:
        bmi_name = "정상"
else:
    bmi_name = "저체중"

print(f"{name}님의 BMI 결과는 키:{cm} cm, 체중:{kg} kg, BMI 지수:{bmi:,.2f}이며, 판정은 {bmi_name}이다.")
"""
"""
ju_basics = 910
gong_basics = 1600
san_basics = 7300
ju_per = 88
gong_per = 182
san_per = 275
a = int(input("사용하시는 전력용도를 말해주세요 (1 : 주택용, 2 : 공업용, 3 : 산업용)"))
b = int(input("사용한 전기량을 입력해주세요"))
if a > 0:
    if a == 2:
        gong_ussed = gong_basics + (gong_per * b)
        print(f"용도:2, 사용량: {b:.2f}, 전기요금: , {gong_ussed:,.2f}원")
    elif a == 3:
        san_used = san_basics + (san_per * b)
        print(f"용도:3, 사용량:{b:.2f}, 전기요금: , {san_used:,.2f}원")
    elif a == 1:
        ju_used = ju_basics + (ju_per * b)
        print(f"용도:1, 사용량:{b:.2f}, 전기요금: , {ju_used:,.2f}원")
    else:
        print(f"잘못된 값을 입력하셨습니다")
else:
    print(f"잘못된 값을 입력하셨습니다")
"""
"""
sum = 0
a = int(input("어떤 정수 ? : ")) # 117 진단문제 
i = 0
for i in range (1, a, 2):
    sum = sum + i
print(f"1에서 {a}까지 홀수의 합 = {sum}")
"""
"""
i = 0
hol = 0
jjac = 0
for i in range(3):
    i = i+1
    a = int(input("어떤 수? : "))
    if a % 2 == 0:
        print(f"{a}는 짝수")
        jjac += 1
    else:
        print(f"{a}는 홀수")
        hol += 1
print(f"홀수의 개수는 {hol}개 이고 짝수의 개수는 {jjac}개 이다.")
"""

"""
zoo = ["rabbit", "goat", "tiger", "lion", "giraffe", "zebra"]

while True:
    animal = input("내가 좋아하는 동물은? (영문으로): ")
    if animal in zoo:
        print(f"{animal}은(는) 동물원에 있습니다")
        break
    else:
        print(f"{animal}은(는) 동물원에 없습니다")
        continue
"""
"""
zoo = ["rabbit", "goat", "tiger", "lion", "giraffe", "zebra"]
cnt = 0
while True:
    cnt = cnt + 1
"""
"""
cnt = 0
while cnt < 5:
    cnt = cnt + 1
    print(str("Python Program") + str(f" {cnt}번 출력"))
"""
"""
cnt = 0
while cnt < 5:
    print(str(f"{cnt}번 ")+str("Python Programming"))
    cnt = cnt + 1
a = int(input("계산하고 싶은 팩토리얼: "))
i = 0
sum = 0
while i > a:
    sum = a * (a-i)
    
print(sum)
"""
"""
a = ['a', 'b', 'c', 'd', 'e']
for i in a:
    print(i, end="")
"""


"""
i = 0
while i<3:
    i = i+1
    print("{}".format(i), end="")
"""
"""
a = int(input("계산하고 싶은 팩토리얼 : "))
sum = 1
while a > 0:
    sum *= a
    a -= 1
print(sum)
"""
#p136 챕 6 수행
"""
i = 0
sum = 0 
while i < 5:
    a = int(input("판별 할 숫자를 입력하시오..: "))
    i += 1
    if a % 2 == 0:
        sum += 1
    else:
        continue
print(f"짝수의 개수는 {sum}개 입니다")
"""
"""
grade = [90,85,70,60,95]
i = 0
jum = 0
for jum in grade:
    i += 1
    if jum >= 90:
        print(f"{i}번 학생 {jum}점 :  장학금 대상 입니다.")
    else:
        print(f"{i}번 학생 {jum}점 : 장학금 대상이 아닙니다.")
"""
"""
i = 0
while True:
    if i < 3:
        print("파이썬 프로그래밍!!")
        i += 1
    else:
        break
"""
"""
name = ["홍길동", "강감찬", "이순신"]
i = ""
for i in name:
    print(f"{i} 씨 반갑습니다.")

"""

#137p 5번은 len() 함수를 꼭 알아야 함!! 

"""
animal = ["dog", "duck", "pony", "donkey", "giraffe", "elephant", "cat"]
i = 0
for i in animal:
    if len(i) < 5:
        print(i)
    else:
        continue
"""

"""name = "KOREA"
cnt = 0
while cnt < len(name):
    print(name[cnt])
    cnt += 1"""

"""
print("구구단을 실행합니다!!")
for i in range(1,10,1):
    for j in range(2,10,1):
        print(f"{str(j)} * {str(i)} = {str(j * i)}", end="\t")
    print()
"""
"""
i = 0
while i < 10:
    gugu = int(input("계산하실 구구단을 입력하시오..: "))
    if gugu != 0:
        for i in range(1,10,1):
            print(f"{gugu} * {i} = {gugu * i}", end="\t")
            continue
        print()
    else:
        print("제대로 된 값을 입력하세요~")
        break
"""

"""
for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(i, end="")
    print()
"""  
"""
1
22
333
4444
55555
"""



"""
for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(j, end="")
    print()    
"""
    
"""
1
12
123
1234
12345
"""
"""
for i in range(5,0,-1):
    for j in range(1,i+1,1):
        print(i, end="")
        i -= 1
    print()    
"""

"""
54321
4321
321
21
1
"""

#146p 
"""
number = 0
sum = 0
while True:
    number = int(input("숫자를 입력해주세요..: "))
    if number != 0:
        sum = sum + number
    else:
        print(sum)
"""


#7장 피피티

"""
number = int(input("숫자 입력: "))         
i = 0


for i in range(number):
    print(i, end=" ")
    if i == 5:
        break
"""

#zoo = ["사슴", "호랑이", "사자", "표범", "기린", "코알라"]
"""
animal = 0
cnt = 0
while True:
    animal = input("내가 좋아하는 동물은?: ")
    cnt += 1
    if animal == "코알라":
        print(f"{cnt}회만에 정답을 맞추셨습니다.")
        break
    else:
        continue        
"""
"""
i = 0

while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=" ")
"""

"""

i = 0
num = [15,23,42,50,22,31,1]
for i in num:
    if i % 2 == 1:
        print(f"{i}", end=" ")
    elif i % 2 == 0:
        pass
    else:
        continue
            
"""
"""
i = 0
sum = 0
number = 0
for i in range(5):
    number = int(input("어떤 수? : "))
    if number > 0:
        sum = number + sum
    else:
        pass 
print(f"양수 정수의 합계 : {sum}")
"""
"""
i = 0
sum = 0
number = 0

for i in range(5):
    number = int(input("계산 할 숫자: "))
    if number != 3:
        sum = number + sum
        print(number)
    else:
        continue
print(sum)
"""
"""
num = [1,2,3,4,5]

for i in num:
    if i == 4:
        print(f"해당 항목 블럭 {i}")
        print(i)
        continue
    else:
        print(i)
"""
"""

for i in range(0,4,1):
    for j in range(0,4,1):
        if j / 2 == 1:
            continue
        else:
            print(f"{i} {j}")
"""
"""
is_prime = True
while(True):
    num = int(input("숫자 입력 : "))
    if num < 2:
        print("소수가 아닙니다")
        break
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
        else:
            is_prime = True
            break
    if is_prime = True:
        print("소수입니다")
    else:
        print("소수가 아닙니다:)                                              
"""






"""

for i in range(5):
    for j in range(5-i+1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()
"""
"""
오른쪽 12345 층 계단
"""
"""
for i in range(0,6,1):
    for j in range(0,i,1):
        print(" ", end="")
    for j in range(5-i):
        print("*", end="
    
    *
"""
"""
for i in range(0,6):
    for j in range(0,i):
        print(" ", end="")
    for j in range(1,6-i):
        print(j, end="")
    print()
"""
"""
12345
 1234
  123
   12
    1
"""




"""

for i in range(5,0,-1):
    for j in range(5-i):
        print(" ", end="")
    for j in range(0,i,1):
        print(j+1, end="")
    print()
"""

"""
for i in range(0,6):
    for j in range(0,i):
        print(" ", end="")
    for j in range(1,6-i):
        print(j+i, end="")
    print()  
"""
#157p 8번


#157p 9번

"""
for i in range(5):
    for j in range(5-i+1):
        print(" ", end="")
    for j in range(i+1):
        print(j+1, end="")
    print()
"""
