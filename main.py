from pyscript import document, display

# Seatwork 1
def checkname(e):
    document.getElementById('output1').innerHTML = "" # clears the previous
    fname = document.getElementById('first').value.strip() # get value of first name and strips spaces
    lname = document.getElementById('last').value.strip() # get value of last name and strips spaces
    fullname = f"{fname} {lname}" # combines the two
    clubmembers = ['Alfred Cases', 'Lance Catu', 'Maiselle Marin', 'Sabine Agacita', 'Edrian Correa', 'Zeeke Fernandez'] # people in the club
    check_status = fullname in clubmembers # checks if they are in the club
    checkagain = int(check_status) # true = 1 false = 0
    messages = ((f"Sorry {fullname}, your name is not on the list."), (f"Congratulations {fullname}! You are part of the Dance Club!")) # tuple messages
    result = messages[checkagain] # check again can be index 0 or 1
    display(result, target='output1') # displays by index of the tuple

# Skills Test
# all non-metal elements
element = {"Hydrogen" : ("H", 1, 1.0079), "Helium" : ("He", 2, 4.0026), "Carbon" : ("C", 6, 12.0107), "Nitrogen" : ("N", 7, 14.0067), "Oxygen" : ("O", 8, 15.9994), "Fluorine" : ("F", 9, 18.9984), "Neon" : ("Ne", 10, 30.1797), "Phosporus" : ("P", 15, 30.9738), "Sulfur" : ("S", 16, 32.065), "Chlorine" : ("Cl", 17, 35.453), "Argon" : ("Ar", 18, 39.948), "Selenium" : ("Se", 34, 78.96), "Bromine" : ("Br", 35, 79.904), "Krypton" : ("Kr", 36, 83.798), "Iodine" : ("I", 53, 126.9045), "Xenon" : ("Xe", 54, 131.293), "Radon" : ("Rn", 86, 222.0)}

# function to search your element
def search_element(e):
    # get input from HTML
    element_1 = document.getElementById("element1").value.title()
    # retrieve information
    results = element.get(element_1, ('Element not found', '-', '-'))
    # display the result in HTML
    document.getElementById('code').innerText = element_1
    document.getElementById('symbol').innerText = results[0]
    document.getElementById('order').innerText = results[1]
    document.getElementById('mass').innerText = results[2]

# Drill 2
display('Dance Club Members:', target="output1")
grade7 = {"Raven Denum", "Atrisha Cañedo", "Anissa Pauig", "Yñigo Sindo"} # set for Grade 7
grade8 = {"Amanda Gadia", "Jay Cañedo", "Mikhaell Sindo"} # set for Grade 8
grade9 = {"Lance Catu", "Ayr Dela Cruz", "Kirsten Caagbay"} # set for Grade 9
grade10 = {"Maiselle Marin", "Maria Coronel"} # set for Grade 10
masterset = grade7|grade8|grade9|grade10 # puts together all sets
display(sorted(masterset), target="output1") # displays original set
def addname(e):
    document.getElementById('output1').innerHTML = "" # clears the previous
    fname = document.getElementById('first').value.strip() # get first name and strip spaces
    lname = document.getElementById('last').value.strip() # get last name and strip spaces
    newname = fname + " " + lname # makes the full name
    masterset.add(newname) # adds it to the set
    display(sorted(masterset), target='output1') # displays new set