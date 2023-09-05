
# # Q1. Write a Python function is_palindrome(s) that takes a string s as input and returns True if the string is a palindrome (reads the same forwards and backwards), and False otherwise.

# def is_palindrome(s):
#     s = s.lower().replace(" ", "")  
#     return s == s[::-1]

# print(is_palindrome("Tirth"))
# print(is_palindrome("raceCaR"))

# # Q2. Write a Python function factorial(n) that calculates and returns the factorial of a non-negative integer n.

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(5))
# # Q3. Write a Python function word_count(sentence) that takes a sentence as input and returns a dictionary where keys are words and values are the counts of those words in the sentence.

# # Examples
# # test_case_1 = "The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog"
# # test_case_2 = "Hello world This is a test Hello world"
# # test_case_3 = "Python Python python python programming Programming is FUN!"

# # Outputs:
# # {'the': 4, 'quick': 2, 'brown': 2, 'fox': 2, 'jumps': 2, 'over': 2, 'lazy': 2, 'dog': 2}
# # {'hello': 2, 'world': 2, 'this': 1, 'is': 1, 'a': 1, 'test': 1}
# # {'python': 4, 'programming': 2, 'is': 1, 'fun': 1}

# # These are just examples for better understanding.
# sentence="The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog"
# def word_count(sentence):
#     words = sentence.lower().split()
#     word_dict = {}
    
#     for word in words:
#         word_dict[word] = word_dict.get(word, 0) + 1
#     print(word_dict)
# word_count(sentence)

# # Q4. Write a Python function flatten_list(nested_list) that takes a nested list as input and returns a flattened version of the list.
# # Examples:
# # nested_list_1 = [1, [2, 3, [4, 5]], 6, [7, 8]]
# # nested_list_2 = [1, [2, [3, [4, [5]]]]]
# # nested_list_3 = [1, 2, 3, 4, 5]

# Outputs:
# [1, 2, 3, 4, 5, 6, 7, 8]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
arr=[1, [2, 3, [4, 5]], 6, [7, 8]]
def flatten_list(nested_list):
    flat_list = []
    def flatten(nested_list):
    
        for i in nested_list:
            if type(i) == list:
                flatten(i)
            else:
                flat_list.append(i)
    flatten(nested_list)
    return flat_list
print(flatten_list(arr))
  
