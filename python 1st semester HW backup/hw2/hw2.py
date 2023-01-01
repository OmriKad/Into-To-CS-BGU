# *************** HOMEWORK 2 ***************
# GOOD LUCK!

# ************************ QUESTION 1 **************************
### WRITE CODE HERE


def encrypt(text, key):
    # The final result will be added to these variables.
    converted_list = []
    finalstr = ''
    # Taking each letter of the sentence and converting it to its ASCII decimal format, stores it in an inital veriable.
    for i in text:
        converted_init = ord(i)
        # The spectrum for capital/small letters in the ASCII table. Taking the number and adding + converting with the desired key to a new list.
        # Takes to consideration the possibility of stepping out of the letters spectrum in the ASCII table. 
        if 65 <= converted_init <= 90:
            capital = converted_init
            if capital + key > 90:
                converted_list.append(chr(capital + key - 26))
            else:
                converted_list.append(chr(capital + key))

        elif 97 <= converted_init <= 122:
            small = converted_init
            if small + key > 122:
                converted_list.append(chr(small + key - 26))
            else:
                converted_list.append(chr(small + key))
        # Taking care of other symbols that don't need to be touched.
        else:
            converted_list.append(chr(converted_init))
    # Taking the new converted list and joining it to a new and final encrypted string.
    return finalstr.join(converted_list)


# ************************ QUESTION 2 **************************
### WRITE CODE HERE

def decrypt(text, key):
    converted_list = []
    finalstr = ''
    for i in text:
        converted_init = ord(i)
        if 65 <= converted_init <= 90:
            capital = converted_init
            if capital - key < 65:
                converted_list.append(chr(capital - key + 26))
            else:
                converted_list.append(chr(capital - key))

        elif 97 <= converted_init <= 122:
            small = converted_init
            if small - key < 97:
                converted_list.append(chr(small - key + 26))
            else:
                converted_list.append(chr(small - key))
        else:
            converted_list.append(chr(converted_init))
    return finalstr.join(converted_list)


# ************************ QUESTION 3 **************************
### WRITE CODE HERE

def naive_break(text):
    converted_list = []
    final_list = []
    for key in range(26):
        for i in text:
            i = ord(i)
            if 65 <= i <= 90:
                capital = i
                if capital - key < 65:
                    converted_list.append(chr(capital - key + 26))
                else:
                    converted_list.append(chr(capital - key))

            elif 97 <= i <= 122:
                small = i
                if small - key < 97:
                    converted_list.append(chr(small - key + 26))
                else:
                    converted_list.append(chr(small - key))
            else:
                converted_list.append(chr(i))
        final_list.append(''.join(converted_list))
        converted_list.clear()
    return (final_list)

# ************************ QUESTION 4.1 **************************
### WRITE CODE HERE
def find_common_letter(text):
    count_list = []
    for i in text:
        i = ord(i)
        if 65 <= i <= 90 or 97 <= i <= 122:
            count_list.append(i)
    print()



# ************************ QUESTION 4.2 **************************
### WRITE CODE HERE
