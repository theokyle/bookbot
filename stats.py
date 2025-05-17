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

def sort_on(dictionary):
    return dictionary["num"]

def sorted_dictionaries (dictionary):
    dictionary_list = []
    keys = dictionary.keys()
    for key in keys:
        if key.isalpha():
            character = {}
            character["char"] = key
            character["num"] = dictionary[key]
            dictionary_list.append(character)
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list

