import random
import sys

# ========================================================================
# NFC UID GENERATION (INTERNATIONAL STANDARD)
# ========================================================================

CARD_TYPES = {
    'classic_1k': {'uid_length': 4},   # 4-byte (8 hex digits)
    'classic_4k': {'uid_length': 4},     # 4-byte (8 hex digits)
    'ultralight': {'uid_length': 7}      # 7-byte (14 hex digits)
}

# ------------------------------------------------------------------------
# Default base patterns for fuzzing (Flipper Zero MIFARE Fuzzer style)
# ------------------------------------------------------------------------
BASE_PATTERNS = {
    'classic_1k': "12BA5AE0",
    'classic_4k': "12BA5AE0",
    'ultralight': "04BA5AE0D12345"
}

def fuzz_uid(base, changes=1):
    """
    Fuzz a base UID by randomly changing a given number of nibble positions.
    :param base: The base UID string (hex digits).
    :param changes: The number of hex digits to change.
    :return: A fuzzed UID string.
    """
    uid_list = list(base)
    indices = random.sample(range(len(base)), changes)
    for i in indices:
        original = uid_list[i]
        choices = [ch for ch in "0123456789ABCDEF" if ch != original]
        uid_list[i] = random.choice(choices)
    return ''.join(uid_list)

# ========================================================================
# UID GENERATION FUNCTION WITH OPTIONAL PATTERN OR FUZZING
# ========================================================================

def generate_nfc_uid(card_type, custom_patterns=None):
    """
    Generate a NFC UID for the given card type.
    
    - If custom_patterns is provided (a list of pattern strings), one of them is
      chosen at random.
      * If the pattern contains '?' wildcards, they will be replaced with random hex digits.
      * If the pattern contains no wildcards, it will be fuzzed (randomly modified) to produce variation.
    - Otherwise, the UID is generated by fuzzing a default base pattern (Flipper Zero MIFARE Fuzzer style)
      by randomly modifying a variable number of hex digits.
    
    The expected UID length in hex digits is: uid_length * 2.
    """
    uid_length = CARD_TYPES[card_type]['uid_length']
    expected_length = uid_length * 2

    if custom_patterns:
        # Randomly select one custom pattern from the provided list.
        pattern = random.choice(custom_patterns).strip()
        if len(pattern) != expected_length:
            raise ValueError(f"Custom pattern '{pattern}' must be exactly {expected_length} hex digits for card type '{card_type}'.")
        if '?' in pattern:
            # Replace '?' with random hex digits.
            uid = ''.join(random.choice("0123456789ABCDEF") if ch == '?' else ch.upper() for ch in pattern)
            return uid
        else:
            # Fuzz the pattern if no wildcards are provided.
            changes = random.randint(1, max(1, len(pattern) // 2))
            return fuzz_uid(pattern, changes=changes)
    else:
        # Use default fuzzing based on a base pattern.
        base = BASE_PATTERNS.get(card_type)
        if base and len(base) == expected_length:
            changes = random.randint(1, max(1, len(base) // 2))
            return fuzz_uid(base, changes=changes)
        else:
            # Fallback to fully random UID generation.
            uid_bytes = [random.randint(0, 255) for _ in range(uid_length)]
            return bytes(uid_bytes).hex().upper()

# ========================================================================
# FILE GENERATION FUNCTION
# ========================================================================

def generate_nfc_file(card_type, count, filename, custom_patterns=None):
    """
    Generate a file with randomly generated NFC UIDs.
    If custom_patterns is provided, UIDs will follow the pattern(s) defined (with fuzzing applied if necessary).
    Otherwise, UIDs are generated by fuzzing a default base pattern.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for _ in range(count):
            uid_hex = generate_nfc_uid(card_type, custom_patterns)
            f.write(f"{uid_hex}\n")
    return filename

# ========================================================================
# MAIN PROGRAM
# ========================================================================

def main():
    print("=== Flipper Zero MIFARE Fuzzer UID Generator ===\n")
    
    # Card type selection
    print("Select card format:")
    cards = list(CARD_TYPES.keys())
    for i, card in enumerate(cards, 1):
        print(f"{i}. {card.replace('_', ' ').title()} ({CARD_TYPES[card]['uid_length']} bytes)")
    
    try:
        card_choice = int(input("\nChoice (1-3): "))
        selected_card = cards[card_choice - 1]
    except (ValueError, IndexError):
        print("\nERROR: Invalid card type choice.")
        sys.exit(1)

    # Determine expected hex length (2 characters per byte)
    uid_hex_length = CARD_TYPES[selected_card]['uid_length'] * 2
    
    # Ask for custom UID pattern(s)
    pattern_input = input(
        f"\nEnter custom UID pattern(s) using '?' for random digits "
        f"(must be {uid_hex_length} hex characters). For multiple patterns, separate them with commas.\n"
        "Leave blank to use default fuzzing generation: "
    ).strip()
    
    custom_patterns = None
    if pattern_input:
        # Split on commas and remove extra whitespace.
        custom_patterns = [p.strip() for p in pattern_input.split(',')]
        # Validate each pattern.
        for pattern in custom_patterns:
            if len(pattern) != uid_hex_length:
                print(f"\nERROR: Pattern '{pattern}' must be exactly {uid_hex_length} hex characters for card type '{selected_card}'.")
                sys.exit(1)
            for ch in pattern:
                if ch != '?' and ch.upper() not in "0123456789ABCDEF":
                    print(f"\nERROR: Invalid character '{ch}' in pattern '{pattern}'. Use hex digits or '?' for wildcards.")
                    sys.exit(1)

    # Quantity selection
    try:
        count = int(input("\nNumber of UIDs to generate (1-1000): "))
        if not 1 <= count <= 1000:
            raise ValueError
        filename = input("\nOutput filename: ").strip() or "nfc_uids.txt"
    except ValueError:
        print("\nERROR: Invalid input values for quantity or filename.")
        sys.exit(1)

    # Generation process
    print(f"\nGenerating {count} NFC UIDs...")
    try:
        generate_nfc_file(selected_card, count, filename, custom_patterns)
    except ValueError as ve:
        print(f"\nERROR: {ve}")
        sys.exit(1)
    print(f"\nSuccess! Output saved to {filename}")

    # Sample output
    sample_uid = generate_nfc_uid(selected_card, custom_patterns)
    print("\nSample Generated UID:")
    print(f"- UID: {sample_uid}")
    
    # Stop the script after output is generated.
    sys.exit(0)

if __name__ == "__main__":
    main()
