import sys
def fact_digit():
    num = int(sys.stdin.readline())
    fact = 1
    i = 1
    while (i <= num):
        fact = fact * i
        i += 1
    ans = str(fact)[-4:].zfill(4)
    print(ans)
if __name__ == "__main__":
    fact_digit()