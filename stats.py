def get_num_words(file_content):
    words = file_content.split()
    num_words = len(words)
    return num_words

def get_num_chars(file_content):
    char_count = {}
    file_content = file_content.lower()
    for char in file_content:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    char_dict = sorted(char_count.items(), key = lambda x : x[1], reverse = True)
    return char_dict