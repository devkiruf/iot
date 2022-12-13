"""tot = 0
def sig(n):
    n = int(input("계산하실 숫자를 입력하시오"))
    for i in range(0,n+1):
        global tot
        tot = i + tot
    print(tot)
sig(100)


total = 0
def hap(n):
    global total
    for i in range(1,n+1,1):
        total += i
    return total

num = int(input("숫자 입력"))
result = hap(num)
print(f"1-{num}까지의 합계:{result}")
"""
"""

def plus(n):
    sum = 0
    for i in range(1,n+1,1):
        sum += i

num = int(input("숫자 입력"))
plus(num)


"""
"""
cnt = 0
def countNum():
    global cnt
    cnt += 1

countNum()
countNum()
countNum()
print("카운트=",cnt)"""
"""
apple = 10
def eatApple(n):
    global apple
    n = int(input("먹고싶은 사과의 갯수는??...:"))
    apple -= n

eatApple(apple)
eatApple(apple)
eatApple(apple)
print("남은 사과의 개수= ", apple)"""
"""
listString = ["1","2","3"]
listNum=list(map(int,listString))
print(listNum)
"""
"""
city = ["seoul","pusan","jeju"]
def tupStr(city):
    city.upper()
    return city.upper()
uprCity = tuple(map(tupStr,city))

print(uprCity)"""
'''
last = ["김","홍","이"]
first = ["유신","길동","순신"]
name = list(zip(last,first))
print(name)'''


"""
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

num = int(input("숫자"))
print("{}!={}".format(num,fact(num)))"""
"""
def powerNum(x,y):
    if y<1 :
        return 1
    else:
        return x*powerNum(x,(y-1))
    
num1, num2 = map(int, input("숫자1,숫자2:").split(','))
print("{}**{}={}".format(num1,num2,powerNum(num1, num2)))"""


"""
try:
    num1=int(input("숫자를 입력해주세요."))
    num2=int(input("숫자를 입력해주세요."))
    num=num1 // num2
    na = num1 % num2
    print("{} / {} = {} ..... {}".format(num1 , num2 , num, na))

except ZeroDivisionError: # 에러일 때 출력
    print("숫자는 0으로 나눌 수 없습니다.")
    exit(1)

else: # 정상출력일 때 만 출력
    print("계산 결과가 정상적으로 출력되었습니다.")

finally: # 에러 상관 없이 출력
    print("저는 정상일 때 또는 에러일 때 무조건 출력됩니다.")"""

"""
listStr = ["python","programming","seoul","korean","university"]

try:
    number = int(input("출력하고자 하는 인덱스 번호를 입력해주십시오"))
    print(listStr[number])
    print(f"{listStr[number]} 의 글자 개수는 {len(listStr[number])}")
except:
    print("인덱스 번호를 초과하셨습니다")
    exit(1)"""
"""

f = open("c:\\python\\sample.txt", "r", encoding="utf-8")
print(f.read())

f.readlines()"""


"""try : 
    f = open("c:\\python\\sample.txt", "r", encoding="utf-8")
    aa = f.readlines()
    for i in aa:
        print(i, end="")

except FileNotFoundError:
    print("파일을 열지 못했습니다.")
    exit(1)"""

"""
try:
    cnt = 0
    f = open("c:\\python\\sam.txt", "r", encoding="utf-8")
    while cnt < 5:
        aa = f.readline(cnt)
        cnt += 1
        print(aa)
except FileNotFoundError:
    print("파일을 열지 못했습니다.")
    exit(1)"""

"""
try:
    f = open("c:\\python\\score.txt", "r", encoding="utf-8")
    score = f.readlines()
    sum = 0
    average = 0
    for i in score:
        print(i)
        sum += int(i)
    average = float(sum/len(score))
    print("총합은 = {}".format(sum))
    print("평균은 = {:.2f}".format(average))
except FileNotFoundError:
    print("파일을 열지 못했습니다.")
    exit(1)
f.close()
"""


