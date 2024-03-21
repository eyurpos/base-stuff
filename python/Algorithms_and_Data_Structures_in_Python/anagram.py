# Construct an algorithm to check whether two words (or phrases) 
# are anagrams or not!
# "An anagram is a word or phrase formed by rearranging the letters 
# of a different word or phrase, typically using all the original letters exactly once"

def is_anagram(str1, str2):

    # your algorithm goes here
    # return True if str1 and str2 are anagrams, otherwise return False
    
    if len(str1) != len(str2):
        return False
    
    sorted_string1 = sorted(list(str1))
    sorted_string2 = sorted(list(str2))
    
    for i in range(len(sorted_string1)):
        if (sorted_string1[i] != sorted_string2[i]):
            return False
            
    return True

print(is_anagram("restful", "fluster"))
print(is_anagram("restdul", "fluster"))