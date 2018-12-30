try:
    infile = open("test.txt", "r")
    outfile = open("outtest.txt","a")
except FileNotFoundError:
    print("file not found")
else:
    print("file found and opened")

    # while (line = infile.readline() != ""):
    #     print(infile.readline())

    contents = infile.readlines()
    outfile.writelines(contents)

    for s in contents:
        print(s.rstrip())
    # print(s.lstrip())
    #     print(s.strip())
# print(infile.seek(2))
# print(infile.read())
infile.close()
outfile.close()


