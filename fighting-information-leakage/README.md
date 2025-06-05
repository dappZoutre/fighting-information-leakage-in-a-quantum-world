# Fighting Information Leakage in a Quantum World

**Author**: James Woods  
**License**: MIT License  
**GitHub**: [dappZoutre](https://github.com/dappZoutre)  
**LinkedIn**: [woodsjames1](https://www.linkedin.com/in/woodsjames1/)  
**Discussions Enabled** | **Issues Disabled**

---

## 📘 About the Book

**Fighting Information Leakage in a Quantum World** is a timely and groundbreaking guide that takes readers to the front lines of post-quantum cryptography (PQC), where the stakes are nothing less than the security of the global digital infrastructure.

With clarity and technical precision, author **James Woods** — cybersecurity architect, cryptography hacker, and U.S. patent holder — walks readers through the fast-approaching reality of quantum-enabled threats. From basic concepts like light switches and wave functions to hands-on quantum attacks against real-world protocols, this book transforms theory into tactical defense.

This repository contains source code, labs, and supplemental material from the book.

---

## 📂 Repository Structure

```
├── README.md                  # You're here!
├── LICENSE                    # MIT License (Appendix A)
├── code/                      # Code examples referenced in the book
│   ├── generate-8bit-RSA-keyPair.py
│   ├── extract-8bit-RSA-publicKeyMaterial.py
│   └── Shor-classicalEdition-8bit.py
├── appendix/                  # Supporting docs and license text
│   └── MIT_LICENSE.txt
└── docs/                      # GitHub Pages site source (optional future)
```

---

## 🧠 Key Topics Covered

- RSA and ECC breakdowns
- Classical vs Quantum factorization
- Shor's Algorithm (classical simulation)
- Public Key exposure and transaction tracking
- PQC migration strategies: hybrid crypto, ML-KEM, Chameleon certificates

---

## 🚀 Getting Started

All examples are tested under:
- Python 3.10.16 (via Anaconda 25.1.1)
- Dependencies: `cryptography`, `base58`, `ecdsa`, `pycryptodome`

```bash
# Install common dependencies
pip install cryptography base58 ecdsa pycryptodome
```

To run the RSA key generator and output files:
```bash
python code/generate-8bit-RSA-keyPair.py
```

To extract and display the public key material:
```bash
python code/extract-8bit-RSA-publicKeyMaterial.py
```

To simulate breaking 8-bit RSA with classical Shor logic:
```bash
python code/Shor-classicalEdition-8bit.py
```

---

## 📜 License

MIT License (see `LICENSE` or `appendix/MIT_LICENSE.txt`)  
All book code samples are open for learning, research, and development use.

---

## 🌐 GitHub Pages
A full GitHub Pages site will be published here once activated:  
👉 **https://dappZoutre.github.io/fighting-information-leakage-in-a-quantum-world/**

---

## ✍️ Author Bio

**James Woods**, CISA, CRISC, CISM, PCI QSA, IT SME INMA, is a cybersecurity innovator with over 30 years of experience spanning information security, quantum risk, cryptography, and blockchain systems. He authored widely referenced educational papers on blockchain and cryptocurrencies, is the sole inventor of U.S. Patent 9,815,573 B2, and has served as a trusted advisor for CISOs and engineering teams alike.

This book draws upon his rare convergence of physics, cryptography, and enterprise cyber defense.

---

## 📣 Connect
- 📘 Book: *Fighting Information Leakage in a Quantum World*  
- 🔗 [LinkedIn Profile](https://www.linkedin.com/in/woodsjames1/)
- 💬 GitHub Discussions (enabled on repo)

---

> "This book is more than a warning — it’s a weapon against the quantum risk."
