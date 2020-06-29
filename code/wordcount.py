import os

os.getcwd()
DIR_NAME = "wordcount_target"
FILE_PATH = os.path.join(os.getcwd(), DIR_NAME)
files = os.listdir(FILE_PATH)

for filename in files:
    count = 0
    txt = os.path.join(FILE_PATH, filename)
    with open(file=txt, mode='r', encoding='utf8') as f:
        lines = f.read().split('\n')
        for line in lines:
            count += len(line)
    print(filename + ' : ' + str(count))