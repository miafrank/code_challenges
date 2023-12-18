# words_1 = ["flower","flow","flight"]
# words_2 = ["dog","racecar","car"]

# Given a list of str words, find the longest common prefix

# Examples:

# Input: words_1 = ["flower","flow","flight"]
# Output: "fl"

# Option 2:
# Store first word in a variable where each letter is a list [FIRST]
# "flower"
# ['f', 'l', 'o'...]
# Iterate over each word in list
# Iterate over list of current word[index]
# Use any([FIRST], ['f']) -> True
# When above is false
# Store values in variable
# Continue to next word

# Option 0.5:
# Use list comprehension to split first word into list of letters
# Use str substring to validate that all words are substrings of each other
# If not return an empty string

# Option 1:
# Store shortest word in letter const - done
# Store first word in a variable where each letter is a list [FIRST] - done
# Iterate over each word[1: end of list] - done
# Store word in characters list - done
# Iterate over each letter in each word - done
# Validate that first index/character is equal to the [FIRST]

def get_shortest_word(words):
    return min(words, key=len)


def get_result(prefix):
    prefix_dict = {}

    for prefix_letter in prefix:
        if prefix_letter in prefix_dict:
            current_value = prefix_dict.get(prefix_letter)
            prefix_dict[prefix_letter] = current_value + 1
        else:
            prefix_dict[prefix_letter] = 1

    result = {k: v for k, v in prefix_dict.items() if v >
              1 or len(prefix_dict) == 1}

    return ''.join(list(result.keys()))


def get_prefixes(words):
    prefix = ""
    if len(words) == 1:
        return ' '.join(words)

    shortest_word = get_shortest_word(words)
    words.remove(shortest_word)

    shortest_word_characters = list(shortest_word)
    for word in range(len(words)):
        word_as_char_list = list(words[word])
        for word_char in range(len(shortest_word_characters)):
            if word_as_char_list[word_char] == shortest_word_characters[word_char]:
                prefix += word_as_char_list[word_char]
            else:
                return get_result(prefix)
    return get_result(prefix)


def longestCommonPrefix(words):
    return get_prefixes(words)


words_1 = ["flower", "flow", "flight"]
words_2 = ["dog", "racecar", "car"]

# print(longestCommonPrefix(words_1))
# print(longestCommonPrefix(words_2))
# print(longestCommonPrefix(["a"]))
# print(longestCommonPrefix(["ab", "a"]))
# print(longestCommonPrefix(["cir", "car"]))
print(longestCommonPrefix(["aa", "aa"]))
