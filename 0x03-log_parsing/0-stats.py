#!/usr/bin/python3
import sys

# Initialize cumulative metrics
total_file_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_stats():
    """Print the statistics in the required format."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

try:
    for line in sys.stdin:
        line = line.strip()
        line_parts = line.split()

        # Parse the line and check format
        if len(line_parts) < 9:
            continue

        # Extract the status code and file size
        status_code = line_parts[-2]
        try:
            file_size = int(line_parts[-1])
        except ValueError:
            continue

        # Update total file size and status code counts if valid
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass
finally:
    # Print the final statistics after keyboard interruption
    print_stats()

