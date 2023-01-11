def gradeA():
    print("A")

def gradeB():
    print ("B")

def gradeC():
    print("C")

def gradeD () :
    print("D")

def gradeF():
    print("F")
    

def main():
    print ("This program returns the letter grade for an input score")
    score = eval(input ("Enter the test score: "))

    if score >= 90: gradeA()
    if 90 > score >= 80: gradeB()
    if 80 > score >= 70: gradeC()
    if 70 > score >= 60: gradeD()
    if 60 > score: gradeF()
    
main()
