def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    keyword_index = 0

    for char in plaintext:
        if char.isalpha():
            key_char = keyword[keyword_index % len(keyword)].upper()
            shift = ord(key_char) - ord('A')
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            pos = ord(char) - base
            new_pos = (pos + shift) % 26
            new_char = chr(base + new_pos)

            ciphertext += new_char
            keyword_index += 1
        else:
            ciphertext += 1
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword_index = 0

    for char in ciphertext:
        if char.isalpha():
            key_char = keyword[keyword_index % len(keyword)].upper()
            shift = ord(key_char) - ord('A')
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            pos = ord(char) - base
            new_pos = (pos - shift) % 26
            new_char = chr(base + new_pos)

            plaintext += new_char
            keyword_index += 1
        else:
            plaintext += char

    return plaintext