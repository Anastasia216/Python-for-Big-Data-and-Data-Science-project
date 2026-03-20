import pandas as pd
def input_from_console():
    """
    function reads the console input from the user
    :return:
    what was inputted by the user
    """
    text = input("Enter something: ")
    return text

def read_from_file(filename):
    """
    function reads information from the file using only python build-in abilities
    :param filename
    parameter is a location of the file program needs to read
    :return:
    content of the file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def read_from_file_with_pandas(filename):
    """
    function reads information from the file using pandas library
    :param filename
    parameter is a location of the file program needs to read
    :return:
    data loaded from the file using pandas
    """
    data = pd.read_csv(filename)
    return data.to_string()