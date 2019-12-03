import hashlib
import numpy as np

from tqdm import tqdm

BUF_SIZE = 2 ** 28  # 256 megs


def md5(file_path):
    """
    Computes md5 hash in a memory reasoned way
    md5hash = hashfile.md5(file_path)
    """
    return _hash_file(file_path, hashlib.md5())


def sha1(file_path):
    """
    Computes sha1 hash in a memory reasoned way
    md5hash = hashfile.sha1(file_path)
    """
    return _hash_file(file_path, hashlib.sha1())


def _hash_file(file_path, hash_obj):
    b = bytearray(BUF_SIZE)
    mv = memoryview(b)
    pbar = tqdm(total=np.ceil(file_path.stat().st_size / BUF_SIZE))
    with open(file_path, 'rb', buffering=0) as f:
        for n in iter(lambda: f.readinto(mv), 0):
            hash_obj.update(mv[:n])
            pbar.update(1)
    pbar.close()
    return hash_obj.hexdigest()
