# This programis to calculate Body Mass Index(BMI) of an Individual
# Written by: Shravya Reddy Akmy
# Date: 30/8/2021
# BMI is the ratio of weight to height
# The formula for BMI is 𝑤𝑒𝑖𝑔ℎ𝑡(𝑝𝑜𝑢𝑛𝑑𝑠)/(ℎ𝑒𝑖𝑔ℎ𝑡(inches))∗(height(inches)∗703
# Input variables to be given: Weight_of_indivial, Height_of_individual
# Output: BMI_of_individual

Weight_of_individual=float(input("Enter the weight in pounds:"))
Height_of_individual=float(input("Enter the height in inches:"))

BMI_of_individual=(Weight_of_individual/(Height_of_individual*Height_of_individual))*703

print ("BMI of individual is:",BMI_of_individual)

if BMI_of_individual in range (18, 26):
    print ("BMI Assesment:Individual is a healthy person/n")
elif BMI_of_individual<18:
    print ("BMI Assesment:Individual is under-weight and has clinical issue/n")
elif BMI_of_individual>25:
    print ("BMI Assesment:Individual is over-weight and has clinical issue")






