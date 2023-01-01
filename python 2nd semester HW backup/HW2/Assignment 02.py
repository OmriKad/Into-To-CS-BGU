def binary_to_decimal(binary_as_str):
    """
    The function converts a given binary number to its decimal form.
    :param binary_as_str: (str) A string representation of a binary number.
    :return: (int) The result decimal form.
    """
    # Returns the highest power of 2 in the statement.
    binary_power = len(binary_as_str) - 1
    res = 0
    # Runs over the binary statement and for each iteration multiplies by the power, adds to the result and reducing
    # power by one.
    for i in binary_as_str:
        if i == "1":
            res += 2 ** binary_power
        binary_power -= 1
    return res


def decimal_to_binary(decimal_num):
    """
    The function converts a given decimal number to its binary form.
    :param decimal_num: (int) A decimal number.
    :return: (str) A string representation of a binary number.
    """
    # Result string
    st = ''
    # The case where the number is specifically 0.
    if decimal_num == 0:
        st = '0'
        return st
    while decimal_num:
        st = str(decimal_num % 2) + st
        decimal_num = decimal_num // 2
    return st


def binary_to_hex_or_oct(binary_as_str, dest_base):
    """
    The function converts a given binary number to octal or hexadecimal form.
    :param binary_as_str: (str) A string representation of a binary number.
    :param dest_base: (int) A whole number - 8 for octal and 16 for hexadecimal.
    :return: (str) A string representation of an octal/hexadecimal number.
    """
    # Dictionary for elements both relevant for hex and octal conversions.
    hex_dict = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    # Conversion to decimal number using our function.
    decimal_num = binary_to_decimal(binary_as_str)
    # Result string
    st = ''
    reminders = []
    # Reminders go to specified list in reverse order. Loop terminates when the number is zero.
    while decimal_num >= 0:
        reminders.insert(0, (decimal_num % dest_base))
        decimal_num = decimal_num // dest_base
        if decimal_num == 0:
            decimal_num = -1
    # Each element in the reminders list gets the corresponding translation and added to the result string.
    for i in reminders:
        st += hex_dict[i]
    return st


def oct_or_hex_to_binary(hexoct_num, orig_base):
    """
    This function converts octal/hexadecimal number to its binary form.
    :param hexoct_num: (str) A string representation of an octal/hexadecimal number.
    :param orig_base: (int) A whole number - 8 for octal and 16 for hexadecimal.
    :return: (str) A string representation of a binary number.
    """
    hex_dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    # Returns the highest power of 8/16 in the statement.
    binary_power = len(hexoct_num) - 1
    res = 0
    # Runs over the binary statement and for each iteration multiplies by the power, adds to the result and reducing
    # power by one.
    for i in hexoct_num:
        res += hex_dict[i] * (orig_base ** binary_power)
        binary_power -= 1
    return decimal_to_binary(res)


def pad_zeros(binary_as_str, length):
    """
    The function adds "0" to the short binary num.
    :param binary_as_str: (str) A binary representation of a number.
    :param length: (int) The desired final length for the number.
    :return: (str) The corrected binary number.
    """
    # Runs the loop no. of times as the length difference and ads "0" at each iteration.
    for i in range(length - len(binary_as_str)):
        binary_as_str = "0" + binary_as_str
    return binary_as_str


