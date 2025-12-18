"""
String Algorithms Implementation
Includes: Word reversal, palindrome detection, word counting, etc.
"""

import re
from collections import Counter

# 11.1 Reversing the order of words in a sentence
def reverse_words(sentence):
    """
    Reverse the order of words in a sentence - O(n) time
    Example: "Hello World" -> "World Hello"
    """
    words = sentence.split()
    return ' '.join(reversed(words))


def reverse_words_preserve_spaces(sentence):
    """
    Reverse words while preserving multiple spaces
    """
    words = sentence.split(' ')
    return ' '.join(reversed(words))


def reverse_characters_in_words(sentence):
    """
    Reverse characters in each word, keep word order
    Example: "Hello World" -> "olleH dlroW"
    """
    words = sentence.split()
    return ' '.join(word[::-1] for word in words)


# 11.2 Detecting a palindrome
def is_palindrome(s):
    """
    Check if string is a palindrome - O(n) time
    Ignores case and non-alphanumeric characters
    """
    # Remove non-alphanumeric and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def is_palindrome_simple(s):
    """
    Simple palindrome check (case-sensitive, all characters)
    """
    return s == s[::-1]


def is_palindrome_two_pointer(s):
    """
    Two-pointer approach - O(n) time, O(1) space
    """
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True


def longest_palindrome_substring(s):
    """
    Find longest palindromic substring - O(n²) time
    """
    if not s:
        return ""
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    for i in range(len(s)):
        # Odd length palindromes
        palindrome1 = expand_around_center(i, i)
        # Even length palindromes
        palindrome2 = expand_around_center(i, i + 1)
        
        current_longest = palindrome1 if len(palindrome1) > len(palindrome2) else palindrome2
        if len(current_longest) > len(longest):
            longest = current_longest
    
    return longest


# 11.3 Counting the number of words in a string
def count_words(s):
    """
    Count words in a string - O(n) time
    """
    return len(s.split())


def count_words_regex(s):
    """
    Count words using regex (more accurate for punctuation)
    """
    words = re.findall(r'\b\w+\b', s)
    return len(words)


def count_words_manual(s):
    """
    Manual word counting - O(n) time
    """
    count = 0
    in_word = False
    
    for char in s:
        if char.isalnum():
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    
    return count


# 11.4 Determining the number of repeated words within a string
def count_repeated_words(s):
    """
    Count how many words appear more than once - O(n) time
    """
    words = s.lower().split()
    word_count = Counter(words)
    
    # Count words that appear more than once
    repeated = sum(1 for count in word_count.values() if count > 1)
    return repeated


def get_repeated_words_dict(s):
    """
    Get dictionary of repeated words with their counts
    """
    words = s.lower().split()
    word_count = Counter(words)
    
    # Return only words that appear more than once
    return {word: count for word, count in word_count.items() if count > 1}


def most_frequent_word(s):
    """
    Find the most frequently occurring word
    """
    words = s.lower().split()
    if not words:
        return None
    
    word_count = Counter(words)
    return word_count.most_common(1)[0]


# 11.5 Determining the first matching character between two strings
def first_matching_character(s1, s2):
    """
    Find first character that appears in both strings - O(n*m) time
    """
    for char in s1:
        if char in s2:
            return char
    return None


def first_matching_character_optimized(s1, s2):
    """
    Optimized using set - O(n+m) time
    """
    char_set = set(s2)
    
    for char in s1:
        if char in char_set:
            return char
    return None


def all_matching_characters(s1, s2):
    """
    Find all characters that appear in both strings
    """
    return list(set(s1) & set(s2))


def first_non_repeating_character(s):
    """
    Find first character that appears only once - O(n) time
    """
    char_count = Counter(s)
    
    for char in s:
        if char_count[char] == 1:
            return char
    return None


# Additional string algorithms
def is_anagram(s1, s2):
    """
    Check if two strings are anagrams - O(n) time
    """
    return sorted(s1.lower()) == sorted(s2.lower())


def remove_duplicates(s):
    """
    Remove duplicate characters while preserving order - O(n) time
    """
    seen = set()
    result = []
    
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)


def compress_string(s):
    """
    Compress string using run-length encoding - O(n) time
    Example: "aaabbc" -> "a3b2c1"
    """
    if not s:
        return ""
    
    compressed = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            count = 1
    
    compressed.append(s[-1] + str(count))
    
    result = ''.join(compressed)
    return result if len(result) < len(s) else s


def is_rotation(s1, s2):
    """
    Check if s2 is a rotation of s1 - O(n) time
    Example: "waterbottle" is rotation of "erbottlewat"
    """
    if len(s1) != len(s2):
        return False
    
    return s2 in s1 + s1


# Example usage and testing
if __name__ == "__main__":
    print("=== String Algorithms Demo ===\n")
    
    # Reverse words
    print("1. Reversing Words:")
    sentence = "Hello World from Python"
    print(f"  Original: '{sentence}'")
    print(f"  Reversed words: '{reverse_words(sentence)}'")
    print(f"  Reversed chars in words: '{reverse_characters_in_words(sentence)}'")
    
    # Palindrome detection
    print("\n2. Palindrome Detection:")
    test_strings = ["racecar", "A man a plan a canal Panama", "hello", "Madam"]
    for s in test_strings:
        print(f"  '{s}' is {'a palindrome' if is_palindrome(s) else 'not a palindrome'}")
    
    print(f"\n  Longest palindrome in 'babad': '{longest_palindrome_substring('babad')}'")
    
    # Word counting
    print("\n3. Word Counting:")
    text = "The quick brown fox jumps over the lazy dog"
    print(f"  Text: '{text}'")
    print(f"  Word count: {count_words(text)}")
    
    text_with_punct = "Hello, world! How are you?"
    print(f"  Text: '{text_with_punct}'")
    print(f"  Word count (regex): {count_words_regex(text_with_punct)}")
    
    # Repeated words
    print("\n4. Repeated Words:")
    repeated_text = "the cat and the dog and the bird"
    print(f"  Text: '{repeated_text}'")
    print(f"  Number of repeated words: {count_repeated_words(repeated_text)}")
    print(f"  Repeated words: {get_repeated_words_dict(repeated_text)}")
    print(f"  Most frequent word: {most_frequent_word(repeated_text)}")
    
    # First matching character
    print("\n5. First Matching Character:")
    s1, s2 = "hello", "world"
    print(f"  String 1: '{s1}'")
    print(f"  String 2: '{s2}'")
    print(f"  First match: '{first_matching_character(s1, s2)}'")
    print(f"  All matches: {all_matching_characters(s1, s2)}")
    
    # Additional algorithms
    print("\n6. Additional String Algorithms:")
    print(f"  'listen' and 'silent' are anagrams: {is_anagram('listen', 'silent')}")
    print(f"  Remove duplicates from 'hello': '{remove_duplicates('hello')}'")
    print(f"  Compress 'aaabbbccc': '{compress_string('aaabbbccc')}'")
    print(f"  'waterbottle' is rotation of 'erbottlewat': {is_rotation('waterbottle', 'erbottlewat')}")
    print(f"  First non-repeating in 'leetcode': '{first_non_repeating_character('leetcode')}'")
