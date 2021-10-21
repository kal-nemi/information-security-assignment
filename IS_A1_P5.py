key_matrix = [[0]*2 for i in range(2)]		# Stores the key matrix

inverseOfKey =  [[0]*2 for i in range(2)]	# for the inverse of key matrix

def keyMatrix(key):	
    '''
    Function taking the text as a parameter and making the key matrix of order 2
    which will be used for encryption.
    '''
    k= 0
    for i in range(2):
        for j in range(2):
            key_matrix[i][j] = ord(key[k]) % 65
            k+=1

def inverseKey():
    '''
    Function for making the inverse of key matrix of order 2
    which will be used for decryption.
    '''
    global inverseOfKey 
    det = (key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]) % 26 
    for i in range(26):
        if (det * i) % 26 == 1:
            det = i 
            break
    inverseOfKey = [[key_matrix[1][1] * det % 26, -1 * key_matrix[0][1] *det % 26],
                    [ -1 * key_matrix[1][0] * det % 26, key_matrix[0][0] * det % 26 ]]



def Hill_cipher_encryption(plain_Text):
    '''
    
    This function will take the plain text input by user and convert it
    into the cipher text using the key matrix by hill cipher algorithm technique.
    
    '''
    encrypted_Message = ''

    plain_Text = plain_Text.replace(" ","")
    print(plain_Text)

    if len(plain_Text) % 2 !=0: 	# this if is to check if plain text is of odd number of character so 
        plain_Text += "0"		# that we can add extra charecter for making pair 

    k = 0
  

    while k < len(plain_Text):
        vector = [ord(plain_Text[k]) -ord('A') + 1, ord(plain_Text[k+1]) - ord('A') +1]
        
        k+=2
        vector = [(key_matrix[0][0] *vector[0] + key_matrix[0][1] * vector[1]) %26,
                  (key_matrix[1][0] * vector[0] + key_matrix[1][1] *vector[1]) %26]
        
        cipher_text = [chr(vector[i] + ord('A') -1) for i in range(2)]
        
        encrypted_Message += ''.join(cipher_text)
    
    return encrypted_Message

def Hill_cipher_decryption(plain_Text):
    '''
    
    This function will take the plain text input by user and convert it
    into the cipher text using the key matrix by hill cipher algorithm technique.
    
    '''

    decrypted_Message = ""
    if len(plain_Text) % 2 != 0:	# this if is to check if plain text is of odd number of character so 
        plain_Text += "0"		# that we can add extra charecter for making pair
     
    k = 0

    print(plain_Text)
    # decryption
    while k < len(plain_Text):
        vector = [ord(plain_Text[k]) - ord('A') + 1, ord(plain_Text[k + 1]) - ord('A') + 1]
        k += 2
        vector = [(inverseOfKey[0][0] * vector[0] + inverseOfKey[0][1] * vector[1]) % 26,
                  (inverseOfKey[1][0] * vector[0] + inverseOfKey[1][1] * vector[1]) % 26]
        
        cipher_text = [chr(vector[i] + ord('A') - 1) for i in range(2)]
        
        decrypted_Message += ''.join(cipher_text)

    return decrypted_Message


def main():
    '''
    This is the main function where the user gets to interact with
    '''
    key = 'ABCD'
    keyMatrix(key)
    inverseKey()

    while True:
        print("----------- Hill Cipher Algorithm For Encryption And Decryption -----------")
        print("\nEnter 1 for Encrypting your text \nEnter 2 For Decrypting the Cipher Text \n Enter 3 for exiting ")

        choice = input("\nEnter you choice:")

        if choice == '1':
            plain_Text = input("Enter the Message : ")
            encrypted_plain_Text = Hill_cipher_encryption(plain_Text.upper())
            print(f"\n Encrypted Message is : {encrypted_plain_Text}")

        elif choice == '2':
            plain_Text = input("Enter the Cipher Text Message you have : ")
            decrypted_plain_Text = Hill_cipher_decryption(plain_Text.upper())
            print(f"\n Your Decrypted Message is : {decrypted_plain_Text}")

        elif choice == '3':
            break

        else:
            print("\n!!! Wrong Choice !!! Please select from the given choices ")


if __name__ == '__main__':
    main()