def binary_addition(binary_as_str1, binary_as_str2):
    """
    This function adds 2 binary numbers.
    :param binary_as_str1: (str) First binary number.
    :param binary_as_str2: (str) Second binary number.
    :return: (str) The result binary number of the sum.
    """
    # Result string
    res = ""
    # Padding the shorter number with "0"
    if len(binary_as_str1) < len(binary_as_str2):
        binary_as_str1 = pad_zeros(binary_as_str1, len(binary_as_str2))
    elif len(binary_as_str2) < len(binary_as_str1):
        binary_as_str2 = pad_zeros(binary_as_str2, len(binary_as_str1))
    # Carry and carry bank
    carry = ["0" for i in range(len(binary_as_str1) + 1)]
    carry_bank = {
        "0+0": "0",
        "0+1": "0",
        "1+0": "0",
        "1+1": "1"
    }
    # Calc bank
    calc_bank = {
        "0+0": "0",
        "0+1": "1",
        "1+0": "1",
        "1+1": "0"
    }
    binary_as_str1 = list(binary_as_str1)
    binary_as_str2 = list(binary_as_str2)
    # Addition run
    for i in range(-1, -1 * len(binary_as_str1) - 1, -1):
        if carry[i] == "1" and binary_as_str1[i] == "1":
            carry[i - 1] = carry_bank[binary_as_str1[i] + "+" + carry[i]]
            binary_as_str1[i] = calc_bank[carry[i] + "+" + binary_as_str1[i]]
            res = calc_bank[binary_as_str1[i] + "+" + binary_as_str2[i]] + res
        else:
            binary_as_str1[i] = calc_bank[carry[i] + "+" + binary_as_str1[i]]
            carry[i - 1] = carry_bank[binary_as_str1[i] + "+" + binary_as_str2[i]]
            res = calc_bank[binary_as_str1[i] + "+" + binary_as_str2[i]] + res
        if carry[0] == "1":
            return "1" + res
    return res


def binary_subtraction(binary_as_str1, binary_as_str2):
    """
    This function subtracts 2 binary numbers.
    :param binary_as_str1: (str) First binary number.
    :param binary_as_str2: (str) Second binary number.
    :return: (str) The result binary number of the subtraction.
    """
    # Result string
    res = ""
    # Padding the shorter number with "0"
    if len(binary_as_str1) < len(binary_as_str2):
        binary_as_str1 = pad_zeros(binary_as_str1, len(binary_as_str2))
    elif len(binary_as_str2) < len(binary_as_str1):
        binary_as_str2 = pad_zeros(binary_as_str2, len(binary_as_str1))

    # Calc bank
    calc_bank = {
        "0-0": "0",
        "0-1": "1",
        "1-0": "1",
        "1-1": "0"
    }
    binary_as_str1 = list(binary_as_str1)
    binary_as_str2 = list(binary_as_str2)
    # Subtraction run
    while binary_as_str1:
        res = calc_bank[binary_as_str1[-1] + "-" + binary_as_str2[-1]] + res
        if binary_as_str1[-1] == "0" and binary_as_str2[-1] == "1":
            last_1_indx = len(binary_as_str1) - binary_as_str1[::-1].index("1") - 1
            binary_as_str1[last_1_indx] = "0"
            for j in range(last_1_indx + 1, len(binary_as_str1) - 1):
                binary_as_str1[j] = "1"
        binary_as_str1 = binary_as_str1[:-1]
        binary_as_str2 = binary_as_str2[:-1]
    # Get rid of excess "0"
    return res[res.index("1"):]


def binary_multiplication(binary_as_str1, binary_as_str2):  # BONUS QUESTION
    """
    This function multiples 2 binary numbers.
    :param binary_as_str1: (str) First binary number.
    :param binary_as_str2: (str) Second binary number.
    :return: (str) The result binary number of the multiplication.
    """
    # Result
    if binary_as_str1 == "0" or binary_as_str2 == "0":
        return "0"
    res = binary_as_str1
    # Multiplier
    mult = binary_to_decimal(binary_as_str2)
    # Multiplying is repetitive addition
    for i in range(mult - 1):
        res = binary_addition(res, binary_as_str1)
    return res


def memory_map(binary_as_str):
    """
    This function maps a binary number to it's correct form by the length.
    The length need's to be a multiply of 8 (byte).
    :param binary_as_str: (str) The given binary number.
    :return: (str) A corrected binary number.
    """
    # Looking for the mod from multiplies of 8
    mod = len(binary_as_str) % 8
    # Gap filling of zeros
    binary_as_str = (8 - mod) * "0" + binary_as_str
    return binary_as_str


