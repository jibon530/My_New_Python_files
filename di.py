# import sys
# def de():
#     num = int(sys.stdin.readline())
#     fact = 1
#     i = 1
#     while (i <= num):
#         fact = fact * i
#         i += 1
#     ans = fact % 10000
#     print(ans)
# if __name__== "__main__":
#     de()
import sys
def name_loop():
    print("What you want to write:",end="")
    sys.stdout.flush()
    num = sys.stdin.readline().strip()
    print("How many times you want to write:",end="")
    sys.stdout.flush()
    n = int(sys.stdin.readline())
    for i in range (1,n+1,1):
        print(num,i)
    
if __name__ == "__main__":
    name_loop()