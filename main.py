from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            if(not opening_brackets_stack):
                first = i;
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            if (not opening_brackets_stack):
                return (i+1)
            if (are_matching(opening_brackets_stack[-1], next)):
                opening_brackets_stack.pop()
            else:
                return (i+1)
            pass
    if (not opening_brackets_stack):
        return 0
    return (first+1)


def main():
    let = input()
    print(let)
    text = input()
    if let == 'F' :
        with open(text) as file:
            text = file.readlines()
    elif let != 'I' :
        print(error)
        return
        
    mismatch = find_mismatch(text)
    print(mismatch)
    print(text)
    if(mismatch==0):
        print("Success")
    else:
        print(mismatch) 


if __name__ == "__main__":
    main()
