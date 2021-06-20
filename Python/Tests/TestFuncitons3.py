# Global vs local variable

def func(valueReceived1,valueReceived2):
    print(">>> Correct input to the function with the values received:", valueReceived1,
          "and",valueReceived2,"<<<")

    # Operations
    t="- The"
    of="of the values is:"
    print(t,"sum", of,valueReceived1+valueReceived2)
    print(t,"subtract", of,valueReceived1-valueReceived2)
    print(t,"multiplication", of,valueReceived1*valueReceived2)
    print(t,"division",of,valueReceived1/valueReceived2)
def main():

    exit=False
    while exit==False:
        # The user is prompted for the two integer-type values
        value1 = int(input("First number: "))
        value2 = int(input("Second number: "))

        print("--- Executing function, sending values:", value1,"and", value2,"---")
        func(value1,value2) # The function is sent to be called by injecting the 2 values

        decision = input("You want to continue? (Y/N): ")
        if decision=="N" or "n": # If the input receives "N", the while loop is terminated.
            break # The break takes me out of the cycle

main()