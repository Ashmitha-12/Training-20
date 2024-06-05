def generateParenthesis(n):
    def backtrack(s, open_count, close_count):
        if len(s) == 2 * n:
            valid_parentheses.append(s)
            return
        if open_count < n:
            backtrack(s + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(s + ')', open_count, close_count + 1)

    valid_parentheses = []
    backtrack('', 0, 0)
    return valid_parentheses

try:
    n = int(input("Enter the number of pairs of parentheses: "))
    if n < 0:
        raise ValueError("Number of pairs must be non-negative.")
    
    valid_parentheses = generateParenthesis(n)
    
    if valid_parentheses:
        print("Valid parentheses in lexicographical order:")
        for parentheses in valid_parentheses:
            print(parentheses)
    else:
        print("No valid parentheses found for the given input.")
except ValueError as e:
    print(f"Invalid input: {str(e)}")
