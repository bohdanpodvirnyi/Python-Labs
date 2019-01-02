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
    with open('a.txt') as text:
        for line in text:
            words = line.split()
            for word in words:
                words_array.append(word.lower())
    count_unique_words(words_array)

    root = XML.Element("root")
    a = XML.SubElement(root, text.name)

    for word in words_dic:
        XML.SubElement(a, "word", name=word).text = str(words_dic[word])

    tree = XML.ElementTree(root)
    tree.write("c.xml")
    text.close()
