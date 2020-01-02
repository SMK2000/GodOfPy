# Input / Output
import time
print("Hello.")
time.sleep(2) # Halts execution for 2 seconds
print("Type your favourite number")
a = int(input()) # accept user input and convert it to int
# Odd/even?
if (a%2)==0:
   print("Even")  
else:
   print("Odd")
# END
# Alternate method for accepting input while giving a hint is a = input("Whatever text you want")\
# and skip the print statement preceding it 
