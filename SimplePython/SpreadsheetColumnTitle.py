# ####################################################################
# MS Excel column titles have the following
# pattern: A, B, C, ..., Z, AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB, ... etc.
# In other words, column 1 is named "A", column 2 is "B", column 26 is "Z", column 27 is "AA" and so forth.
# Given a positive integer, find its corresponding column name.
#
# Examples:
# Input: 26
# Output: Z
#
# Input: 51
# Output: AY
#
# Input: 52
# Output: AZ
#
# Input: 676
# Output: YZ
#
# Input: 702
# Output: ZZ
#
# Input: 704
# Output: AAB
#####################################################################

import string

alpha_dict = {n: ch for n, ch in enumerate(string.ascii_uppercase)}

def convertToColumnName(index:int):
    resultStr = ""
    index-=1
    while(index>0):
        rem = index%26
        resultStr += alpha_dict[rem]
        index //= 26
        index -= 1
    if index==0:
        resultStr += 'A'

    return resultStr[::-1]

print(convertToColumnName(1)) # A
print(convertToColumnName(456976)) # YYYZ
print(convertToColumnName(28)) # AB
print(convertToColumnName(51)) # AY
print(convertToColumnName(52)) # AZ
print(convertToColumnName(704))