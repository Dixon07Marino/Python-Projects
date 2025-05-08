#¿Es un anagrama?

def isAnagram(word_one: str, word_two: str):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(f"Anagram?: {isAnagram("caca", "Acac")}")