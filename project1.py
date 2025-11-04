import random

print('Choose one of the templates')

templates = input('Enter 1, 2, or 3 (or press Enter for random): ')

if templates == '':
    templates = random.choice(['1', '2', '3'])

if templates == '1':
    number = input('Input a number: ')
    time = input('Measure of time: ')
    transport = input('Input mode of transport: ')
    adjective1 = input('Input adjective: ') 
    adjective2 = input('Input adjective again: ')
    noun = input('Input noun: ')
    color = input('Input color: ')
    body = input('Input part of the body: ')
    verb = input('Input verb: ')  
    number2 = input('Input a number again: ')
    noun2 = input('Input noun again: ')
    noun3 = input('Input noun again: ')
    body2 = input('Input part of the body again: ')
    verb2 = input('Input verb again: ')
    noun4 = input('Input noun again: ')
    adjective3 = input('Input adjective again: ')
    word = input('Input a silly word: ')
    noun5 = input('Input noun again: ')

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
    name = input('Input name: ')
    noun = input('Input a noun: ')
    feeling = input('Input feeling: ')
    verb = input('Input verb: ') 
    feeling2 = input('Input feeling again: ')
    animal = input('Input animal: ')
    verb2 = input('Input verb again: ')
    color = input('Input a color: ')
    verb3 = input('Input a verb + ing: ')
    adverb = input('Input an adverb + ly: ')
    number = input('Input number: ')
    time = input('Measure of time: ')
    color2 = input('Input color again: ')
    animal2 = input('Input animal again: ')
    number2 = input('Input number again: ')
    word = input('Input silly word: ')
    noun2 = input('Input noun again: ')

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
    name = input('Input name: ')
    adjective = input('Input adjective: ')
    color = input('Input a color: ')
    animal = input('Input an animal: ')
    place = input('Input a place: ')
    adjective2 = input('Input adjective again: ')
    magical_creature = input('Input magical creature (plural): ')
    adjective3 = input('Input adjective again: ')
    magical_creature2 = input('Input magical creature (plural) again: ')
    room = input('Input a room in a house: ')
    noun = input('Input a noun: ')
    noun2 = input('Input a noun again: ')
    noun3 = input('Input a plural noun again: ')
    adjective4 = input('Input adjective again: ')
    noun4 = input('Input a plural noun again: ')
    number = input('Input a number: ')
    time = input('Measure of time: ')
    verb = input('Input a verb + ing: ')
    adjective5 = input('Input adjective again: ')
    noun5 = input('Input a noun again: ')

    story = (
        f"Dear {name}, you are a {adjective} friend. "
        f"You live in a {color} house with your pet {animal}. "
        f"You love to visit {place} with your {adjective2} {magical_creature}. "
        f"At home, your {adjective3} {magical_creature2} waits for you in the {room}. "
        f"You have a collection of {noun3} and {noun4}. "
        f"Every {time}, you spend {number} hours {verb}. "
        f"Your favorite possession is your {adjective5} {noun5}. "
        f"Love, Your best friend."
    )

else:
    print("Invalid input. Please enter 1, 2, or 3.")

if story:
    print(story)