"""
try:
    f = open("c:\\python\\gugudan.txt", "w", encoding="utf-8")
    gugu = int(input("원하는 구구단 :"))
    for i in range(1,10,1):
        f.write("{}*{}={}\n".format(gugu,i,(gugu*i)))

except FileNotFoundError:
    print("파일을 열지 못했습니다.")
    exit(1)
f.close()"""
"""
try:
    r = open("c:\\python\\flower_r.txt", "r", encoding="utf-8")
    w = open("c:\\python\\flower_w.txt", "w", encoding="utf-8")

    aa = r.readlines()
    for i in aa:
        w.write(i.upper())
    
except FileNotFoundError:
    print("파일을 열지 못했습니다.")
    exit(1)

r.close()
w.close()"""

"""
try:
    aw = open("c:\\python\\animal.txt", "w", encoding="utf-8")
    for i in range(5):
        bb = input("기입하실 동물의 이름을 말씀해주세요")
        aw.write(bb + "\n")


except FileNotFoundError:
    print("파일을 열지 못했습니다.")
    exit(1)
"""
"""
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1&s2
s4 = s1^s2
s5 = s1-s2
s6 = s1|s2"""



"""
num = [1,1,3,3,2,1,5,1,4,2,3,5]
newNum = set(num)
print(newNum)
listNum = list(newNum)
print(listNum)
"""

"""
num = {"one","two","three"}
num.update(["four","five","six"])
print(num)"""

"""
animal = ("병아리", "오리", "강아지","오리","거위","송아지","오리","암탉")
cnt = 0
for i in animal:
    if i == "오리":
        cnt += 1
    else:
        pass
print("오리 항목 개수:{}".format(cnt))
"""
"""
animal = ("병아리", "오리", "강아지","오리","거위","송아지","오리","암탉")
newAnimal = list(animal)
newAnimal.insert(0,"얼룩소")
newAnimal.append("염소")
lastAniaml = tuple(newAnimal)
print(lastAniaml)
"""
"""
animal = ("얼룩소","병아리", "오리", "강아지","오리","거위","송아지","오리","암탉","염소")
newAnimal = sorted(set(animal), reverse=True)
print(newAnimal)
"""
"""
num = [5,6,1,1,4,4,3,3,4,4,2,5]
newNum = sorted(set(num), reverse=False)
print(newNum)
"""
"""
inputData = [("Java", 15000),("Python", 25000),("C", 18000),("Java",19000)]
newData = set(inputData)
for i,j in newData:
    print(i,j)"""
"""
print("영화제목\t예매율\t순위\t")
print("========\t======\t====")

cnt = 0
movie_list = [("오징어게임",50.45),("이터널스",35.46),("그레비티",9.8),("노타임투다이",52.5),("스파이더맨",15.47)]
newMovie = dict(movie_list)
movie = sorted(newMovie.items(), key=lambda x:x[1], reverse=True)

for i,j in movie:
  cnt += 1
  print("{}\t{}\t{}".format(i,j,cnt))"""
"""
a = int(input("어떤 수 ? "))
sum = 0
for i in range(1,a+1):
    sum += i
    print(i)
print("1-{}까지 합계={}".format(a,sum))
"""
"""
def hap(num):
    hap = 0
    for i in num:
        print(i)
        hap+=i
    print("합={}".format(hap))

num=[1,2,3,4,5]
hap(num)"""

"""
a = int(input("씨발을 반복 할 횟수는 ??"))
for i in range(1,a):
    print("시발 집에 보내줘 추워 시발")
"""
"""
def printArgs(*args):
    print(type(args))
    for i in args:
        print(i)
printArgs("나는","배고파","뭐 먹지","진짜 배고파","배고파")

"""
"""
def nameAge(**kwargs):
    print(type(kwargs))
    for i,j in kwargs.items():
        print(f"{i} : {j}")
nameAge(key="김훈",values="20살")"""
"""
def myFunction(code):
    if code == 2022100775:
        password = int(input("비밀번호를 입력하시오 , (숫자만)..: "))
        if password == 12383399 :
            return "학번: {}는 우리학교 학생입니다.".format(code)
        else:
            return "우리 학교가 아니네? 꺼져 시발련아."

code = int(input("학교 코드 : "))
result = myFunction(code)
print(result)
"""
"""
def namePrinter(name):
    return "{}님, 환영합니다.".format(name)

name = input("이름:")
print(namePrinter(name))"""
"""
import math
x = 2.4214
y = -2.12312

print(math.ceil(x))
print(math.ceil(y))
print(math.floor(x))
print(math.floor(y))
print(math.trunc(x))
print(math.trunc(y))
print(math.sqrt(100))
print(math.sqrt(4))
print(math.factorial(5))
print(pow(x,y))
print(round(x))
print(round(y))
print(abs(x))
print(abs(y))
print(divmod(15,3))
print(divmod(13.0 , 2.0))
print(15,2)
"""
"""
num = [123,324,656,124,536,745,235,645,768,548,788]
print("최소값 : {} & 최대값 : {}".format(min(num), max(num)))
print(sum(num))"""
"""
import statistics
num1 = [7,5,2,6,7]
print(statistics.mean(num1))
num2 = [3.5,6.2,7.8]
print(statistics.fmean(num2))
#이지 버전
print(sum(num1)/len(num1))
"""

