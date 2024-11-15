def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]
input_string = input("Enter a word or phrase: ")
if is_palindrome(input_string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")
