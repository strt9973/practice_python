from bisect import bisect_left

word_list = input("Enter words(separated by space): ").split()
search_word = input("Enter search word: ")

sorted_word_list = sorted(word_list)

def binary_search(word_list, search_word):
    index = bisect_left(word_list, search_word)
    if index <= len(word_list) and word_list[index] == search_word:
        return print("Found {}".format(search_word))
    return print("Not Found")

binary_search(sorted_word_list, search_word)
