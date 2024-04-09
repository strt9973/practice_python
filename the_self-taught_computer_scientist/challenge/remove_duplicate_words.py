from collections import defaultdict


remove_duplicate_char = input("Enter str: ")


def remove_duplicate(str):
    word_list = str.split()
    check_dict = defaultdict(int)
    for word in word_list:
        if check_dict[word]:
            continue
        else:
            check_dict[word] = 1

    return " ".join([w for w in check_dict.keys()])


print(remove_duplicate(remove_duplicate_char))
