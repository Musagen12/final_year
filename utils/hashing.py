import hashlib

def get_hash(path: str, algorithm="sha256"):
    hasher = hashlib.new(algorithm)

    with open(path, 'rb') as file:
        # Read the file in chunks of 8192 bytes
        while chunk := file.read(8192):
            hasher.update(chunk)
        
    return hasher.hexdigest()

file_hash = get_hash(path="/teamspace/studios/this_studio/memory_dumps/output.lime", algorithm="sha256")
print(f"The file hash is {file_hash}")