def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # TODO: Implement stack logic to validate parentheses
    stack = []

    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in s:
        if char in "({[":
            stack.append(char)
        
        elif char in ")}]":
            if not stack:
                return False
            
            top = stack.pop()

            if top != pairs[char]:
                return False
    
    return len(stack) == 0
