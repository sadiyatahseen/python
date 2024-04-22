#'r': Read mode (default). Opens a file for reading
fileptr=open("python.txt","r")
fileptr=open("python.txt","a")
fileptr.write("yaseen is yaseeennaaa and amreen is within abrar")
print(fileptr)
if fileptr:
    print("open successfully")
fileptr.close()