def twos_compliment(num_dec):
    """
    This function shows the twos compliment form for a given number.
    :param num_dec: (int) The given number.
    :return: (str) The binary representation for the number.
    """
    # Case of a non-negative num.
    if num_dec >= 0:
        return memory_map(decimal_to_binary(num_dec))
    # Case of a negative num
    else:
        return decimal_to_binary(num_dec * -1)


def create_dict(destination_base):
    """
    This function creates a dictionary with binary nums as keys and corresponding destination form as value.
    :param destination_base: (int) can be either octal(8) or hexadecimal(16).
    :return: result dictionary.
    """
    # Result dict
    res = {}
    for i in range(destination_base):
        # Conversion to binary
        binary_form = decimal_to_binary(i)
        # Regulates the proper appearance for the 4-bit number by adding "0" if necessary.
        mod = len(binary_form) % 4
        if mod != 0:
            binary_form = (4 - mod) * "0" + binary_form
        # The conversion to the prober from using the given base and adding to the result dict.
        destination_form = binary_to_hex_or_oct(binary_form, destination_base)
        res[binary_form] = destination_form
    return res


def dict_reversal(dictionary):
    """
    This function reverses the keys and values of a given dictionary.
    :param dictionary: (dict) The original dictionary.
    :return: (dict) The reversed dictionary.
    """
    # List of OG keys.
    keys = list(dictionary.keys())
    # List of OG values.
    values = list(dictionary.values())
    res_dict = {}
    # Iterates using index numbers and adding to new result dict but in reverse.
    for i in range(len(keys)):
        res_dict[values[i]] = keys[i]
    return res_dict


def base_conversion_w_tests(number_as_str, orig_base, dest_base):
    """
    The function Takes a given number and translate it to a different base.
    :param number_as_str: (str) Original number as a string.
    :param orig_base: (int) Original base number.
    :param dest_base: (int) Destination base.
    :return: (int) Decimal number form, (str) Binary/Octal/Hexadecimal form.
    """
    # All conversion cases for base 2.
    if orig_base == 2:
        if dest_base == 8 or dest_base == 16:
            return binary_to_hex_or_oct(number_as_str, dest_base)
        if dest_base == 10:
            return binary_to_decimal(number_as_str)
    # All conversion cases for base 8.
    if orig_base == 8:
        if dest_base == 16:
            return binary_to_hex_or_oct(oct_or_hex_to_binary(number_as_str, orig_base), dest_base)
        if dest_base == 2:
            return oct_or_hex_to_binary(number_as_str, orig_base)
        if dest_base == 10:
            return binary_to_decimal(oct_or_hex_to_binary(number_as_str, orig_base))
    # All conversion cases for base 10.
    if orig_base == 10:
        if dest_base == 2:
            return decimal_to_binary(number_as_str)
        if dest_base == 8 or dest_base == 16:
            return decimal_to_binary(binary_to_hex_or_oct(number_as_str, dest_base))
    # All conversion cases for base 16.
    if orig_base == 16:
        if dest_base == 8:
            return binary_to_hex_or_oct(oct_or_hex_to_binary(number_as_str, orig_base), dest_base)
        if dest_base == 2:
            return oct_or_hex_to_binary(number_as_str, orig_base)
        if dest_base == 10:
            return binary_to_decimal(oct_or_hex_to_binary(number_as_str, orig_base))


