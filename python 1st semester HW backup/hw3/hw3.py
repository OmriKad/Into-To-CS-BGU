# *************** HOMEWORK 3 ***************
# GOOD LUCK!

# ************************ QUESTION 1 **************************
### WRITE CODE HERE
def verify_nonogram_board(board, rows_constraints, columns_constraints):
    """
    This functions checks a solution of a given nonogram board.
    :param board: (lst) list representing a nonogram board with 1 as True and 0 as True.
    :param rows_constraints: (lst) list of rows constraints.
    :param columns_constraints: (lst) list of columns constraints.
    :return: True if the solution is legal and False if not.
    """
    # Creates a list of the columns
    columns_lst = [[row[i] for row in board] for i in range(len(board[0]))]
    # Checks the constraints in the rows
    for x, y in zip(board, rows_constraints):
        if x.count(True) != y:
            return False
    # Checks the constraints in the columns
    for x, y in zip(columns_lst, columns_constraints):
        if x.count(True) != y:
            return False
    # check if Trues are far apart in the rows
    for i in range(len(board)):
        if board[i].count(True) > 1:
            while True:
                first = board[i].index(True)
                second = board[i].index(True, first + 1)
                if second - first > 1:
                    return False
                if board[i].count(True) != len(board[i]) - 1:
                    board[i].remove(True)
                break
    # check if Trues are far apart in the columns
    for i in range(len(columns_lst)):
        if columns_lst[i].count(True) > 1:
            while True:
                first = columns_lst[i].index(True)
                second = columns_lst[i].index(True, first + 1)
                if second - first > 1:
                    return False
                if columns_lst[i].count(True) != len(columns_lst[i]) - 1:
                    columns_lst[i].remove(True)
                break
    return True

    # ************************ QUESTION 2a **************************


### WRITE CODE HERE
def get_all_capital_letters(text):
    '''
    This is a function that sorts a given texts and returns a list with it's capital letters.
    :param text: (str)
    :return: (lst) list of capital letters
    '''
    capital_lst = []
    for i in text:
        # Using ASCII format we know if the i word is Capital.
        if 65 <= ord(i) <= 90:
            capital_lst.append(i)
    return capital_lst


# ************************ QUESTION 2b **************************
### WRITE CODE HERE
def split_text_to_tokens(text):
    '''
    This function eliminates unwanted characters in a given text.
    :param text: (str) A text with unwanted characters.
    :return: (lst) A list with the clean words of the original text in their order.
    '''
    final_lst = []
    tmp_str = ''
    for i in text:
        # The ASCII decimal for space key. This way we can know when a word ended.
        if ord(i) == 32:
            final_lst.append(tmp_str)
            tmp_str = ''
            continue
        # Deals with the wanted characters.
        elif 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            tmp_str = tmp_str + i
    final_lst.append(tmp_str)
    # In the cases of unwanted indexes as "space", this removes them.
    while '' in final_lst:
        final_lst.remove('')
    return final_lst


# ************************ QUESTION 2c **************************
### WRITE CODE HERE
def grade_text_tone(text):
    '''
    The function grades the text by it's tone and output's the average.
    :param text: (str) A string of text
    :return: (str) a number representing the text score
    '''
    cleaned_text = split_text_to_tokens(text)
    # The case of an empty string.
    if not cleaned_text:
        return str(format(0, '.4f'))
    count_dict = {}
    counter = 0
    result = 0
    # This section runs to count capital letters in the word, then adds them as a value with the word as a key.
    for i in cleaned_text:
        for j in i:
            if 65 <= ord(j) <= 90:
                counter += 1
                count_dict[i] = counter
        counter = 0
    # Here the code iterates on the final dictionary, the local average is being calculated and adds to the result.
    # After all local averages have been calculated and summed, the summery is divided by the text length.
    # Final result has been formatted to show all 4 digits after the decimal point.
    for x, y in count_dict.items():
        result += y / len(x)
    result = result / len(cleaned_text)
    return str(format(result, '.4f'))


# ************************ QUESTION 3a **************************
### WRITE CODE HERE
def register_students_submissions(students_raw_submissions):
    '''
    The function is receiving a raw submission of all students, correct their name if necessary and stores
    their name and submission in a dictionary. The system stores only the latest submission within the original order.
    :param students_raw_submissions: (lst) List of all raw submissions.
    :return: (dict) A dictionary of all updated and correct submissions.
    '''
    sub_dict = {}
    # The algorithm is as following: go over the input, split it do differentiate between the name and the text,
    # clean the name from unnecessary values, go over each letter in the name and correct if necessary,
    # combine the words into the full name and store it with the text in the submission dictionary.
    for i in students_raw_submissions:
        name = i[0: i.index(chr(124))]
        name = split_text_to_tokens(name)
        full_name = []
        for j in name:
            first_letter = j[0:1]
            other_letters = j[1:]
            if first_letter.isupper() and other_letters.islower():
                full_name.append(first_letter + other_letters)
            else:
                first_letter = first_letter.upper()
                other_letters = other_letters.lower()
                full_name.append(first_letter + other_letters)
        sub_dict[' '.join(full_name)] = i[i.index(chr(124)) + 1:]
    return sub_dict


# ************************ QUESTION 3b **************************
### WRITE CODE HERE
def grade_students_submissions(students_submissions):
    '''
    This functions grades each student work and stores it all in a dictionary. The work length should be between
    2 to 10 letters, Violation will result an 'F'.
    :param students_submissions: (dict) Dictionary of student name as key and work as value
    :return:(dict) Dictionary of student name as key and score as value.
    '''
    result_dict = {}
    for k, i in students_submissions.items():
        text_unspaced = i.replace(' ', '')
        if 2 > len(text_unspaced) or len(text_unspaced) > 10:
            result_dict[str(k)] = 'F'
        else:
            counter = 0
            result = 0
            for j in text_unspaced:
                if 65 <= ord(j) <= 90:
                    counter += 1
            result = format(counter / len(text_unspaced), '.4f')
            result_dict[str(k)] = str(result)
            counter = 0
    return result_dict


# ************************ QUESTION 3c **************************
### WRITE CODE HERE

def calculate_tokens_frequencies(students_submissions):
    '''
    This function outputs a dictionary with words of the students submission as a key and their count as a value.
    The functions rely on split text to tokens function to clean the words, and strips out the "list" residue symbols.
    :param students_submissions: (dict) The original students submissions.
    :return: (dict) dictionary with words of the students submission as a key and their count as a value.
    '''
    count_dict = {}
    for i, j in students_submissions.items():
        students_submissions.update({i: str(split_text_to_tokens(j.lower()))})
    values = students_submissions.values()
    values = ' '.join(values)
    values = values.replace('[', '')
    values = values.replace(']', '')
    values = values.replace(' " ', '')
    values = values.replace(',', '')
    values = values.replace("'", '')
    values = values.split()
    unduplicated_values = list(dict.fromkeys(values))
    for i in unduplicated_values:
        count_dict.update({i: values.count(i)})
    return count_dict
