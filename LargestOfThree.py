def find_largest_nested_if(num1, num2, num3 ):
    if num1>=num2:
        if num1>=num3:
            return num1
        else:
            return num3
    else:
        if num2>=num3:
            return num2
        else:
            return num3
num1 = int(input("Enter the first interger: "))
num2 = int(input("Enter the secod interger: "))
num3 = int(input("Enter the third interger: "))

largest_number = find_largest_nested_if(num1, num2, num3)
print("The largest number is: ", largest_number)
