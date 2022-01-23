"""

    NAND GATE PROGRAMMING LANGUAGE
    by K01e

Ever wanted to write code 4528x slower? Now you can!


    SYNTAX

This is how to define the initial conditions for updates, each slash shows a jump between frames.

| %input1,input2/input1,input2%

This is how you create objects.

| //: This is a comment!!! :
| !&: this is a nand gate, in1, in2, out1/out2 :
| <<: this is an input, out :
| >>: this is an output, in :

The !& (nand) object takes 4 arguments:
    name,
    input1,
    input2,
    output

The << (input) object takes 2 arguments:
    name,
    output

The >> (output) object takes 2 arguments:
    name,
    input

And the // (comment) object doesn't care.

"""

DEBUG = False

import re


def get_file_contents(filepath: str) -> str:
    with open(filepath, 'r') as file:
        text = file.read()
    return text


# this code extracts, stores and subsequently removes the initial condition definition

def get_origin_data(text: str) -> tuple[str | list[str]]:
    pattern = re.compile(r'^%[^\n]*%')
    one = re.match(pattern, text)[0]
    two = one.replace('%', '')
    three = two.split('/')
    four = []
    for i in three:
        four.append(i.split(","))
    return (text.replace(one, ''), four)


# this code removes all whitespace, and sets up the text to be ran in parse

def clean(text: str) -> list[list[str | list[str]]]:
    pattern = re.compile(r'\s+')
    dark = re.sub(pattern, '', text)
    split = dark.split(':')
    layered = []
    for obj in split:
        layered.append(obj.split(','))
    return layered


# this code generates a set of objects that refresh can understand

def parse(text: list[list[str | list[str]]]) -> dict[list[list[str] | str]]:

    keywords = [
        "!&",
        "<<",
        ">>",
        "//"
    ]

    state = -1      # used to determine the current thing the parser is looking at

    all_obj = {}

    for obj in text:
        
        if state == -1:

            if obj[0] in keywords: 
                state = keywords.index(obj[0])
        
        else:

            all_obj[obj[0]] = []
            
            append = lambda obk : all_obj[obj[0]].append(obk)       # anonymous function to append an object to all_obj

            append(keywords[state])
            append(obj[1:])

            state = -1
    
    return all_obj


# this code does the rest of the work

def refresh(update_list: list[str], states: dict[bool], objects: dict[list[list[str] | str]]) -> tuple[list[str] | dict[bool]]:

    new_update_list = []

    for item in update_list:
        itemdata = objects[item]                                # stores the data about the current object

        if itemdata[0] == "!&":
            
            states[item] = not ( states[ itemdata[1][0] ] and states[ itemdata[1][1] ] )        # nand operation 
            
            for output in itemdata[1][2].split('/'):            # makes sure to add all outputs to new_update_list
                new_update_list.append(output)
        
        if itemdata[0] == "<<":

            user = bool(int(input(item + " << ")))
            if user != "": states[item] = user

            for output in itemdata[1][0].split('/'):            # see above
                new_update_list.append(output)

        if itemdata[0] == ">>":

            states[item] = states[itemdata[1][0]]
            print(item + " >> " + str(int(states[item])))

    return (new_update_list, states)

        

def main():
    
    # setup all requered variables

    print("INITIALIZING")

    framecount = 0

    FILE = "./code.nnd"
    text = get_file_contents(FILE)
    originless_text, origin = get_origin_data(text)
    cleaned_text = clean(originless_text)
    objects = parse(cleaned_text)

    update_list = []
    states = {}

    for obj in objects.keys():
        states[obj] = False    

    if DEBUG:
        print(origin)
        print(objects)
        print(states)

    while True:
        
        try:
            for obj in origin[framecount]:          # add objects in origin to update_list
                update_list.append(obj)
        except: pass

        update_list, states = refresh(update_list, states, objects)
        update_list = list(dict.fromkeys(update_list))              # remove duplicates from list

        framecount += 1

        if len(update_list) == 0:           # exit loop if completed
            break 
    
    print("COMPLETED")


if __name__ == "__main__": main()