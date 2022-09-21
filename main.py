from morse_code_dict import MORSE_CODE

def main():
    cifer = MORSE_CODE().MORSE_CODE_DICT
    plain_text = input('Provide a string to be cifered: ').upper()
    morse_text = ''
    try:
        for letter in str(plain_text):
            morse_text += cifer[letter]
        print(morse_text)
    except KeyError:
        print('You included characters that have no translation to morse code! Please try again.')
        main()


if __name__ =='__main__':
    main()

