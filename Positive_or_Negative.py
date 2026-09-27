import sys
def positive_Negative():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = float(sys.stdin.readline())
        if n > 0:
            print("The",n,"number is Positive.")
        elif n < 0:
            print("The",n,"number is Negative.")
        else:
            print("The number is zero.")
if __name__=="__main__":
    positive_Negative()