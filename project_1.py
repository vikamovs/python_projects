import random

def get_nonempty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be blank. Please try again.")

def get_numeric_input(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return value
        print("Please enter a valid number.")

print('Choose one of the templates')

while True:
    templates = input('Enter 1, 2 or 3: ').strip()
    if templates in ['1', '2', '3']:
        break
    print("Invalid input. Please enter 1, 2, or 3.")

if templates == '1':
    number = get_numeric_input('Input a number: ')
    time = get_nonempty_input('Measure of time: ')
    transport = get_nonempty_input('Input mode of transport: ')
    adjective1 = get_nonempty_input('Input adjective: ') 
    adjective2 = get_nonempty_input('Input adjective again: ')
    noun = get_nonempty_input('Input noun: ')
    color = get_nonempty_input('Input color: ')
    body = get_nonempty_input('Input part of the body: ')
    verb = get_nonempty_input('Input verb: ')  
    number2 = get_numeric_input('Input a number again: ')
    noun2 = get_nonempty_input('Input noun again: ')
    noun3 = get_nonempty_input('Input noun again: ')
    body2 = get_nonempty_input('Input part of the body again: ')
    verb2 = get_nonempty_input('Input verb again: ')
    noun4 = get_nonempty_input('Input noun again: ')
    adjective3 = get_nonempty_input('Input adjective again: ')
    word = get_nonempty_input('Input a silly word: ')
    noun5 = get_nonempty_input('Input noun again: ')

    story = (
        f"It was about {number} {time} ago when I arrived at the hospital in a {transport}. "
        f"The hospital is a/an {adjective1} place, there are a lot of {adjective2} {noun} here. "
        f"There are nurses here who have {color} {body}. "
        f"If someone wants to come into my room I told them that they have to {verb} first. "
        f"I’ve decorated my room with {number2} {noun2}. "
        f"Today I talked to a doctor and they were wearing a {noun3} on their {body2}. "
        f"I heard that all doctors {verb2} {noun4} every day for breakfast. "
        f"The most {adjective3} thing about being in the hospital is the {word} {noun5}!"
    )

elif templates == '2':
    name = get_nonempty_input('Input name: ')
    noun = get_nonempty_input('Input a noun: ')
    feeling = get_nonempty_input('Input feeling: ')
    verb = get_nonempty_input('Input verb: ') 
    feeling2 = get_nonempty_input('Input feeling again: ')
    animal = get_nonempty_input('Input animal: ')
    verb2 = get_nonempty_input('Input verb again: ')
    color = get_nonempty_input('Input a color: ')
    verb3 = get_nonempty_input('Input a verb + ing: ')
    adverb = get_nonempty_input('Input an adverb + ly: ')
    number = get_numeric_input('Input number: ')
    time = get_nonempty_input('Measure of time: ')
    color2 = get_nonempty_input('Input color again: ')
    animal2 = get_nonempty_input('Input animal again: ')
    number2 = get_numeric_input('Input number again: ')
    word = get_nonempty_input('Input silly word: ')
    noun2 = get_nonempty_input('Input noun again: ')

    story = (
        f"This weekend I am going camping with {name}. "
        f"I packed my lantern, sleeping bag, and {noun}. "
        f"I am so {feeling} to {verb} in a tent. "
        f"I am {feeling2} we might see a(n) {animal}, I hear they’re kind of dangerous. "
        f"While we’re camping, we are going to hike, fish, and {verb2}. "
        f"I have heard that the {color} lake is great for {verb3}. "
        f"Then we will {adverb} hike through the forest for {number} {time}. "
        f"If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! "
        f"At night we will tell {number2} {word} stories and roast {noun2} around the campfire!!"
    )

elif templates == '3': 
    name = get_nonempty_input('Input name: ')
    adjective = get_nonempty_input('Input adjective: ')
    color = get_nonempty_input('Input a color: ')
    animal = get_nonempty_input('Input an animal: ')
    place = get_nonempty_input('Input a place: ')
    adjective2 = get_nonempty_input('Input adjective again: ')
    magical_creature = get_nonempty_input('Input magical plural: ')
    adjective3 = get_nonempty_input('Input adjective again: ')
    magical_creature2 = get_nonempty_input('Input magical (plural) again: ')
    room = get_nonempty_input('Input room in house: ')
    noun = get_nonempty_input('Input a noun: ')
    noun2 = get_nonempty_input('Input a noun again: ')
    noun3 = get_nonempty_input('Input a noun (plural) again: ')
    adjective4 = get_nonempty_input('Input adjective again: ')
    noun4 = get_nonempty_input('Input a noun (plural) again: ')
    number = get_numeric_input('Input a number: ')
    time = get_nonempty_input('Measure of time: ')
    verb = get_nonempty_input('Input a verb + ing: ')
    adjective5 = get_nonempty_input('Input adjective again: ')
    noun5 = get_nonempty_input('Input a noun again: ')

    story = (
        f"Dear {name}, "
        f"I am writing to you from a {adjective} castle in an enchanted forest. "
        f"I found myself here one day after going for a ride on a {color} {animal} in {place}. "
        f"There are {adjective2} {magical_creature} and {adjective3} {magical_creature2} here! "
        f"In the {room}, there is a pool full of {noun}. "
        f"I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}. "
        f"It feels as though I have lived here for {number} {time}. "
        f"I hope one day you can visit, although the only way to get here now is {verb} on a {adjective5} {noun5}!!"
    )

print("\n" + story)

