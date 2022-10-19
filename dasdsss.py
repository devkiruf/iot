"""for i in range(1,10,1):
    for j in range(2,10,1):
        print(f"{j}*{i}={j*i}", end="")
    print()

for i in range(1,6,1):
    for j in range(5, i-1, -1): # i 횟수에 따라 반복
        print(j, end="")
    print()
for i in range(5,0,-1):
    for j in range(5, i-1, -1): # i 횟수에 따라 반복
        print(j, end="")
    print()


for i in range(5,0,-1):
    for j in range(1, i+1, 1): # i 횟수에 따라 반복
        print(5-j, end="")
    print()
"""
"""
num= int(input("반복할 횟수를 말씀하십시오"))
i = 0 
while i < num:
    print(i, end="")
    i = i+1
    if i == 5:
        break
"""
'''
sum= 0
while True:
    num = int(input("계산할 숫ㅈ를 입력하시오"))
    if num == 0:
        print(f"합계는{sum}")
        break
    else:
        sum+=num
'''
'''
while True:
    animal = input("좋아하는 동물은?")
    if animal == "코알라":
        print("정답입니다")
        break
    else:
        continue
        '''
'''     
num = [23,15,42,50,22,31,1]


for i in num:
    if i % 2 ==0:
        continue
    else:
        print(i, end="")
            '''
sum = 0
for i in range(5):
    num=int(input('숫자'))
    if num == 3:
        continue
    else:
        print(num)
        sum+=num
print("합계", sum)
    
