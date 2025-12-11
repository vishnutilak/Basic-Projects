def longest_unique_substring(s):
    seen = {}
    left = 0
    longest = 0

    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        seen[ch] = right
        longest = max(longest, right - left + 1)

    return longest
