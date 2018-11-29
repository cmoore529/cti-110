#cti 110
#P4HW1: Budget Analysis
#Chase Moore
#11/27/18

def main():

    budget = int(input("What is your budget?"))
    more = "y"
    while more =='y':
    
        total = 0
    

      
       
        weeksExpense = int(input("amount spent this week: "))
        #add weeksExpense to the month
        total += weeksExpense
        print("This week you spent" ,total)
        more = input("More expenses? y/n ")
    #print("You're finished budgeting.")
    if budget < total:
        print("You're over budget by", budget+weeksExpense)
    elif budget > total:
            print("You're under budget by", weeksExpense-budget)



    #call main() to start the program
    #why did you comment out that print statement
main()


