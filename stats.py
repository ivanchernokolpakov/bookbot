
#word_count takes in a string "file_text", and splits it into a separated list of every word
#it then returns the length of the list
def word_count(file_text):
    word_list = file_text.split()
    return len(word_list)

#char_count is a function that returns a dictionary with separated characters for the entire string
#NOTE: it does not distinguish between upper and lower case, all characters are considered lowercase
def char_count(file_text):
    char_dict = {}
    for char in file_text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] +=1
    return char_dict

def dict_to_list(dict):
    char_list =[]
    for x in dict:
        char_list.append({"char":x, "num":dict[x]})
    return char_list

