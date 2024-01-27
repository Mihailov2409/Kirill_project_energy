import json
import os
'''
    Save string with it module for json python. 
'''
def library_save(a, b, position, name_path):
    mass = {"A": a, "B": b, "Pos": position, "Name_Path": name_path}
    with open(f'library_{name_path}.json', 'w') as f:
        json.dump(mass, f, indent=4, sort_keys=True)
def save_fail(name, mass):
    person = {'Name': name, 'Mass': int(mass)}
    with open('user.json', 'w') as f:
        json.dump(person, f, indent=4, sort_keys=True)
def pars_fail():
    person = {'Name': 'user', 'Mass': int(0)}
    if os.path.isfile('user.json') == False:
        with open('user.json', 'w') as f:
            json.dump(person, f, indent=4, sort_keys=True)
    with open('user.json', 'r') as f:
        person = json.load(f)
        name = person['Name']
        mass = person['Mass']
    return name, mass
def pars_mar(march):
    with open(f'library_{march}.json', 'r') as f:
        march_s = json.load(f)
        name_a = march_s["A"]
        name_b = march_s["B"]
        name_pos = march_s["Pos"]
        name_m = march_s["Name_Path"]
        return name_a, name_b, name_pos, name_m