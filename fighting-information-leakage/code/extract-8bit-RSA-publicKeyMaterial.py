# Python filename: extract-8bit-RSA-publicKeyMaterial.py
# 
# @author James Woods
# @date May 2025
# @description Fighting Information Leakage in a Quantum World
# @license MIT (Appendix A) 

from cryptography.hazmat.primitives import serialization

# WHAT THIS SCRIPT DOES:
# This script takes a PEM-formatted RSA public key file and extracts
# the raw mathematical components (N and e) that make up the public key.
# 
# RECAP: An RSA public key consists of just two numbers:
# - N (modulus): The product of two secret prime numbers (p × q)
# - e (exponent): Usually a small number like 3, 17, or 65537
#
# These two numbers are what someone uses to encrypt messages to you.

# STEP 1: Load the PEM file
# PEM format wraps the key data in a standardized text format with
# "-----BEGIN PUBLIC KEY-----" and "-----END PUBLIC KEY-----" markers
# The data between these markers is base64-encoded binary data
print("Loading RSA public key from PEM file...")

with open("public_key.pem", "rb") as f:
    # Read the file in binary mode ('rb') because PEM files contain
    # both text (the BEGIN/END markers) and binary data (base64 decoded)
    pem_data = f.read()
    print(f"Raw PEM data read: {len(pem_data)} bytes")
    
    # Parse the PEM format and extract the actual RSA key structure
    public_key = serialization.load_pem_public_key(pem_data)
    print("✓ Successfully parsed PEM file into RSA public key object")

# STEP 2: Extract the mathematical components
# The public_key object contains the parsed RSA parameters
# We use .public_numbers() to access the raw mathematical values
public_numbers = public_key.public_numbers()

print("\n" + "="*60)
print("RSA PUBLIC KEY COMPONENTS EXTRACTED:")
print("="*60)

# STEP 3: Display the modulus (N)
# This is the product of the two secret primes: N = p × q
# In our educational example: N = 11 × 17 = 187
modulus_n = public_numbers.n
print(f"Modulus (N): {modulus_n}")
print(f"  ↳ This is p × q where p and q are secret prime numbers")
print(f"  ↳ In our example: N = 11 × 17 = {modulus_n}")
print(f"  ↳ Bit length: {modulus_n.bit_length()} bits")

# STEP 4: Display the public exponent (e)  
# This is the encryption exponent - typically 3, 17, or 65537
exponent_e = public_numbers.e
print(f"\nExponent (e): {exponent_e}")
print(f"  ↳ This is the public encryption exponent")
print(f"  ↳ Common values: 3 (fast), 17, or 65537 (most secure)")
print(f"  ↳ Our example uses: {exponent_e}")

# STEP 5: Explain what these numbers mean for encryption
print("\n" + "="*60)
print("HOW THESE NUMBERS ARE USED:")
print("="*60)
print("To encrypt a message 'm' to this key holder:")
print(f"1. Convert message to a number less than {modulus_n}")
print(f"2. Calculate: ciphertext = (message^{exponent_e}) mod {modulus_n}")
print("3. Send the ciphertext")
print("\nOnly the holder of the private key can decrypt it because:")
print("- They know the secret primes p and q that multiply to N")
print("- They can calculate the private exponent 'd'")
print("- Decryption: message = (ciphertext^d) mod N")

# STEP 6: Security analysis for our educational example
print("\n" + "="*60)
print("SECURITY ANALYSIS OF THIS KEY:")
print("="*60)
if modulus_n < 1000:
    print("⚠️  EXTREMELY WEAK - Educational only!")
    print(f"   This {modulus_n.bit_length()}-bit key can be broken instantly")
    print("   Real keys need 4096+ bits (600+ decimal digits)")
    
    # For small N, we can actually factor it to show the vulnerability
    print(f"\n🔓 BREAKING THIS KEY (finding p and q from N={modulus_n}):")
    for i in range(2, int(modulus_n**0.5) + 1):
        if modulus_n % i == 0:
            p, q = i, modulus_n // i
            print(f"   Found factors: {p} × {q} = {modulus_n}")
            print(f"   Secret primes exposed! Private key compromised!")
            break
else:
    print(f"This {modulus_n.bit_length()}-bit key has reasonable security")

print("\n" + "="*60)
print("✓ Public key analysis complete!")
print("="*60)
