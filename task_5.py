# Get user's name and favorite numbers
name = input("Enter your name: ")
num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))
favorite_numbers = [num1, num2, num3]
print(f"\nHello, {name}! Let's explore your favorite numbers:")

# Check if each number is even or odd
even_odd_info = []
for number in favorite_numbers:
    if number % 2 == 0:
        even_odd_info.append((number, "even"))
    else:
        even_odd_info.append((number, "odd"))
for number, status in even_odd_info:
    print(f"The number {number} is {status}.")

# Calculate the square of each number
squares_info = []
for number in favorite_numbers:
    square = number * number
    squares_info.append((number, square))
for number, square in squares_info:
    print(f"The number {number} and its square: ({number}, {square})")

# Calculate the sum of the numbers
total_sum = sum(favorite_numbers)
print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

# Check if the sum is a prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(total_sum):
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"{total_sum} is not a prime number.")
