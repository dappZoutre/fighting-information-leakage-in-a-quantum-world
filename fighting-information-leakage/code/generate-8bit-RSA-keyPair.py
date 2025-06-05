# Python filename: generate-8bit-RSA-keyPair.py
# 
# @author James Woods
# @date May 2025
# @description Fighting Information Leakage in a Quantum World
# @license MIT (Appendix A) 

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# RSA BASICS FOR BEGINNERS:
# RSA is a "public key" cryptography system where you have two keys:
# 1. PUBLIC KEY: Anyone can use this to encrypt messages TO you
# 2. PRIVATE KEY: Only you have this and use it to decrypt messages
# The math ensures that messages encrypted with the public key can ONLY
# be decrypted with the corresponding private key.

# STEP 1: Choose two prime numbers
# In real RSA, these would be HUGE primes (hundreds of digits long)
# We're using tiny primes here just for learning purposes
p = 11  # First prime number
q = 17  # Second prime number

# STEP 2: Calculate N (the "modulus")
# This is one of the two numbers that make up your public key
N = p * q  # 11 × 17 = 187
print(f"N (modulus) = {N}")

# STEP 3: Choose the public exponent 'e'
# This is the other number in your public key
# 'e' must be coprime to φ(N) where φ(N) = (p-1) × (q-1)
# Common choices are 3, 17, or 65537. We're using 3 for simplicity.
e = 3  # Public exponent

# Let's calculate φ(N) to understand why e=3 works
phi_n = (p - 1) * (q - 1)  # (11-1) × (17-1) = 10 × 16 = 160
print(f"φ(N) = {phi_n}")
print(f"e = {e} is coprime to φ(N) = {phi_n}: {phi_n % e != 0}")

# STEP 4: Calculate the private exponent 'd'
# This is the "secret sauce" of your private key
# 'd' is the modular multiplicative inverse of 'e' modulo φ(N)
# In other words: (e × d) mod φ(N) = 1
# The value 107 was precomputed: (3 × 107) mod 160 = 321 mod 160 = 1
d = 107
print(f"d (private exponent) = {d}")
print(f"Verification: (e × d) mod φ(N) = ({e} × {d}) mod {phi_n} = {(e * d) % phi_n}")

# STEP 5: Create the RSA private key object
# The RSA algorithm uses several precomputed values for efficiency:
private_key = rsa.RSAPrivateNumbers(
    p=p,                    # First prime
    q=q,                    # Second prime  
    d=d,                    # Private exponent (the main secret)
    dmp1=d % (p - 1),       # d mod (p-1) - speeds up decryption
    dmq1=d % (q - 1),      # d mod (q-1) - speeds up decryption  
    iqmp=pow(q, -1, p),    # Modular inverse of q mod p
    public_numbers=rsa.RSAPublicNumbers(e, N)  # The public key components
).private_key()

print(f"dmp1 = d mod (p-1) = {d} mod {p-1} = {d % (p - 1)}")
print(f"dmq1 = d mod (q-1) = {d} mod {q-1} = {d % (q - 1)}")
print(f"iqmp = q^(-1) mod p = {q}^(-1) mod {p} = {pow(q, -1, p)}")

# STEP 6: Extract the public key
# The public key contains only (N, e) - the parts that are safe to share
public_key = private_key.public_key()

# STEP 7: Convert to PEM format
# PEM is a standard text format for storing cryptographic keys
# It's the format you see with "-----BEGIN PUBLIC KEY-----" headers
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Display the results
print("\n" + "="*50)
print("SUMMARY:")
print(f"Your PUBLIC key components: N={N}, e={e}")
print(f"Your PRIVATE key components: N={N}, d={d} (plus p,q and optimization values)")
print("\nAnyone can use your public key to encrypt messages to you.")
print("Only you can decrypt those messages using your private key.")
print("="*50)

print("\nPublic key in PEM format:")
print(pem.decode())

# SECURITY WARNING FOR EDUCATIONAL PURPOSES:
print("\⚠️  IMPORTANT SECURITY NOTES:")
print("1. This key is ONLY for learning - it's far too small for real use!")
print("2. Real RSA keys use primes that are 4096 bits long (600+ decimal digits)")
print("3. This 8-bit key could be broken in less than a second by a computer")
print("4. Never use small primes like this in production systems!")

# SAVE PUBLIC KEY TO PEM
with open("public_key.pem", "wb") as pub_file:
    pub_file.write(pem)
    print("\n📁 Public key written to 'public_key.pem'")

# OPTIONAL: Save private key too
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

with open("private_key.pem", "wb") as priv_file:
    priv_file.write(private_pem)
    print("📁 Private key written to 'private_key.pem'")
