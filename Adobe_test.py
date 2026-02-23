from collections import defaultdict

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""
import collections
from collections import defaultdict


def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num]= i
    return []

# Example usage:
nums = [2,7,11,15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]


list = [1, 0, 3, 4, 5]
for i, v in enumerate(list):
# print the index of the first item smaller than the prev item
    if i > 0 and v < list[i-1]:
        print(i)
        break

#create 3x3 matrix with random integers between 1 and 10 and print the transpose of the matrix
import random
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(random.randint(1, 10))
    matrix.append(row)
print("Original matrix:")
for row in matrix:
    print(row)
print("Transpose of the matrix:")
transpose = []
for j in range(3):
    new_row = []
    for i in range(3):
        new_row.append(matrix[i][j])
    transpose.append(new_row)
for row in transpose:
    print(row)


"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
# def group_anagrams(strs):
#     ans = defaultdict(list)
#     for s in strs:
#         key ="".join(sorted(s))
#         ans[key].append(s)
#     return list(ans.values())

# Example usage:
# strs = ["eat","tea","tan","ate","nat","bat"]
# # result = group_anagrams(strs)
# print(result)  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


"""Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

Constraints:

1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
"""
def top_k_frequent(words, k):
    count = defaultdict(int)
    for word in words:
        count[word] += 1
    sorted_words = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    return [word for word, freq in sorted_words[:k]]
# Example usage:
words = ["i","love","leetcode","i","love","coding"]
k = 2
result = top_k_frequent(words, k)
print(result)  # Output: ["i","love"]



"""Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

 

Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
Example 3:

Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:

Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^
Example 5:

Input: s = "words and 987"

Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.

 

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'."""
def myAtoi(s):
    s = s.strip()
    if not s:
        return 0
    sign = 1
    if s[0] in ['-','+']:
        if s[0] == '-':
            sign = -1
        s = s[1:]
    result = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break
    result *= sign
    return max(-2**31, min(result, 2**31 - 1))

# Example usage:
s = " -042"
result = myAtoi(s)


"""Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?"""
def isPalindrome(x):
    if x < 0:
        return False
    original = x
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    return original == reversed_num
# Example usage:
x = 121
result = isPalindrome(x)
print("palindrome", result)

"""Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1"""
def longestIncreasingPath(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    cache = [[0] * n for _ in range(m)]

    def dfs(i, j):
        if cache[i][j] != 0:
            return cache[i][j]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        max_length = 1
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                length = 1 + dfs(ni, nj)
                max_length = max(max_length, length)
        cache[i][j] = max_length
        return max_length

    longest_path = 0
    for i in range(m):
        for j in range(n):
            longest_path = max(longest_path, dfs(i, j))
    return longest_path
# Example usage:
matrix = [[9,9,4],[6,6,8],[2,1,1]]
result = longestIncreasingPath(matrix)
print("lengest path", result)

# given a tree and a target sum, return true if there is a path from root to leaf that equals the target sum, otherwise return false
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def hasPathSum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == targetSum
    targetSum -= root.val
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)
# Example usage:
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
targetSum = 22
result = hasPathSum(root, targetSum)
print("has path sum", result)

"""Given a tree return the depth of the tree. The depth of a tree is the number of nodes along the longest path from the root node down to the farthest leaf node."""
def maxDepth(root):
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1
# Example usage:
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
result = maxDepth(root)
print("max depth", result)

"""You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 

Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
"""
import random
class Solution:
    def __init__(self, w):
        self.prefix_sums = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sums.append(current_sum)

    def pickIndex(self):
        target = random.randint(1, self.prefix_sums[-1])
        left, right = 0, len(self.prefix_sums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
# Example usage:
solution = Solution([1, 3])
print(solution.pickIndex())  # Output: 1 (with probability 0.75)
"""given the list of list, return a flattened list of all the elements in the list of list"""
def flatten(lst):
    result = []
    for sublist in lst:
        for item in sublist:
            result.append(item)
    return result
# Example usage:
lst = [[1, 2], [3, 4], [5, 6]]
result = flatten(lst)
print("flattened list", result)

"""Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters."""


def longestPalindrome(s: str) -> str:
    res = ""

    for i in range(len(s)):
        # Odd length
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(res):
                res = s[l:r + 1]
            l -= 1
            r += 1

        # Even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(res):
                res = s[l:r + 1]
            l -= 1
            r += 1

    return res
# Example usage:
s = "babad"
result = longestPalindrome(s)
print("longest palindrome", result)

"""Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0."""
def removeKdigits(num: str, k: int) -> str:
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    while k > 0:
        stack.pop()
        k -= 1
    result = ''.join(stack).lstrip('0')
    return result if result else '0'
# Example usage:
num = "1432219"
k = 3
result = removeKdigits(num, k)
print("smallest number", result)

"""You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
# Example usage:

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("original matrix:", [[1,2,3],[4,5,6],[7,8,9]])
rotate(matrix)
print("rotated matrix:")
for row in matrix:
    print(row)

"""Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
def spiralOrder(matrix):
    if not matrix:
        return []
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

# Example usage:
matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = spiralOrder(matrix)
print("spiral order", result)

"""Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters."""
def firstUniqChar(s):
    char_count = defaultdict(int)
    print(char_count)
    for char in s:
        print(char)
        char_count[char] += 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            print(char, char_count[char])
            return i
    return -1
# Example usage:
s = "leetcode"
result = firstUniqChar(s)
print("first unique character index", result)

"""Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string."""
def minWindow(s, t):
    if not s or not t:
        return ""

    dict_t = defaultdict(int)
    for char in t:
        dict_t[char] += 1

    required = len(dict_t)
    l, r = 0, 0
    formed = 0
    window_counts = defaultdict(int)
    ans = float("inf"), None, None

    while r < len(s):
        character = s[r]
        window_counts[character] += 1

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        while l <= r and formed == required:
            character = s[l]
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            l += 1

        r += 1

    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

"""You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104."""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
def mergeKLists(lists):
    min_heap = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i].val, i))

    dummy = ListNode(0)
    current = dummy

    while min_heap:
        val, idx = heapq.heappop(min_heap)
        current.next = ListNode(val)
        current = current.next
        if lists[idx].next:
            lists[idx] = lists[idx].next
            heapq.heappush(min_heap, (lists[idx].val, idx))

    return dummy.next
# Example usage:
lists = [[1,4,5],[1,3,4],[2,6]]
# Convert lists of integers to linked lists
linked_lists = []
for lst in lists:
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    linked_lists.append(dummy.next)
result = mergeKLists(linked_lists)
# Convert the resulting linked list back to a list of integers for display
merged_list = []
while result:
    merged_list.append(result.val)
    result = result.next
print("merged linked list:", merged_list)

"""You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""
def maxAreaOfIsland(grid):
    if not grid:
        return 0

    max_area = 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0
        grid[r][c] = 0  # Mark as visited
        area = 1
        area += dfs(r + 1, c)
        area += dfs(r - 1, c)
        area += dfs(r, c + 1)
        area += dfs(r, c - 1)
        return area

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))

    return max_area