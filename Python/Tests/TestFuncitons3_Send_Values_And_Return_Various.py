# Global vs local variable

def func(valueReceived1,valueReceived2):
    print(">>> Correct input to the function with the values received:", valueReceived1,
          "and",valueReceived2,"<<<")

    # Operations
    sendable1 = valueReceived1+valueReceived2
    sendable2 = valueReceived1-valueReceived2
    sendable3 = valueReceived1*valueReceived2
    sendable4 = valueReceived1/valueReceived2

    return sendable1, sendable2, sendable3, sendable4 # The final values returned

def main():

    exit=False
    while exit==False:
        # The user is prompted for the two integer-type values
        value1 = int(input("First number: "))
        value2 = int(input("Second number: "))

        print("--- Executing function, sending values:", value1,"and", value2,"---")
        tupleReturned = func(value1,value2) # The function is sent to be called by injecting the 2 values
        t="- The"
        of="of the values is:"
        print(t,"sum", of,tupleReturned[0])
        print(t,"subtract", of,tupleReturned[1])
        print(t,"multiplication", of,tupleReturned[2])
        print(t,"division", of,tupleReturned[3])

        decision = input("You want to continue? (Y/N): ")
        if decision=="N": # If the input receives "N", the while loop is terminated.
            break # The break takes me out of the cycle

main()