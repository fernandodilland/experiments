# Global vs local variable

def func():
    print("test")

def main():
    exit=False
    while exit==False:
        decision = input("You want to continue? (Y/N)3: ")
        if decision=="Y":
            break

main()