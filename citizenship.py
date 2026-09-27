import sys
def citizen():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = float(input("Enter age:"))
        country = str(input("Enter Your Country name:"))
        coun = country.lower()
        if n >= 18 and coun == "bangladesh":
            print("You can vote.")
        else:
            print("You can't vote.")
if __name__=="__main__":
    citizen()