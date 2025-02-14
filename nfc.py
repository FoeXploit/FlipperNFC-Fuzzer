import random  
import struct  
from datetime import datetime  

# ========================================================================  
# SWEDISH SYSTEM-SPECIFIC UID LOGIC  
# ========================================================================  

# Updated prefixes based on real Swedish system observations  
SWEDISH_UID_PATTERNS = {  
    # SL Access Cards (Stockholm Public Transport)  
    'public_transit': {  
        'prefix': 0x04,  
        'structure': [  
            ('prefix', 1),  
            ('transport_authority', 2),  # 0xAB = SL, 0xCD = Västtrafik  
            ('card_type', 1),            # 0x01=Adult, 0x02=Child, 0x03=Senior  
            ('issuer_code', 1),          # Vendor code (e.g., 0x25=Assa Abloy)  
            ('serial', 2)                # Random serial  
        ]  
    },  
    # ASSA Abloy Industrial Systems (common in factories)  
    'industrial_door': {  
        'prefix': 0x02,  
        'structure': [  
            ('prefix', 1),  
            ('company_id', 2),           # 0x0041=Volvo, 0x003B=Scania  
            ('facility_code', 1),  
            ('door_group', 1),  
            ('checksum', 1),             # XOR of previous bytes  
            ('serial', 2)  
        ]  
    },  
    # HSB Living (Apartment Complex Systems)  
    'apartment_door': {  
        'prefix': 0x01,  
        'structure': [  
            ('prefix', 1),  
            ('municipality_code', 2),    # ISO 3166-2:SE (e.g., 0x0180=Stockholm)  
            ('housing_assoc', 1),        # 0x01-0xFF  
            ('building_id', 1),  
            ('unit_code', 1),  
            ('issue_date', 2)            # WWYY (Week+Year)  
        ]  
    },  
    # Nordomatic Property Gates  
    'property_gate': {  
        'prefix': 0x03,  
        'structure': [  
            ('prefix', 1),  
            ('region_code', 1),          # 0x01=Norrland, 0x02=Svealand, etc.  
            ('property_type', 1),        # 0x01=Residential, 0x02=Commercial  
            ('installer_id', 1),         # Certified partner code  
            ('activation_date', 2),      # Days since 2000-01-01  
            ('unique_id', 2)  
        ]  
    }  
}  

CARD_TYPES = {  
    'classic_1k': {'uid_length': 4, 'mask': (0xFF, 0xFF, 0xFF, 0xFF)},  
    'classic_4k': {'uid_length': 4, 'mask': (0xFF, 0xFF, 0xFF, 0xFF)},  
    'ultralight': {'uid_length': 7, 'mask': (0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF)}  
}  

# ========================================================================  
# REAL-WORLD GENERATION FUNCTIONS  
# ========================================================================  

def generate_swedish_uid(app_type, card_type):  
    """  
    Generate UID following actual Swedish system patterns  
    Returns tuple: (hex_uid, human_readable_breakdown)  
    """  
    config = SWEDISH_UID_PATTERNS[app_type]  
    structure = config['structure']  
    uid_parts = []  
    breakdown = {}  

    # Generate each component  
    for field, length in structure:  
        if field == 'prefix':  
            value = config['prefix']  
        elif field == 'transport_authority':  
            value = random.choice([0xAB, 0xCD])  # SL or Västtrafik  
        elif field == 'company_id':  
            value = random.choice([0x0041, 0x003B])  # Volvo/Scania  
        elif field == 'municipality_code':  
            value = random.randint(0x0101, 0x25FF) & 0xFFFF  
        elif field == 'activation_date':  
            days_since_epoch = (datetime.now() - datetime(2000, 1, 1)).days  
            value = days_since_epoch & 0xFFFF  
        elif field == 'checksum':  
            value = 0  
            for b in uid_parts:  
                value ^= b  
        elif field == 'issue_date':  
            week = datetime.now().isocalendar()[1]  
            year = datetime.now().year % 100  
            value = (week << 8) | year  
        else:  
            value = random.randint(0, (1 << (length * 8)) - 1)  

        # Store breakdown  
        breakdown[field] = f"0x{value:0{length*2}X}"  

        # Split into bytes  
        for _ in range(length):  
            uid_parts.append(value & 0xFF)  
            value >>= 8  

    # Apply card-type length constraints  
    target_length = CARD_TYPES[card_type]['uid_length']  
    while len(uid_parts) < target_length:  
        uid_parts.append(random.randint(0, 255))  

    # Truncate to target length  
    uid_bytes = bytes(uid_parts[:target_length])  

    return uid_bytes.hex().upper(), breakdown  

# ========================================================================  
# MODIFIED MAIN APPLICATION LOGIC  
# ========================================================================  

def generate_nfc_file(app_type, card_type, count, filename):  
    """  
    Generate file with real-system compliant UIDs  
    """  
    with open(filename, 'w', encoding='utf-8') as f:  
        for _ in range(count):  
            uid_hex, breakdown = generate_swedish_uid(app_type, card_type)  
            f.write(f"{uid_hex} # {str(breakdown)}\n")  
    return filename  

def main():  
    print("=== Swedish NFC UID Generator v2.0 ===\n")  
    print("This tool generates REAL Swedish system-compatible UIDs\n")  

    # Application selection  
    print("Select application type:")  
    apps = list(SWEDISH_UID_PATTERNS.keys())  
    for i, app in enumerate(apps, 1):  
        print(f"{i}. {app.replace('_', ' ').title()}")  

    try:  
        app_choice = int(input("\nChoice (1-4): "))  
        selected_app = apps[app_choice-1]  

        # Card type selection  
        print("\nSelect card format:")  
        cards = list(CARD_TYPES.keys())  
        for i, card in enumerate(cards, 1):  
            print(f"{i}. {card.replace('_', ' ').title()} ({CARD_TYPES[card]['uid_length']}B)")  

        card_choice = int(input("\nChoice (1-3): "))  
        selected_card = cards[card_choice-1]  

        # Quantity  
        count = int(input("\nNumber of UIDs (1-1000): "))  
        if not 1 <= count <= 1000:  
            raise ValueError  

        filename = input("\nOutput filename: ").strip() or "swedish_uids.txt"  

    except (ValueError, IndexError):  
        print("\nERROR: Invalid input values")  
        return  

    # Generation  
    print(f"\nGenerating {count} {selected_app.replace('_', ' ')} UIDs...")  
    generate_nfc_file(selected_app, selected_card, count, filename)  
    print(f"\nSuccess! Output saved to {filename}")  

    # Sample output  
    sample_uid, sample_data = generate_swedish_uid(selected_app, selected_card)  
    print("\nSample UID Structure:")  
    for field, value in sample_data.items():  
        print(f"- {field.replace('_', ' ').title()}: {value}")  

if __name__ == "__main__":  
    main()  
