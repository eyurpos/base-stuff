# Your task is to design an efficient algorithm to reverse a given integer. 
# For example if the input of the algorithm is 1234 then the output should be 4321.

def reverse_integer(n):
    # your implementation goes here
    result = 0
    while n != 0 :
        result = result * 10 + int(n % 10)
        n = int(n/10)
        
    return result
