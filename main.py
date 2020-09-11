# Author: Eric Benditt erb5623@psu.edu  
# Collaborator: Joseph Phillips jmp7146@psu.edu  
# Collaborator: Kaitlyn Byrnes krb5906@psu.edu
# Collaborator: Srihulas Nidamanuru sbn5256@psu.edu
# Section: 4
# Breakout: 2


def getLetterGrade(grade): 
  getLetterGrade = float(input("Enter your CMPSC 131 grade: ")) 
  if getLetterGrade >= 93.0 :
    return 'A\n'
  elif getLetterGrade >= 90.0 :
    return 'A-\n'
  elif getLetterGrade >= 87.0 :
    return 'B+\n'
  elif getLetterGrade >= 83.0 :
    return 'B\n'
  elif getLetterGrade >= 80.0 :
    return 'B-\n'
  elif getLetterGrade >= 77.0 :
    return 'C+\n'
  elif getLetterGrade >= 70.0 :
    return 'C\n'
  elif getLetterGrade >= 60.0 :
    return 'D\n'
  elif getLetterGrade <= 60.0 :
    return 'F\n'
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade()}.") 

def run():
  if __name__ == '__main__':
    run()  




 
  


  

  
  


