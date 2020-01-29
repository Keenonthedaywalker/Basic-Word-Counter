# __          __           _    _____                  _            
# \ \        / /          | |  / ____|                | |           
#  \ \  /\  / /__  _ __ __| | | |     ___  _   _ _ __ | |_ ___ _ __ 
#   \ \/  \/ / _ \| '__/ _` | | |    / _ \| | | | '_ \| __/ _ \ '__|
#    \  /\  / (_) | | | (_| | | |___| (_) | |_| | | | | ||  __/ |   
#     \/  \/ \___/|_|  \__,_|  \_____\___/ \__,_|_| |_|\__\___|_|   

#The commented code below is just some previous code.

#words = ["Winner", "Loser", "Epic", "Sweet", "Gay", "Nice"]

#numOfWords = len(words)

#print(numOfWords)




#Creates a variable called file that opens a text document and then reads it/
file = open("TextToRead.txt", "r")

#Prints some text, then reads and then prints whatever was in the text file.
print("Text in the File: '" + file.read() + "'")

#Creates a new var called file that opens and reads a txt file.
#Note: You have to do this again, otherwise the code wont work.
file = open("TextToRead.txt", "r")

#Creates a new var that stores file.read().
words = file.read()

#Creates a new var splits the text within the file it is reading, whenever it detects a space
#(Note: It doesn't have to be a space, you can make it anything i.e. ,)
#Then it gets the length of the variable(Which counts the amount of characters in the var)
#Then it converts it all into a string
numOfWords = str(len(words.split(" ")))

#Then it prints some text and then the variable numOfWords.
print("Number of words used in the File: " + numOfWords)






