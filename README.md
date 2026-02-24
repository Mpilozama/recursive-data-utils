WeThinkCode Mock Test 3 – Recursion, Data Structures, and String Formatting

Instructions:

Time limit: 120 minutes (adjust as needed for extra questions).

Solve each function according to the rules.

Pay attention to exact string formatting and edge cases.

You can complete questions in any order.

Question 1 – Nested Sum

Write a recursive function nested_sum(lst) that calculates the sum of numbers in a nested list.

# Example:
# nested_sum([1, [2, 3], [4, [5]]]) -> 15
# nested_sum([]) -> 0

Requirements:

Must handle arbitrarily deep nested lists.

Must use recursion; no itertools or flattening tricks.

Question 2 – Reverse Dictionary

Write a function reverse_dict(d) that takes a dictionary where keys are strings and values are integers, and returns a new dictionary where: 

The keys are the values from the original dictionary.

The values are lists of original keys that had that value.

# Example:
# reverse_dict({'a':1,'b':2,'c':1}) -> {1:['a','c'], 2:['b']}

Requirements:

Preserve the order of keys in lists as they appear in the original dict.

Question 3 – Fibonacci Check

Write a recursive function is_fibonacci(n) that returns True if n is a Fibonacci number, False otherwise.

# Example:
# is_fibonacci(13) -> True
# is_fibonacci(14) -> False

Constraints:

Must be recursive.

Do not use loops.

Optimize by using helper parameters if needed to track sequence position.

Question 4 – Deep Flatten

Write a recursive function deep_flatten(lst) that returns a single-level list of all elements in a nested list.

# Example:
# deep_flatten([1, [2, [3, 4], 5], 6]) -> [1,2,3,4,5,6]
Question 5 – String Pattern Printer

Write a function pyramid_pattern(s) that prints a pyramid of letters from a string.

Each row adds one more letter.

Align left.

# Example:
# pyramid_pattern("WTC") prints:
# W
# WT
# WTC

Input: Any non-empty string.

Question 6 – Max Consecutive Duplicate

Write a function max_consecutive(lst) that returns the highest number of consecutive duplicate elements in a list.

# Example:
# max_consecutive([1,1,2,2,2,3,3,3,3,2]) -> 4
# max_consecutive([]) -> 0

Works for numbers or strings.

Can be iterative or recursive.

Question 7 – Dictionary Filter

Write a function filter_dict(d, threshold) that returns a new dictionary containing only the key-value pairs where the value is greater than or equal to threshold.

# Example:
# filter_dict({'a':5,'b':3,'c':10}, 5) -> {'a':5,'c':10}

Preserve the order of keys as they appear.

Question 8 – Nested Max Depth

Write a recursive function max_depth(lst) that calculates the maximum depth of a nested list.

# Example:
# max_depth([1, [2,3], [4, [5]]]) -> 3
# max_depth([]) -> 1

A flat list has depth 1.

Handle empty lists inside nested lists correctly.

Question 9 – Recursive String Reverser

Write a function reverse_words_rec(sentence) that reverses words in a sentence using recursion.

# Example:
# reverse_words_rec("This is a test") -> "test a is This"

Do not reverse letters inside words.

Must use recursion (no built-in split + reverse trick alone).

Question 10 – Bonus: Matrix Column Sum

Write a function column_sum(matrix) that takes a 2D list (matrix) and returns a list of sums of each column.

# Example:
# column_sum([[1,2,3],[4,5,6],[7,8,9]]) -> [12,12,18]

Works with any number of rows/columns.

Should handle empty matrix ([]) → returns [].