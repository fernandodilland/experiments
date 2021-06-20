# Experiment programmed for practice by: Fernando Dilland Mireles Cisneros

# Global vs local variable

def func():
    print("Number on function is:",number)
    # number=number-1 No workspace

def main():
    times=20
    global number
    number=3
    print("Number is:",number)
    while times>0:
        print("Repeated:",times)
        times=times-1
        func()

main()