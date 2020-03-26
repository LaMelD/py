# day 3
# =========================================================
# if 문
# if [조건식] : 형태를 사용한다.
money = 100
if money :
    print("show me the money")
else :
    print("fuck off")
# 조건식에는 여러가지 비교 연산자가 들어갈 수 있다.
# ==, !=, <, >, <=, >=
# 조건식에는 여러가지 조건식이들어갈 수 있다.
# A <= B and B == C
# and, or, not
# 조건식에는 아래와 같은 형식도 적용될 수 있다.
# in 관련
# x in 리스트
# x in 튜플
# x in 문자열
# not in 관련
# x not in 리스트
# x not in 튜플
# x not in 문자열

#elif 문 : 이전 조건문이 거짓일 때 수행된다.
money = 0
card = 1
if money :
    pass    # money가 0이 아닐 경우
elif card :
    pass    # card가 0이 아닐 경우
else :
    pass    # 나머지 경우

# -----------------------------------------------------------

# while 문
# while 조건식 :
# 조건식을 만족할 동안 반복한다.
# break를 통해 강제로 while문을 나갈 수 있다.

money = 0
while money < 10 :
    money += 1  # 반복문에서 money를 1씩 더하는데 10이되면 while문을 빠져나간다.

money = 0
while True :
    money += 1
    if 10 <= money :
        break
# 위와 같은 동작을 하는 코드이다.

# -----------------------------------------------------------

# for문

# 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list :
    print(i)

# 다양한 for문 사용이 가능하다
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a :
    print(first + last)

# continue
# continue를 만나면 for문의 처음으로 돌아가게 된다.

# range 함수
# 숫자 리스트를 자동으로 만들어준다.
a = range(10)
print(a)
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 10은 포함되지 않는다.
for i in range(10):
    print(i)

# 리스트 안에 for문 포함하기
a = [1, 2, 3, 4]
result = []
for num in a :
    result.append(num * 3)
print(result)

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

# 짝수만 담고 싶다면?
# 생각보다 보기 힘들어 보인다...
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# for문을 2개 이상 사용하는 것도 가능하다. ex 구구단...
# 이건 쓰기가 더 힘들 것 같은데... 익숙해지면 괜찮을 듯...?
result = [x * y for x in range(2, 10) for y in range(1,10)]
print(result)

# ============================================================