import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hash Cracker")
print(ascii_banner)

print("Algorithms available: MD5 | SHA1 | SHA224 | SHA512 | SHA384")

hash_type = input("What's the hash type? ").upper()
wordlist_location = input("Enter wordlist location: ")
hash_to_crack = input("Enter hash: ")

try:
    with open(wordlist_location, "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            hash_object = hashlib.new(hash_type)
            hash_object.update(word.encode("utf-8"))
            hashed = hash_object.hexdigest()
            
            if hash_to_crack == hashed:
                print(f"\033[1;32m HASH FOUND: {word}\n")
                break
        else:
            print(f"Hash not found in the wordlist for {hash_type}.")
except FileNotFoundError:
    print("Wordlist file not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
