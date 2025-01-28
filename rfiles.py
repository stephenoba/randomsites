#!/usr/bin/env python3

import sys
import random
import string
import os

def generate_random_name(length=8):
    """
    Generates a random string of given length using lowercase letters and digits.
    """
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choices(chars, k=length))

def print_usage():
    print("Usage:")
    print("  1) Generate directories:")
    print("     python generate_random_files.py directory <number_of_dirs> [names_comma_separated]")
    print("     Example: python generate_random_files.py directory 3 dirA,dirB,dirC")
    print("")
    print("  2) Generate files:")
    print("     python generate_random_files.py file <number_of_files> <extensions_comma_separated> [names_comma_separated]")
    print("     Example without names: python generate_random_files.py file 5 txt,png,jpg")
    print("     Example with names:    python generate_random_files.py file 3 txt,png file1,file2,file3")
    print("")
    sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print_usage()

    mode = sys.argv[1].lower()  # "directory" or "file"
    num_items = int(sys.argv[2])

    # Validate mode
    if mode not in ["directory", "dir", "file", "files"]:
        print("Error: Invalid mode. Must be 'directory' or 'file'.\n")
        print_usage()

    if mode in ["directory", "dir"]:
        # -------------------------------------------
        #         GENERATE RANDOM DIRECTORIES
        # -------------------------------------------
        # Optional list of names (must match num_items if provided)
        if len(sys.argv) > 3:
            dir_names = sys.argv[3].split(",")
            if len(dir_names) != num_items:
                print("Error: The number of directory names must match <number_of_dirs>.")
                sys.exit(1)
        else:
            dir_names = None

        for i in range(num_items):
            if dir_names:
                directory_name = dir_names[i]
            else:
                directory_name = generate_random_name()

            # Create the directory (if it doesn't exist)
            os.makedirs(directory_name, exist_ok=True)
            print(f"Created directory: {directory_name}")

    else:
        # -------------------------------------------
        #            GENERATE RANDOM FILES
        # -------------------------------------------
        if len(sys.argv) < 4:
            print("Error: For 'file' mode, you need <extensions_comma_separated> as a third argument.\n")
            print_usage()

        extensions = sys.argv[3].split(",")

        # Optional list of file names (must match num_items if provided)
        if len(sys.argv) > 4:
            file_names = sys.argv[4].split(",")
            if len(file_names) != num_items:
                print("Error: The number of provided names must match <number_of_files>.")
                sys.exit(1)
        else:
            file_names = None

        for i in range(num_items):
            # Pick a random extension from the list
            extension = random.choice(extensions)

            # Determine the base filename
            if file_names:
                base_filename = file_names[i]
            else:
                base_filename = generate_random_name()

            filename = f"{base_filename}.{extension}"

            # Generate random file content (optional behavior).
            # Here, we write a random number of bytes between 1KB and 10KB.
            file_size = random.randint(1024, 10 * 1024)  # 1 KB to 10 KB
            random_data = bytes(random.getrandbits(8) for _ in range(file_size))

            # Create and write to the file
            with open(filename, "wb") as f:
                f.write(random_data)

            print(f"Created file: {filename}")

if __name__ == "__main__":
    main()
