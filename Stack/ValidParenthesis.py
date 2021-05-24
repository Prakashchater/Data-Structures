from stack import Stack

def isMatch(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def isValidParenthesis(paren_str):
    s = Stack()
    i = 0
    is_valid = True
    while i < len(paren_str) and is_valid:
        paren = paren_str[i]
        if paren in "({[":
            s.push(paren)
        else:
            if s.isEmpty():
                is_valid = False
            else:
                top = s.pop()
                if not isMatch(top, paren):
                    is_valid = False
        i += 1

    if s.isEmpty() and is_valid:
        return True
    else:
        return False

if __name__ == '__main__':
    paren_str = input("Enter the Parenthesis: ")
    print(isValidParenthesis(paren_str))
