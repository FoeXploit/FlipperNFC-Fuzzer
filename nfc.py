import random
import datetime

SWEDISH_PRESETS = {
    'property_gate': {
        'uid_length': 4,
        'description': 'Property gate (4-byte UID)'
    },
    'apartment_door': {
        'uid_length': 4,
        'description': 'Residential door systems'
    },
    'industrial_door': {
        'uid_length': 4,
        'description': 'Industrial systems'
    },
    'public_transit': {
        'uid_length': 4,
        'description': 'Transit-like cards'
    }
}

def generate_uid(length):
    """Generate 4-byte UID in Swedish common format"""
    return bytes([random.randint(0x00, 0xFF) for _ in range(length)])

def generate_nfc_file(preset, count, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for _ in range(count):
            config = SWEDISH_PRESETS[preset]
            uid = generate_uid(config['uid_length'])
            hex_uid = uid.hex().upper()
            f.write(f"{hex_uid}\n")
    return filename

def main():
    print("=== Swedish NFC Generator ===")
    presets = list(SWEDISH_PRESETS.keys())

    for i, preset in enumerate(presets, 1):
        print(f"{i}. {preset.replace('_', ' ').title()} ({SWEDISH_PRESETS[preset]['description']})")

    try:
        choice = int(input("\nEnter your choice (1-4): "))
        if not 1 <= choice <= len(presets):
            raise ValueError("Invalid choice.")

        count = int(input("How many UIDs do you want to generate (1-100)? "))
        if not (1 <= count <= 100):
            raise ValueError("Count must be between 1 and 100.")
        
        output_filename = input("Enter output filename (e.g., generated.txt): ").strip()
        if not output_filename:
            output_filename = "generated.txt"
    except ValueError as e:
        print(f"Error: {e}")
        return

    selected_preset = presets[choice - 1]
    print(f"\nGenerating {count} {selected_preset.replace('_', ' ')} UIDs...")
    generated_file = generate_nfc_file(selected_preset, count, output_filename)
    print(f"\nSuccessfully created {generated_file}")
    print("Sample entry format: 12BA5AE0")

if __name__ == "__main__":
    main()
