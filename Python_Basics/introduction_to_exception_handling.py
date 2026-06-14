# Exception = An event that interrupts the flow of a program
#             (ZeroDivisionError,TypeError,ValueError,KeyboardInterrupt,...)
#             (try, except, finally)



try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ValueError:
    print("Enter only a number please")
except ZeroDivisionError:
    print("You can't divide by zero")
except KeyboardInterrupt:
    print("keyboard interrupted, or something in buffer")
except Exception:
    print("Something went wrong")
finally:
    print("This portion of code runs 'finally' both with try and with exception")