import base64
import sys

def encode_base64(text):
    """Encodes a normal string into Base64."""
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode_base64(b64_string):
    """Decodes a Base64 string back to normal text."""
    try:
        decoded_bytes = base64.b64decode(b64_string)
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return f"[-] Error decoding: Invalid Base64 string."

if __name__ == "__main__":
    print("🛠️ Base64 Encoder/Decoder")
    
    secret_message = "admin_password_123!"
    
    encoded = encode_base64(secret_message)
    print(f"\n[+] Original: {secret_message}")
    print(f"[+] Encoded Payload: {encoded}")
    
    decoded = decode_base64(encoded)
    print(f"[+] Decoded Payload: {decoded}")