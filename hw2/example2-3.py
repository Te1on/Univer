def count_unique_codes(words):
    morse_signs = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."
    ]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    morse_base = dict(zip(alphabet,  morse_signs))
    cipher_sentence = []
    for word in words:
        cipher_word = ''
        for letter in word:
            cipher_word += morse_base[letter]
        cipher_sentence += [cipher_word]
    return len(set(cipher_sentence))


if __name__ == "__main__":
    print(count_unique_codes(["gin", "zen", "gig", "msg"]))
