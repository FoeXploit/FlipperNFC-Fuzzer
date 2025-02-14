# 🇸🇪 Swedish NFC UID Generator v2.0 🚀

This Python tool simulates the generation of **real Swedish system-compatible UIDs** for various applications. It is designed to mimic the UID formats used in Swedish systems, such as Stockholm Public Transport (SL), industrial systems by ASSA Abloy, apartment door systems, and property gates. Each application type is based on specific field structures and includes a fixed prefix, ensuring that the generated UIDs resemble actual UIDs from Swedish systems.

---

## ✨ Features

- **Application-Specific UID Generation** 🔑  
  Generate UIDs that follow predefined structures for:
  - **Public Transit** (e.g., SL Access Cards) 🚌
  - **Industrial Door Systems** (e.g., ASSA Abloy industrial systems) 🏭
  - **Apartment Door Systems** (e.g., HSB Living) 🏢
  - **Property Gates** (e.g., Nordomatic systems) 🚪

- **Card Type Selection** 📇  
  Supports multiple card formats:
  - **Classic 1K & Classic 4K:** 4-byte UIDs  
  - **Ultralight:** 7-byte UIDs

- **Detailed Breakdown** 📝  
  Each generated UID includes a human-readable breakdown of its constituent fields (e.g., prefix, transport authority, company ID, etc.) in the output file.

- **Realistic UID Structure** 🔍  
  The generation logic uses fixed prefixes and realistic field assignments (including random selections and date-based calculations) to simulate production-grade UID formats.

---

## 📚 System-Specific UID Logic

The script defines system-specific patterns in the `SWEDISH_UID_PATTERNS` dictionary. For example:

- **Public Transit** 🚌  
  - **Prefix:** `0x04`  
  - **Structure:**  
    - `prefix` (1 byte)  
    - `transport_authority` (2 bytes; e.g., `0xAB` for SL or `0xCD` for Västtrafik)  
    - `card_type` (1 byte; different values for Adult, Child, Senior)  
    - `issuer_code` (1 byte; e.g., `0x25` for Assa Abloy)  
    - `serial` (2 bytes; random)

- **Industrial Door** 🏭  
  - **Prefix:** `0x02`  
  - **Structure:**  
    - `prefix` (1 byte)  
    - `company_id` (2 bytes; e.g., `0x0041` for Volvo, `0x003B` for Scania)  
    - `facility_code` (1 byte)  
    - `door_group` (1 byte)  
    - `checksum` (1 byte; calculated as XOR of previous bytes)  
    - `serial` (2 bytes; random)

- **Apartment Door** 🏢  
  - **Prefix:** `0x01`  
  - **Structure:**  
    - `prefix` (1 byte)  
    - `municipality_code` (2 bytes; ISO 3166-2:SE code)  
    - `housing_assoc` (1 byte)  
    - `building_id` (1 byte)  
    - `unit_code` (1 byte)  
    - `issue_date` (2 bytes; encoded as week and year)

- **Property Gate** 🚪  
  - **Prefix:** `0x03`  
  - **Structure:**  
    - `prefix` (1 byte)  
    - `region_code` (1 byte; e.g., `0x01` for Norrland)  
    - `property_type` (1 byte; e.g., Residential or Commercial)  
    - `installer_id` (1 byte; certified partner code)  
    - `activation_date` (2 bytes; days since 2000-01-01)  
    - `unique_id` (2 bytes; random)

The card types determine the total length of the UID. For example, Classic cards produce 4-byte UIDs, while Ultralight cards produce 7-byte UIDs.

---

## 🛠️ Requirements

- Python 3.6 or higher

---

## ▶️ How to Use

1. **Clone or Download the Repository**  
   Save the script (e.g., as `swedish_uid_generator.py`) to your local machine.

2. **Run the Script**

   Open a terminal and execute:

   ```bash
   python swedish_uid_generator.py
   ```

3. **Follow On-Screen Prompts**

   - **Select Application Type:**  
     Choose from options like Public Transit, Industrial Door, Apartment Door, or Property Gate.

   - **Select Card Format:**  
     Choose the card type (Classic 1K, Classic 4K, or Ultralight).

   - **Specify UID Quantity:**  
     Enter the number of UIDs you wish to generate (between 1 and 1000).

   - **Provide an Output Filename:**  
     The generated UIDs (with field breakdowns) will be saved to the specified file.

4. **Review the Output**  
   Each line in the output file includes the generated UID in uppercase hexadecimal format followed by a comment with the breakdown of each field.

---

## 📖 Example Output

An example line in the output file might look like:

```
04AB01A9253F # {'prefix': '0x04', 'transport_authority': '0xABCD', 'card_type': '0x01', 'issuer_code': '0x25', 'serial': '0x3F92'}
```

This line shows:
- The UID: `04AB01A9253F`  
- A breakdown of its components: the fixed prefix, selected transport authority, card type, issuer code, and a randomly generated serial number.

---

## ⚠️ Disclaimer

This tool is a simulation designed to mimic real Swedish system UID structures. The generated UIDs are **not** valid for use in any official or commercial systems. They are intended for testing, educational purposes, or internal development only.

---

## 📜 License

This project is provided "as is" without any warranties. Use it at your own risk. Feel free to modify and distribute as needed.

---

Enjoy generating your Swedish NFC UIDs! 🎉
```
