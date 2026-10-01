from distributed_scanner import DistributedScanner
from file_hasher import FileHasher


scanner = DistributedScanner()
hasher = FileHasher()

files = scanner.scan_nodes("nodes")

hash_map = {}
duplicates = []

for file in files:

    file_hash = hasher.get_hash(file)

    if file_hash in hash_map:
        duplicates.append(file)
    else:
        hash_map[file_hash] = file


total_files = len(files)
unique_files = len(hash_map)
duplicate_count = len(duplicates)


print("\nDeduplication Report")
print("--------------------")

print("Total Files:", total_files)
print("Unique Files:", unique_files)
print("Duplicate Files:", duplicate_count)

print("\nDuplicate File List:")

for file in duplicates:
    print(file)