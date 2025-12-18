/*
 * String Algorithms Implementation in C
 * Includes: Word reversal, palindrome detection, word counting, etc.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

// 11.1 Reversing the order of words in a sentence
void reverse_words(char* sentence) {
    int len = strlen(sentence);
    
    // Reverse entire string
    for (int i = 0; i < len / 2; i++) {
        char temp = sentence[i];
        sentence[i] = sentence[len - 1 - i];
        sentence[len - 1 - i] = temp;
    }
    
    // Reverse each word
    int start = 0;
    for (int i = 0; i <= len; i++) {
        if (sentence[i] == ' ' || sentence[i] == '\0') {
            int end = i - 1;
            while (start < end) {
                char temp = sentence[start];
                sentence[start] = sentence[end];
                sentence[end] = temp;
                start++;
                end--;
            }
            start = i + 1;
        }
    }
}

// 11.2 Detecting a palindrome
bool is_palindrome(const char* s) {
    int len = strlen(s);
    int left = 0, right = len - 1;
    
    while (left < right) {
        // Skip non-alphanumeric characters
        while (left < right && !isalnum(s[left])) left++;
        while (left < right && !isalnum(s[right])) right--;
        
        if (tolower(s[left]) != tolower(s[right])) {
            return false;
        }
        
        left++;
        right--;
    }
    
    return true;
}

bool is_palindrome_simple(const char* s) {
    int len = strlen(s);
    for (int i = 0; i < len / 2; i++) {
        if (s[i] != s[len - 1 - i]) {
            return false;
        }
    }
    return true;
}

// 11.3 Counting the number of words in a string
int count_words(const char* s) {
    int count = 0;
    bool in_word = false;
    
    for (int i = 0; s[i] != '\0'; i++) {
        if (isalnum(s[i])) {
            if (!in_word) {
                count++;
                in_word = true;
            }
        } else {
            in_word = false;
        }
    }
    
    return count;
}

// 11.4 Determining the number of repeated words
typedef struct {
    char word[100];
    int count;
} WordCount;

int count_repeated_words(const char* s) {
    WordCount words[100];
    int word_count = 0;
    char temp[1000];
    strcpy(temp, s);
    
    // Convert to lowercase
    for (int i = 0; temp[i]; i++) {
        temp[i] = tolower(temp[i]);
    }
    
    // Tokenize
    char* token = strtok(temp, " \t\n.,!?;:");
    while (token != NULL) {
        // Check if word already exists
        int found = -1;
        for (int i = 0; i < word_count; i++) {
            if (strcmp(words[i].word, token) == 0) {
                found = i;
                break;
            }
        }
        
        if (found != -1) {
            words[found].count++;
        } else {
            strcpy(words[word_count].word, token);
            words[word_count].count = 1;
            word_count++;
        }
        
        token = strtok(NULL, " \t\n.,!?;:");
    }
    
    // Count words that appear more than once
    int repeated = 0;
    for (int i = 0; i < word_count; i++) {
        if (words[i].count > 1) {
            repeated++;
        }
    }
    
    return repeated;
}

void get_repeated_words(const char* s) {
    WordCount words[100];
    int word_count = 0;
    char temp[1000];
    strcpy(temp, s);
    
    // Convert to lowercase
    for (int i = 0; temp[i]; i++) {
        temp[i] = tolower(temp[i]);
    }
    
    // Tokenize
    char* token = strtok(temp, " \t\n.,!?;:");
    while (token != NULL) {
        int found = -1;
        for (int i = 0; i < word_count; i++) {
            if (strcmp(words[i].word, token) == 0) {
                found = i;
                break;
            }
        }
        
        if (found != -1) {
            words[found].count++;
        } else {
            strcpy(words[word_count].word, token);
            words[word_count].count = 1;
            word_count++;
        }
        
        token = strtok(NULL, " \t\n.,!?;:");
    }
    
    printf("  Repeated words: {");
    bool first = true;
    for (int i = 0; i < word_count; i++) {
        if (words[i].count > 1) {
            if (!first) printf(", ");
            printf("'%s': %d", words[i].word, words[i].count);
            first = false;
        }
    }
    printf("}\n");
}

// 11.5 First matching character between two strings
char first_matching_character(const char* s1, const char* s2) {
    for (int i = 0; s1[i] != '\0'; i++) {
        for (int j = 0; s2[j] != '\0'; j++) {
            if (s1[i] == s2[j]) {
                return s1[i];
            }
        }
    }
    return '\0';
}

// Additional: Check if two strings are anagrams
bool is_anagram(const char* s1, const char* s2) {
    int len1 = strlen(s1);
    int len2 = strlen(s2);
    
    if (len1 != len2) return false;
    
    int count[256] = {0};
    
    for (int i = 0; i < len1; i++) {
        count[tolower(s1[i])]++;
        count[tolower(s2[i])]--;
    }
    
    for (int i = 0; i < 256; i++) {
        if (count[i] != 0) return false;
    }
    
    return true;
}

// Additional: Remove duplicate characters
void remove_duplicates(char* s) {
    int len = strlen(s);
    bool seen[256] = {false};
    int write_index = 0;
    
    for (int i = 0; i < len; i++) {
        if (!seen[(unsigned char)s[i]]) {
            seen[(unsigned char)s[i]] = true;
            s[write_index++] = s[i];
        }
    }
    s[write_index] = '\0';
}

// Additional: String compression (run-length encoding)
void compress_string(const char* s, char* result) {
    int len = strlen(s);
    if (len == 0) {
        result[0] = '\0';
        return;
    }
    
    int write_index = 0;
    int count = 1;
    
    for (int i = 1; i <= len; i++) {
        if (i < len && s[i] == s[i-1]) {
            count++;
        } else {
            result[write_index++] = s[i-1];
            write_index += sprintf(result + write_index, "%d", count);
            count = 1;
        }
    }
    
    result[write_index] = '\0';
    
    // Return original if compressed is longer
    if (strlen(result) >= len) {
        strcpy(result, s);
    }
}

// Additional: Check if s2 is rotation of s1
bool is_rotation(const char* s1, const char* s2) {
    int len1 = strlen(s1);
    int len2 = strlen(s2);
    
    if (len1 != len2) return false;
    
    char* concat = (char*)malloc(2 * len1 + 1);
    strcpy(concat, s1);
    strcat(concat, s1);
    
    bool result = (strstr(concat, s2) != NULL);
    free(concat);
    
    return result;
}

// Main function for testing
int main() {
    printf("=== String Algorithms Demo (C) ===\n\n");
    
    // Reverse words
    printf("1. Reversing Words:\n");
    char sentence[] = "Hello World from C";
    printf("  Original: '%s'\n", sentence);
    reverse_words(sentence);
    printf("  Reversed words: '%s'\n", sentence);
    
    // Palindrome detection
    printf("\n2. Palindrome Detection:\n");
    const char* test_strings[] = {"racecar", "A man a plan a canal Panama", "hello", "Madam"};
    for (int i = 0; i < 4; i++) {
        printf("  '%s' is %s\n", test_strings[i], 
               is_palindrome(test_strings[i]) ? "a palindrome" : "not a palindrome");
    }
    
    // Word counting
    printf("\n3. Word Counting:\n");
    const char* text = "The quick brown fox jumps over the lazy dog";
    printf("  Text: '%s'\n", text);
    printf("  Word count: %d\n", count_words(text));
    
    // Repeated words
    printf("\n4. Repeated Words:\n");
    const char* repeated_text = "the cat and the dog and the bird";
    printf("  Text: '%s'\n", repeated_text);
    printf("  Number of repeated words: %d\n", count_repeated_words(repeated_text));
    get_repeated_words(repeated_text);
    
    // First matching character
    printf("\n5. First Matching Character:\n");
    const char* s1 = "hello";
    const char* s2 = "world";
    printf("  String 1: '%s'\n", s1);
    printf("  String 2: '%s'\n", s2);
    char match = first_matching_character(s1, s2);
    if (match != '\0') {
        printf("  First match: '%c'\n", match);
    } else {
        printf("  No match found\n");
    }
    
    // Additional algorithms
    printf("\n6. Additional String Algorithms:\n");
    printf("  'listen' and 'silent' are anagrams: %s\n", 
           is_anagram("listen", "silent") ? "true" : "false");
    
    char dup_str[] = "hello";
    remove_duplicates(dup_str);
    printf("  Remove duplicates from 'hello': '%s'\n", dup_str);
    
    char compressed[100];
    compress_string("aaabbbccc", compressed);
    printf("  Compress 'aaabbbccc': '%s'\n", compressed);
    
    printf("  'waterbottle' is rotation of 'erbottlewat': %s\n",
           is_rotation("waterbottle", "erbottlewat") ? "true" : "false");
    
    return 0;
}
