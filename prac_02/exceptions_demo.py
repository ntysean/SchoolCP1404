



try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

### 1. ValueError will occur when an input that is not an integer is made.
### 2. Zerodivision error will occur when a number is divided by 0, which will happen if the demoninator is 0.
### 3. yes