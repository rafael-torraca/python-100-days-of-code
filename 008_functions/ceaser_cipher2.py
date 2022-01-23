#let's import string
import string

# Let's create a list of alphabets which we'll use for encryption
alphabets = list((string.ascii_lowercase + string.ascii_uppercase)*2)

#let's create the main function that will run this program
def ceaser_cypher():

    #let's get user's intention, whether they want to encrypt or decrypt
    code_route = input('Do you want to encrypt or decrypt?, type in "encrypt" to encrypt or type in "decrypt" to decrypt\n').lower()

    #let's creat a list of keywords we expect from users
    code_route_response = ['decrypt', 'encrypt']

    
    #let's force the user to put only the information we need
    while code_route not in code_route_response:
        code_route = input('Please enter the right keyword❗, type in "encrypt" to encrypt or type in "decrypt" to decrypt\n')
    
    
#     let's get the user shift key which will use in encrypting and decrypting
#     and also capture and eliminate possible errors when the user tries putting anything else but integer
    while True:
        try:
            shift_num = int(input('Please type in your encrypt/decrypt shift key number, it must be digits:\n'))
        except:
            print('Please make sure you only typed in an integer for your encrypt/decrypt shift number:\n')
            continue