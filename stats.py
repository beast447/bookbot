def count_words(text):
    split_string = text.split()
    word_count = len(split_string)
    return word_count

def count_chars(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
           char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_dict(dictionary):
    list_of_dicts = []
    for key in dictionary:
        count = dictionary[key]
        entry = {}
        entry["char"] = key
        entry["num"] = count
        list_of_dicts.append(entry)
    list_of_dicts.sort(key=sort_on, reverse=True)
    return list_of_dicts

def sort_on(dictionary):
    return dictionary["num"]

