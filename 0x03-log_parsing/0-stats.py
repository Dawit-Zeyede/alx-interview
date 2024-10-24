#!/usr/bin/python3
import sys


def print_msg(dict_sc, total_file_size):
    """
    Method to print statistics.
    Args:
        dict_sc: dict of status codes
        total_file_size: total file size
    Returns:
        None
    """
    print(f"File size: {total_file_size}")
    for key in sorted(dict_sc):
        if dict_sc[key] > 0:
            print(f"{key}: {dict_sc[key]}")


def update_dict_sc(code, dict_sc):
    """
    Update the status code dictionary.
    Args:
        code: The status code to update
        dict_sc: The dictionary of status codes
    """
    if code in dict_sc:
        dict_sc[code] += 1


total_file_size = 0
dict_sc = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
}
counter = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue

        try:
            file_size = int(parts[-1])
            status_code = parts[-2]
        except ValueError:
            continue

        total_file_size += file_size
        update_dict_sc(status_code, dict_sc)
        counter += 1

        if counter == 10:
            print_msg(dict_sc, total_file_size)
            counter = 0

finally:
    print_msg(dict_sc, total_file_size)
