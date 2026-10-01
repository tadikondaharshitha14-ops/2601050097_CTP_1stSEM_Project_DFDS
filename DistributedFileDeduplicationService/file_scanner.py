import os


class FileScanner:

    def scan(self, folder):
        files = []

        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                files.append(os.path.join(root, filename))

        return files


scanner = FileScanner()

files = scanner.scan("storage")

print("Files found:")

for file in files:
    print(file)