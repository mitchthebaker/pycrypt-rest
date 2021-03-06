from flask import Flask, jsonify, request
from pyDes import *
from Crypto.Cipher import AES
import time

app = Flask(__name__)

enc_types = [
    { 'des_key': "-8B key-", 'des_plaintext': "Sample plaintext for des, one of the least secure modes of encryption"},
    { '3des_key': "-16Byte key 123-", '3des_plaintext': "Sample plaintext for 3des, more secure than des but still meh" },
    { 'aes_key': "P6fx78($bfq@3sh^", 'aes_plaintext': "Sample plaintext for aes, a 256 bit key is solid"}
]

@app.route("/")
def root():
    return "Root route\n"

@app.route("/enc-types", methods=["GET"])
def getEncTypes():
    return jsonify(enc_types)

@app.route("/des", methods=["GET"])
# Add @profile above a function to test it with line_profiler
@profile
def desEncryption():

    # Record the starting time for the function
    start = time.time()

    # Get query parameters from the request
    args = request.args
    print(args)

    # Get plaintext from query parameter, then convert it to bytes
    plaintext_b = bytes(args['plaintext'], encoding='utf8')

    # Convert des key here to bytes
    des_key_b = bytes(args['key'], encoding='utf8')

    # Generate the des key
    key = des(des_key_b, CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

    # Encrypt the plaintext to create the ciphertext
    ciphertext = key.encrypt(plaintext_b)
    print(ciphertext)

    # Decrypt the ciphertext back into plaintext
    cipher_to_plain = key.decrypt(ciphertext)
    print(cipher_to_plain)

    # Convert the plaintext in bytes back into type string
    plaintext_s = plaintext_b.decode('utf8')
    print(plaintext_s)

    # Record the ending time for the function
    end = time.time()

    # Calculate total time taken
    timeTaken = end - start

    print(f"Runtime of the program is {timeTaken}")

    return jsonify(dict(data=[f"Runtime of DES encryption with plaintext: '{plaintext_s}', and key '{args['key']}' is {timeTaken} seconds."]))

@app.route("/3des", methods=["GET"])
#@profile 
# ^ uncomment when testing
def tripleDESEncryption():

     # Record the starting time for the function
    start = time.time()

    # Get query parameters from the request
    args = request.args
    print(args)

    # Get plaintext from query parameter, then convert it to bytes
    plaintext_b = bytes(args['plaintext'], encoding='utf8')

    # Convert des key here to bytes
    triple_des_key_b = bytes(args['key'], encoding='utf8')

    # Generate the 3des key
    key = triple_des(triple_des_key_b, CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

    # Encrypt the plaintext to create the ciphertext
    ciphertext = key.encrypt(plaintext_b)
    print(ciphertext)

    # Decrypt the ciphertext back into plaintext
    cipher_to_plain = key.decrypt(ciphertext)
    print(cipher_to_plain)

    # Convert the plaintext in bytes back into type string
    plaintext_s = plaintext_b.decode('utf8')
    print(plaintext_s)

    # Record the ending time for the function
    end = time.time()

    # Calculate total time taken
    timeTaken = end - start

    print(f"Runtime of the program is {timeTaken}")

    return jsonify(dict(data=[f"Runtime of 3DES encryption with plaintext: '{plaintext_s}', and key '{args['key']}' is {timeTaken} seconds."]))

@app.route("/aes", methods=["GET"])
#@profile 
# ^ uncomment when testing
def aesEncryption():

    # Record the starting time for the function
    start = time.time()

    # Get query parameters from the request
    args = request.args
    print(args)

    # Get plaintext from query parameter, then convert it to bytes
    plaintext_b = bytes(args['plaintext'], encoding='utf8')

    # Convert aes key here to bytes
    aes_key_b = bytes(args['key'], encoding='utf8')

    # Generate the aes cipher key
    cipher = AES.new(aes_key_b, AES.MODE_ECB)

    # Encrypt the plaintext to create the ciphertext
    ciphertext = cipher.encrypt(plaintext_b)
    print(ciphertext)

    # Generate the aes decipher key
    d_cipher = AES.new(aes_key_b, AES.MODE_ECB)

    # Decrypt the ciphertext back into plaintext
    cipher_to_plain = d_cipher.decrypt(ciphertext)
    print(cipher_to_plain)

    # Convert the plaintext in bytes back into type string
    plaintext_s = plaintext_b.decode('utf8')
    print(plaintext_s)

    # Record the ending time for the function
    end = time.time()

    # Calculate total time taken
    timeTaken = end - start

    print(f"Runtime of the program is {timeTaken}")

    return jsonify(dict(data=[f"Runtime of AES encryption with plaintext: '{plaintext_s}', and key '{args['key']}' is {timeTaken} seconds."]))

if __name__ == '__main__':
    app.run(port=3000)
    