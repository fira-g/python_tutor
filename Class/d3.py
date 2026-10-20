# # #conditional statements

age = 21
if age >= 18:
    print("You are eligible to vote.")
    print("123")
    print("456")
else:
    print("You are not eligible to vote.")
    print("789")
print("This is outside the if-else block.")

# #indentation 

# #nested if statements

age = 20
gender = "Male"
if age >= 18:
    if gender == "Male":
        print("You are an adult male.")
    else:
        print("You are an adult female.")
else:
    print("You cant vote")


#elif statements(else if statements)

num = 0
if num>0:
    print("The number is positive.")
elif num<0: #if num>0 is false and num<0 is true
    print("The number is negative.")

else:
    print("The number is zero.")

grade = 85
#exercise

# 1. write a program to grade a student based on their marks. The grading criteria is as follows:
# Marks >= 90: Grade A
# Marks >= 80: Grade B
# Marks >= 70: Grade C
# Marks < 70: Grade D


grade = 99

# the code below have a logical error(the more specific conditions should come first)
if grade <70:
    print("Grade: D")
elif grade >=70:
    print("Grade: C")
elif grade >=80:
    print("Grade: B")
elif grade >=90:
    print("Grade: A")

#this is the right version
if grade >=90:
    print("Grade: A")
elif grade >=80:
    print("Grade: B")
elif grade >=70:
    print("Grade: C")


#2. write a code to check wether a number is an even or odd number. If the number is even, print "The number is even." If the number is odd, print "The number is odd."
#HINT : modulus operator(%)


num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

