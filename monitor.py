import os
import hashlib
import json

MONITOR_DIR = "files_to_monitor"
HASH_DB = "file_hashes.json"

def get_file_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

def scan_directory():
    hashes = {}
    for root, _, files in os.walk(MONITOR_DIR):
        for file in files:
            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, MONITOR_DIR)
            hashes[rel_path] = get_file_hash(path)
    return hashes

def load_previous_hashes():
    if os.path.exists(HASH_DB):
        with open(HASH_DB, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_DB, "w") as f:
        json.dump(hashes, f, indent=4)

def compare_hashes(old, new):
    added = [f for f in new if f not in old]
    removed = [f for f in old if f not in new]
    modified = [f for f in old if f in new and old[f] != new[f]]
    return added, removed, modified

def main():
    print("🔍 Scanning files...")
    current = scan_directory()
    previous = load_previous_hashes()

    added, removed, modified = compare_hashes(previous, current)

    if not (added or removed or modified):
        print("✅ No changes detected.")
    else:
        print("⚠️ Changes found!")
        if added:
            print("🟢 Added:", *added)
        if removed:
            print("🔴 Removed:", *removed)
        if modified:
            print("🟡 Modified:", *modified)

    save_hashes(current)

if __name__ == "__main__":
    main()
