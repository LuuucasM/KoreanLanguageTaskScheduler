import random
import time
import sys
from grammar_list import grammar, grammar_reference

def main(n):
    n = int(n)
    total = n
    while n > 0:
        print("----------------------------")
        print("Next up: Grammar Generation: " + str(n) + " out of " + str(total))
        print("----------------------------")
        gram = random.choice(grammar)
        print(gram)
        input("type done to reveal answer")
        input("are you sure you are finished?")
        print(grammar_reference[gram])
        n -= 1

if __name__ == '__main__':
    main(sys.argv[1])