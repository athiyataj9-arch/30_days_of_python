# Topic: The Stack Data Structure (LIFO - Last In, First Out).
# ==========================================
# DAY 28: DATA STRUCTURES (STACKS) 🏗️
# ==========================================

# PROBLEM 1: VALID PARENTHESES
# Challenge: Given a string containing '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
def is_valid(s):
    stack = []
    # Map closing brackets to their matching opening brackets
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping: # If it's a closing bracket
            # Pop the top element if stack isn't empty, else use a dummy
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else: # If it's an opening bracket
            stack.append(char)
            
    return not stack # If stack is empty, it's valid

# PROBLEM 2: BACKSPACE STRING COMPARE
# Challenge: Check if two strings are equal when '#' means a backspace.
def backspace_compare(s, t):
    def build(string):
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return "".join(stack)
    
    return build(s) == build(t)

# --- Testing ---
print(f"Is '{{[()]}}' valid? {is_valid('{[()]}')}") # True
print(f"Compare 'ab#c' and 'ad#c': {backspace_compare('ab#c', 'ad#c')}") # True