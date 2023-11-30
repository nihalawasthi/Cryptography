#12 Sbox input bit substitution program

def sbox_substitution(input_bits, sbox):
    """
    Perform S-box substitution on the input bit pattern using the given S-box.
    
    Args:
        input_bits (str): Input bit pattern as a string of '0' and '1' characters.
        sbox (list): List representing the S-box. Each element is a binary string.
        
    Returns:
        str: Output bit pattern after S-box substitution.
    """
    if len(input_bits) != len(sbox[0]):
        raise ValueError("Input bit pattern length doesn't match S-box size.")
    
    row = int(input_bits[0] + input_bits[-1], 2)
    col = int(input_bits[1:5], 2)
    output_bits = sbox[row][col]
    
    return output_bits

sbox_4x16 = [
    "1100", "1010", "1110", "0100",
    "0001", "1101", "0010", "1111",
    "1000", "0011", "0101", "1011",
    "0110", "1001", "0000", "0111"
]

input_bits = "1010"
output_bits = sbox_substitution(input_bits, sbox_4x16)
print("Input:  ", input_bits)
print("Output: ", output_bits)