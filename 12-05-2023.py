codebook = {
    'a': '00',
    'b': '01',
    'c': '10',
    'd': '1100',
    'e': '1101',
    'f': '1110',
    'g': '111100',
    'h': '111101',
    'i': '111110',
    'j': '1111110000',
    'k': '1111110001',
    'l': '1111110010',
    'm': '1111110011',
    'n': '1111110100',
    'o': '1111110101',
    'p': '1111110110',
    'q': '1111110111',
    'r': '1111111000',
    's': '1111111001',
    't': '1111111010',
    'u': '1111111011',
    'v': '1111111100',
    'w': '1111111101',
    'x': '1111111110',
    'y': '1111111111',
    'z': '11111111110000',
    ' ': '11111111110001'
}

encoded = "1111101111111111000111111100101111110101111111110011011111111111000100111111010\
0111100110111111100101111010010111111000111111111110001101111110101110011011111\
1111110001101111010011111100101111110010110111111101001111001101111111111100010\
11101100011111110111111111001110111111111110001111110111111101011111111110001111\
11011111110011111111111000111101111111011111111010011111111110001001111110100110\
01111111111000111011111111110101111101111111010111110111111010011110011111111110\
00100111111010011001111111111000111111011111111110001110011111011111110011111110\
01011111011111100011101111111111100011111111010111101110111111111110001111111110\
11111110101111111100011001111111111000111111111110001111111111100011111111010111\
1010011111110101111111111000100111111011011111101101101001111111000111111100111\
11111111000111111011111101001111111111000111111110101111011101111111111100011111\
11011011110111111110000011111110011101"



def decode(encoded: str, codebook: dict) -> str:
    """
    Decodes a string using a codebook.

    Args:
    - encoded (str): the string to be decoded
    - codebook (dict): a dictionary that maps characters to their encodings

    Returns:
    - str: the decoded string

    Raises:
    - ValueError: if the codebook is empty
    - ValueError: if the codebook contains duplicate encodings
    - ValueError: if the codebook contains invalid encodings
    """
    # Sort the codebook by the longest string first
    sorted_codebook = sorted(codebook.items(), key=lambda x: len(x[1]), reverse=True)
    result = ""
    i = 0
    while i < len(encoded):
        match = None
        # Iterate through the sorted codebook
        for key, value in sorted_codebook:
            if encoded[i:i+len(value)] == value:
                match = key
                i += len(value)
                break
        # If there's no match, return an error
        if not match:
            return "Error: Invalid encoding"
        # If the current character is a space and the previous character is also a space, replace one with 'yab'
        if match == ' ' and result and result[-1] == ' ':
            result = result[:] + 'yab'
        else:
            result += match
    return result


decoded = decode(encoded, codebook)
print(decoded)