# 🔑 NFC UID Generator

## 📌 Overview
This script generates NFC UIDs based on international standards for different types of MIFARE cards. It supports custom UID patterns, random fuzzing, and batch generation of UID lists, making it ideal for testing NFC applications, particularly with tools like Flipper Zero.

## ✨ Features
- ✅ Supports MIFARE Classic 1K, Classic 4K, and Ultralight cards.
- 🔄 Generates UIDs using predefined base patterns.
- 🎨 Supports custom UID patterns with `?` wildcards for randomness.
- 🎲 Random fuzzing of UID digits for variation.
- 📂 Batch UID file generation.

## ⚙️ Prerequisites
- 🐍 Python 3.x

## 📥 Installation
Clone or download this repository, then navigate to the script location in a terminal.

```bash
git clone <repository-url>
cd <repository-folder>
```

## 🚀 Usage
Run the script using Python:

```bash
python nfc_uid_generator.py
```

### 🖥️ Interactive Mode
The script will prompt for:
1. 📌 Card type selection (MIFARE Classic 1K, 4K, or Ultralight).
2. 🏗️ Optional custom UID pattern(s) with `?` wildcards for random digits.
3. 🔢 Number of UIDs to generate.
4. 📝 Output filename (defaults to `nfc_uids.txt`).

### 📜 Example Usage
#### 🏗️ Generating a Default UID List
```
python nfc_uid_generator.py
```
Follow the interactive prompts to generate NFC UIDs.

#### 🎨 Generating UIDs with a Custom Pattern
If prompted for a pattern, enter something like:
```
12??5AE0
```
This will replace `?` with random hex digits.

#### 📂 Batch Generation to a File
```
python nfc_uid_generator.py
```
Enter the desired quantity and filename when prompted.

## 📊 Example Output
```
=== Flipper Zero MIFARE Fuzzer UID Generator ===

Select card format:
1. Classic 1K (4 bytes)
2. Classic 4K (4 bytes)
3. Ultralight (7 bytes)

Choice (1-3): 1

Enter custom UID pattern(s) using '?' for random digits (must be 8 hex characters). 
For multiple patterns, separate them with commas.
Leave blank to use default fuzzing generation:

Number of UIDs to generate (1-1000): 5
Output filename: test_uids.txt

Generating 5 NFC UIDs...
✅ Success! Output saved to test_uids.txt

📌 Sample Generated UID:
- UID: 12C35AE0
```

## 📜 License
This script is open-source and provided under the MIT License.

## ⚠️ Disclaimer
This tool is intended for educational and testing purposes only. Use responsibly and ensure compliance with local regulations when working with NFC technology.

