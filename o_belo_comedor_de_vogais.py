
user_word = input("Insira uma palavra: ")

user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:
    
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    
    word_without_vowels += letter

print("Palavra sem vogais:", word_without_vowels)
