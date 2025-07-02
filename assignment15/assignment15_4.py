import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: filename.py file1 file2")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if os.path.exists(file1) and os.path.exists(file2):
        fobj1 = open(file1, "r")
        data1 = fobj1.read()
        fobj1.close()

        fobj2 = open(file2, "r")
        data2 = fobj2.read()
        fobj2.close()

        if data1 == data2:
            print("Success: Both files are same")
        else:
            print("Failure: Both files are different")
    else:
        print("One or both files do not exist")

if __name__ == "__main__":
    main()