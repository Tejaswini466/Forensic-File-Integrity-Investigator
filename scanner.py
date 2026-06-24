import os
import hashlib

def calculate_hash(file_path, algo='sha256'):
    hash_func = hashlib.sha256() if algo == 'sha256' else hashlib.md5()

    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except:
        return None


def scan_directory(directory):
    data = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)

            try:
                stats = os.stat(path)

                file_data = {
                    "path": path,
                    "name": file,
                    "size": stats.st_size,
                    "mtime": stats.st_mtime,
                    "extension": os.path.splitext(file)[1],
                    "hash": calculate_hash(path)
                }

                data.append(file_data)

            except Exception as e:
                print(f"Skipped: {path}")

    return data