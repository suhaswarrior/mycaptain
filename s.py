def main():
    print("opening a file mycap.txt")
    f= open("mycapt.txt","w+")
    print("file opened writing contents")
    f.write("This is line \n")
    print("closing file")
    f.close()
    print("opening file to read contents")
    f=open("mycapt.txt", "r")
    contents =f.read()
    print("printing data in file")
    print(contents)
if __name__== "__main__":
  main()