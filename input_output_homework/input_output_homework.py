# Reading all the content of the file in one variable
def reading():
    file = open('./students_names.txt').read()
    print(file)
    
# Writing a list of random names to my file
def writingRandomNames():
    randomNames = ['Nikhil Shaw', 'Bernard Reyes', 'Giovanna Nixon', 'Kyra Rivas', 'Liana Bright', 'Rayan Tate', 'Saul Mahoney', 'Juliet Deleon', 'Paulina Roth', 'Zariah Johnston', 'Ismael Sweeney', 'Cale Rivera']

    file = open('./students_names.txt', mode='a')
    for name in randomNames:
        file.write("\n"+name) 

# Reading the first n lines of a file
def readingFirstNLines():
    n = int(input("Read the first n lines (n is a positive integer greater than 0): "))
    file = open('./students_names.txt').read().split('\n')

    for line in file[:n]:
        print(line)

# Reading the last n lines of a file
def readingNLastLines():
    n = int(input("Read the last n lines (n is a positive integer greater than 0): "))
    file = open('./students_names.txt').read().split('\n')

    for line in file[-n:]:
        print(line)
        
# Checking if a given name is in the file
def checkIfNamesExists():
    file = open('students_names.txt').read().upper()
    name = input("Give me a name: ").upper()

    if name in file:
        print(name, "is in the file!")
    else:
        print(name, "is not in the file :(")
        
# Generating 26 files
def generateFiles():
    currentASCII = 65 # This is the ascii encoding of 'A'. I am using ascii to aviod creating a string containing all the alphabets
    for i in range(1,27):
        open(chr(currentASCII)+'.txt', mode='w')
        currentASCII+=1
