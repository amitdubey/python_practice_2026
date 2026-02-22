from typing import List


# def hasduplicate(nums:List[int]) -> bool:
#     """
#     Given an integer array nums, return true if any value appears at least twice in the array,
#     and return false if every element is distinct.
#     """
#     return print(len(nums) != len(set(nums)))
#
# List =[1, 2,2, 3, 4, 5, 6, 7, 8, 9, 10]
# hasduplicate(List)

def isAnagram(s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if t is an anagram of s and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.
    """
    return print(sorted(s) == sorted(t))

s = "racecar"
t = "carrace"
isAnagram(s, t)

def TwoSum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return print([num_map[complement], i])
        num_map[num] = i

nums = [2, 7, 11, 15]
target = 9
TwoSum(nums, target)

" print identity matrix"
def identity_matrix(n: int) -> List[List[int]]:
    """
    Generate an identity matrix of size n x n.
    """
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
n = 4
identity = identity_matrix(n)
for row in identity:
    print(row)

""" write a python function to traverse and print only the values which are 1 in the matrix"""
def print_identity_values(matrix: List[List[int]]) -> None:
    """ Prints values of 1 in the identity matrix."""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                print(f"Value at position ({i}, {j}) is 1")
matrix = identity_matrix(n)
print_identity_values(matrix)

""" write a python function to traverse and print only the values which are 0 in the matrix"""
def print_zero_values(matrix: List[List[int]]) -> None:
    """ Prints values of 0 in the matrix."""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                print(f"Value at position ({i}, {j}) is 0")
matrix = identity_matrix(n)
print_zero_values(matrix)
def print_matrix(matrix: List[List[int]]) -> None:
    """ Prints the matrix in a readable format."""
    for row in matrix:
        print(" ".join(map(str, row)))
