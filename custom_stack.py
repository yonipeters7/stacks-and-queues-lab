def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # Create an empty stack to track opening brackets
    stack = []

    # Map closing brackets to their corresponding opening brackets
    matching = {')': '(', '}': '{', ']': '['}

    # Process each character in the string
    for char in s:
        if char in '({[':
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
        elif char in ')}]':
            # If it's a closing bracket, check if it matches the top of the stack
            if not stack or stack[-1] != matching[char]:
                # Stack is empty or doesn't match - invalid
                return False
            # Valid match - pop from stack
            stack.pop()

    # Valid only if stack is empty (all brackets were matched)
    return len(stack) == 0
