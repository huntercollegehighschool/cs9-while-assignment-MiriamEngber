'''
***PART 2***

Write a program that prompts the user to enter a number. The program then prints "Hunter" the number of times the user entered. Use a while loop.

Example of what should appear when the program runs:

Times to print: 3
Hunter
Hunter
Hunter

'''
number = int(input("Times to print: "))
hunter_times = 0
while number > 0:
  '''print("number=", number, " hunter_times=", hunter_times)'''
  print("Hunter") 
  hunter_times = hunter_times + 1
  '''print("I have now printed Hunter", hunter_times, "times")
  print("is", hunter_times, "equal to", number, "?")'''
  if hunter_times == number:
    '''print("Yes.")'''
    break
  else:
    '''print("No, I'll keep running!")'''