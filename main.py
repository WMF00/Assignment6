def piglatin():
    words = str(input("Input Sentence:")).split()
    for word in words:
        print(word[1:] + word[0] + "ay", end = " ")
    print ()


if __name__ == '__main__':
    piglatin()
