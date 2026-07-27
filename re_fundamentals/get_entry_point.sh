#!/bin/bash

# Check if an argument was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <elf_file>" >&2
    exit 1
fi

file_name="$1"

# Check if the file exists
if [ ! -f "$file_name" ]; then
    echo "Error: File '$file_name' does not exist." >&2
    exit 1
fi

# Check if messages.sh exists and source it
if [ -f "./messages.sh" ]; then
    # shellcheck source=/dev/null
    source ./messages.sh
else
    echo "Error: messages.sh not found in the current directory." >&2
    exit 1
fi

# Verify if the file is an ELF binary using the readelf header check
if ! readelf -h "$file_name" > /dev/null 2>&1; then
    echo "Error: '$file_name' is not a valid ELF file." >&2
    exit 1
fi

# Extract ELF header details using readelf
header_info=$(readelf -h "$file_name")

# 1. Extract Magic Number (e.g., 7f 45 4c 46 ...)
magic_number=$(echo "$header_info" | grep -i "Magic:" | sed -E 's/^[[:space:]]*Magic:[[:space:]]*//')

# 2. Extract Class (e.g., ELF32 or ELF64)
class=$(echo "$header_info" | grep -i "Class:" | awk -F: '{print $2}' | xargs)

# 3. Extract Byte Order / Data (e.g., 2's complement, little endian)
byte_order=$(echo "$header_info" | grep -i "Data:" | awk -F: '{print $2}' | xargs)

# 4. Extract Entry Point Address (e.g., 0x1050)
entry_point_address=$(echo "$header_info" | grep -i "Entry point address:" | awk -F: '{print $2}' | xargs)

# Call the function defined in messages.sh
display_elf_header_info
