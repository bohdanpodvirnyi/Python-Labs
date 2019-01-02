def count_unique_words(array):
    for word in array:
        if word in words_dic.keys():
            words_dic[word] += 1
        else:
            words_dic[word] = 1


if __name__ == "__main__":
    words_array = []
    words_dic = {}
    with open('text.txt') as text:
        for line in text:
            words = line.split()
            for word in words:
                words_array.append(word)
    count_unique_words(words_array)
    for word in words_dic:
        print("{0} - {1}".format(word, words_dic[word]))
