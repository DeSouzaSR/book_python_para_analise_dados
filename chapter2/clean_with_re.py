import re

def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result

states = ['AlabaMa ', 'Georgia! ', 'Georgia', 'georgia' , 'FlOrida' , 'west Virginia?']

print(states)
print(clean_strings(states))


