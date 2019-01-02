if __name__ == "__main__":
    b1 = []
    b2 = []
    file_b1 = open("b1.txt", "w+")
    file_b2 = open("b2.txt", "w+")
    with open('a.txt') as poem:
        i = 1
        for line in poem:
            words = line.split()
            if i % 2 == 0:
                for word in words:
                    file_b1.write(word.upper() + " ")
                file_b1.write("\n")
            else:
                for word in words:
                    file_b2.write(word.lower() + " ")
                file_b2.write("\n")
            i += 1
    file_b1.close()
    file_b2.close()
