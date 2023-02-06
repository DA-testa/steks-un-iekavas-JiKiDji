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
            if ((next ==')' and opening_brackets_stack[-1] == '(') or (next =='}' and opening_brackets_stack[-1] == '{') or (next ==']' and opening_brackets_stack[-1] == '[')):
                opening_brackets_stack.pop()
            else:
                return i+1
            pass
    if (len(opening_brackets_stack) == 0):
        return 0
    return i+1


def main():
    text = input()
    mismatch = find_mismatch(text)
    if(mismatch==1):
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
