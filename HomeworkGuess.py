import random

calc_min = 1
calc_max = 7
calc_ops = 5

calc_ans = random.randint(calc_min, calc_max)



def get_input():

    while True:
        
        num = int(input("Enter value between 1 and 7:"))


        if calc_min <= num <= calc_max:

            return num


        else:
            print("Calc error. Please enter a value between the specified range.") 



def run_calc(num, calc_ans):

    if num == calc_ans:
        return("Solved")

    elif num < calc_ans:

        return "Add more"

    else:
        
        return "Sub more"




def start_calc():

    steps = 0
    done = False


    while steps < calc_ops:


        attemps = steps + 1
        num = get_input()
        out = run_calc(num, calc_ans)



        if out == "Solved":

            print(f"Calculation done! Your value {calc_ans} matched in {steps} steps.")
            done = True
            break

        else:
            print(f"{out}. Try again.") 


    if not done:
        print(f"Failed! You ran out of steps, the target value is {calc_ans}.") 



if __name__ == "__main__":
    print("Welcome to the calculator!")
    start_calc()