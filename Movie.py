import sys
def movie():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(input("Enter your age:"))
        if n >= 18:
            print("You can watch the movie.")
        else:
            print("You can't watch the movie")
if __name__=="__main__":
    movie()