def word_count (string):
    return len(string.split())

def character_count (string):
    characters = {}
    for char in string.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters