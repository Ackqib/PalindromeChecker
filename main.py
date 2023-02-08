  print("Palindrome Word Checker")
#Get word
word = input("Enter a word: ")
#Find length of word
word_length = len(word)
#Loop word from first word to last using length
palindrome = True
for i in range(word_length):
    if word[0+i] != word[word_length-1-i]:
        palindrome = False
if palindrome == True:
    print(word, "is a palindrome.")
elif palindrome == False:
    print(word,'is not a palindrome.')
