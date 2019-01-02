import re
import xml.etree.ElementTree as XML


def count_unique_words(array):
    for word in array:
        if word in words_dic.keys():
            words_dic[word] += 1
        else:
            words_dic[word] = 1


if __name__ == "__main__":
    words_array = []
    words_dic = {}
    words_info = []
    with open('a.txt') as text:
        line_number = 1
        for line in text:
            words = line.split()
            word_number = 1
            for word in words:
                words_array.append(word.lower())
                words_info.append((word.lower(), line_number, word_number))
                word_number += 1
            line_number += 1
    endings_array = []
    for word in words_array:
        result = re.findall(r'\w\w\w\b', word)
        if len(result) > 0:
            endings_array.append(result[0])
    count_unique_words(endings_array)

    root = XML.Element("root")
    a = XML.SubElement(root, text.name)

    text = open("a.txt")
    ending_info = []
    i = 0
    for word in words_dic:
        for info in words_info:
            needs_to_continue = False
            result = re.findall(r'\w\w\w\b', info[0])
            if len(result) > 0:
                if result[0] == word:
                    ending_info.append(info)
        XML.SubElement(a, "ending", name=word).text = "count: " + str(words_dic[word]) + "  -  " + str(ending_info)
        ending_info.clear()
        i += 1
    tree = XML.ElementTree(root)
    tree.write("c.xml")
