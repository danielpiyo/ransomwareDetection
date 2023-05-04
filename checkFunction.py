import os
import hashlib
import psutil

# List of file extensions that are commonly associated with ransomware
# Feel free to modify this list based on your needs
RANSOMWARE_EXTENSIONS = [
    '.crypt', '.enc', '.encrypted', '.locked',
    '.kraken', '.zzzzz', '.zepto', '.locky',
    '.odin', '.osiris', '.keypass', '.vesrato',
    '.mbed', '.crypted000007', '.cerber',
    '.arena', '.ragnar', '.lockbit', '.clop',
    '.brrr', '.aleta', '.vvoa', '.uudjvu',
    '.qbtex', '.onion',
]


def get_running_processes():
    """
    Returns a list of all running processes on the system !important.
    """
    return psutil.process_iter()


def get_files_in_directory(directory):
    """
    Returns a list of all files in the specified directory.
    """
    return os.listdir(directory)


def get_file_hash(filename):
    """
    Computes the SHA256 hash of the specified file.
    """
    with open(filename, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def is_ransomware(filename):
    """
    Returns True if the specified file has an extension commonly associated with ransomware.
    """
    return os.path.splitext(filename)[-1] in RANSOMWARE_EXTENSIONS


def has_changed(filename):
    """
    Returns True if the specified file has been modified since the last time it was checked.
    """
    file_hash = get_file_hash(filename)
    if filename in last_checked_files and last_checked_files[filename] == file_hash:
        return False
    last_checked_files[filename] = file_hash
    return True


last_checked_files = {}
