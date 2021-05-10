from flask import Flask, jsonify

app = Flask(__name__)

enc_types = [
    { 'des_key': "-8B key-", 'des_plaintext': "Sample plaintext for des, one of the least secure modes of encryption"},
    { '3des_key': "-16Byte key 123-", '3des_plaintext': "Sample plaintext for 3des, more secure than des but still meh" },
    { 'aes_key': "P6fx78($bfq@3sh^", 'aes_plaintext': "Sample plaintext for aes, 256 bit key is solid"}
]

@app.route("/")
def root():
    return "Root route\n"

@app.route("/enc-types", methods=["GET"])
def getEncTypes():
    return jsonify(enc_types)

if __name__ == '__main__':
    app.run(port=3000)