# Author: Eric Benditt erb5623@psu.edu  
# Collaborator: Joseph Phillips jmp7146@psu.edu  
# Collaborator: Kaitlyn Byrnes krb5906@psu.edu
# Collaborator: Srihulas Nidamanuru sbn5256@psu.edu
# Section: 4
# Breakout: 2


def getLetterGrade(grade): 
  if grade >= 93.0 :
    return 'A\n'
  elif grade >= 90.0 :
    return 'A-\n'
  elif grade >= 87.0 :
    return 'B+\n'
  elif grade >= 83.0 :
    return 'B\n'
  elif grade >= 80.0 :
    return 'B-\n'
  elif grade >= 77.0 :
    return 'C+\n'
  elif grade >= 70.0 :
    return 'C\n'
  elif grade >= 60.0 :
    return 'D\n'
  else:
    return 'F\n'

def run():
  grade = input("Enter your CMPSC 131 grade: ") 
  numbergrade = float(grade) 
  if numbergrade>=93.0:
    print("Your letter grade for CMPSC 131 is",getLetterGrade(100.0)+".")
  elif numbergrade>=90.0 and numbergrade<=93.0:
    print("Your letter grade for CMPSC 131 is",getLetterGrade(92.0)+".")
  elif numbergrade>= 87.0 and numbergrade<=90.0: 
    print("Your letter grade for CMPSC 131 is",getLetterGrade(88.0)+".")
  elif numbergrade>= 83.0 and numbergrade<=87.0:
    print("Your letter grade for CMPSC 131 is",getLetterGrade(84.0)+".")
  elif numbergrade>= 80.0 and numbergrade<=83.0:
    print("Your letter grade for CMPSC 131 is",getLetterGrade(81.00)+".")
  elif numbergrade>= 77.0 and numbergrade<=80.0:
    print("Your letter grade for CMPSC 131 is",getLetterGrade(78.0)+".")
  elif numbergrade>= 70.0 and numbergrade<=77.0:
    print("Your letter grade for CMPSC 131 is",getLetterGrade(71.0)+".")
  elif numbergrade>= 60.0 and numbergrade<=70.0:
    print("Your letter grade for CMPSC 131 is",getLetterGrade(61.0)+".")
  else: 
    print("Your letter grade for CMPSC 131 is",getLetterGrade(59.0)+".")

if __name__ == '__main__':
  run()  




 
  


  

  
  


