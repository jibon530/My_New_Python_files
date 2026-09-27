import sys
def zero():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = float(sys.stdin.readline())
        num = int(sys.stdin.readline())
        if (n >= 33) and (num >= 75):
            print("You pass the exam.")
        else:
            print("You aren't pass the exam.")
if __name__=="__main__":
    zero()