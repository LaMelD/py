# day 4

# ==============================================================

# 외장 함수
# --------------------------------------------------------------
# sys 모듈
import sys
# 명령 행에서 인수 전달하기
print(sys.argv)
# 스크립트 강제 종료
"sys.exit()"
# 모듈 불러오기...
"sys.path.append(\"모듈의 위치\")"
# --------------------------------------------------------------
# pickle 모듈 : 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
import pickle
# 저장
"pickle.dump(data, file)"
# 불러오기
"data = pickle.load(file)"
# --------------------------------------------------------------
# os 모듈
import os
# 환경 변수 알아내기
print(os.environ)
# 디렉터리 위치 변경하기
"os.chdir(\"위치\")"
# 디렉터리 위치 리턴받기
print(os.getcwd())
# 시스템 명령어 호출하기
print(os.system("dir"))
# 실행한 명령어의 결과값 리턴받기
"f = os.popen(\"dir\")"
# --------------------------------------------------------------
# shutil 모듈 : 파일을 복사해 주는 파이썬 모듈
import shutil
# 파일 복사하기
"shutil.copy(\"복사할 파일\", \"목적지 파일\")"
# --------------------------------------------------------------
# glob 모듈 : 특정 디렉토리에 있는 파일 이름을 모두 알아야 할 때
import glob
# 디렉터리에 있는 파일들을 리스트로 만들기
G = glob.glob("C:/*")
print(G)
# --------------------------------------------------------------
# tempfile 모듈 : 파일을 임시로 만들어서 사용할 때 유용한 모듈
import tempfile
# 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 리턴
filename = tempfile.mktemp()
print(filename)
# 임시 저장 공간으로 사용될 파일 객체를 리턴한다. 이 파일은 기본적으로 바이너리 쓰기 모드를 갖는다.
f = tempfile.TemporaryFile()
f.close()   # 호출 시 파일 객체는 자동으로 사라짐
# --------------------------------------------------------------
# time 모듈 : 시간 관련
import time
# UTC를 기준으로 현재 시간을 실수 형태로 리턴
print(time.time())
# 형태를 바꿔줌
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print("", time.localtime(time.time())) # 앞 문자열에는 형식이 들어간다.
# 일정 시간 간격을 둔다
time.sleep(2)   # 2초의 시간 간격을 둔다.
# --------------------------------------------------------------
# calendar 모듈 : 달력 모듈
import calendar
# 해당 연도의 전체 달력을 볼 수 있다.
print(calendar.calendar(2020))
calendar.prcal(2020)
# 해당 연도, 월의 달력을 볼 수 있다.
calendar.prmonth(2020, 8)
# 해당 연도, 월, 일의 요일을 알 수 있다. 0 : 월, 6 : 일
print(calendar.weekday(2020, 8, 15))
# 해당 연도, 월의 1일이 무슨 요일이고 그 달이 몇일까지 있는지 튜플로 리턴
print(calendar.monthrange(2020,8))
# --------------------------------------------------------------
# random 모듈 : 난수를 발생시키는 모듈
import random
# 실수 난수 리턴
print(random.random())
# 정수 난수 리턴
print(random.randint(1, 10))
# 입력으로 받은 리스트에서 무작위로 하나를 선택하여 리턴한다.
li = [1,2,3,4,5]
number = random.choice(li)
li.remove(number)
print(li)
# 입력으로 받은 리스트를 무작위로 섞고 싶을 때
li = [1,2,3,4,5]
random.shuffle(li)
print(li)
# --------------------------------------------------------------
# webbrowser 모듈 : 자신의 시스템에서 사용하는 기본 웹 브라우저가 자동으로 실행하게 하는 모듈
import webbrowser
# 웹 브라우저를 실행시키고 해당 URL로 이동
"webbrowser.open(\"http://google.com\")"
# 새로운 창으로 해당 URL이 열리도록
"webbrowser.open_new(\"http://google.com\")"
# --------------------------------------------------------------
# thread 모듈 : 하나의 프로세스에서 2가지 또는 그 이상의 일을 동시에 수행할 수 있게 하는 모듈
import threading
import time

def say(msg) :
    while True :
        time.sleep(1)
        print(msg)

for msg in ['you', 'need', 'python'] :
    t = threading.Thread(target=say,args=(msg,))
    t.daemon = True
    t.start()

for i in range(100) :
    time.sleep(0.1)
    print(i)
# 위 아래가 같은 동작을 하는 코드이다.
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, msg):
        threading.Thread.__init__(self)
        self.msg = msg
        self.daemon = True
    def run(self):
        while True:
            time.sleep(1)
            print(self.msg)
for msg in ['you', 'need', 'python']:
    t = MyThread(msg)
    t.start()
for i in range(100):
    time.sleep(0.1)
    print(i)
# --------------------------------------------------------------
