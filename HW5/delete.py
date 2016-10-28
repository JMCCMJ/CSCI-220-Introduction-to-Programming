def main():
    
    infile = open('testfile.txt','r')
    file_string = infile.read()
    infile.close()
    print(file_string)


main()
