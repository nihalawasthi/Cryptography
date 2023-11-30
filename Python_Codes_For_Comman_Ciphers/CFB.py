#21
class CFB:
    def _init_(self, message, iv):
        self.cipher_table = {
            '0b00': '0b01',
            '0b01': '0b10',
            '0b10': '0b11',
            '0b11': '0b00'
        }
        self.message = message
        self.cipherText = []
        self.IV = iv

    def toBinary(self, message):
        binaryList = []
        for c in message:
            string = "{:08b}".format(ord(c))
            for i in range(0, len(string), 2):
                binaryList.append("0b" + string[i:i + 2])
        return binaryList

    def toString(self, message):
        string = ""
        start = 0
        end = 8
        while end < len(message) + 1:
            string += chr(int(message[start:end], 2))
            start += 8
            end += 8
        return string

    def CFB_cipher(self):
        binaryMessage = self.toBinary(self.message)
        initializationVector = self.IV
        for m in binaryMessage:
            key = self.cipher_table.get(initializationVector)
            xor = '0b{:02b}'.format(int(key, 2) ^ int(m, 2))
            initializationVector = xor
            self.cipherText.append(xor)
            print("The cipher text is: " + xor)

    def CFB_decipher(self):
        initializationVector = self.IV
        plaintextBinary = ""
        for b in self.cipherText:
            key = self.cipher_table.get(initializationVector)
            xor = '{:02b}'.format(int(key, 2) ^ int(b, 2))
            initializationVector = b
            plaintextBinary += xor
            print("The plaintext in binary is: " + xor)
        plaintext = self.toString(plaintextBinary)
        return plaintext

userInput = input("Enter plaintext: ")
iv = input("Enter the Initialization Vector (IV): ")
mode = input("Enter 'encrypt' or 'decrypt': ").lower()

cfb = CFB(userInput, iv)

if mode == 'encrypt':
    cfb.CFB_cipher()
    print("The ciphertext is: " + cfb.CFB_decipher())
elif mode == 'decrypt':
    cfb.CFB_decipher()
    print("The plaintext is: " + cfb.CFB_cipher())
else:
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")