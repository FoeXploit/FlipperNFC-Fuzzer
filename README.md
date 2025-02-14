# 🇸🇪 Swedish NFC Generator 🔑

A simple command-line tool written in Python to generate random 4-byte UIDs in the Swedish common format for NFC systems. This script supports multiple presets tailored for different applications such as property gates, residential doors, industrial systems, and public transit. **It is specifically designed for use with the Flipper Zero device**, enabling you to generate NFC UIDs that are ready to be deployed on your Flipper Zero for various NFC applications.

## 📋 Table of Contents

- [Features ✨](#features-)
- [Installation 💻](#installation-)
- [Usage 🚀](#usage-)
- [Flipper Zero Compatibility 📱](#flipper-zero-compatibility-)
- [Code Overview 🧐](#code-overview-)
- [Customization 🛠️](#customization-)
- [Contributing 🤝](#contributing-)
- [License 📄](#license-)
- [Disclaimer ⚠️](#disclaimer-)
- [Acknowledgements 🙏](#acknowledgements-)

## ✨ Features

- **Multiple Presets:** Supports various NFC systems:
  - **Property Gate:** For 4-byte UID property access systems.
  - **Apartment Door:** For residential door systems.
  - **Industrial Door:** For industrial security systems.
  - **Public Transit:** For transit-like cards.
- **Interactive CLI:** Choose presets, specify the number of UIDs (1-100), and set the output filename interactively.
- **Random UID Generation:** Generates random hexadecimal UIDs using Python’s built-in libraries.
- **Flipper Zero Ready:** Generate UIDs in a format that is compatible with the Flipper Zero's NFC emulation features.

## 💻 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/nfc.python.git

    Navigate to the project directory:

cd nfc.python

(Optional) Create a virtual environment:

This project uses only standard libraries, but it’s good practice to work in a virtual environment.

    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    pip install --upgrade pip

🚀 Usage

Run the script using Python:

python nfc.py

You will be guided through a series of prompts:

    Select a Preset: A list of available presets will be displayed. Enter the corresponding number (1-4).
    Specify Quantity: Input how many UIDs you want to generate (between 1 and 100).
    Set Output Filename: Provide a name for the output file (e.g., generated.txt). If left blank, it defaults to generated.txt.

Example session:

=== Swedish NFC Generator ===
1. Property Gate (Property gate (4-byte UID))
2. Apartment Door (Residential door systems)
3. Industrial Door (Industrial systems)
4. Public Transit (Transit-like cards)

Enter your choice (1-4): 2
How many UIDs do you want to generate (1-100)? 10
Enter output filename (e.g., generated.txt): apartment_uids.txt

Generating 10 apartment door UIDs...
Successfully created apartment_uids.txt
Sample entry format: 12BA5AE0

The generated file will contain the specified number of UIDs in uppercase hexadecimal format, one per line.
📱 Flipper Zero Compatibility

This tool is Flipper Zero ready! The generated NFC UIDs are perfectly formatted for use with the Flipper Zero device, a versatile multi-tool for pentesters, hackers, and tech enthusiasts. Simply generate the UIDs, load them onto your Flipper Zero, and start exploring NFC functionalities.

For more information on the Flipper Zero, visit the official website.
🧐 Code Overview

    SWEDISH_PRESETS:
    A dictionary that stores configurations (UID length and description) for each preset.

    generate_uid(length):
    Generates a random UID of the specified length (in bytes). The UID is returned as a bytes object.

    generate_nfc_file(preset, count, filename):
    Generates the desired number of UIDs based on the selected preset and writes them to the provided filename.

    main():
    Provides the command-line interface for user interaction, allowing selection of presets, count, and output filename. It then triggers UID generation and writes the results to a file.

🛠️ Customization

Feel free to modify or extend this tool:

    Add New Presets:
    Modify the SWEDISH_PRESETS dictionary to include additional NFC system configurations.

    Change UID Length:
    Adjust the uid_length parameter in any preset to generate UIDs of different lengths.

    Integrate with Other Systems:
    Use the generated UIDs as part of a larger NFC management or testing system.

🤝 Contributing

Contributions are welcome! If you have suggestions, feature requests, or bug fixes, please feel free to open an issue or submit a pull request. For major changes, please discuss them first via an issue.
📄 License

This project is licensed under the MIT License. See the LICENSE file for more details.
⚠️ Disclaimer

This tool is intended for educational purposes only. It is provided as-is and for demonstration and learning purposes. The author and contributors are not responsible for any misuse or legal issues that may arise from its use. Please use it responsibly and in compliance with all applicable laws and regulations.
🙏 Acknowledgements

This tool was created to provide a quick and easy way to generate Swedish-format NFC UIDs for various applications, especially tailored for the Flipper Zero. Special thanks to all contributors and the open-source community for their support.
