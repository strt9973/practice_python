check_str = input("Enter check str(only parentheses): ")


def check_parentheses(a_string):
    stack = []
    for c in a_string:
        if c == "(" or c == "{":
            stack.append(c)
        if c == ")" or c == "}":
            if len(stack) == 0:
                return False
            else:
                tmp = stack.pop()
                if not (c == ")" and tmp == "(") and not (c == "}" and tmp == "{"):
                    return False
    return len(stack) == 0


print(check_parentheses(check_str))
