# Fundamental-of-AIML-project

# QR Code Analyzer

A simple Python tool that lets you generate QR codes and scan them. It also checks if a scanned URL looks suspicious.

---

## What It Can Do

- **Generate QR Codes** – Enter a URL and a name, and it saves a QR code image for you.
- **Scan QR Codes** – Give it an image file and it will read the QR code inside.
- **Analyze URLs** – After scanning, it checks the URL for common phishing keywords and gives a risk level.It guides you whether the QR code is fraud or not.

---

## Requirements

Make sure you have Python installed, then install these libraries:

```bash
pip install qrcode[pil] opencv-python pyzbar
```

---

## How to Run

```bash
python QRcode_analyzer.py
```

You'll see a menu with three options:

```
1. Generate QR Code
2. Scan QR Code
3. Exit
```

---

## How to Use

### Generate a QR Code
1. Choose option `1`
2. Enter the URL you want to encode
3. Enter a name for the file (e.g. `myqr` → saves as `myqr.png`)

### Scan a QR Code
1. Choose option `2`
2. Enter the path to the QR image (e.g. `myqr.png`)
3. It will show you the decoded data and a risk level

### Risk Levels
| Level | Meaning |
|-------|---------|
| ✅ LOW | Looks safe |
| ⚠️ LOW-MEDIUM | One suspicious word found |
| ⚠️ MEDIUM | Two suspicious words found |
| 🚨 HIGH | Three or more suspicious words found |



## Notes

- QR images must be in `.png` or `.jpg` format for best results
- The phishing detection is basic — it checks for common keywords only
- Non-URL data (plain text, etc.) is always rated LOW risk

## Example Image
<img width="693" height="325" alt="image" src="https://github.com/user-attachments/assets/3983ed71-5027-49d9-bc95-7abb889057a9" />

#### This would be the starting point; After this choose your options and act accordingly, Thank You! 😊

