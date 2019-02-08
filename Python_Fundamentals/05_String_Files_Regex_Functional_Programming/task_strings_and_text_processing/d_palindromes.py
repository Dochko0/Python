line = input().split()
palindromes = []

for word in line:
    reverse_word = word[::-1]
    if word == reverse_word and word not in palindromes:
        palindromes.append(word)

print(', '.join(sorted(palindromes, key=str.lower)))