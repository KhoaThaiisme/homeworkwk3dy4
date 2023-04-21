# def word_to_length(list1):
#     length = []
#     for word in list1:
#         length.append(word)
#         length.append(len(word))
#     return length

# list = ['hello', 'hi', 'goodbuy']
# print(word_to_length(list))


def word_to_length(list1):
    length = {}
    for word in list1:
        length[word] = len(word)
    return length

list = ['hello', 'hi', 'goodbuy']
print(word_to_length(list))