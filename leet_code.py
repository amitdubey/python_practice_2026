"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

def twosum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

"""You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string."""

def merge_strings(word1, word2):
    merged = []
    len1, len2 = len(word1), len(word2)
    for i in range(max(len1, len2)):
        if i < len1:
            merged.append(word1[i])
        if i < len2:
            merged.append(word2[i])
    return ''.join(merged)

"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""
def canFinish(numCourses, prerequisites):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    visited_courses = 0

    while queue:
        course = queue.popleft()
        visited_courses += 1
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return visited_courses == numCourses

print(canFinish(2, [[1,0],[0,1]]))

"""
Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.

 

Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true
"""
def canPermutePalindrome(s):
    from collections import Counter
    count = Counter(s)
    odd_count = sum(1 for freq in count.values() if freq % 2 != 0)
    return odd_count <= 1
print(canPermutePalindrome("code"))

"""
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
def numberToWords(num):
    if num == 0:
        return "Zero"

    def one(num):
        switcher = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }
        return switcher.get(num)

    def two_less_20(num):
        switcher = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        return switcher.get(num)

    def ten(num):
        switcher = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }
        return switcher.get(num)

    def helper(num):
        if num == 0:
            return ""
        elif num < 10:
            return one(num) + " "
        elif num < 20:
            return two_less_20(num) + " "
        elif num < 100:
            return ten(num // 10) + " " + helper(num % 10)
        else:
            return one(num // 100) + " Hundred " + helper(num % 100)

    billion = num // 1000000000
    million = (num - billion * 1000000000) // 1000000
    thousand = (num - billion * 1000000000 - million * 1000000) // 1000
    remainder = num % 1000

    result = ""
    if billion:
        result += helper(billion) + "Billion "
    if million:
        result += helper(million) + "Million "
    if thousand:
        result += helper(thousand) + "Thousand "
    if remainder:
        result += helper(remainder)
    return result.strip()
print(numberToWords(1234567))

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
print(longestCommonPrefix(["flower","flow","flight"]))

"""
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
 

Example 1:

Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]

Explanation
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.
"""
class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.pop(0)
        return len(self.hits)


hitCounter = HitCounter()

hitCounter.hit(1)       # hit at timestamp 1.
hitCounter.hit(2)       # hit at timestamp 2.

"""
An IP address is a formatted 32-bit unsigned integer where each group of 8 bits is printed as a decimal number and the dot character '.' splits the groups.

For example, the binary number 00001111 10001000 11111111 01101011 (spaces added for clarity) formatted as an IP address would be "15.136.255.107".
A CIDR block is a format used to denote a specific set of IP addresses. It is a string consisting of a base IP address, followed by a slash, followed by a prefix length k. The addresses it covers are all the IPs whose first k bits are the same as the base IP address.

For example, "123.45.67.89/20" is a CIDR block with a prefix length of 20. Any IP address whose binary representation matches 01111011 00101101 0100xxxx xxxxxxxx, where x can be either 0 or 1, is in the set covered by the CIDR block.
You are given a start IP address ip and the number of IP addresses we need to cover n. Your goal is to use as few CIDR blocks as possible to cover all the IP addresses in the inclusive range [ip, ip + n - 1] exactly. No other IP addresses outside of the range should be covered.

Return the shortest list of CIDR blocks that covers the range of IP addresses. If there are multiple answers, return any of them.

 

Example 1:

Input: ip = "255.0.0.7", n = 10
Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
Explanation:
The IP addresses that need to be covered are:
- 255.0.0.7  -> 11111111 00000000 00000000 00000111
- 255.0.0.8  -> 11111111 00000000 00000000 00001000
- 255.0.0.9  -> 11111111 00000000 00000000 00001001
- 255.0.0.10 -> 11111111 00000000 00000000 00001010
- 255.0.0.11 -> 11111111 00000000 00000000 00001011
- 255.0.0.12 -> 11111111 00000000 00000000 00001100
- 255.0.0.13 -> 11111111 00000000 00000000 00001101
- 255.0.0.14 -> 11111111 00000000 00000000 00001110
- 255.0.0.15 -> 11111111 00000000 00000000 00001111
- 255.0.0.16 -> 11111111 00000000 00000000 00010000
The CIDR block "255.0.0.7/32" covers the first address.
The CIDR block "255.0.0.8/29" covers the middle 8 addresses (binary format of 11111111 00000000 00000000 00001xxx).
The CIDR block "255.0.0.16/32" covers the last address.
Note that while the CIDR block "255.0.0.0/28" does cover all the addresses, it also includes addresses outside of the range, so we cannot use it.
Example 2:

Input: ip = "117.145.102.62", n = 8
Output: ["117.145.102.62/31","117.145.102.64/30","117.145.102.68/31"]
"""
def ipToCIDR(ip, n):
    def ip_to_int(ip):
        parts = list(map(int, ip.split('.')))
        return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]

    def int_to_ip(num):
        return f"{(num >> 24) & 255}.{(num >> 16) & 255}.{(num >> 8) & 255}.{num & 255}"

    result = []
    start = ip_to_int(ip)

    while n > 0:
        step = start & -start
        while step > n:
            step >>= 1
        prefix_length = 32 - step.bit_length() + 1
        result.append(f"{int_to_ip(start)}/{prefix_length}")
        start += step
        n -= step

    return result

print(ipToCIDR("255.0.0.7",10))

"""
iven an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
"""
def firstMissingPositive(nums):
    n = len(nums)

    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1
print(firstMissingPositive([3,4,-1,1]))


"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

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
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
print(twoSum([2,7,11,15],9))

"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""
def maxProduct(nums):
    if not nums:
        return 0

    max_prod = min_prod = result = nums[0]

    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)

        result = max(result, max_prod)

    return result
print(maxProduct([2,3,-2,4]))

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""
def romanToInt(s):
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total
print(romanToInt("MCMXCIV"))

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next

list1 = ListNode(1, ListNode(2, ListNode(4)))

"""
Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.
 

Example 1:

Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false
 

Constraints:

-105 <= number <= 105
-231 <= value <= 231 - 1
At most 104 calls will be made to add and find.
"""
class TwoSum:

    def __init__(self):
        self.nums = []
        self.num_set = set()

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.num_set.add(number)

    def find(self, value: int) -> bool:
        for num in self.nums:
            complement = value - num
            if complement in self.num_set:
                if complement != num or self.nums.count(num) > 1:
                    return True
        return False

twoSum = TwoSum()
twoSum.add(1)   # [] --> [1]
twoSum.add(3)   # [1] --> [1,3]
twoSum.add(5)   # [1,3] --> [1,3,5]
print(twoSum.find(4))  # 1 + 3 = 4, return true
print(twoSum.find(7))  # No two integers sum up to 7, return false


"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
def spiralOrder(matrix):
    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20"""
def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top, bottom = 0, n - 1
    left, right = 0, n - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix
print(generateMatrix(3))


"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

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

    return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))

"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
"""

def findDiagonalOrder(mat):
    if not mat:
        return []

    m, n = len(mat), len(mat[0])
    result = []
    for d in range(m + n - 1):
        if d % 2 == 0:
            r = min(d, m - 1)
            c = d - r
            while r >= 0 and c < n:
                result.append(mat[r][c])
                r -= 1
                c += 1
        else:
            c = min(d, n - 1)
            r = d - c
            while c >= 0 and r < m:
                result.append(mat[r][c])
                r += 1
                c -= 1

    return result
print(findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))

"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 

Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

"""
def matrixReshape(mat, r, c):
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        return mat

    flat = [num for row in mat for num in row]
    reshaped = [flat[i * c:(i + 1) * c] for i in range(r)]

    return reshaped
print(matrixReshape([[1,2],[3,4]],1,4))

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

def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
print(twoSum([2,7,11,15],9))

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""
def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
print(longestCommonPrefix(["flower","flow","flight"]))

