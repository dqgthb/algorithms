import os, sys, shutil


def main():
    for obj in os.listdir():
        if obj.isdigit():
            newName = obj
            while os.path.exists("./baekjoon/" + newName):
                print(newName + " directory already exists!")
                newName = newName + "New"
                print(newName + " created instead.")
            shutil.move(obj, "./baekjoon/" + newName)

if __name__ == "__main__":
    main()