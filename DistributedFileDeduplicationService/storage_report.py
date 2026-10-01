import os

from distributed_scanner import DistributedScanner
from file_hasher import FileHasher


scanner = DistributedScanner()
hasher = FileHasher()

files = scanner.scan_nodes("nodes")

hash_map = {}
duplicates = []

total_size = 0
saved_size = 0

for file in files:

    file_size = os.path.getsize(file)
    total_size += file_size

    file_hash = hasher.get_hash(file)

    if file_hash in hash_map:

        duplicates.append(file)
        saved_size += file_size

    else:

        hash_map[file_hash] = file


unique_size = total_size - saved_size


print("\nStorage Report")
print("--------------")

print("Total Files:", len(files))
print("Unique Files:", len(hash_map))
print("Duplicate Files:", len(duplicates))

print("Storage Before:", total_size, "bytes")
print("Storage After:", unique_size, "bytes")
print("Space Saved:", saved_size, "bytes")