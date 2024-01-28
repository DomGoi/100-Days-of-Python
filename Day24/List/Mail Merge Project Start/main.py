#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", mode="r") as file:
    names=file.read().splitlines()

text_let=open("./Input/Letters/starting_letter.txt", mode="r")
letter_template=text_let.read()


for name in names:
    # Replace the placeholder [name] with the actual name
    personalized_letter = letter_template.replace("[name]", name)

    # Save the personalized letter to the "ReadyToSend" folder
    with open(f"./Output/ReadyToSend/invitation_{name}.txt", mode="w") as new_letter:
        new_letter.write(personalized_letter)

text_let.close()
