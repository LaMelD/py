# day 3

# =========================================================

# 함수
# 구조
def sum(a, b) :
    return a + b
# 사용
print (sum(7,2))
res = sum(15,246)
# 일반적인 함수 
"""
def 함수명(입력 인수) :
    수행할 문자
    ...
    return 결과값
"""
# 입력값이 없는 함수 
"""
def 함수명() :
    수행할 문자
    ...
    return 결과값
"""
# 결과값이 없는 함수 
"""
def 함수명(입력 인수) :
    수행할 문자
    ...
"""
# 입력값과 결과값이 없는 함수 
"""
def 함수명() :
    수행할 문자
    ...
"""
# 여러 개의 입력값을 받는 함수 만들기
def sum_many(*nums) :
    sum = 0
    for i in nums :
        sum += i
    return sum
print(sum_many(1,2,3,4,5,6,7,8,9,10))

def sum_mul(choice, *nums) :
    if choice == "sum" :
        res = 0
        for i in nums :
            res += i
    elif choice == "mul" :
        res = 1
        for i in nums :
            res *= i
    return res
print(sum_mul("sum", 1, 2, 3, 4, 5))
print(sum_mul("mul", 1, 2, 3, 4, 5))
# 입력 인수에 초깃값 미리 설정하기
def say_myself(name, old, man = True) :
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")
say_myself("이", 37)
say_myself("이", 37, False)

# 함수 안에서 선언된 변수의 효력 범위
    # 함수 안에서 선언된 변수의 효력 범위는 함부 내부이다.
    # 밖에서는 함수 내부의 변수에 접근할 수 없다.
a = 1
def vartest_1(a) :
    a = a + 1
    return a
vartest_1(a)
print(a)
# 함수 안에서 함수 밖의 수 변경하는 방법 :: return 이용하기
a = 1
def vartest_2(a) :
    a = a + 1
    return a
a = vartest_2(a)
print(a)
# 함수 안에서 함수 밖의 수 변경하는 방법 :: global 이용하기
a = 1
def vartest_3() :
    global a
    a = a + 1
vartest_3()
print(a)

# ------------------------------------------------------------------

# 입출력 관리
# 사용자 입력 :: input()
# number = input("숫자를 입력하세요 : ")
number = "123142"
print(number)
# 사용자 출력
print("life""is""too short")
print("life" "is" "too short")
print("life" + "is" + "too short")
print(number, end="hi hi")       # 한 줄에 결과값 출력하기
print()

# --------------------------------------------------------------------

# 파일 입출력
# 열기 :: f = open("[파일 경로]", '[파일 열기  모드]')
# 닫기 :: f.close

# 파일 열기 모드
# r : 읽기 모드
# w : 쓰기 모드
# a : 추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용
# 파일 입력 
# f.write("추가할 내용\n") :: 자동으로 개행을 해주진 않는다.
# 파일 읽기
# f.readline() :: 한 줄을 읽는다. 자동으로 파일 포인터를 옮겨준다.
# 파일 모두 읽기 
"""
f = open("C:/Python/새파일.txt", 'r') 
while True:
    line = f.readline() 
    if not line :
        break 
    print(line) 
f.close()
"""
# f.readlines() :: 파일 전체를 읽어 줄 별로 리스트에 저장하여 리턴한다.
"""
f = open("C:/Python/새파일.txt", 'r') 
lines = f.readlines() 
for line in lines :
    print(line) 
f.close()
"""
# f.read() :: 파일 전체를 읽어 문자열로 리턴한다.
# a 모드로 열면 파일의 포인터가 마지막의 새로운 줄을 가리킨다.
# with문 사용하기 :: with문을 이용하면 with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close된다.
"""
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
"""

# sys 모듈로 입력 인수 주기 :: argument를 받아올 수 있다.
"""
# sys1.py
# 아래와 같은 내용을 파이썬에선 모듈이라고 한다.
import sys

# argv[0]은 파일이름이 들어간다.
args = sys.argv[1:]
for i in args :
    print(i)
"""
# 사용법 :: python sys1.py aaa bbb ccc

# ================================================================

# 클래스
# 클래스의 필요성...
# 클래스의 개념...
# 객체와 인스턴스의 차이
"""
클래스에 의해서 만들어진 객체를 인스턴스라고도 한다.
navi = Cat() 이라고 했을 때
navi는 객체이다.
navi는 Cat 클래스의 인스턴스이다.
"""
# 클래스 예시
# 파이썬에서는 클래스에서 사용하는 함수의 첫번째 인자(parameter)를 self로 사용하는 것이 원칙입니다.
# 예시 1
class service :
    secret = "Thanks"
    def sum (self, a, b) :
        res = a + b
        print("%s + %s = %s입니다." % (a, b, res))
test = service()
test.sum(1, 2)
# 예시 2
class StudyMember :
    # 생성자...인스턴스를 생성할 때...초기화...
    def __init__(self, name, age, purpose) :
        self.name = name
        self.age = age
        self.purpose = purpose
    def getPurpos(self) :
        return self.purpose
    def getName(self) :
        return self.name
    def getAge(self) :
        return self.age
A = StudyMember("lee", 124, "OpenStack")
B = StudyMember("park", 132, "Network")
C = StudyMember("choi", 15, "Programming")

# 클래스의 상속
class stuff :
    num1 = 1
class ipTime(stuff) :
    num4 = 4
h = ipTime()
print(h.num1)
print(h.num4)

# 메서드 오버라이딩과 연산자 오버로딩
## 메서드 오버라이딩
### 대상인 클래스의 메서드와 이름은 같지만 행동은 다르게
### 상속받는 클래스에서 동일한 이름의 메서드를 다시 구현하면 된다.
## 연산자 오버로딩
### 연산자를 객체끼리 사용할 수 있게 하는 기법
class person :
    def __init__(self, name) :
        self.fullname = name
    def love(self, other) :
        print("%s, %s TTTTTT" % (self.fullname, other.fullname))
    def __add__(self, other) :
        print("%s, %s VVVVVV" % (self.fullname, other.fullname))
