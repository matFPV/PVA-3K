def is_palindrome(number):
    return str(number) == str(number)[::-1]

def next_smallest_palindrome(from_num):
    if is_palindrome(from_num):
        from_num += 1

    while True:
        if is_palindrome(from_num):
            return from_num  # Success
        from_num += 1
