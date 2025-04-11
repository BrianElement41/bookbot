def get_num_words(file_contents):
    words = file_contents.split()
    letters = word_list(words)
    return len(words), letters

def word_list(words):
    letters = {}
    for word in words:
        for letter in word.lower():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    sort_letters_list(letters)
    return letters

def sort_letters_list(letters):
    def sort_on(dict):
        return dict["num"]
    
    sorted_list = []
    for key, value in letters.items():
        sorted_list.append({"letter": key, "num": value})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    #letters.sort(reverse=True, key=sort_on)