"""
str = "나는 섹스가 존나 하고싶다 섹스는 여러가지 의미로 섹스라고 할 수 있는데 일단 섹스의 장점은 섹스하면 너무 기분좋고 기분이 마치 섹스다"
print(str.count("섹스"))"""
"""
print(chr(65),chr(97))
print(ord('a'),ord('A'))
str = "sex sex sex"
print(str.find('s'))"""
"""
str = "python programming"
print(str.index("o"))
print(str.index("o",7,18))"""
"""
num = [15,25,33,17,88,25]
sum = 0
def sums() :
    global sum
    for i in num:
        print(i, end=" ")
        sum += i
    print(f"합계:{sum}")
sums()"""
"""
sum = 1
def fact() :
    global sum
    num = int(input("숫자 입력: "))
    for i in range(1,num+1):
        sum *= i
    print("합계:",sum)
fact()"""

"""
def asci() :
    num = eval(input("수식 입력: "))
    if 65 <= num <= 90:
        print(chr(num))
    elif 97 <= num <= 122:
        print(chr(num))
    else:
        print(num)
asci()"""

"""
def upperStr(str) :
    return str.upper()
mapTuple = tuple(map(upperStr, ("korea","seoul","university")))
print(mapTuple)
"""
"""
def strLen(str):
    return len(str)
str = ["apple","banana","mango",'tomato',"cherry","durian"]
strnum = list(map(strLen,str))
print(strnum)
"""
"""
listNum = [1, 2, 3, 4, 5]
listMap = list(map(lambda x:x*2, listNum))
print(listMap)"""
"""
def gob(a,b):
    return a*b

a = int(input("숫자 "))
b = int(input("숫자 "))
print(gob(a,b))

print("두 인자의 곱 =",(lambda a,b : a*b)(a,b))
"""

"""
lambdaGob = lambda a,b : a*b
print(lambdaGob(2,4))"""
"""
listNum = [1,3,5,7,9]
lambdaList = list(map(lambda x:x*x, listNum))
print(lambdaList)"""
"""
num = ["one", "two","three"]
su = ['1','2','3']
numSu = list(zip(num,su))
print(numSu)
"""
"""
num = ["one", "two","three"]
su = ['1','2','3']
for i,j in zip(num,su):
    print(i,j)
"""
"""
def strLen(str):
    return len(str)
str = ["apple","banana","mango",'tomato',"cherry","durian"]
strNum = list(map(strLen,str))
for i,j in zip(str, strNum):
    print(i,j)"""
"""
lastName = ['이','홍','김','유','아']
firstName = ['순신','길동','유신','관순','이키']
for i,j in zip(lastName,firstName):
    print(i,j)"""
"""
def recuHap(num) :
    if num > 0:
        return num + recuHap(num-1)
    else:
        return 0
    
num = int(input("숫자 입력 : "))
print(recuHap(num))
"""
"""
def recuFact(x):
    if x == 1:
        return 1
    else:
        return (x * recuFact(x-1))

num = int(input("팩토리얼 계산 할 값 입력 : "))
print(recuFact(num))"""

"""def powerNum(x,y):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif y == 0:
        return 1
    else:
        return x**y
a = int(input("숫자 1...?"))
b = int(input("숫자 2...?"))
print(powerNum(a,b))"""
"""a = 0
sum = 0
result = 0
def numPrt(x):
    global sum 
    global result
    x = int(input("숫자 입력"))
    return result(sum + x)
print(numPrt(a))
print(numPrt(a))
print(numPrt(a))"""

"""half = int(input("반지름 입력"))
def circle(half):
    return (half * half * 3.14)
print("원의 넓이=",circle(half))
"""
"""
sum_ = 0

def numPrt(value):
  global sum_
  sum_ += value
  print(sum_)

numPrt(10)
numPrt(20)
numPrt(30)"""


