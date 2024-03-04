#Ask the user to type in a word in upper case. If they type it in lower case, ask them to try again. Keep repeating this until they type in a message all in uppercase. 

file = open("Names.txt","a")

new_name = input("Enter a new name: ")

file.write(new_name ,"\n")

file.close()

file = open("Names.txt","r")

print(file.read())

file.close()