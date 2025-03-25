def match_pattern(inputS, pattern):
    # Base case: If both input and pattern are empty, it's a match
    if not pattern:
        return not inputS

    # Check if the first character matches or if the pattern starts with '.'
    first_match = bool(inputS) and (pattern[0] == inputS[0] or pattern[0] == '.')

    # Handle '*' in the pattern
    if len(pattern) >= 2 and pattern[1] == '*':
        # Two possibilities:
        # 1. Skip the '*' and its preceding character in the pattern
        # 2. Use the '*' to match the first character of the input (if it matches)
        return (match_pattern(inputS, pattern[2:]) or
                (first_match and match_pattern(inputS[1:], pattern)))

    # Handle normal characters and '.'
    return first_match and match_pattern(inputS[1:], pattern[1:])

# Test cases
print("Input: 'aa', Pattern: 'b*'")
result = match_pattern("aa", "b*")  # Output: False
print("result=", result)

print("Input: 'aa', Pattern: 'a'")
result = match_pattern("aa", "a")  # Output: False
print("result=", result)

print("Input: 'aa', Pattern: 'a*'")
result = match_pattern("aa", "a*")  # Output: True  
print("result=", result)

print("Input: 'aa', Pattern: '.*'")
result = match_pattern("aa", ".*")  # Output: True  
print("result=", result)

print("Input: 'ab', Pattern: '.*'")
result = match_pattern("ab", ".*")  # Output: True  
print("result=", result)

print("Input: 'aab', Pattern: 'c*a*b'")
result = match_pattern("aab", "c*a*b")  # Output: True
print("result=", result)

print("Input: 'mississippi', Pattern: 'mis*is*p*.'")
result = match_pattern("mississippi", "mis*is*p*.")  # Output: False    
print("result=", result)

print("Input: 'mississippi', Pattern: 'mis*is*p*.*'")
result = match_pattern("mississippi", "mis*is*p*.*")  # Output: True   
print("result=", result)

print("Input: 'abc', Pattern: 'a.c'")
result = match_pattern("abc", "a.c")  # Output: True
print("result=", result)

print("Input: 'abc', Pattern: 'a*d'")
result = match_pattern("abc", "a*d")  # Output: False
print("result=", result)
