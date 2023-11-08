def code_morze(value):
    '''
    please add your solution here or call your solution implemented in different function from here
    then change return value from 'False' to value that will be returned by your solution
    '''
    morze_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
     'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
      'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
      'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
       '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-'}
    value = value.upper()

    result = []

    for char in value:
        if char == '':
            result.append('')
        elif char in morze_code_dict:
            result.append(morze_code_dict[char])

    return ' '.join(result)

value = 'Data Science-2022'

print(code_morze(value))