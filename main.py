
def input1():
    sentence = input ("input sentence: ")
    for words in sentence.split():
        print(words)

def input2():
    sentence = input("input sentence: ")
    words = sentence.replace(" ", "\n")
    print(words)




if __name__ == '__main__':
    input1()
    input2()
