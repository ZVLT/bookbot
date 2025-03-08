def number_of_words(books):
    words = books.split()
    return len(words)

def number_of_letters(books):
    letters = {}
    lower_words = books.lower()
    split_lower_words = lower_words.split()
    num = 1
    for low in split_lower_words:
        letter = list(low)
        for l in letter:
            if l in letters:
                letters[l] += 1
            else: 
                letters[l] = num      
    return letters

def sort_on(letters):
    for l in letters:
        return letters[l]

def sorted_letters(letters):
    letters_to_sort = []
    for l in letters:
        letter_dict = {}
        letter_dict[l] = letters[l]
        letters_to_sort.append(letter_dict)
    after_sorted = letters_to_sort.sort(reverse = True, key = sort_on)
    return letters_to_sort