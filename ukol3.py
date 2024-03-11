def is_palindrome(number):
    return str(number) == str(number)[::-1]

def next_smallest_palindrome(from_num):
    if is_palindrome(from_num):
        from_num += 1

    while True:
        if is_palindrome(from_num):
            return from_num  # Success
        from_num += 1

# Example usage:
from_num = int(input("Enter the number to start from: "))

next_palindrome_num = next_smallest_palindrome(from_num)

print("Next smallest palindrome is:", next_palindrome_num)
