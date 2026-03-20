from app.io.input import input_from_console, read_from_file, read_from_file_with_pandas
from app.io.output import console_output, write_to_file


def main():
    console_text = input_from_console()
    file_text = read_from_file("data/input.txt")
    pandas_text = read_from_file_with_pandas("data/input.csv")

    console_output(console_text)
    console_output(file_text)
    console_output(pandas_text)

    write_to_file("data/output.txt", console_text)
    write_to_file("data/output.txt", file_text)
    write_to_file("data/output.txt", pandas_text)


pass

if __name__ == '__main__':
    main()