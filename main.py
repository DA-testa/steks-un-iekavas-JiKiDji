# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            if ((next ==')' and opening_brackets_stack[-1] == '(') or (next =='}' and opening_brackets_stack[-1] == '{') or (next =='[' and opening_brackets_stack[-1] == ']')):
                opening_brackets_stack.pop()
            else:
                return i
            pass
    return 0


def main():
    text = input()
    mismatch = find_mismatch(text)
    if(mismatch==0):
        print("Success")
    else:
        print(mismatch+1)


if __name__ == "__main__":
    main()
