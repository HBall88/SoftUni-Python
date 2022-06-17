input_word = input()
words_list = input_word.split(' ')
palindrome = input()
palindromes_list = [word for word in words_list if word == word[::-1]]
palindromes_needed = [word for word in words_list if word == palindrome]
print(palindromes_list)
print(f'Found palindrome {len(palindromes_needed)} times')