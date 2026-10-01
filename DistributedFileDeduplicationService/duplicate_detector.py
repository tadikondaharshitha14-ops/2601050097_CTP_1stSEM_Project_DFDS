from file_scanner import FileScanner
from file_hasher import FileHasher


class DuplicateDetector:

    def find_duplicates(self, folder):

        scanner = FileScanner()
        hasher = FileHasher()

        files = scanner.scan(folder)

        hash_map = {}
        duplicates = []

        for file in files:

            file_hash = hasher.get_hash(file)

            if file_hash in hash_map:
                duplicates.append(file)
            else:
                hash_map[file_hash] = file

        return duplicates


detector = DuplicateDetector()

duplicates = detector.find_duplicates("storage")

print("Duplicate files:")

if duplicates:
    for file in duplicates:
        print(file)
else:
    print("No duplicate files found.")