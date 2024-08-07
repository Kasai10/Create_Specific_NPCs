with open('Haupt_Npcs.md', 'a') as file:
    ""

def construct_atrribute_string(string):
    atrributes = string.split(',')
    string = ""
    for attribute in atrributes:
        attribute= attribute.capitalize()
        attribute = attribute.strip()
        string = string + '- ' + attribute + '\n'
    return string

def get_character():
    print("---------Create Character---------")
    name = input("Name: ").strip()
    age = input("Age: ").strip()
    gender = input("Gender: ").capitalize().strip()
    looks = input("Beschreibung: ").capitalize().strip()
    faction = input("Faction: ").capitalize().strip()
    job = input("Job: ").capitalize().strip()
    attributes = input("Attributes: ").strip()
    main_motivation = input("Main motivation: ").strip()
    background = input("Background: ").strip()

    character_description = f"""
------------------------------------------
## **{name} {age}**

**Geschlecht: **{gender}
**Fraktion: **{faction}
**Beruf: **{job}

### Aussehen
**{looks}**

### Attribute
{construct_atrribute_string(attributes)}

### Haupt Motivation
**{main_motivation}**

### Hintergrund
{background}
"""
        
    print(character_description)
    with open('Haupt_Npcs.md', 'r') as file:
        lines = file.readlines()

    # Find the index where you want to insert the character
    for i, line in enumerate(lines):
        if faction in line:
            index = i
            break
    else:
        # If the substring is not found, append to the end of the file
        index = len(lines)
        lines.insert(index, f"""
                     
# {faction}
                     """)

    # Insert the character description at the specified location
    lines.insert(index + 1, character_description)
    

    with open('Haupt_Npcs.md', 'w') as file:
        file.writelines(lines)

while True:
    get_character()



