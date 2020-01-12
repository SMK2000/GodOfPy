# function which return reverse of a string 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False
  
  
# Driver code 
print("Enter text:")
s = input().lower()
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Palindrome") 
else: 
    print("Not A Palindrome")