"""
soso = True
def sosu(num):
    global soso
    for i in range(2,num):
        if num % i == 0:
            soso = False
            break
        else:
            soso = True
    if soso == True:
        print("소수입니다.")
    else:
        print("소수가 아닙니다.")
sosu(4)
"""
"""
sum = 0
def sumList(num):
    global sum
    for i in num:
        sum += i
    return sum

num = [1,3,5,7,9]
print(sumList(num))"""
"""
lanStr = ("Java", "C","Python","R","Web")
newLan = list(map(lambda x:len(x), lanStr))
listStr = list(lanStr)
for i,j in zip(listStr,newLan):
    print("{}\t{}".format(i,j))"""
"""
phone = ("iphone","galaxy","xiaomi")
company = ("애플","삼성",'샤오미')
for i,j in zip(phone,company):
    print("{}\t{}".format(i,j))"""
"""
try:
    num = int(input("정수 입력: "))
    n = int(input("나눌 수: "))
    if num%n==0:
        print("짝수입니다.")
    else:
        print("홀수입니다.")
except:
    print('오류 발생')"""
"""
listNum = [12,15,7,15,24]
try:
    idx = int(input("리스트 항목 인덱스 위치를 입력하세요:"))
    num = int(input("나눌 숫자를 입력하세요:"))
    print(listNum[idx] / num)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("숫자가 아닌 잘못된 값 입니다.")
except IndexError:
    print("찾고자하는 인덱스가 없습니다.")"""
"""
num = int(input("5의 배수를 입력하십시오..: "))
try:
    if num % 5 != 0:
        raise Exception(f"{num}은(는) 5의 배수가 아닙니다.")
    print(f"{num}은(는) 5의 배수가 맞습니다. ")
except Exception as e:
    print("예외가 발생했습니다.", e)""" 
"""
listStr = ["python", "programming","korea","seoul","university"]
try:
    num = int(input("문자열 인덱스를 입력하시오..: "))
    lenNum = len(listStr[num])
    print(listStr[num],".....",lenNum)
except IndexError:
    print("찾고자하는 인덱스가 없습니다.")"""
"""
import pandas as pd
file1=pd.read_csv("c:\\file1\\grade_1.csv")
file2=pd.read_csv("c:\\file2\\grade_2.csv")
filecombine = pd.concat([file1,file2])

df = filecombine
"""
"""
def fibo(n) :
    if n <= 1 :
        return n
    else :
        return fibo(n-1) + fibo(n-2) 
        

n = int(input("계산할 숫자를 입력하시오"))        
fibo_list = []
for i in range(n):
    fibo_list.append(fibo(i))
print(fibo_list)
"""
'''
num = [1,2,3,3,4,5,6,7,2,3,8,9,10]
odd = 0
even = 0
for i in range(len(num)):
    if i % 2 == 0:
        even += 1
    if i % 2 != 0:
        odd += 1
print(f"{num}에는 홀수의 개수는 {odd}개 있고 짝수의 개수는 {even}개 있습니다")



num = [1,2,3,3,4,5,6,7,2,3,8,9,10]
odd = 0
even = 0
for i in range(len(num)):
    if num[i] % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"{num}에는 홀수의 개수는 {odd}개 있고 짝수의 개수는 {even}개 있습니다")


alphalist = ['a','b','c','d','e','f','g','h']

print(alphalist[4])
print(alphalist[3])

'''
#ascending 오름차순 : 0,1,2,3......,8,9 
#descending 내림차순 : 10,9,8,.....3,2,1

#SORT
#1. 리스트변수,sort()
#2. sorted()
"""
numlist = [42,12,3,7,72,25]
aa = sorted(numlist)
print(aa)
bb = sorted(numlist, reverse=True)
print(bb)"""

"""num = [11,23,5,7,15,9,8]
print("정열 전:",num)
print("정렬 후:", sorted(num,reverse=True))"""

"""flower=["장미","백합","튤립","국화","수선화"]
for i in flower:
    if len(i) == 3:
        print(i)"""
"""flower=["장미","백합","튤립","국화","수선화"]
for i in range(len(flower)):
    if len(flower[i]) == 3:
        print(flower[i])"""