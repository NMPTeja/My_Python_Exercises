################################################################################
# Return the longest run of 1s for a given integer n's binary representation.
#
# Example:
#
# Input: 242
# Output: 4
#
# 242 in binary is 0b11110010, so the longest run of 1 is 4.
################################################################################

def longestOneRun(n:int):
    count = 1
    max=-1
    while n>0:
        rem = n%2
        if(rem == 1):
            count +=1
        else:
            count=0
        n //=2
        max = max if max>=count else count
    return max

n = int(input("Enter a number: "))
print(longestOneRun(n))