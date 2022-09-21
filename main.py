from morse_code_dict import MORSE_CODE

def main():
    # Get the morse code cifer
    cifer = MORSE_CODE().MORSE_CODE_DICT

    #Get the string from the user
    plain_text = input('Provide a string to be cifered: ').upper()
    morse_text = ''
    try:
        # Convert each character to morse code using the cifer
        for letter in str(plain_text):
            morse_text += cifer[letter]
        print(morse_text)
    # If there is a character in the string that does not occur in our dictionary propmt user for another input    
    except KeyError as e:
        print(f'You included characters {e.args} that have no translation to morse code! Please try again.')
        main()


if __name__ =='__main__':
    main()

