# Ethan Lawrence
# Dec 11 2024
# evidence report
def convert_to_fahrenheit(temp):
    '''Takes in a temp in C and turns it into the same temp in F'''
    temp = temp * 9 / 5
    temp += 32
    return temp
for celsuis in range(0, 21):
    print(f'celsuis: {celsuis}   Fahrenheit: {convert_to_fahrenheit(celsuis):.1f}')