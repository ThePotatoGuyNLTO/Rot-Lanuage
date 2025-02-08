import os

import sys

contents = []

codefile = open("main.rot","r")

if len(sys.argv) > 1:
    file_path = sys.argv[1]  # This gets the path of the dragged file
    codefile = open(file_path,"r")
else:
    print("No file was provided.")

variable_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

conditnal_line = 0

def get_fanum(inputText):
    if inputText[6] == "'":
        output = inputText[7]
        index = 7
        full_output = ""
        while True:
            output = inputText[index]
            full_output = full_output+output
            if output == "'":
                break
            index += 1

        full_output = full_output[:-1]

        return full_output
    else:
        variable = ord(inputText[6])-97
        value = variable_values[variable]
        return value

def declare(inputText):
    index = 0
    while True:
        index += 1
        if inputText[index] == " ":
            break
    index += 1

    variable = inputText[index]
    variable = ord(variable)-97

    value = ""
    index += 6
    if not "low" in inputText:
        index += 1
    while True:
        index += 1
        if inputText[index] == "$":
            break
        value = value + inputText[index]
    
    value = value[:-1]

    if not "rizz" in inputText:
        if "low" in inputText:
            value = float(value)
        else:
            value = value[:-1]
    
    if not "rizz" in inputText:
        variable_values[variable] = value
    else:
        variable_values[variable] = variable_values[ord(value)-97]

def run_peice(inputText):
    if "fanum" in inputText:
        print(get_fanum(inputText))
    elif "taper" in inputText and "fade" in inputText:
        declare(inputText)
    elif "taper" in inputText and "input" in inputText:
        inputText_text = input()
        variable_values[ord(inputText[6])-97] = inputText_text
    if "add" in inputText and "skibidi" in inputText:
        full_output = ""

        index = 0
        while True:
            index += 1
            if inputText[index] == "'":
                break
        while True:
            index += 1
            if inputText[index] == "'":
                break
            full_output = full_output + inputText[index]
        index += 1
        if inputText[14] == "1":
            variable_values[ord(inputText[12])-97] = (variable_values[ord(inputText[12])-97]+full_output)
        if inputText[14] == "0":
            variable_values[ord(inputText[12])-97] = (full_output+variable_values[ord(inputText[12])-97])
    if "bye" in inputText and "sigma" in inputText:
        os.system("cls")
    if "then" in inputText:
        conditnal_line = line

        
        

line = 0
for x in codefile.readlines():
    line += 1
    if not conditnal_line == line:
        run_peice(x)