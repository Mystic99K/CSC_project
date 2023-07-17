import base64
from profile_data import get_profile_data


def encrypt_pass(prof_pass):
    pass_byte = bytes(prof_pass, "utf-8")
    encrypted_data = base64.b64encode(pass_byte)

    return encrypted_data


def decrypt_pass(name):
    prof_data = get_profile_data(name)
    prof_enc_pass = prof_data[4]
    decrypted_data = base64.b64decode(prof_enc_pass)
    return decrypted_data
