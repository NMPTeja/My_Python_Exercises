###############################################################
#
# Given a file path with folder names, '..' (Parent directory), and '.' (Current directory),
# return the shortest possible file path (Eliminate all the '..' and '.').
#
# Example
# Input: '/Users/Joma/Documents/../Desktop/./../'
# Output: '/Users/Joma/'
#
###############################################################
from collections import deque

stack = deque()

def shortest_path(file_path):
    inp = file_path.split("/")

    for e in inp:
        if e == "..":
            if stack:
                stack.pop()
            else:
                return "Please provide proper input."
        elif e == ".":
            continue
        else:
            stack.append(e)

    return "/".join([stack.popleft() for _ in range(len(stack))])


print(shortest_path('/Users/Teja/Documents/../Desktop/./../Folder1/.././Folder2/../'))
