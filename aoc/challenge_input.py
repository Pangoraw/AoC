"""
Handles the file inputs foreach challenge
"""

import os
import os.path
import getpass

import requests

YEAR = 2020
CACHE_FOLDER = "inputs"
SESSION_KEY_FILENAME = "session_key.txt"


def get_input_for_day(day):
    """
    Downloads the input for the current day
    Skips if the input already exists
    Parameters
    ==========
        day: Int - the current day of the month
    """

    file_path = os.path.join(CACHE_FOLDER, f"{day}.txt")
    session_key_file = os.path.join(CACHE_FOLDER, SESSION_KEY_FILENAME)

    if not os.path.isdir(CACHE_FOLDER):
        print(f">> Creating cache folder at ({CACHE_FOLDER})")
        os.mkdir(CACHE_FOLDER)

    if not os.path.isfile(session_key_file):
        print(">> No session key file found")
        session_key = getpass.getpass(prompt="SESSION_KEY = ")
        with open(session_key_file, "w") as f_handle:
            f_handle.write(session_key)
        print(f">> Created session key file ({session_key_file})")

    if not os.path.isfile(file_path):
        file_url = build_url(day)
        print(f">> Downloading input file at ({file_url})")
        with open(session_key_file, "r") as f_handle:
            session_key = f_handle.read()
        input_value = download_file(file_url, session_key)
        with open(file_path, "w") as f_handle:
            f_handle.write(input_value)
        print(f">> Created input file ({file_path})")
    else:
        input_value = read_file(file_path)

    return input_value


def build_url(day):
    """Returns the input url for the current day"""
    return f"https://adventofcode.com/{YEAR}/day/{day}/input"


def download_file(url, session_key):
    """Downloads a file a the specified url and saves it"""
    res = requests.get(url, headers={"Cookie": f"session={session_key}"})
    res.raise_for_status()

    return res.text


def read_file(file_path):
    """Reads a string from a file"""
    with open(file_path, "r") as f_handle:
        return f_handle.read()
