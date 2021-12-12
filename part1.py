'''
***PART 1***

The program below is supposed to find and print the number of perfect squares that exist that are less than or equal to the number the user inputs. However, as is, there is an infinite loop. Fix the code so that it has no infinite loop and runs the way it's supposed to. (Note: there's nothing wrong with the print statement. Do not change that.)

(Hint: there should only be one change made/added.)

Example of what should appear on the console when this part runs:

Enter a number: 50
Number of squares less than or equal to 50: 7

'''
number = int(input("Enter a number:"))
numbertosquare = 1
numsquares = 0
while numbertosquare ** 2 <= number:
  numsquares = numsquares + 1
  '''print("numsquares=",numsquares,"numbertosquare=",numbertosquare,"numbertosquare**2=",numbertosquare ** 2,"number=",number)'''
  numbertosquare = numbertosquare + 1
else:
  '''print("No,", numbertosquare, "squared is not less than or equal to", number)'''
    
print("Number of squares less than or equal to", str(number)+':', numsquares)