"""
You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

Return the total number of good pairs.

 

Example 1:

Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1

Output: 5

Explanation:

The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).
Example 2:

Input: nums1 = [1,2,4,12], nums2 = [2,4], k = 3

Output: 2

Explanation:

The 2 good pairs are (3, 0) and (3, 1).

 

Constraints:

1 <= n, m <= 50
1 <= nums1[i], nums2[j] <= 50
1 <= k <= 50
"""
def countPairs(nums1, nums2, k):
    count = 0
    for num1 in nums1:
        for num2 in nums2:
            if num1 % (num2 * k) == 0:
                count += 1
    return count

"""
You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

Return the total number of good pairs.

 

Example 1:

Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1

Output: 5

Explanation:

The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).
Example 2:

Input: nums1 = [1,2,4,12], nums2 = [2,4], k = 3

Output: 2

Explanation:

The 2 good pairs are (3, 0) and (3, 1).

 

Constraints:

1 <= n, m <= 105
1 <= nums1[i], nums2[j] <= 106
1 <= k <= 103
"""
def countPairs(nums1, nums2, k):
    from collections import Counter

    count = 0
    freq_map = Counter(num // k for num in nums2 if num % k == 0)

    for num in nums1:
        count += freq_map.get(num, 0)

    return count
print(countPairs([1,3,4],[1,3,4],1))

"""
You are given an integer array nums of size n where n is even, and an integer k.

You can perform some changes on the array, where in one change you can replace any element in the array with any integer in the range from 0 to k.

You need to perform some changes (possibly none) such that the final array satisfies the following condition:

There exists an integer X such that abs(a[i] - a[n - i - 1]) = X for all (0 <= i < n).
Return the minimum number of changes required to satisfy the above condition.

 

Example 1:

Input: nums = [1,0,1,2,4,3], k = 4

Output: 2

Explanation:
We can perform the following changes:

Replace nums[1] by 2. The resulting array is nums = [1,2,1,2,4,3].
Replace nums[3] by 3. The resulting array is nums = [1,2,1,3,4,3].
The integer X will be 2.

Example 2:

Input: nums = [0,1,2,3,3,6,5,4], k = 6

Output: 2

Explanation:
We can perform the following operations:

Replace nums[3] by 0. The resulting array is nums = [0,1,2,0,3,6,5,4].
Replace nums[4] by 4. The resulting array is nums = [0,1,2,0,4,6,5,4].
The integer X will be 4.

 

Constraints:

2 <= n == nums.length <= 105
n is even.
0 <= nums[i] <= k <= 105
"""


def minChanges( nums, k):
    n = len(nums)
    change_count = [0] * (k + 2)
    change_count[0] = n // 2

    for i in range(n // 2):
        left = nums[i]
        right = nums[n - i - 1]
        cur_diff = abs(left - right)
        max_diff = max(left, right, k - left, k - right)

        change_count[cur_diff] -= 1
        change_count[cur_diff + 1] += 1
        change_count[max_diff + 1] += 1

    cur_changes = 0
    min_changes = n // 2
    for i in range(k + 1):
        cur_changes += change_count[i]
        min_changes = min(min_changes, cur_changes)

    return min_changes
print(minChanges([1,0,1,2,4,3],4))



"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""

def partitionLabels(s):
    last_occurrence = {char: i for i, char in enumerate(s)}
    partitions = []
    start, end = 0, 0

    for i, char in enumerate(s):
        end = max(end, last_occurrence[char])
        if i == end:
            partitions.append(i - start + 1)
            start = i + 1

    return partitions

print(partitionLabels("ababcbacadefegdehijhklij"))

"""
DataFrame products
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| quantity    | int    |
| price       | int    |
+-------------+--------+
Write a solution to fill in the missing value as 0 in the quantity column.

The result format is in the following example.

 

Example 1:
Input:+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | None     | 135   |
| WirelessEarbuds | None     | 821   |
| GolfClubs       | 779      | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
Output:
+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | 0        | 135   |
| WirelessEarbuds | 0        | 821   |
| GolfClubs       | 779      | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
Explanation: 
The quantity for Wristwatch and WirelessEarbuds are filled by 0.
"""
# def fill_missing_quantity(products):
#     products['quantity'] = products['quantity'].fillna(0)
#     return products
# products =[1,2,3,None]
# print(fill_missing_quantity(products))


"""
You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.

Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.

Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.

 

Example 1:

Input: rolls = [3,2,4,3], mean = 4, n = 2
Output: [6,6]
Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
Example 2:

Input: rolls = [1,5,6], mean = 3, n = 4
Output: [2,3,2,2]
Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.
Example 3:

Input: rolls = [1,2,3,4], mean = 6, n = 4
Output: []
Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.
 

Constraints:

m == rolls.length
1 <= n, m <= 105
1 <= rolls[i], mean <= 6"""

def missingRolls(rolls, mean, n):
    m = len(rolls)
    total_sum = mean * (n + m)
    current_sum = sum(rolls)
    missing_sum = total_sum - current_sum

    if missing_sum < n or missing_sum > 6 * n:
        return []

    base_value = missing_sum // n
    remainder = missing_sum % n

    result = [base_value] * n
    for i in range(remainder):
        result[i] += 1

    return result
print(missingRolls([3,2,4,3],4,2))

def searchrange(nums,target):
    def find_left(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def find_right(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left_index = find_left(nums, target)
    right_index = find_right(nums, target)

    if left_index <= right_index:
        return [left_index, right_index]
    else:
        return [-1, -1]


"""Given a string s, return whether s is a valid number.

For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

Formally, a valid number is defined using one of the following definitions:

An integer number followed by an optional exponent.
A decimal number followed by an optional exponent.
An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

Digits followed by a dot '.'.
Digits followed by a dot '.' followed by digits.
A dot '.' followed by digits.
An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.

 

Example 1:

Input: s = "0"

Output: true

Example 2:

Input: s = "e"

Output: false

Example 3:

Input: s = "."

Output: false

 

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'."""
def isNumber(s):
    s = s.strip()
    if not s:
        return False

    num_seen = False
    dot_seen = False
    e_seen = False
    num_after_e = True

    for i, char in enumerate(s):
        if char.isdigit():
            num_seen = True
            num_after_e = True
        elif char == '.':
            if dot_seen or e_seen:
                return False
            dot_seen = True
        elif char in ('e', 'E'):
            if e_seen or not num_seen:
                return False
            e_seen = True
            num_after_e = False
        elif char in ('+', '-'):
            if i != 0 and s[i - 1] not in ('e', 'E'):
                return False
        else:
            return False

    return num_seen and num_after_e


def odd_even(a):
    odd = [x for x in a if x % 2 != 0]
    even = [x for x in a if x % 2 == 0]
    return odd + even
print(odd_even([1,2,3,4,5,6,7,8,9]))

def delete_duplicates(A):
    if not A:
        return 0
    write_index =1
    for i in range(1, len(A)):
        if A[write_index-1] !=A[i]:
            A[write_index]=A[i]
            write_index +=1
    return write_index
print(delete_duplicates([1,1,2,2,3,4,4,5]))
# def remove_element(nums,val):
#     write_index =0
#     for i in range(len(nums)):
#         if nums[i] !=val:
#             nums[write_index]=nums[i]
#             write_index +=1
#     return write_index
# print(remove_element([3,2,2,3],3))

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
print(max_profit([7,1,5,3,6,4]))

def is_palindrome(s):

    return s == s[::-1]
s= "racecar"
print(is_palindrome(s))

def reverse_words(s):
    return ' '.join(reversed(s.split()))
print(reverse_words("the sky is blue"))


"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 
"""

def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n

    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]

    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer
print(productExceptSelf([1,2,3,4]))


"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head):
    if not head or not head.next:
        return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next

    return head
head = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
print(head.val)
deleteMiddle(head)


def mergeAlternate(list1, list2):
    i =0
    j= 0
    result =[]
    while i< len(list1) and j < len(list2):
        result.append(list1[i])
        result.append(list2[j])
        i +=1
        j +=1
    return "".join(result)
print(mergeAlternate("abc","pqr"))

"""
create a singly liked list with insert at the beginging, insert at the end, delete a node,insert a node after a given node, display the linked list, find the length of the linked list, find circle in the linked list
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if not temp:
            return
        prev.next = temp.next
        temp = None

    def insert_after_node(self, prev_node, data):
        # Check if the given previous node exists
        if not prev_node:
            print("The given previous node must be in LinkedList.")
            return
        #
        new_node = Node(data)
        #
        new_node.next = prev_node.next
        prev_node.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
sll = SinglyLinkedList()
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_beginning(0)
sll.insert_after_node(sll.head.next, 1.5)
sll.display()
print("Length of linked list:", sll.length())
print("Has cycle:", sll.has_cycle())
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = reverse_linked_list(head)
temp = reversed_head
while temp:
    print(temp.val, end=" -> ")
    temp = temp.next
print("None")
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    for _ in range(n + 1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next

    return dummy.next
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new_head = remove_nth_from_end(head, 2)

"""
write a python code to create doubly linked list with insert at beginging, insert at the end, delete a node, insert a node after a given node, display the linked list in both forward and backward direction, find the length of the linked list, find circle in the linked list
"""
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            temp = None
            return
        while temp and temp.data != key:
            temp = temp.next
        if not temp:
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
        temp = None

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("The given previous node must be in LinkedList.")
            return
        new_node = DoublyNode(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            last = temp
            temp = temp.next
        print("None")
        return last

    def display_backward(self):
        last = self.display_forward()
        while last:
            print(last.data, end=" <-> ")
            last = last.prev
        print("None")

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_beginning(0)
dll.insert_after_node(dll.head.next, 1.5)
dll.display_forward()
dll.display_backward()
print("Length of linked list:", dll.length())
print("Has cycle:", dll.has_cycle())
def reverse_doubly_linked_list(head):
    current = head
    prev = None
    while current:
        prev = current.prev
        current.prev = current.next
        current.next = prev
        current = current.prev
    if prev:
        head = prev.prev
    return head
head = DoublyNode(1)
head.next = DoublyNode(2)
head.next.prev = head
head.next.next = DoublyNode(3)
head.next.next.prev = head.next
reversed_head = reverse_doubly_linked_list(head)
temp = reversed_head
while temp:
    print(temp.data, end=" <-> ")
    temp = temp.next
print("None")
def remove_nth_from_end_doubly(head, n):
    dummy = DoublyNode(0)
    dummy.next = head
    if head:
        head.prev = dummy
    first = dummy
    second = dummy

    for _ in range(n + 1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    if second.next:
        second.next = second.next.next
        if second.next:
            second.next.prev = second

    return dummy.next
head = DoublyNode(1)
head.next = DoublyNode(2)
head.next.prev = head
head.next.next = DoublyNode(3)
head.next.next.prev = head.next
new_head = remove_nth_from_end_doubly(head, 2)
temp = new_head
while temp:
    print(temp.data, end=" <-> ")
    temp = temp.next
print("None")

def spiralOrder(matrix):
    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result
print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top, bottom = 0, n - 1
    left, right = 0, n - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    return matrix
print(generateMatrix(3))
def canJump(nums):
    max_reachable = 0
    for i, jump in enumerate(nums):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + jump)
    return True

"""
create a binary tree, insert a node, delete a node, search a node, inorder traversal, preorder traversal, postorder traversal, level order traversal, find the height of the tree, find the minimum value in the tree, find the maximum value in the tree, check if the tree is a valid binary search tree, find the lowest common ancestor of two nodes in the tree, find if the tree  is a mirror,, find the depth of the tree, perform breath first and depoth first traversal. 
"""
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
            return
        self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_rec(node.left, key)
        return self._search_rec(node.right, key)

    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, node, key):
        if node is None:
            return node
        if key < node.val:
            node.left = self._delete_rec(node.left, key)
        elif key > node.val:
            node.right = self._delete_rec(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete_rec(node.right, temp.val)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        return self._inorder_rec(self.root)

    def _inorder_rec(self, node):
        return self._inorder_rec(node.left) + [node.val] + self._inorder_rec(node.right) if node else []

    def preorder(self):
        return self._preorder_rec(self.root)

    def _preorder_rec(self, node):
        return [node.val] + self._preorder_rec(node.left) + self._preorder_rec(node.right) if node else []

    def postorder(self):
        return self._postorder_rec(self.root)

    def _postorder_rec(self, node):
        return self._postorder_rec(node.left) + self._postorder_rec(node.right) + [node.val] if node else []
    def level_order(self):
        if not self.root:
            return []
        result, queue = [], [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
    def height(self):
        return self._height_rec(self.root)
    def _height_rec(self, node):
        if node is None:
            return -1
        left_height = self._height_rec(node.left)
        right_height = self._height_rec(node.right)
        return max(left_height, right_height) + 1
    def min_value(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.val
    def max_value(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.val
    def is_valid_bst(self):
        return self._is_valid_bst_rec(self.root, float('-inf'), float('inf'))
    def _is_valid_bst_rec(self, node, low, high):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return (self._is_valid_bst_rec(node.left, low, node.val) and
                self._is_valid_bst_rec(node.right, node.val, high))
    def lowest_common_ancestor(self, n1, n2):
        return self._lca_rec(self.root, n1, n2)
    def _lca_rec(self, node, n1, n2):
        if node is None:
            return None
        if node.val > n1 and node.val > n2:
            return self._lca_rec(node.left, n1, n2)
        if node.val < n1 and node.val < n2:
            return self._lca_rec(node.right, n1, n2)
        return node
    def is_mirror(self):
        return self._is_mirror_rec(self.root, self.root)
    def _is_mirror_rec(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return (node1.val == node2.val and
                self._is_mirror_rec(node1.left, node2.right) and
                self._is_mirror_rec(node1.right, node2.left))
    def depth(self):
        return self._depth_rec(self.root)
    def _depth_rec(self, node):
        if node is None:
            return 0
        return max(self._depth_rec(node.left), self._depth_rec(node.right)) + 1
    def bfs(self):
        if not self.root:
            return []
        result, queue = [], [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
    def dfs(self):
        return self._dfs_rec(self.root)
    def _dfs_rec(self, node):
        return [node.val] + self._dfs_rec(node.left) + self._dfs_rec(node.right) if node else []
bt = BinaryTree()
bt.insert(5)
bt.insert(3)
bt.insert(7)
bt.insert(2)
bt.insert(4)
bt.insert(6)
bt.insert(8)
print("Inorder:", bt.inorder())
print("Preorder:", bt.preorder())
print("Postorder:", bt.postorder())
print("Level Order:", bt.level_order())
print("Height:", bt.height())
print("Min Value:", bt.min_value())
print("Max Value:", bt.max_value())
print("Is Valid BST:", bt.is_valid_bst())
lca_node = bt.lowest_common_ancestor(2, 4)
print("LCA of 2 and 4:", lca_node.val if lca_node else None)
print("Is Mirror:", bt.is_mirror())
print("Depth:", bt.depth())
print("BFS:", bt.bfs())
print("DFS:", bt.dfs())
bt.delete(3)
print("Inorder after deletion:", bt.inorder())
def kth_largest(nums, k):
    import heapq
    return heapq.nlargest(k, nums)[-1]
print(kth_largest([3,2,1,5,6,4],2))
def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
print(find_peak_element([1,2,3,1]))
from collections import Counter
def countPairs(nums1, nums2, k):
    count = 0
    freq_map = Counter(nums2)
    for num in nums1:
        target = k - num
        if target in freq_map:
            count += freq_map[target]
    return count
# print(countPairs([1,2,3,4],5))
def findDuplicates(nums):
    duplicates = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            duplicates.append(abs(num))
        else:
            nums[index] = -nums[index]
    return duplicates
print(findDuplicates([4,3,2,7,8,2,3,1]))
def findErrorNums(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(set(nums))
    duplicate = sum(nums) - actual_sum
    missing = expected_sum - actual_sum
    return [duplicate, missing]
print(findErrorNums([1,2,2,4]))
def findMaxConsecutiveOnes(nums):
    max_count = 0
    current_count = 0
    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count
print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
print(findMin([3,4,5,1,2]))
def findKthLargest(nums, k):
    import heapq
    return heapq.nlargest(k, nums)[-1]
print(findKthLargest([3,2,1,5,6,4],2))
def minChanges(nums, k):
    n = len(nums)
    change_count = [0] * (k + 2)
    for i in range(n // 2):
        left = nums[i]
        right = nums[n - i - 1]
        cur_diff = abs(left - right)
        max_diff = max(left, right, k - left, k - right)

        change_count[cur_diff] -= 1
        change_count[cur_diff + 1] += 1
        change_count[max_diff + 1] += 1
        change_count[k + 1] -= 1
        change_count[0] += 2
        change_count[1] -= 2
    min_changes = float('inf')
    current_changes = 0
    for i in range(k + 1):
        current_changes += change_count[i]
        min_changes = min(min_changes, current_changes)
    return min_changes
print(minChanges([1,2,4,3],4))
def partitionLabels(s):
    last_occurrence = {char: i for i, char in enumerate(s)}
    partitions = []
    start, end = 0, 0

    for i, char in enumerate(s):
        end = max(end, last_occurrence[char])
        if i == end:
            partitions.append(i - start + 1)
            start = i + 1

    return partitions
print(partitionLabels("ababcbacadefegdehijhklij"))
# def fill_missing_quantity(products):
#     products['quantity'] = products['quantity'].fillna(0)
#     return products
# products =[1,2,3,None]
# print(fill_missing_quantity(products))

def missingRolls(rolls, mean, n):
    m = len(rolls)
    total_sum = mean * (n + m)
    current_sum = sum(rolls)
    missing_sum = total_sum - current_sum

    if missing_sum < n or missing_sum > 6 * n:
        return []

    base_value = missing_sum // n
    remainder = missing_sum % n

    result = [base_value] * n
    for i in range(remainder):
        result[i] += 1

    return result
print(missingRolls([3,2,4,3],4,2))
def searchrange(nums,target):
    def find_left(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def find_right(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left_index = find_left(nums, target)
    right_index = find_right(nums, target)

    if left_index <= right_index:
        return [left_index, right_index]
    else:
        return [-1, -1]
print(searchrange([5,7,7,8,8,10],8))
def isNumber(s):
    s = s.strip()
    if not s:
        return False

    num_seen = False
    dot_seen = False
    e_seen = False
    num_after_e = True

    for i, char in enumerate(s):
        if char.isdigit():
            num_seen = True
            num_after_e = True
        elif char == '.':
            if dot_seen or e_seen:
                return False
            dot_seen = True
        elif char in ('e', 'E'):
            if e_seen or not num_seen:
                return False
            e_seen = True
            num_after_e = False
        elif char in ('+', '-'):
            if i != 0 and s[i - 1] not in ('e', 'E'):
                return False
        else:
            return False

    return num_seen and num_after_e
s= "0"
print(isNumber(s))
def odd_even(a):
    odd = [x for x in a if x % 2 != 0]
    even = [x for x in a if x % 2 == 0]
    return odd + even
print(odd_even([1,2,3,4,5,6,7,8,9]))
def delete_duplicates(A):
    if not A:
        return 0
    write_index =1
    for i in range(1, len(A)):
        if A[write_index-1] !=A[i]:
            A[write_index]=A[i]
            write_index +=1
    return write_index
print(delete_duplicates([1,1,2,2,3,4,4,5]))


"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""
def compress(chars):
    write_index = 0
    i = 0
    n = len(chars)
    # Read pointer
    while i < n:
        # Current character
        char = chars[i]
        count = 0
        # Count occurrences of the current character
        while i < n and chars[i] == char:
            i += 1
            count += 1
        # Write the character
        chars[write_index] = char
        write_index += 1
        # Write the count if greater than 1
        if count > 1:
            for digit in str(count):
                chars[write_index] = digit
                write_index += 1

    return write_index
print(compress(["a","a","b","b","c","c","c"]))

"""write a python function to word frequency in a given string"""
def word_frequency(s):
    words = s.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
print(word_frequency("this is a test this is only a test"))
"""write a python program to count the characters in a string"""
def char_count(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq
print(char_count("hello world"))
""" write a python code to print fibonacci sequence"""

def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]
print(fibonacci(10))
"""write a python code to check if a number is prime or not"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(29))

""" write a function to find a free time in a calendar given a list of busy time intervals"""
def find_free_time(busy_intervals, start, end):
    busy_intervals.sort()
    free_intervals = []
    current_start = start

    for interval in busy_intervals:
        if interval[0] > current_start:
            free_intervals.append((current_start, interval[0]))
        current_start = max(current_start, interval[1])

    if current_start < end:
        free_intervals.append((current_start, end))

    return free_intervals
print(find_free_time([(1, 3), (5, 6), (2, 4)], 0, 7))


"""write a python code to implement all neural network activation functions using numpy"""
import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def relu(x):
    return np.maximum(0, x)
def tanh(x):
    return np.tanh(x)
def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum(axis=0)
def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, x * alpha)
def elu(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))
def swish(x):
    return x * sigmoid(x)
def gelu(x):
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3))))
def hard_sigmoid(x):
    return np.clip((x + 1) / 2, 0, 1)
def softplus(x):
    return np.log1p(np.exp(x))
def softsign(x):
    return x / (1 + np.abs(x))
def binary_step(x):
    return np.where(x >= 0, 1, 0)
def relu6(x):
    return np.minimum(np.maximum(0, x), 6)
def mish(x):
    return x * np.tanh(softplus(x))
def hard_swish(x):
    return x * hard_sigmoid(x)
def log_sigmoid(x):
    return -np.logaddexp(0, -x)
def gaussian(x):
    return np.exp(-np.power(x, 2))
def bent_identity(x):
    return (np.sqrt(np.power(x, 2) + 1) - 1) / 2 + x
def bipolar_sigmoid(x):
    return (1 - np.exp(-x)) / (1 + np.exp(-x))
def sinc(x):
    return np.sinc(x / np.pi)
def soft_exponential(x, alpha):
    if alpha < 0:
        return -np.log(1 - alpha * (x + alpha)) / alpha
    elif alpha == 0:
        return x
    else:
        return (np.exp(alpha * x) - 1) / alpha + alpha

""" write a feed forward neural network from scratch using numpy with 5 input layers and 1 output layer and use relu activation function for hidden layers and linear regression  for output layer"""
class FeedForwardNN:
    def __init__(self, input_size, hidden_sizes, output_size):
        self.layers = []
        layer_sizes = [input_size] + hidden_sizes + [output_size]
        for i in range(len(layer_sizes) - 1):
            weight = np.random.randn(layer_sizes[i], layer_sizes[i + 1]) * 0.01
            bias = np.zeros((1, layer_sizes[i + 1]))
            self.layers.append((weight, bias))

    def relu(self, x):
        return np.maximum(0, x)

    def linear(self, x):
        return x

    def forward(self, X):
        a = X
        for i in range(len(self.layers) - 1):
            weight, bias = self.layers[i]
            z = np.dot(a, weight) + bias
            a = self.relu(z)
        weight, bias = self.layers[-1]
        z = np.dot(a, weight) + bias
        output = self.linear(z)
        return output
# Example usage
nn = FeedForwardNN(input_size=5, hidden_sizes=[10, 10, 10], output_size=1)
X = np.random.randn(1, 5)
output = nn.forward(X)
print(output)

"""write a pytorch simple linear regression model with 5 input features and 1 output feature"""
import torch
import torch.nn as nn
import torch.optim as optim
class LinearRegressionModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_size, output_size)

    def forward(self, x):
        return self.linear(x)

# Example usage
input_size = 5
output_size = 1
model = LinearRegressionModel(input_size, output_size)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Dummy data
X = torch.randn(10, input_size)
y = torch.randn(10, output_size)
# Training loop
for epoch in range(100):
    model.train()
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')
# Testing
model.eval()
with torch.no_grad():
    test_input = torch.randn(1, input_size)
    predicted = model(test_input)
    print(f'Predicted value: {predicted.item():.4f}')
"""write a pytorch feed forward neural network with 5 input features, 3 hidden layers with relu activation function and 1 output layer with linear regression"""
class FeedForwardNNPyTorch(nn.Module):
    def __init__(self, input_size, hidden_sizes, output_size):
        super(FeedForwardNNPyTorch, self).__init__()
        layers = []
        layer_sizes = [input_size] + hidden_sizes + [output_size]
        for i in range(len(layer_sizes) - 1):
            layers.append(nn.Linear(layer_sizes[i], layer_sizes[i + 1]))
            if i < len(layer_sizes) - 2:
                layers.append(nn.ReLU())
        self.network = nn.Sequential(*layers)

    def forward(self, x):
        return self.network(x)
# Example usage
nn_pytorch = FeedForwardNNPyTorch(input_size=5, hidden_sizes=[10, 10, 10], output_size=1)
X = torch.randn(1, 5)
output = nn_pytorch(X)
print(output)

""" write python code to create, rotate, display matrix in alternative, transpose a matrix, multiply two matrices, find the determinant of a matrix, find the inverse of a matrix, add two matrices, subtract two matrices, find the trace of a matrix, find the rank of a matrix, find the eigenvalues and eigenvectors of a matrix, perform matrix decomposition (LU, QR, SVD) without using numpy """


import numpy as np
def create_matrix(rows, cols, fill_value=0):
    return np.full((rows, cols), fill_value)
def rotate_matrix(matrix):
    return np.rot90(matrix)
def display_matrix(matrix):
    print(matrix)
def transpose_matrix(matrix):
    return np.transpose(matrix)
def multiply_matrices(A, B):
    return np.dot(A, B)
def determinant(matrix):
    return np.linalg.det(matrix)
def inverse(matrix):
    return np.linalg.inv(matrix)
def add_matrices(A, B):
    return np.add(A, B)
def subtract_matrices(A, B):
    return np.subtract(A, B)
def trace(matrix):
    return np.trace(matrix)
def rank(matrix):
    return np.linalg.matrix_rank(matrix)
def eigenvalues_eigenvectors(matrix):
    return np.linalg.eig(matrix)
def lu_decomposition(matrix):
    from scipy.linalg import lu
    return lu(matrix)
def qr_decomposition(matrix):
    return np.linalg.qr(matrix)
def svd_decomposition(matrix):
    return np.linalg.svd(matrix)
# Example usage
A = create_matrix(3, 3, 1)
B = create_matrix(3, 3, 2)
display_matrix(A)
print("Rotated Matrix:")
display_matrix(rotate_matrix(A))


""" write python code to create, rotate, display square matrix in alternative, transpose a matrix, multiply two matrices, find the determinant of a matrix, find the inverse of a matrix, add two matrices, subtract two matrices, find the trace of a matrix, find the rank of a matrix, find the eigenvalues and eigenvectors of a matrix, perform matrix decomposition (LU, QR, SVD) without using numpy"""

class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def rotate(self):
        self.data = [list(row) for row in zip(*self.data[::-1])]
        self.rows, self.cols = self.cols, self.rows

    def display(self):
        for row in self.data:
            print(row)

    def transpose(self):
        self.data = [list(row) for row in zip(*self.data)]
        self.rows, self.cols = self.cols, self.rows

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Incompatible matrices for multiplication")
        result = [[0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Determinant not defined for non-square matrices")
        if self.rows == 1:
            return self.data[0][0]
        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        det = 0
        for c in range(self.cols):
            minor = [row[:c] + row[c+1:] for row in self.data[1:]]
            det += ((-1) ** c) * self.data[0][c] * Matrix(minor).determinant()
        return det

    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted")
        if self.rows == 2:
            return Matrix([[self.data[1][1] / det, -self.data[0][1] / det],
                           [-self.data[1][0] / det, self.data[0][0] / det]])
        raise NotImplementedError("Inverse not implemented for matrices larger than 2x2")

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must be of the same dimensions to add")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)
    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must be of the same dimensions to subtract")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)
    def trace(self):
        if self.rows != self.cols:
            raise ValueError("Trace not defined for non-square matrices")
        return sum(self.data[i][i] for i in range(self.rows))
    def rank(self):
        def rref(matrix):
            A = [row[:] for row in matrix]
            rows, cols = len(A), len(A[0])
            r = 0
            for c in range(cols):
                if r >= rows:
                    break
                pivot = max(range(r, rows), key=lambda i: abs(A[i][c]))
                if A[pivot][c] == 0:
                    continue
                A[r], A[pivot] = A[pivot], A[r]
                for i in range(r + 1, rows):
                    factor = A[i][c] / A[r][c]
                    for j in range(c, cols):
                        A[i][j] -= factor * A[r][j]
                r += 1
            return A

        rref_matrix = rref(self.data)
        rank = sum(1 for row in rref_matrix if any(abs(x) > 1e-10 for x in row))
        return rank
    def eigenvalues_eigenvectors(self):
        raise NotImplementedError("Eigenvalues and eigenvectors calculation not implemented")
    def lu_decomposition(self):
        raise NotImplementedError("LU decomposition not implemented")
    def qr_decomposition(self):
        raise NotImplementedError("QR decomposition not implemented")
    def svd_decomposition(self):
        raise NotImplementedError("SVD decomposition not implemented")
# Example usage
A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])
A.display()
print("Rotated Matrix:")
A.rotate()
A.display()
A.transpose()
A.display()
C = A.multiply(B)
C.display()
print("Determinant:", A.determinant())
try:
    A_inv = A.inverse()
    A_inv.display()
except ValueError as e:
    print(e)
print("Added Matrix:")
D = A.add(B)
D.display()
print("Subtracted Matrix:")
E = A.subtract(B)
E.display()
print("Trace:", A.trace())
print("Rank:", A.rank())
"""write python code to create, rotate, display square matrix in alternative, transpose a matrix, multiply two matrices, find the determinant of a matrix, find the inverse of a matrix, add two matrices, subtract two matrices, find the trace of a matrix, find the rank of a matrix, find the eigenvalues and eigenvectors of a matrix, perform matrix decomposition (LU, QR, SVD) without using numpy"""
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def rotate(self):
        self.data = [list(row) for row in zip(*self.data[::-1])]
        self.rows, self.cols = self.cols, self.rows

    def display(self):
        for row in self.data:
            print(row)

    def transpose(self):
        self.data = [list(row) for row in zip(*self.data)]
        self.rows, self.cols = self.cols, self.rows

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Incompatible matrices for multiplication")
        result = [[0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Determinant not defined for non-square matrices")
        if self.rows == 1:
            return self.data[0][0]
        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        det = 0
        for c in range(self.cols):
            minor = [row[:c] + row[c+1:] for row in self.data[1:]]
            det += ((-1) ** c) * self.data[0][c] * Matrix(minor).determinant()
        return det

    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted")
        if self.rows == 2:
            return Matrix([[self.data[1][1] / det, -self.data[0][1] / det],
                           [-self.data[1][0] / det, self.data[0][0] / det]])
        raise NotImplementedError("Inverse not implemented for matrices larger than 2x2")

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must be of the same dimensions to add")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)
    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must be of the same dimensions to subtract")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)
    def trace(self):
        if self.rows != self.cols:
            raise ValueError("Trace not defined for non-square matrices")
        return sum(self.data[i][i] for i in range(self.rows))
    def rank(self):
        def rref(matrix):
            A = [row[:] for row in matrix]
            rows, cols = len(A), len(A[0])
            r = 0
            for c in range(cols):
                if r >= rows:
                    break
                pivot = max(range(r, rows), key=lambda i: abs(A[i][c]))
                if A[pivot][c] == 0:
                    continue
                A[r], A[pivot] = A[pivot], A[r]
                for i in range(r + 1, rows):
                    factor = A[i][c] / A[r][c]
                    for j in range(c, cols):
                        A[i][j] -= factor * A[r][j]
                r += 1
            return A

        rref_matrix = rref(self.data)
        rank = sum(1 for row in rref_matrix if any(abs(x) > 1e-10 for x in row))
        return rank
    def eigenvalues_eigenvectors(self):
        raise NotImplementedError("Eigenvalues and eigenvectors calculation not implemented")
    def lu_decomposition(self):
        raise NotImplementedError("LU decomposition not implemented")
    def qr_decomposition(self):
        raise NotImplementedError("QR decomposition not implemented")
    def svd_decomposition(self):
        raise NotImplementedError("SVD decomposition not implemented")
# Example usage
A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])
A.display()
print("Rotated Matrix:")


""" write a python function to impute missing values in a  streaming dataframe using mean, median, mode and forward fill and backward fill methods for a given set of columns"""
import pandas as pd
def impute_missing_values(df, columns, method='mean'):
    for col in columns:
        if method == 'mean':
            df[col].fillna(df[col].mean(), inplace=True)
        elif method == 'median':
            df[col].fillna(df[col].median(), inplace=True)
        elif method == 'mode':
            df[col].fillna(df[col].mode()[0], inplace=True)
        elif method == 'ffill':
            df[col].fillna(method='ffill', inplace=True)
        elif method == 'bfill':
            df[col].fillna(method='bfill', inplace=True)
        else:
            raise ValueError("Method not recognized. Use 'mean', 'median', 'mode', 'ffill', or 'bfill'.")
    return df
# Example usage
data = {'A': [1, 2, None, 4], 'B': [None, 2, 3, None], 'C': [1, None, None, 4]}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\nDataFrame after imputing missing values with mean:")
imputed_df = impute_missing_values(df, ['A', 'B', 'C'], method='mean')
print(imputed_df)

""" write a python fucntion to impute missing values from a streaming dataframe read from a parquet file, calculate the dynamic mean, mode and median of a given columns for Missing at random, missing not at random, missing completely at random data and fill the missing values using forward fill and backward fill methods and save the dataframe to a new parquet file"""
import pandas as pd
def impute_missing_values_parquet(input_file, output_file, columns, method='mean'):
    df = pd.read_parquet(input_file)
    for col in columns:
        if method == 'mean':
            df[col].fillna(df[col].mean(), inplace=True)
        elif method == 'median':
            df[col].fillna(df[col].median(), inplace=True)
        elif method == 'mode':
            df[col].fillna(df[col].mode()[0], inplace=True)
        elif method == 'ffill':
            df[col].fillna(method='ffill', inplace=True)
        elif method == 'bfill':
            df[col].fillna(method='bfill', inplace=True)
        else:
            raise ValueError("Method not recognized. Use 'mean', 'median', 'mode', 'ffill', or 'bfill'.")
    df.to_parquet(output_file)
    return df

# Example usage

input_file = 'input.parquet'
output_file = 'output.parquet'
columns = ['A', 'B', 'C']
imputed_df = impute_missing_values_parquet(input_file, output_file, columns, method='mean')
print("DataFrame after imputing missing values with mean and saving to new parquet file:")
print(imputed_df)

""" write a python function to auto label a given dataset using kmeans clustering algorithm and save the labeled dataset to a new csv file"""
import pandas as pd
from sklearn.cluster import KMeans
def auto_label_dataset(input_file, output_file, n_clusters):
    df = pd.read_csv(input_file)
    kmeans = KMeans(n_clusters=n_clusters)
    df['Cluster'] = kmeans.fit_predict(df.select_dtypes(include=['number']))
    df.to_csv(output_file, index=False)
    return df
# Example usage
input_file = 'input.csv'
output_file = 'labeled_output.csv'
n_clusters = 3
labeled_df = auto_label_dataset(input_file, output_file, n_clusters)
print("Labeled DataFrame saved to new csv file:")
print(labeled_df)

""" write a python function to auto label and impute certain columns based on the data types from a streaming json file using kmeans clustering algorithm and save the labeled and imputed dataset to a new json file"""
import pandas as pd
from sklearn.cluster import KMeans
def auto_label_impute_json(input_file, output_file, n_clusters, impute_columns, impute_method='mean'):
    df = pd.read_json(input_file)
    kmeans = KMeans(n_clusters=n_clusters)
    df['Cluster'] = kmeans.fit_predict(df.select_dtypes(include=['number']))
    for col in impute_columns:
        if impute_method == 'mean':
            df[col].fillna(df[col].mean(), inplace=True)
        elif impute_method == 'median':
            df[col].fillna(df[col].median(), inplace=True)
        elif impute_method == 'mode':
            df[col].fillna(df[col].mode()[0], inplace=True)
        elif impute_method == 'ffill':
            df[col].fillna(method='ffill', inplace=True)
        elif impute_method == 'bfill':
            df[col].fillna(method='bfill', inplace=True)
        else:
            raise ValueError("Method not recognized. Use 'mean', 'median', 'mode', 'ffill', or 'bfill'.")
    df.to_json(output_file, orient='records', lines=True)
    return df
# Example usage
input_file = 'input.json'
output_file = 'labeled_imputed_output.json'
n_clusters = 3
impute_columns = ['A', 'B', 'C']
labeled_imputed_df = auto_label_impute_json(input_file, output_file, n_clusters, impute_columns, impute_method='mean')
print("Labeled and Imputed DataFrame saved to new json file:")

"""write a python function to identify and analyze missing values, outliers, dupliucate records, incorrect data types in a sample streaming dataset and generate a data quality report and save the report to a new csv file"""
import pandas as pd
def data_quality_report(input_file, output_file):
    df = pd.read_csv(input_file)
    report = {}

    # Missing values
    report['Missing Values'] = df.isnull().sum()

    # Outliers using Z-score
    from scipy import stats
    z_scores = stats.zscore(df.select_dtypes(include=['number']))
    outliers = (abs(z_scores) > 3).sum(axis=0)
    report['Outliers'] = outliers

    # Duplicate records
    report['Duplicate Records'] = df.duplicated().sum()

    # Incorrect data types
    incorrect_types = {}
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                pd.to_numeric(df[col])
            except ValueError:
                incorrect_types[col] = 'Non-numeric values found'
        elif df[col].dtype == 'int64' or df[col].dtype == 'float64':
            if not pd.api.types.is_numeric_dtype(df[col]):
                incorrect_types[col] = 'Non-numeric values found'
    report['Incorrect Data Types'] = incorrect_types

    # Convert report to DataFrame and save to CSV
    report_df = pd.DataFrame.from_dict(report, orient='index').transpose()
    report_df.to_csv(output_file, index=False)
    return report_df
# Example usage
input_file = 'sample_data.csv'
output_file = 'data_quality_report.csv'
report_df = data_quality_report(input_file, output_file)

print("Data Quality Report saved to new csv file:")
print(report_df)
print(report_df)
""" write a memory effcient python function to merge two large streaming dataframes on common columns and impute values in O(1) space time complexity and save the merged dataframe to a new csv file"""
import pandas as pd
def merge_impute_dataframes(file1, file2, output_file, on_columns, impute_columns, impute_method='mean', chunksize=10000):
    merged_chunks = []
    for chunk1 in pd.read_csv(file1, chunksize=chunksize):
        for chunk2 in pd.read_csv(file2, chunksize=chunksize):
            merged_chunk = pd.merge(chunk1, chunk2, on=on_columns, how='outer')
            for col in impute_columns:
                if impute_method == 'mean':
                    merged_chunk[col].fillna(merged_chunk[col].mean(), inplace=True)
                elif impute_method == 'median':
                    merged_chunk[col].fillna(merged_chunk[col].median(), inplace=True)
                elif impute_method == 'mode':
                    merged_chunk[col].fillna(merged_chunk[col].mode()[0], inplace=True)
                elif impute_method == 'ffill':
                    merged_chunk[col].fillna(method='ffill', inplace=True)
                elif impute_method == 'bfill':
                    merged_chunk[col].fillna(method='bfill', inplace=True)
                else:
                    raise ValueError("Method not recognized. Use 'mean', 'median', 'mode', 'ffill', or 'bfill'.")
            merged_chunks.append(merged_chunk)
    final_df = pd.concat(merged_chunks, ignore_index=True)
    final_df.to_csv(output_file, index=False)
    return final_df
# Example usage
file1 = 'large_data1.csv'
file2 = 'large_data2.csv'
output_file = 'merged_imputed_output.csv'
on_columns = ['ID']
impute_columns = ['A', 'B', 'C']
merged_imputed_df = merge_impute_dataframes(file1, file2, output_file, on_columns, impute_columns, impute_method='mean')
print("Merged and Imputed DataFrame saved to new csv file:")
print(merged_imputed_df)

""" write a spark code to read the streaming IOT sensor information in the csv format, build a medallion data architecture and save the data in delta format in bronze, silver and gold layers"""
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col, avg, window
# from delta.tables import DeltaTable
# spark = SparkSession.builder \
#     .appName("IOT Sensor Data Medallion Architecture") \
#     .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
#     .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
#     .getOrCreate()
# # Read streaming data from CSV
# input_path = "path/to/iot/sensor/data"
# sensor_df = spark.readStream.option("header", "true").csv(input_path)
# # Bronze Layer: Raw Data
# bronze_path = "path/to/bronze/layer"
# sensor_df.writeStream.format("delta").option("checkpointLocation", bronze_path + "/_checkpoints").start(bronze_path)
# # Silver Layer: Cleaned Data
# bronze_table = DeltaTable.forPath(spark, bronze_path)
# silver_path = "path/to/silver/layer"
# silver_df = bronze_table.toDF().filter(col("sensor_value").isNotNull())
# silver_df.writeStream.format("delta").option("checkpointLocation", silver_path + "/_checkpoints").start(silver_path)
# # Gold Layer: Aggregated Data
# silver_table = DeltaTable.forPath(spark, silver_path)
# gold_path = "path/to/gold/layer"
# gold_df = silver_table.toDF() \
#     .withWatermark("timestamp", "1 minute") \
#     .groupBy(window(col("timestamp"), "5 minutes"), col("sensor_id")) \
#     .agg(avg("sensor_value").alias("avg_sensor_value"))
# gold_df.writeStream.format("delta").option("checkpointLocation", gold_path + "/_checkpoints").start(gold_path)
# print("Medallion architecture layers created and data saved in Delta format.")

""" write a python pandasql code to read a streaming csv file, perform data transformations using sql queries and save the transformed data to a new csv file"""
import pandas as pd
import pandasql as ps
def transform_data_sql(input_file, output_file, query):
    df = pd.read_csv(input_file)
    transformed_df = ps.sqldf(query, locals())
    transformed_df.to_csv(output_file, index=False)
    return transformed_df
# Example usage
input_file = 'streaming_data.csv'
output_file = 'transformed_data.csv'
query = """ SELECT column1, column2, AVG(column3) as avg_column3 
            FROM df 
            GROUP BY column1, column2 """
"""write a python code to find and replace a word in large array of steaming text files"""
import os
def find_replace_in_files(directory, find_word, replace_word):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                content = file.read()
            content = content.replace(find_word, replace_word)
            with open(file_path, 'w') as file:
                file.write(content)

# Example usage
directory = 'path/to/text/files'
find_word = 'old_word'
replace_word = 'new_word'
find_replace_in_files(directory, find_word, replace_word)
print("Word replacement completed in text files.")

"""write a python code to insert, update, delete a dataset rowwise in star schema and snowflake schema using panda sql """
import pandas as pd
import pandasql as ps
def insert_row(df, row_data):
    new_row = pd.DataFrame([row_data], columns=df.columns)
    return pd.concat([df, new_row], ignore_index=True)
def update_row(df, condition, update_data):
    df.loc[condition, list(update_data.keys())] = list(update_data.values())
    return df
def delete_row(df, condition):
    return df.loc[~condition]
# Example usage
data = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Insert a new row
new_row_data = {'ID': 4, 'Name': 'David', 'Age': 28}
df = insert_row(df, new_row_data)
print("\nDataFrame after inserting a new row:")
print(df)
# Update a row
update_condition = df['ID'] == 2
update_data = {'Name': 'Robert', 'Age': 31}
df = update_row(df, update_condition, update_data)
print("\nDataFrame after updating a row:")
print(df)
# Delete a row
delete_condition = df['ID'] == 1
df = delete_row(df, delete_condition)
print("\nDataFrame after deleting a row:")
print(df)

""" write a python code to read and store streaming data from kafka topic using pyspark and save the data to a delta lake in parquet format"""
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col
# from delta.tables import DeltaTable
# spark = SparkSession.builder \
#     .appName("Kafka to Delta Lake") \
#     .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
#     .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
#     .getOrCreate()
# # Read streaming data from Kafka
# kafka_bootstrap_servers = "localhost:9092"
# kafka_topic = "your_kafka_topic"
# kafka_df = spark.readStream \
#     .format("kafka") \
#     .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
#     .option("subscribe", kafka_topic) \
#     .load()
# # Convert the binary value column to string
# value_df = kafka_df.selectExpr("CAST(value AS STRING) as message")
# # Save the data to Delta Lake in Parquet format
# delta_path = "path/to/delta/lake"
# value_df.writeStream \
#     .format("delta") \
#     .option("checkpointLocation", delta_path + "/_checkpoints") \
#     .start(delta_path)
# print("Streaming data from Kafka saved to Delta Lake in Parquet format.")
# Note: Uncomment the above code and provide appropriate paths and Kafka configurations to run in a PySpark environment.
print("DataFrame after transforming data using SQL and saving to new csv file:")

"""write a python function to store and read data in O(1) space time complexity using hdf5 file format"""
import pandas as pd
def store_read_hdf5(file_path, df=None, key='data', mode='a'):
    if df is not None:
        df.to_hdf(file_path, key=key, mode=mode, format='table', append=True)
    return pd.read_hdf(file_path, key=key)
# Example usage
file_path = 'data.h5'
data = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
store_read_hdf5(file_path, df)
read_df = store_read_hdf5(file_path)
print("DataFrame read from HDF5 file:")
print(read_df)
""" write a python function to read and store streaming data from kafka topic using kafka-python and save the data to a delta lake in parquet format"""
from kafka import KafkaConsumer
import pandas as pd
from delta import DeltaTable
import os
def kafka_to_delta(kafka_bootstrap_servers, kafka_topic, delta_path, group_id='my-group', auto_offset_reset='earliest'):
    consumer = KafkaConsumer(
        kafka_topic,
        bootstrap_servers=kafka_bootstrap_servers,
        group_id=group_id,
        auto_offset_reset=auto_offset_reset,
        value_deserializer=lambda x: x.decode('utf-8')
    )
    for message in consumer:
        data = message.value
        df = pd.DataFrame([data.split(',')])  # Assuming CSV format
        if not os.path.exists(delta_path):
            df.to_parquet(delta_path, index=False)
        else:
            existing_df = pd.read_parquet(delta_path)
            combined_df = pd.concat([existing_df, df], ignore_index=True)
            combined_df.to_parquet(delta_path, index=False)
    consumer.close()
# Example usage
kafka_bootstrap_servers = 'localhost:9092'
kafka_topic = 'your_kafka_topic'
delta_path = 'path/to/delta/lake'
kafka_to_delta(kafka_bootstrap_servers, kafka_topic, delta_path)
print("Streaming data from Kafka saved to Delta Lake in Parquet format.")
# Note: Ensure that the Kafka server is running and the topic exists. Adjust the data parsing logic as per the actual data format.
print(read_df)
print("DataFrame read from HDF5 file:")
print(read_df)

""" write a python program to get the height and width of a tree with and without using recursion"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def height_recursive(node):
    if node is None:
        return 0
    return 1 + max(height_recursive(node.left), height_recursive(node.right))
def height_iterative(root):
    if root is None:
        return 0
    queue = [(root, 1)]
    max_height = 0
    while queue:
        current, height = queue.pop(0)
        max_height = max(max_height, height)
        if current.left:
            queue.append((current.left, height + 1))
        if current.right:
            queue.append((current.right, height + 1))
    return max_height
# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("Height of tree (recursive):", height_recursive(root))
print("Height of tree (iterative):", height_iterative(root))

""" write a python program to list all anagram pairs in a given list of words"""
from collections import defaultdict
def find_anagram_pairs(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    anagram_pairs = []
    for group in anagrams.values():
        if len(group) > 1:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    anagram_pairs.append((group[i], group[j]))
    return anagram_pairs


""" write a python code to one hot encode a given categorical column in a pandas dataframe without using pandas get_dummies function"""
import pandas as pd
def one_hot_encode(df, column):
    unique_values = df[column].unique()
    for value in unique_values:
        df[f"{column}_{value}"] = (df[column] == value).astype(int)
    df.drop(column, axis=1, inplace=True)
    return df
# Example usage
data = {'ID': [1, 2, 3], 'Color': ['Red', 'Blue', 'Green']}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
encoded_df = one_hot_encode(df, 'Color')
print("\nOne-Hot Encoded DataFrame:")
print(encoded_df)

"""# Questions:
# 1. Can you create an incidence matrix that shows which aircraft can land on which airports?
# 2. Can you rank airports by how many aircraft types can land on them?
# 3. Can you tell us in which airport/runway we have spent the most time?
# 4. Can you rank airports/runways by number of images captured?

### Data ### 
from pprint import pprint
import pandas as pd

data_dict = pd.read_pickle("/home/coderpad/data/data.pickle")

aircraft = {
    "A21N": {"range": 4000, "landing_distance": 1600},
    "B738": {"range": 3000, "landing_distance": 2600},
    "C172": {"range": 518, "landing_distance": 390},
    "A380": {"range": 8210, "landing_distance": 2700},
}

# pprint(data_dict.keys())

### Start your solution here ###
# 1. Can you create an incidence matrix that shows which aircraft can land on which airports?
# 2. Can you rank airports by how many aircraft types can land on them?
# 3. Can you tell us in which airport/runway we have spent the most time?
# 4. Can you rank airports/runways by number of images captured?"""
# 1. Create an incidence matrix that shows which aircraft can land on which airports
import pandas as pd
import numpy as np
# Create a list of airports and aircraft
airports = list(data_dict.keys())
aircraft_types = list(aircraft.keys())
# Initialize the incidence matrix with zeros
incidence_matrix = pd.DataFrame(0, index=airports, columns=aircraft_types)
# Populate the incidence matrix
for airport in airports:
    for ac in aircraft_types:
        if data_dict[airport]['runway_length'] >= aircraft[ac]['landing_distance']:
            incidence_matrix.at[airport, ac] = 1
print("Incidence Matrix:")
print(incidence_matrix)
# 2. Rank airports by how many aircraft types can land on them
airport_ranking = incidence_matrix.sum(axis=1).sort_values(ascending=False)
print("\nAirport Ranking by Aircraft Types:")
print(airport_ranking)
# 3. Find the airport/runway where the most time was spent
time_spent = {}
for airport in airports:
    time_spent[airport] = data_dict[airport]['time_spent']
most_time_airport = max(time_spent, key=time_spent.get)
print(f"\nAirport/Runway with Most Time Spent: {most_time_airport} with {time_spent[most_time_airport]} hours")
# 4. Rank airports/runways by number of images captured
image_count = {}
for airport in airports:
    image_count[airport] = len(data_dict[airport]['images'])
airport_image_ranking = pd.Series(image_count).sort_values(ascending=False)
print("\nAirport/Runway Ranking by Number of Images Captured:")
print(airport_image_ranking)


""" write a python code to create a incidence matrix from data_dict which is dictionary of pandas dataframes"""
import pandas as pd
import numpy as np
# Sample data_dict with pandas DataFrames
data_dict = {
    'Airport1': pd.DataFrame({'Aircraft': ['A21N', 'B738'], 'Landing_Distance': [1600, 2600]}),
    'Airport2': pd.DataFrame({'Aircraft': ['C172', 'A380'], 'Landing_Distance': [390, 2700]}),
    'Airport3': pd.DataFrame({'Aircraft': ['A21N', 'C172'], 'Landing_Distance': [1600, 390]})
}
# Create a list of airports and aircraft
airports = list(data_dict.keys())
aircraft_types = set()
for df in data_dict.values():
    aircraft_types.update(df['Aircraft'].tolist())
aircraft_types = list(aircraft_types)
# Initialize the incidence matrix with zeros
incidence_matrix = pd.DataFrame(0, index=airports, columns=aircraft_types)
# Populate the incidence matrix
for airport, df in data_dict.items():
    for ac in df['Aircraft']:
        incidence_matrix.at[airport, ac] = 1
print("Incidence Matrix:")
print(incidence_matrix)
# Example usage
# 2. Rank airports by how many aircraft types can land on them
airport_ranking = incidence_matrix.sum(axis=1).sort_values(ascending=False)

# 3. Find the airport/runway where the most time was spent
time_spent = {
    'Airport1': 5,
    'Airport2': 8,
    'Airport3': 3
}
most_time_airport = max(time_spent, key=time_spent.get)
print(f"\nAirport/Runway with Most Time Spent: {most_time_airport} with {time_spent[most_time_airport]} hours")
# 4. Rank airports/runways by number of images captured
image_count = {
    'Airport1': 10,
    'Airport2': 15,
    'Airport3': 5
}
airport_image_ranking = pd.Series(image_count).sort_values(ascending=False)
print("\nAirport/Runway Ranking by Number of Images Captured:")
print(airport_image_ranking)
print(airport_ranking)
print("\nAirport Ranking by Aircraft Types:")
print(airport_ranking)
print("Incidence Matrix:")
print(incidence_matrix)


""" write a python code to create a neural network using pytorch to showcase self attention, multi head attention and cross attention mechanisms"""
import torch
import torch.nn as nn
import torch.nn.functional as F
class SelfAttention(nn.Module):
    def __init__(self, embed_size, heads):
        super(SelfAttention, self).__init__()
        self.embed_size = embed_size
        self.heads = heads
        self.head_dim = embed_size // heads

        assert (
            self.head_dim * heads == embed_size
        ), "Embedding size needs to be divisible by heads"

        self.values = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.keys = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.queries = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.fc_out = nn.Linear(heads * self.head_dim, embed_size)

    def forward(self, values, keys, queries, mask):
        N = queries.shape[0]
        value_len, key_len, query_len = values.shape[1], keys.shape[1], queries.shape[1]

        # Split the embedding into self.heads different pieces
        values = values.reshape(N, value_len, self.heads, self.head_dim)
        keys = keys.reshape(N, key_len, self.heads, self.head_dim)
        queries = queries.reshape(N, query_len, self.heads, self.head_dim)

        values = self.values(values)
        keys = self.keys(keys)
        queries = self.queries(queries)

        # Scaled dot-product attention
        energy = torch.einsum("nqhd,nkhd->nhqk", [queries, keys])
        if mask is not None:
            energy = energy.masked_fill(mask == 0, float("-1e20"))

        attention = torch.softmax(energy / (self.embed_size ** (1 / 2)), dim=3)

        out = torch.einsum("nhqk,nkhd->nqhd", [attention, values]).reshape(
            N, query_len, self.heads * self.head_dim
        )

        out = self.fc_out(out)
        return out

