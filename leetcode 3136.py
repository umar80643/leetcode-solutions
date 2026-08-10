word = "234Adas"
vowels = "aeiouAEIOU"

if len(word) >= 3 and word.isalnum():
    has_vowel = any(c in vowels for c in word)
    has_consonant = any(c.isalpha() and c not in vowels for c in word)
    print(has_vowel and has_consonant)
else:
    print(False)