# Topic: Advanced Hashing and Grouping.
# ==========================================
# DAY 29: HASHING & GROUPING 🔑
# ==========================================

# PROBLEM 1: GROUP ANAGRAMS
# Challenge: Group a list of strings that are anagrams of each other.
# Strategy: Use a sorted string as a Dictionary Key.
def group_anagrams(strs):
    anagram_map = {}
    
    for s in strs:
        # Sort the string to create a unique key
        sorted_s = "".join(sorted(s))
        if sorted_s not in anagram_map:
            anagram_map[sorted_s] = []
        anagram_map[sorted_s].append(s)
        
    return list(anagram_map.values())

# PROBLEM 2: TOP K FREQUENT ELEMENTS
# Challenge: Return the k most frequent elements in a list.
def top_k_frequent(nums, k):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    
    # Sort dictionary by value (frequency) in descending order
    sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_items[:k]]

# --- Testing ---
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"Grouped Anagrams: {group_anagrams(words)}")
print(f"Top 2 frequent in [1,1,1,2,2,3]: {top_k_frequent([1,1,1,2,2,3], 2)}")