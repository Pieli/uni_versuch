# The following variable will be provided by the grading environment, you can
# access it without declaration. However, you can freely adopt the following
# value to play around with the script, as long as you keep it in the "if".
if __name__ == "__main__":
    plain_text = "abc"
    shift_by = 1

# perform a ROTn encoding
print(plain_text)
encoded = ''
for plain in plain_text:
    if not plain.isalpha():
        encoded = encoded + plain
        continue

    shift = shift_by % 26

    notplain = ord(plain) + shift

    if plain.islower():
        if notplain % 123 < 97:
            b = chr(97 + (notplain % 123))
        else:
            b = chr(notplain % 123)
    if plain.isupper():
        if notplain % 91 < 65:
            b = chr(65 + (notplain % 91))
        else:
            b = chr(notplain % 91)
    encoded = encoded + b
