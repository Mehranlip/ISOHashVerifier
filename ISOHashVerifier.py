import hashlib
import os
import datetime
from tqdm import tqdm
import pycdlib

def calculate_hash(file_path, hash_type):

    hash_function = {
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512,
        "md5": hashlib.md5
    }
    hash_obj = hash_function[hash_type]()
    file_size = os.path.getsize(file_path)
    try:
        with open(file_path, "rb") as f:
            with tqdm(total=file_size, desc=f"Calculating {hash_type.upper()}", unit="B", unit_scale=True) as pbar:
                while chunk := f.read(8192):
                    hash_obj.update(chunk)
                    pbar.update(len(chunk))
        return hash_obj.hexdigest()
    except FileNotFoundError:
        return None


def check_iso_integrity(file_path):

    try:
        iso_info = pycdlib.PyCdlib()
        iso_info.open(file_path)
        iso_info.close()
        return True
    except Exception as e:
        return False

def print_file_info_and_integrity(file_path):

    print(f"\nChecking file: {file_path}")
    print("=" * 50)


    hash_results = []
    for hash_type in ["sha256", "sha512", "md5"]:
        file_hash = calculate_hash(file_path, hash_type)
        hash_results.append((hash_type.upper(), file_hash))
    
    print("\nHashes:")
    for h_type, h_value in hash_results:
        print(f"  - {h_type}: {h_value}")

    # Check and display ISO integrity
    if check_iso_integrity(file_path):
        print("\n✅ ISO file structure is valid.")
    else:
        print("❌ Invalid ISO file structure.")
    
    # Timestamp
    print("\nChecked on: ", datetime.datetime.now())

def main():
    print("""
**************************************************************************************          

 _____  _____  _____  _   _              _      _   _              _   __  _                                     
|_   _|/  ___||  _  || | | |            | |    | | | |            (_) / _|(_)                                    
  | |  \ `--. | | | || |_| |  __ _  ___ | |__  | | | |  ___  _ __  _ | |_  _   ___  _ __                         
  | |   `--. \| | | ||  _  | / _` |/ __|| '_ \ | | | | / _ \| '__|| ||  _|| | / _ \| '__|                        
 _| |_ /\__/ /\ \_/ /| | | || (_| |\__ \| | | |\ \_/ /|  __/| |   | || |  | ||  __/| |                           
 \___/ \____/  \___/ \_| |_/ \__,_||___/|_| |_| \___/  \___||_|   |_||_|  |_| \___||_|                           
                                                                                                                 
                                                                                                                 
______                     _                          _   _             ___  ___       _                         
|  _  \                   | |                        | | | |            |  \/  |      | |                        
| | | |  ___ __   __  ___ | |  ___   _ __    ___   __| | | |__   _   _  | .  . |  ___ | |__   _ __   __ _  _ __  
| | | | / _ \\ \ / / / _ \| | / _ \ | '_ \  / _ \ / _` | | '_ \ | | | | | |\/| | / _ \| '_ \ | '__| / _` || '_ \ 
| |/ / |  __/ \ V / |  __/| || (_) || |_) ||  __/| (_| | | |_) || |_| | | |  | ||  __/| | | || |   | (_| || | | |
|___/   \___|  \_/   \___||_| \___/ | .__/  \___| \__,_| |_.__/  \__, | \_|  |_/ \___||_| |_||_|    \__,_||_| |_|
                                    | |                           __/ |                                          
                                    |_|                          |___/                                           
                                                                                                                           
**************************************************************************************
 
    """)
    print("Welcome to the ISO Hash Verifier!")
    print("Enter the path to your ISO file below:")

    file_path = input("ISO file path: ").strip()


    print_file_info_and_integrity(file_path)

if __name__ == "__main__":
    main()
