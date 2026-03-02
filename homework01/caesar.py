
def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    shift = 3
    for char in plaintext:
        if char.isalpha():
            base_up = ord('A')
            base_low = ord('a')
            if char.isupper():
                pos = ord(char) - base_up
                new_pos = (pos + shift) % 26
                new_char = chr(base_up + new_pos)
            else:
                pos = ord(char) - base_low
                new_pos = (pos + shift) % 26
                new_char = chr(base_low + new_pos)

            ciphertext += new_char
        else:
            ciphertext += char

    return ciphertext


def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    shift = 3

    for char in ciphertext:
        if char.isalpha():
            base_up = ord('A')
            base_low = ord('a')
            if char.isupper():
                pos = ord(char) - base_up
                new_pos = (pos - shift) % 26
                new_char = chr(base_up + new_pos)
            else:
                pos = ord(char) - base_low
                new_pos = (pos - shift) % 26
                new_char = chr(base_low + new_pos)

            plaintext += char
        else:
            plaintext += char

    return plaintext