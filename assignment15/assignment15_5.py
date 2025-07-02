import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: filename.py file_name string_name")
        return

    file_name = sys.argv[1]
    str_name = sys.argv[2]

    if os.path.exists(file_name):
        fobj = open(file_name, "r")
        data = fobj.read()
        fobj.close()

        freq = data.count(str_name)
        print(f"The string '{str_name}' occurred {freq} times in the file.")
    else:
        print("The file does not exist.")

if __name__ == "__main__":
    main()