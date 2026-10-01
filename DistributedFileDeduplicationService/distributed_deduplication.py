from distributed_scanner import DistributedScanner
from file_hasher import FileHasher


class DistributedDeduplication:

    def find_duplicates(self, nodes_folder):

        scanner = DistributedScanner()
        hasher = FileHasher()

        files = scanner.scan_nodes(nodes_folder)

        hash_map = {}
        duplicates = []

        for file in files:

            file_hash = hasher.get_hash(file)

            if file_hash in hash_map:
                duplicates.append(file)
            else:
                hash_map[file_hash] = file

        return duplicates


service = DistributedDeduplication()

duplicates = service.find_duplicates("nodes")

print("\nDistributed Duplicate Report")
print("----------------------------")

if duplicates:

    print("Duplicate files:")

    for file in duplicates:
        print(file)

else:

    print("No duplicate files found.")