pey = person("pey")
juliet = person("juliet")
pey.love(juliet)
pey + juliet

# ------------------------------------------------------------------

# 모듈의 이해   - p212
# 패키지의 이해 - p222

# 예외 처리
# 오류 및 예외 처리 기법
# try, except, else, finally

try :
    # 시도한다
    a = 3
    b = 3
    a = a / b
    print(a)
except :
    # 에러가 발생하면
    print("error")
else :
    # 에러가 발생하지 않으면
    # 반드시 except 뒤에 위치해야 함
    print("else")
finally :
    # 에러 여부와 상관 없이 
    print("always show")

# try, except만 쓰는 방법
## 오류가 발생하기만 하면 except 실시
"""
try :
    ...
except :
    ...
"""
# 발생 오류만 포함한 except문
## 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행
"""
try : 
    ...
except 발생 오류 :
    ...
"""
# 발생 오류와 오류 메시지 변수까지 표함한 except문
## 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행
## 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법
"""
try :
    ...
except 발생 오류 as 오류 메시지 변수 :
    ...
"""
# pass 를 사용하여 오류 상황을 무시할 수 있다.
"""
except :
    pass
"""
# 일부러 오류를 발생시킬 수 있다. :: raise
"""
raise NotImplementedError
"""

# --------------------------------------------------------------

# 내장 함수
# print, input, del type, ...
# 따로 import하지 않고 사용할 수 있는 내장 함수

# 절대값
print(abs(-11))
# x^y를 리턴 x의 y승한 결과를 리턴
print(pow(2, 3))
# 반복 가능한 자료형이 모두 참인지, 하나라도 거짓이 있는지 판별
print(all([0,12,3]))
print(all([12,314,1]))
# all의 반대, 하나라도 참이 있다면 True
print(any([0,12,3]))
print(any([12,314,1]))
# ASCII 코드값을 입력으로 받아 그 코드에 해당하는 문자를 출력
print(chr(65))
print(chr(97))
# 문자를 입력으로 받아 그 문자의 ASCII 코드값을 출력
print(ord('a'))
print(ord('0'))
# 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
print(dir([1,2,3]))
print(dir({1:'a'}))
# 나머지와 몫을 튜플 형태로 리턴한다.
print(divmod(7, 3))
print(divmod(1.3, 0.2))
# enumerate : 열거하다 - 순서있는 자료형을 입력으로 받아 enumerate 객체를 리턴
# 순서와 함께 값이 나온다. 유용할 듯 하다.
for i,name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
# 실행 가능한 문자열(1+2, 'hi' + 'a', 등)을 입력받아 문자열을 실행한 결과값을 리턴하는 함수
# 보통 eval은 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶은 경우 사용된다.
print(eval('1+2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))
# 걸러내는 함수. 첫 번째 인수로 함수 이름, 두 번째 인수로 반복 가능한 자료형
# 반복가능한 자료형 요소들이 첫 번째 인수인 함수에 입력되었을 때 리턴값이 참인 것만 묶어서 돌려준다.
"""
def positive(numlist) :
    res = []
    for num in numlist :
        if num > 0 :
            res.append(num)
    return res
print(positive([1, -3, 2, 0, -5, 6]))
"""
# 아래와 같이 간단히 쓸 수 있다.
"""
def positive(x) :
    return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
"""
# 10진 정수를 입력받아서 16진수로 변환하여 리턴하는 함수
print(hex(234))
print(hex(3))
# 10진 정수를 입력받아서 8진수로 변환하여 리턴하는 함수
print(oct(234))
print(oct(3))
# 객체를 입력받아 객체의 고유 주소값(레퍼런스)을 리턴하는 함수
a = 3
b = a
print(id(3))
print(id(a))
print(id(b)) # 3, a, b 가 모두 같은 객체를 가리킴
# 첫번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
# 입력받은 인스턴스가 그 클래스의 인스턴스인지 판단하여 참이면 true 리턴
print(isinstance(pey, person))

# lambda... 
# 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을 한다.
# 보통 함수를 한 줄로 간결하게 만들 때 사용한다. 
# 사용법 :: lambda 인수1, 인수2, ... : 인수를 이용한 표현식
sum = lambda a, b : a + b
print(sum(3, 10))
# 입력값의 길이 또는 요소의 전체 개수를 리턴한다.
print(len("python"))
print(len([1,2,3,4,51,5,6,123,124,2]))

# map
# map(f, iterable)은 함수와 반복 가능한 자료형을 입력으로 받는다.
# map은 입력 받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴하는 함수이다.
"""
def two_times(numlist) :
    res = []
    for num in numlist :
        res.append(num * 2)
    return res
res = two_times([1, 2, 3, 4])
print(res)
"""
# 아래와 같이 간단히 쓸 수 있다.
"""
def positive(x) : return x * 2
print(list(map(positive, [1, 2, 3, 4])))
"""

# 인수로 반복 가능한 자료형을 입력받아 그 최대값을 리턴하는 함수
print(max([1,2,3]))
print(max("python"))
# 인수로 반복 가능한 자료형을 입력받아 그 최소값을 리턴하는 함수
print(min([1,2,3]))
print(min("python"))

# sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 리턴하는 함수
# 원본은 바뀌지 않는다.
li = [3, 1, 2]
print(sorted(li))
print(li)

# 자료형이 무엇인지 알려주는 함수
print(type("abc"))
print(type(13))

# 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수이다.
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip("abc", "def")))

# ---------------------------------------------------------------