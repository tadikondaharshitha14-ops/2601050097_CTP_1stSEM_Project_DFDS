import os


class DistributedScanner:

    def scan_nodes(self, nodes_folder):

        files = []

        for node in os.listdir(nodes_folder):

            node_path = os.path.join(nodes_folder, node)

            if os.path.isdir(node_path):

                for root, folders, filenames in os.walk(node_path):

                    for filename in filenames:

                        file_path = os.path.join(root, filename)
                        files.append(file_path)

        return files


scanner = DistributedScanner()

files = scanner.scan_nodes("nodes")

print("Files in distributed nodes:")

for file in files:
    print(file)