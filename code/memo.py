import sys

args = sys.argv

if args.__len__() == 1:
    print("usage : memo.py [option] [memo]")
    sys.exit()
    
if args[1] == "-a":
    if args.__len__() == 2:
        print("usage : memo.py [option] [memo]")
        sys.exit()

    f = open("./memo.txt", "a")
    f.write(args[2])
    f.write("\n")
    f.close()
elif args[1] == "-v":
    try:
        f = open("./memo.txt", "r")
    except FileNotFoundError:
        print("write memo first")
    else:
        memo = f.read()
        f.close()
        print(memo)