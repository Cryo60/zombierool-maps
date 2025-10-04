#!/usr/bin/env python3
"""
ZombieRool Maps Checksum Generator
Génère les checksums SHA-256 pour vos maps
Usage: python generate_checksums.py maps/
"""

import os
import sys
import hashlib
import json
from pathlib import Path

def calculate_sha256(filepath):
    """Calcule le SHA-256 d'un fichier"""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        # Lire par chunks pour gérer les gros fichiers
        for byte_block in iter(lambda: f.read(8192), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def main():
    print("=== ZombieRool Maps Checksum Generator ===")
    print()
    
    if len(sys.argv) < 2:
        print("Usage: python generate_checksums.py <maps_directory>")
        print("Example: python generate_checksums.py maps/")
        sys.exit(1)
    
    maps_dir = Path(sys.argv[1])
    
    if not maps_dir.exists() or not maps_dir.is_dir():
        print(f"Error: Directory '{maps_dir}' not found")
        sys.exit(1)
    
    print(f"Scanning directory: {maps_dir}")
    print()
    
    checksums = []
    
    # Scanner tous les fichiers .zip
    for file_path in sorted(maps_dir.glob("*.zip")):
        filename = file_path.name
        print(f"Processing: {filename}")
        
        try:
            checksum = calculate_sha256(file_path)
            checksums.append({
                "file": filename,
                "sha256": checksum
            })
            print(f"  ✓ SHA-256: {checksum}")
        except Exception as e:
            print(f"  ✗ Error: {e}")
        
        print()
    
    # Sauvegarder en JSON
    output = {
        "checksums": checksums
    }
    
    output_file = "checksums.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print("=" * 50)
    print(f"Checksums saved to: {output_file}")
    print("=" * 50)
    print()
    print("To use these checksums, copy them into your maps.json file.")
    print('Example:')
    print('  "sha256": "a1b2c3d4..."')
    print()
    
    # Afficher un exemple de maps.json
    if checksums:
        print("Example maps.json entry:")
        print(json.dumps({
            "id": "my_map",
            "name": checksums[0]["file"].replace(".zip", ""),
            "description": "Description here",
            "download_url": f"https://github.com/YOUR_USERNAME/zombierool-maps/raw/main/maps/{checksums[0]['file']}",
            "sha256": checksums[0]["sha256"]
        }, indent=2))

if __name__ == "__main__":
    main()