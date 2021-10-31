import sys
import argparse

def string1():
    n = len(sys.argv)
    print("Total arguments passed", n)
    print("\nName of Python script:", sys.argv[0])
    print("\nArguments passed:", end=" ")
    for i in range(1, n):
        print(sys.argv[i])
        print("\nResult:", sum)

def part2():
    parser = argparse.ArgumentParser()
    parser.parse_args()


if __name__ == '__main__':
    string1()
    part2()
