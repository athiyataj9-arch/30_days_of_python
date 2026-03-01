# Topic: The Sliding Window Technique (Optimizing Substrings).
# ==========================================
# DAY 30: FINAL CAPSTONE (SLIDING WINDOW) 🏆
# ==========================================

# THE CHALLENGE: LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# This is a classic "hard-level" logic problem.
# Efficiency: O(n) Time | O(min(m, n)) Space
def length_of_longest_substring(s):
    char_map = {} # stores char : last_seen_index
    max_length = 0
    start = 0 # Left pointer of our window
    
    for end in range(len(s)): # Right pointer moves across
        current_char = s[end]
        
        # If we've seen this char and it's inside our current window
        if current_char in char_map and char_map[current_char] >= start:
            # Shrink the window by moving start past the duplicate
            start = char_map[current_char] + 1
            
        # Update the last seen index of the character
        char_map[current_char] = end
        # Calculate current window size and update max
        max_length = max(max_length, end - start + 1)
        
    return max_length

# --- Testing ---
test_str = "abcabcbb"
print(f"Final Challenge: Longest substring of '{test_str}' is {length_of_longest_substring(test_str)}")
# Result should be 3 ("abc")