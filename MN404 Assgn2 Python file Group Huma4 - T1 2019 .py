#Accept the Name and MIT ID of the student

Name=str(input("Enter your Name: "))
ID=str(input("Enter your MIT ID: "))


#Accept the input for Class Test and Calculation

ClassTestMark= float(input("Enter your Class Test marks out of (30): "))
while ClassTestMark>30:
    print ("The marks you entered is invalid ") 
    ClassTestMark= float(input("Enter your Class Test marks out of (30): "))
    
ClassTestFullMark=30
ClassTestPercentage=10
ClassTestFinalMark = (ClassTestMark/ClassTestFullMark) * ClassTestPercentage
    
#Accept the input for Assignment1 and Calculation

Assignment1Mark= float(input("Enter your Assignment1 marks out of (55): "))
while Assignment1Mark>55:
    print ("The marks you entered is invalid")
    Assignment1Mark= float(input("Enter your Assignment1 marks out of (55): "))

Assignment1FullMark=55
Assignment1Percentage=20
Assignment1FinalMark = (Assignment1Mark/Assignment1FullMark) * Assignment1Percentage


#Accept the input for Assignment2 and Calculation

Assignment2Mark= float(input("Enter your Assignment2 marks out of (90): "))
while Assignment2Mark>90:
    print ("The marks you entered is invalid")
    Assignment2Mark= float(input("Enter your Assignment2 marks out of (90): "))

Assignment2FullMark=90
Assignment2Percentage=20
Assignment2FinalMark = (Assignment2Mark/Assignment2FullMark) * Assignment2Percentage

#Accept the input for PBL and LAB and Calculation

PblLabMark= float(input("Enter your Pbl & Tutorial marks out of (10): "))
while PblLabMark>10:
    print ("The marks you entered is invalid")
    PblLabMark= float(input("Enter your Pbl & Tutorial marks out of (10): "))

PblLabFullMark=10
PblLabPercentage=10
PblLabFinalMark = (PblLabMark/PblLabFullMark) * PblLabPercentage

#Accept the input for Exam and Calculation

ExamMark= float(input("Enter your Exam Marks out of (100): "))
while ExamMark>100:
    print ("The marks you entered is invalid")
    ExamMark= float(input("Enter your Exam Marks out of (100): "))
if ExamMark==0:
    print (" The Exam was deffered")
    exit()  

ExamFullMark= 100
ExamPercentage=40
ExamFinalMark = (ExamMark/ExamFullMark) * ExamPercentage

print()
print()

#Calculation for final mark

FinalMarkObtained= (ClassTestFinalMark + Assignment1FinalMark + Assignment2FinalMark + PblLabFinalMark + ExamFinalMark)

print ("Your CLass Test Marks is", "%.2f" %ClassTestFinalMark, "%")
print ("Your Assignment1 Marks is", "%.2f" %Assignment1FinalMark, "%")
print ("Your Assignment2 Marks is", "%.2f" %Assignment1FinalMark, "%")
print ("Your Pbl and Lab Marks is", "%.2f" %PblLabFinalMark, "%")
print ("Your Exam Marks is", "%.2f" %ExamFinalMark, "%")
print ("Your Final Marks Obtained % iS", "%.2f" %FinalMarkObtained, "%")

#Calculate the Grade

if FinalMarkObtained>=80:
    Grade= 'HD' 
    print("The Grade of", Name,ID, ("is"), Grade)
elif FinalMarkObtained>=70:
    Grade= 'D'
    print("The Grade of", Name,ID, ("is"), Grade)
elif FinalMarkObtained>=60:
    Grade= 'C'
    print("The Grade of", Name,ID, ("is"), Grade)
elif FinalMarkObtained>=50:
    Grade= 'P'
    print("The Grade of", Name,ID, ("is"), Grade)
elif FinalMarkObtained>=40:
    Grade= 'MN'
    print("The Grade of", Name,ID, ("is"), Grade)
elif FinalMarkObtained>=0:
    Grade= 'N'
    print("The Grade of", Name,ID, ("is"), Grade)
               
print()
print()

from tabulate import tabulate
print(tabulate([["Name",Name], ["ID",ID], ["ClassTestFinalMark", "%.2f" %ClassTestFinalMark], ["Assignment1FinalMark", "%.2f" %Assignment1FinalMark], ["Assignment2FinalMark", "%.2f" %Assignment2FinalMark], ["PblLabFinalMark", "%.2f" %PblLabFinalMark],["ExamFinalMark", "%.2f" %ExamFinalMark], ["FinalMarkObtained", "%.2f" %FinalMarkObtained], ["The Grade", Grade]], tablefmt="grid"))

    
    
      

