import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: filename.py input file name")
        return

    FileName = sys.argv[1]

    ret = os.path.exists(FileName)

    if(ret == True):
        print("File is present in the current directory")

        fobj1 = open(FileName, "r")
        data = fobj1.read()
        fobj1.close()

        fobj2 = open("demo.txt", "w")
        fobj2.write(data)
        fobj2.close()

        print("Data copied successfully into 'demo.txt'")

    else:
        print("There is no such file")

if __name__== "__main__":
    main()