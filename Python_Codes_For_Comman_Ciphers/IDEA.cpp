#include <iostream>

using namespace std;


void IDEAEncrypt(int* plaintext, int* key) {
    int rounds = 8;
    int modulus = 0x10001;

    for (int i = 0; i < rounds; ++i) {
        plaintext[0] = (plaintext[0] * key[i]) % modulus;
        plaintext[1] = (plaintext[1] + key[i + 8]) % modulus;
        plaintext[2] = (plaintext[2] + key[i + 16]) % modulus;
        plaintext[3] = (plaintext[3] * key[i + 24]) % modulus;

        int tmp1 = plaintext[0] ^ plaintext[2];
        int tmp2 = plaintext[1] ^ plaintext[3];

        tmp1 = (tmp1 * key[i + 32]) % modulus;
        tmp2 = (tmp2 + tmp1) % modulus;
        tmp2 = (tmp2 * key[i + 40]) % modulus;
        tmp1 = (tmp1 + tmp2) % modulus;

        plaintext[0] ^= tmp2;
        plaintext[2] ^= tmp1;

        int tmp3 = plaintext[1] ^ plaintext[3];
        plaintext[1] = plaintext[2] ^ tmp2;
        plaintext[2] = tmp3 ^ tmp1;
        plaintext[3] = tmp2 ^ tmp3;
    }

    plaintext[0] = (plaintext[0] * key[48]) % modulus;
    plaintext[1] = (plaintext[1] + key[49]) % modulus;
    plaintext[2] = (plaintext[2] + key[50]) % modulus;
    plaintext[3] = (plaintext[3] * key[51]) % modulus;
}


int main() {
    int key[52] = {0x1234, 0x5678, 0x9ABC, 0xDEF0, 0x1234, 0x5678, 0x9ABC, 0xDEF0, 
                   0x1234, 0x5678, 0x9ABC, 0xDEF0, 0x1234, 0x5678, 0x9ABC, 0xDEF0,
                   0x1234, 0x5678, 0x9ABC, 0xDEF0, 0x1234, 0x5678, 0x9ABC, 0xDEF0,
                   0x1234, 0x5678, 0x9ABC, 0xDEF0, 0x1234, 0x5678, 0x9ABC, 0xDEF0,
                   0x1234, 0x5678, 0x9ABC, 0xDEF0, 0x1234, 0x5678, 0x9ABC, 0xDEF0,
                   0x1234, 0x5678, 0x9ABC, 0xDEF0, 0x1234, 0x5678, 0x9ABC, 0xDEF0,
                   0x1234, 0x5678, 0x9ABC, 0xDEF0}; // Example 128-bit key

    int plaintext[4] = {0x1234, 0x5678, 0x9ABC, 0xDEF0}; // Example 64-bit plaintext

    // Encrypt
    IDEAEncrypt(plaintext, key);

    cout << "Cipher Text: ";
    for (int i = 0; i < 4; ++i) {
        cout << hex << plaintext[i] << " ";
    }
    cout << endl;

    return 0;
}