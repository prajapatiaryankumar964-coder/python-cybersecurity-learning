import os
import hashlib


def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


folder_path = input("Enter folder path: ")
baseline_file = "baseline.txt"

current_files = {}


# Scan current files
for filename in os.listdir(folder_path):

    filepath = os.path.join(folder_path, filename)

    if os.path.isfile(filepath):
        current_files[filename] = calculate_hash(filepath)


# First run: Create baseline
if not os.path.exists(baseline_file):

    with open(baseline_file, "w") as file:

        for filename, file_hash in current_files.items():
            file.write(f"{filename}|{file_hash}\n")

    print("\n✅ Baseline created successfully!")

else:

    # Read old baseline
    old_files = {}

    with open(baseline_file, "r") as file:

        for line in file:
            filename, file_hash = line.strip().split("|")
            old_files[filename] = file_hash


    print("\n===== FILE INTEGRITY REPORT =====\n")


    # Check New / Modified / Unchanged
    for filename, current_hash in current_files.items():

        if filename not in old_files:
            print("🆕 NEW FILE:", filename)

        elif current_hash != old_files[filename]:
            print("⚠️ MODIFIED FILE:", filename)

        else:
            print("✅ UNCHANGED:", filename)


    # Check Deleted files
    for filename in old_files:

        if filename not in current_files:
            print("❌ DELETED FILE:", filename)