def main():
    # Define Tests
    # binary_to_decimal
    input_list = ["1010", "111010", "0", "11111110"]
    expected_output = [10, 58, 0, 254]
    for i in range(0, len(input_list)):
        your_output = binary_to_decimal(input_list[i])
        print("Function: binary_to_decimal\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
                                                                                                expected_output[i]),
              your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # decimal_to_binary
    input_list = [10, 58, 0, 254]
    expected_output = ["1010", "111010", "0", "11111110"]
    for i in range(0, len(input_list)):
        your_output = decimal_to_binary(input_list[i])
        print("Function: decimal_to_binary\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
                                                                                                expected_output[i]),
              your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # binary_to_hex_or_oct
    input_list = [("1010", 16), ("111010", 8), ("0", 8), ("11111110", 16)]
    expected_output = ["A", "72", "0", "FE"]
    for i in range(0, len(input_list)):
        your_output = binary_to_hex_or_oct(*input_list[i])
        print("Function: binary_to_hex_or_oct\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
                                                                                                   expected_output[i]),
              your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # oct_or_hex_to_binary
    input_list = [("A", 16), ("3A", 16), ("0", 8), ("FE", 16)]
    expected_output = ["1010", "111010", "0", "11111110"]
    for i in range(0, len(input_list)):
        your_output = oct_or_hex_to_binary(*input_list[i])
        print("Function: oct_or_hex_to_binary\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
                                                                                                   expected_output[i]),
              your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # pad_zeros
    input_list = [("1010", 8), ("111010", 7), ("0", 4), ("11111110", 16)]
    expected_output = ["00001010", "0111010", "0000", "0000000011111110"]
    for i in range(0, len(input_list)):
        your_output = pad_zeros(*input_list[i])
        print("Function: pad_zeros\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
                                                                                        expected_output[i]),
              your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # binary_addition
    input_list = [("1010", "111"), ("111010", "101000"), ("0", "1"), ("11111110", "10")]
    expected_output = ["10001", "1100010", "1", "100000000"]
    for i in range(0, len(input_list)):
        your_output = binary_addition(*input_list[i])
        print("Function: binary_addition\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
                                                                                              expected_output[i]),
              your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # binary_subtraction
    input_list = [("1010", "111"), ("111010", "101000"), ("1", "0"), ("1110100", "1010101")]
    expected_output = ["11", "10010", "1", "11111"]
    for i in range(0, len(input_list)):
        your_output = binary_subtraction(*input_list[i])
        print("Function: binary_subtraction\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
                                                                                                 expected_output[i]),
              your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # binary_multiplication
    input_list = [("1010", "111"), ("111010", "101000"), ("1", "0"), ("11", "101")]
    expected_output = ["1000110", "100100010000", "0", "1111"]
    for i in range(0, len(input_list)):
        your_output = binary_multiplication(*input_list[i])
        print("Function: binary_multiplication\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
                                                                                                    expected_output[i]),
              your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # memory_map
    input_list = ["101", "1000101", "10101110101", "1111"]
    expected_output = ["00000101", "01000101", "0000010101110101", "00001111"]
    for i in range(0, len(input_list)):
        your_output = memory_map(input_list[i])
        print("Function: memory_map\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
                                                                                         expected_output[i]),
              your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # twos_compliment
    input_list = [-128, 255, 64]
    expected_output = ["10000000", "0000000011111111", "01000000", ]
    for i in range(0, len(input_list)):
        your_output = twos_compliment(input_list[i])
        print("Function: twos_compliment\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
                                                                                              expected_output[i]),
              your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # create_dict
    input_list = [8, 16]
    expected_output = [{"0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4", "0101": "5", "0110": "6", "0111": "7"}, {"0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4", "0101": "5", "0110": "6", "0111": "7", "1000": "8", "1001": "9", "1010": "A", "1011": "B", "1100": "C", "1101": "D", "1110": "E", "1111": "F"}]
    for i in range(0, len(input_list)):
        your_output = create_dict(input_list[i])
        print("Function: create_dict\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
                                                                                          expected_output[i]),
              your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # dict_reversal
    input_list = [{'a':1, 'b':2,'c':3,'d':4}]
    expected_output = [{1:'a', 2:'b', 3: 'c', 4: 'd'}]
    for i in range(0, len(input_list)):
        your_output = dict_reversal(input_list[i])
        print("Function: dict_reversal\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
            expected_output[i]), your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # base_conversion_with_tests
    input_list = [("A", 16, 2), ("1010",2,10),("24",8,16),(255,10,2)]
    expected_output = ["1010",10,"14","11111111"]
    for i in range(0, len(input_list)):
        your_output = base_conversion_w_tests(*input_list[i])
        print("Function: base_conversion_with_tests\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
            expected_output[i]), your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))


if __name__ == "__main__":
    main()
