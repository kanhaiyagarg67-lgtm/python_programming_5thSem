# Take input from user
num = int(input("Enter a number: "))

# Store original number in temp variable
temp = num

# Count total digits in the number
digits = len(str(num))

# Variable to store sum of powers of digits
sum = 0

# Loop runs until all digits are separated
while temp > 0:
    # Get last digit of the number
    digit = temp % 10

    # Add digit raised to power of total digits
    sum = sum + digit ** digits

    # Remove last digit from number
    temp = temp // 10

# Check whether calculated sum is equal to original number
if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")
