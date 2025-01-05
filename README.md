# ISOHashVerifier

A Python-based tool for verifying the integrity of ISO files by calculating hash values (SHA-256, SHA-512, MD5) and checking the structure of the ISO file.

## Features

- **Hash Calculation**: Calculate the hash (SHA-256, SHA-512, MD5) of an ISO file to verify its integrity.
- **ISO Structure Validation**: Check if the ISO file has a valid structure and is readable.
- **Progress Bar**: Visual feedback during the hash calculation process with a progress bar.
- **Compatibility**: Works with any ISO file.

## Requirements

- Python 3.x
- `pycdlib` for ISO file structure validation
- `tqdm` for progress bar during hash calculation

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mehranlip/ISOHashVerifier.git
    cd ISOHashVerifier

    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```bash
    python ISOHashVerifier.py
    ```

2. Enter the path of your ISO file when prompted.

3. The program will:
   - Display the hash values for the ISO file (SHA-256, SHA-512, MD5).
   - Check the integrity of the ISO file structure.
   - Show a progress bar while calculating the hash.

## Example

```bash
**************************************************************************************

 _____  _____  _____  _   _              _      _   _              _   __  _                                     
|_   _|/  ___||  _  || | | |            | |    | | | |            (_) / _|(_)                                    
  | |  \ `--. | | | || |_| |  __ _  ___ | |__  | | | |  ___  _ __  _ | |_  _   ___  _ __                         
  | |   `--. \| | | ||  _  | / _` |/ __|| '_ \ | | | | / _ \| '__|| ||  _|| | / _ \| '__|                        
 _| |_ /\__/ /\ \_/ /| | | || (_| |\__ \| | | |\ \_/ /|  __/| |   | || |  | ||  __/| |                            
 \___/ \____/  \___/ \_| |_/ \__,_||___/|_| |_| \___/  \___||_|   |_||_|  |_| \___||_|                           

Welcome to the ISO Hash Verifier!
Enter the path to your ISO file below:

ISO file path: example.iso

Checking file: example.iso
==================================================

Hashes:
  - SHA256: <Calculated SHA256 Hash>
  - SHA512: <Calculated SHA512 Hash>
  - MD5: <Calculated MD5 Hash>

ISO file structure validation: ✅ Valid

Checked on:  2025-01-01 12:34:56
