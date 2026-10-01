import os

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


print("\nDuplicate Files")
print("----------------")

for file in duplicates:
    print(file)


choice = input("\nDelete duplicate files? (yes/no): ")


if choice.lower() == "yes":

    for file in duplicates:

        os.remove(file)
        print("Deleted:", file)

    print("\nDuplicates removed successfully.")

else:

    print("\nNo files were deleted.")