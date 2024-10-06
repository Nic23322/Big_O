"""
Student information for this assignment:

On my/our honor, Nicholas Selesi and Tise Mobuse, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: nos264
UT EID 2: ojm437
"""


def length_of_longest_substring_n3(s):

    """
    Finds the length of the longest substring without repeating characters
    using a brute force approach (O(N^3)).

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
        in s that contains no repeating characters.
    """
    my_list = []
    max_len = 0
    for i in range(len(s)):
        for j in range(i, len(s)):  # prevents unnecessary checking
            if s[j] in s[i:j]:
                break
            else:
                my_list = s[i:j + 1]  # Removed unnecessary parentheses
                if len(my_list) > max_len:
                    max_len = len(my_list)
    return max_len


def length_of_longest_substring_n2(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N^2)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
        in s that contains no repeating characters.
    """
    frequency = {}
    substrings = []
    max_len = 0

    for char in s:
        frequency[char] = 0

    for i in range(len(s)):
        frequency_copy = frequency.copy()
        for j in range(i, len(s)):  # prevents unnecessary checking
            frequency_copy[s[j]] += 1
            if frequency_copy[s[j]] > 1:
                j -= 1
                break
        substrings.append(s[i:j + 1]) # Appends the substring into a list, including last char

    for substr in substrings:
        if len(substr) > max_len:
            max_len = len(substr)

    return max_len



# TODO: implement this function. You may delete this comment when you are done.
def length_of_longest_substring_n(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list. However, this approach stops early, breaking out of the inner
    loop when a repeating character is found. You may also choose to challenge
    yourself by implementing a sliding window approach.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
        in s that contains no repeating characters.
    """
