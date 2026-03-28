import string
import secrets

def generate_secure_password(length=16):
    """Generates a cryptographically secure password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔐 Welcome to the Cyber Utility Belt!")
    print(f"Your secure password is: {generate_secure_password()}")