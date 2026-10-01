from distributed_scanner import DistributedScanner


def divide_files(files):

    middle = len(files) // 2

    group1 = files[:middle]
    group2 = files[middle:]

    return group1, group2


scanner = DistributedScanner()

files = scanner.scan_nodes("nodes")

group1, group2 = divide_files(files)

print("Group 1:")

for file in group1:
    print(file)

print("\nGroup 2:")

for file in group2:
    print(file)