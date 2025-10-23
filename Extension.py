
filename=input("ener the file name with extension")

if '.' in filename:
    name,extension=filename.rsplit('.',1)
    print("the extension is",extension)
else:
    print("ivalid format")