import os
import time

filename = input("Enter file path: ")

if os.path.exists(filename):

    file_size = os.path.getsize(filename)

    created_time = os.path.getctime(filename)
    modified_time = os.path.getmtime(filename)

    file_name = os.path.basename(filename)
    file_extension = os.path.splitext(filename)[1]

    print("\n===== FILE METADATA REPORT =====")

    print("File Name:", file_name)
    print("Extension:", file_extension)
    print("File Size:", file_size, "bytes")

    print(
        "Created Time:",
        time.ctime(created_time)
    )

    print(
        "Last Modified:",
        time.ctime(modified_time)
    )

else:
    print("❌ File not found!")