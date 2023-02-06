from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            if(len(opening_brackets_stack) == 0):
                first = i;
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            if (len(opening_brackets_stack) == 0):
                return (i+1)
            if (are_matching(next, opening_brackets_stack[-1])):
                opening_brackets_stack.pop()
            else:
                return (i+1)
            pass
    if (len(opening_brackets_stack) == 0):
        return 0
    return (first)


def main():
    text = input()
    mismatch = find_mismatch(text)
    if(mismatch==0):
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
