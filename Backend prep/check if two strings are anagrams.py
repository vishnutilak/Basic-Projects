def are_anagrams(a, b):
    # Anagrams must have same length
    if len(a) != len(b):
        return False

    # Dictionary counting characters in first string
    freq = {}

    for char in a:
        freq[char] = freq.get(char, 0) + 1

    # Decrement for second string
    for char in b:
        if char not in freq:
            return False
        freq[char] -= 1
        if freq[char] < 0:
            return False

    return True
