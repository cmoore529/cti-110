# CTI-110
#P3Lab
#Chase Moore
#11/15/18

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50
    # TO DO: define the rest of the scores

    
    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is a: A')
    else:
        if score >= B_score:
            print('Your grade is a: B')
        else:
                if score >= C_score:
                     print('Your grade is a: C')
                else:
                        if score >= D_score:
                             print('Your grade is a: D')
                        else:
                            if score  >= F_score:
                                 print('Your grade is a: F')
                                 
                                 
                                           
                                           







# program start
main()
