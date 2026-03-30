import qrcode
import cv2
from pyzbar.pyzbar import decode
import os
import sys


# important
def check_non_empty_input(user_input, field_name):
    if not user_input:
        print(f"❌ Error: {field_name} cannot be empty.")
        return False
    return True


def check_file_exists(path):
    if not os.path.exists(path):
        print("❌ Error: File does not exist.")
        return False
    return True


# QR generator

def generate_qr_code():
    print("📌 QR CODE GENERATION ")

    URL = input("Enter a URL to generate QR code: ").strip()
    if not check_non_empty_input(URL, "URL"):
        return

    name = input("Enter a name for your QR code: ").strip()
    if not check_non_empty_input(name, "Name"):
        return

    file_path = f"{name}.png"

    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )

        qr.add_data(URL)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_path)

        print("\n✅ QR code successfully generated!")
        print(f"📁 Saved as: {file_path}")

    except Exception as e:
        print(f"❌ Unexpected error during QR generation: {e}")


# QR scanner

def scan_qr():
    print("📌 QR CODE SCANNING MODULE")

    path = input("Enter QR image path: ").strip()
    if not check_non_empty_input(path, "File path"):
        return

    if not check_file_exists(path):
        return

    try:
        img = cv2.imread(path)

        if img is None:
            print("❌ Error: Unable to read image file.")
            return

        decoded_objects = decode(img)

        if not decoded_objects:
            print("❌ No QR code detected in the image.")
            return

        print("\n🔍 QR Code(s) Detected:", len(decoded_objects))

        for index, obj in enumerate(decoded_objects, start=1):
            data = obj.data.decode("utf-8")
            print(f"QR #{index} Data: {data}")
            analyze_data(data)

    except Exception as e:
        print(f"❌ Error during scanning: {e}")


# Analysis
def analyze_data(data):
    data_lower = data.lower()

    if data.startswith("http" or "https"):
        print("📌 Type Detected: URL")

        suspicious_keywords = [
            "login", "verify", "bank", "secure", "update", "now or never", "jackpot"
            "account", "password", "otp", "signin", "confirm","fraud", "urgent",
            "prize", "lottery"
        ]

        risk_score = 0
        detected_keywords = []

        for keyword in suspicious_keywords:
            if keyword in data_lower:
                risk_score += 1
                detected_keywords.append(keyword)

        print(f"🔎 Suspicious Indicators Found: {detected_keywords if detected_keywords else 'None'}")

        # Risk checker
        if risk_score >= 3:
            print("🚨 Risk Level: HIGH (Strong Phishing Indicators)")
        elif risk_score == 2:
            print("⚠️ Risk Level: MEDIUM (Moderate Suspicion)")
        elif risk_score == 1:
            print("⚠️ Risk Level: LOW-MEDIUM (Minor Suspicion)")
        else:
            print("✅ Risk Level: LOW (Likely Safe)")

    else:
        print("📌 Type Detected: TEXT / OTHER")
        print("✅ Risk Level: LOW")


# Main Function

def main():
    print("--------------------------------")
    print("   AI-BASED QR CODE ANALYZER  ")
    print("--------------------------------")

    while True:
        print("\nAvailable Options:")
        print("1. Generate QR Code")
        print("2. Scan QR Code")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            generate_qr()
        elif choice == "2":
            scan_qr()
        elif choice == "3":
            print("👋 Exiting program. Goodbye!")
            sys.exit()
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()