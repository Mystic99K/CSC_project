import base64


def encrypt_file(data):
    data.extend(decrypt_file())
    pass_w = ''
    for word in data:
        pass_w += word
    pass_byte = bytes(pass_w, "utf-8")
    encrypted_data = base64.b64encode(pass_byte)

    with open('password.enc', "wb") as file:
        file.write(encrypted_data)


def decrypt_file():
    with open('password.enc', "rb") as file:
        encrypted_data = file.read()

    decrypted_data = base64.b64decode(encrypted_data)
    dec_nf_l_ns = str(decrypted_data)[:-1]
    dec_nf_l = dec_nf_l_ns.split('-')
    dec_l = []

    for i in range(len(dec_nf_l)):
        if i == 0:
            dec_l.append(dec_nf_l[i][2:])
        else:
            dec_l.append(dec_nf_l[i])

    if dec_l[-1] == '\'"':
        dec_l.pop(-1)

    return dec_l

