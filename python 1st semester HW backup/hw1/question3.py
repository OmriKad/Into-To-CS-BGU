# ************************ HOMEWORK 1 QUESTION 3 **************************
def question3(input_num):
    print('************ TO DO: Question 3 ************')  # TODO - DELETE BEFORE SUBMISSION
    ### WRITE CODE HERE
    # Relates for an even number
    if input_num % 2 == 0:
        summery_even = 0
        for i in range(1, input_num, 2):
            summery_even = summery_even + i
        print(summery_even)

    # Relates for an odd number
    elif input_num % 2 != 0:
        summery_odd = 0
        for i in range(1, input_num+1, 2):
            summery_odd = summery_odd + i
        print(summery_odd)
