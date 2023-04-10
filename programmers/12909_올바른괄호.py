def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif len(stack) and i == ")":
            stack.pop(i)
        else:
            return False
    return False if len(stack) else True