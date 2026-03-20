def console_output(text):
    """
    function that writes text to console
    :param text:
    text that needs to be written to terminal
    """
    print(text)

def write_to_file(text, filename):
    """
    function that writes text to file
    :param text:
    text that needs to be written to file
    :param filename:
    Location of the file for the text to be written to
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text + "\n")