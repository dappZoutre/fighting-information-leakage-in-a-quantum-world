# Python filename: Shor-classicalEdition.py
# 
# @author James Woods
# @date May 2025
# @description Fighting Information Leakage in a Quantum World
# @license MIT (Appendix A) 

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

# RSA DECRYPTION BASICS FOR BEGINNERS:
# This script demonstrates how RSA decryption works with our tiny 8-bit educational key.
# 
# ENCRYPTION vs DECRYPTION:
# - ENCRYPTION: Uses PUBLIC key (N, e) → ciphertext = (message^e) mod N
# - DECRYPTION: Uses PRIVATE key (N, d) → message = (ciphertext^d) mod N
#
# The mathematical relationship ensures that encrypting with e and decrypting 
# with d will recover the original message, but ONLY if you know the secret d!

print("="*70)
print("RSA DECRYPTION DEMONSTRATION - 8-BIT EDUCATIONAL VERSION")
print("="*70)

# STEP 1: Recreate our educational RSA key pair
# Using the same tiny primes from our generation script
print("\n🔧 STEP 1: Recreating the 8-bit RSA key pair...")

p = 11  # First secret prime
q = 17  # Second secret prime  
N = p * q  # Modulus: 187
e = 3   # Public exponent
d = 107 # Private exponent (precomputed)

print(f"Key parameters: p={p}, q={q}, N={N}, e={e}, d={d}")

# Create the RSA private key object (contains both public and private components)
private_key = rsa.RSAPrivateNumbers(
    p=p,
    q=q, 
    d=d,
    dmp1=d % (p - 1),
    dmq1=d % (q - 1),
    iqmp=pow(q, -1, p),
    public_numbers=rsa.RSAPublicNumbers(e, N)
).private_key()

public_key = private_key.public_key()
print("✓ RSA key pair recreated successfully")

# STEP 2: Demonstrate raw mathematical RSA encryption/decryption
print("\n🧮 STEP 2: Raw mathematical RSA demonstration...")
print("(This shows the pure math without padding or formatting)")

# Choose a simple message that's smaller than our modulus N=187
original_message = 42  # Must be < 187 for our tiny key
print(f"Original message (as number): {original_message}")

# ENCRYPTION: ciphertext = (message^e) mod N
raw_ciphertext = pow(original_message, e, N)
print(f"Encryption: {original_message}^{e} mod {N} = {raw_ciphertext}")

# DECRYPTION: message = (ciphertext^d) mod N  
decrypted_message = pow(raw_ciphertext, d, N)
print(f"Decryption: {raw_ciphertext}^{d} mod {N} = {decrypted_message}")

# Verify we got back our original message
if decrypted_message == original_message:
    print("✅ Raw RSA math works! Message recovered successfully.")
else:
    print("❌ Something went wrong with the math!")

# STEP 3: Demonstrate text message encryption/decryption
print("\n📝 STEP 3: Text message encryption/decryption...")
print("(This shows how real text gets converted to numbers and back)")

# For our tiny key, we can only encrypt very short messages
# Each character must fit within our modulus when converted to ASCII
text_message = "Hi"  # Keep it short for our 8-bit demo
print(f"Original text message: '{text_message}'")

# Convert text to bytes, then to a number
message_bytes = text_message.encode('utf-8')
print(f"As bytes: {message_bytes}")

# Convert bytes to integer (big-endian)
message_as_number = int.from_bytes(message_bytes, 'big')
print(f"As number: {message_as_number}")

# Check if our message fits in our tiny modulus
if message_as_number >= N:
    print(f"⚠️  WARNING: Message too large! {message_as_number} >= {N}")
    print("Using a smaller example instead...")
    message_as_number = 72  # ASCII for 'H'
    text_message = chr(72)

print(f"Encrypting number: {message_as_number}")

# Encrypt the message
encrypted_number = pow(message_as_number, e, N)
print(f"Encrypted as: {encrypted_number}")

# Decrypt the message  
decrypted_number = pow(encrypted_number, d, N)
print(f"Decrypted as: {decrypted_number}")

# Convert back to text
try:
    decrypted_bytes = decrypted_number.to_bytes((decrypted_number.bit_length() + 7) // 8, 'big')
    decrypted_text = decrypted_bytes.decode('utf-8')
    print(f"Decrypted text: '{decrypted_text}'")
    
    if decrypted_text == text_message:
        print("✅ Text encryption/decryption successful!")
    else:
        print("❌ Text didn't match original")
except:
    print(f"Decrypted as single character: '{chr(decrypted_number)}'")

# STEP 4: Show why padding is important (and why our key is too small)
print("\n🛡️  STEP 4: Why real RSA uses padding...")
print("Our 8-bit key is too small for proper padding schemes like OAEP.")
print("Real RSA keys (2048+ bits) have room for:")
print("- Random padding to prevent identical messages from creating identical ciphertext")
print("- Integrity checks to detect tampering") 
print("- Structured formatting to prevent certain attacks")

# Try to show what would happen with proper padding (will fail due to key size)
print("\nTrying standard OAEP padding with our tiny key...")
try:
    # This will fail because our key is too small for OAEP padding
    tiny_message = b"X"  # Single byte
    encrypted = public_key.encrypt(
        tiny_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("✅ Somehow worked with OAEP!")
except Exception as err:
    print(f"❌ Failed as expected: {str(err)[:100]}...")
    print("This is why real RSA keys need to be much larger!")

try:
    print(f"Public information known to attacker: N={N}, e={e}")
except NameError as err:
    print(f"⚠️ Variable missing: {err}")
    exit(1)

# STEP 5: Security demonstration - show how easy it is to break
print("\n🔓 STEP 5: Breaking our 8-bit RSA key...")
print("Let's pretend we're an attacker who only knows the public key (N, e)")

print(f"Public information known to attacker: N={N}, e={e}")
print("Attacker's goal: Find the private exponent d")

# Factoring N to retrieve p and q
print(f"Factoring N={N}...")
found_p, found_q = None, None
for i in range(2, int(N**0.5) + 1):
    if N % i == 0:
        found_p, found_q = i, N // i
        print(f"Found secret primes: p={found_p}, q={found_q}")
        break

if found_p and found_q:
    # Calculate φ(N)
    phi_n = (found_p - 1) * (found_q - 1)
    print(f"Calculated φ(N) = {phi_n}")

    # Use known e to compute d
    try:
        found_d = pow(e, -1, phi_n)
        print(f"Calculated private exponent d = {found_d}")
        if found_d == d:
            print("🚨 PRIVATE KEY COMPLETELY COMPROMISED!")
        else:
            print("⚠️  Decryption key mismatch (still broken though).")
    except ValueError:
        print("❌ Modular inverse failed — e may not be coprime with φ(N)")
else:
    print("❌ Failed to factor N — unexpected for an 8-bit demo.")
