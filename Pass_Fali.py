import sys
def pass_fail():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        if n >= 33:
            print("Pass")
        else:
            print("Sorry.. You are fail")
if __name__=="__main__":
    pass_fail()