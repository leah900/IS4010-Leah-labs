from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64
import os
import json

SALT_SIZE = 16


def _derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def init_store(path: str, password: str):
    salt = os.urandom(SALT_SIZE)
    key = _derive_key(password, salt)
    f = Fernet(key)
    data = {"entries": []}
    token = f.encrypt(json.dumps(data).encode())
    with open(path, "wb") as f_out:
        f_out.write(salt + token)


def load_store(path: str, password: str) -> dict:
    with open(path, "rb") as f_in:
        raw = f_in.read()
    salt = raw[:SALT_SIZE]
    token = raw[SALT_SIZE:]
    key = _derive_key(password, salt)
    f = Fernet(key)
    dec = f.decrypt(token)
    return json.loads(dec.decode())


def save_store(path: str, password: str, data: dict):
    with open(path, "rb") as f_in:
        raw = f_in.read()
    salt = raw[:SALT_SIZE]
    key = _derive_key(password, salt)
    f = Fernet(key)
    token = f.encrypt(json.dumps(data).encode())
    with open(path, "wb") as f_out:
        f_out.write(salt + token)


def add_entry(path: str, password: str, name: str, username: str, pwd: str):
    store = load_store(path, password)
    store["entries"].append({"name": name, "username": username, "password": pwd})
    save_store(path, password, store)


def list_entries(path: str, password: str):
    store = load_store(path, password)
    return [e["name"] for e in store["entries"]]


def get_entry(path: str, password: str, name: str):
    store = load_store(path, password)
    for e in store["entries"]:
        if e["name"] == name:
            return e
    return None


def generate_password(length: int = 16, use_symbols: bool = True) -> str:
    """Generate a secure random password."""
    import secrets
    import string

    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def update_entry(path: str, password: str, name: str, username: str = None, pwd: str = None) -> bool:
    """Update an existing entry. Returns True if updated, False if not found."""
    store = load_store(path, password)
    for e in store["entries"]:
        if e["name"] == name:
            if username is not None:
                e["username"] = username
            if pwd is not None:
                e["password"] = pwd
            save_store(path, password, store)
            return True
    return False


def delete_entry(path: str, password: str, name: str) -> bool:
    """Delete an entry by name. Returns True if deleted."""
    store = load_store(path, password)
    orig_len = len(store["entries"])
    store["entries"] = [e for e in store["entries"] if e["name"] != name]
    if len(store["entries"]) < orig_len:
        save_store(path, password, store)
        return True
    return False


def search_entries(path: str, password: str, query: str):
    """Return entries where name or username contains the query (case-insensitive)."""
    store = load_store(path, password)
    q = query.lower()
    return [e for e in store["entries"] if q in e["name"].lower() or q in e["username"].lower()]
