# "A palindrome is a string that reads the same forward and backward"

# you can define helper methods if needed
def is_palindrome(s):
    
    # your implementation of the algorithm goes here 
    start = 0
    end = len(s) - 1 
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1 
        end -= 1
    
    return True

