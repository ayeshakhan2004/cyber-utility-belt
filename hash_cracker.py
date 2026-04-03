import hashlib

def crack_md5_hash(target_hash, dictionary_file):
    print(f"[*] Attempting to crack MD5 Hash: {target_hash}\n" + "-" * 45)
    
    try:
        with open(dictionary_file, 'r') as file:
            for line in file:
                word = line.strip()
                word_hash = hashlib.md5(word.encode('utf-8')).hexdigest()
                
                if word_hash == target_hash:
                    print(f"[+] 🔓 HASH CRACKED! The password is: {word}")
                    return True
                    
        print("[-] 🔒 Password not found in the dictionary.")
        return False
        
    except FileNotFoundError:
        print(f"[-] Error: Dictionary file '{dictionary_file}' not found.")

if __name__ == '__main__':
    target = 'cbfa85d6b4904dc1ad9a21221b66df75' 
    
    with open('mini_wordlist.txt', 'w') as f:
        f.write("admin\n123456\nletmein\npassword123\nqwerty")
        
    crack_md5_hash(target, 'mini_wordlist.txt')