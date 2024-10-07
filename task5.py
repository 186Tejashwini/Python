def pal_checker(word):
    # Check if the word is equal to its reverse
    if word == word[::-1]:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

word = input("Enter a word: ")
pal_checker(word)
