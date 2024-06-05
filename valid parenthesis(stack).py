def isValidOrder(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return not stack
input_str = input()
if isValidOrder(input_str):
    print("True")
else:
    print("False")

