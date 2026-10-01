from multiprocessing import Process
from file_hasher import FileHasher


def process_files(files):

    hasher = FileHasher()

    for file in files:

        file_hash = hasher.get_hash(file)

        print(file)
        print("Hash:", file_hash)


if __name__ == "__main__":

    group1 = [
        "nodes/node1/file1.txt",
        "nodes/node2/file2.txt"
    ]

    group2 = [
        "nodes/node2/file3.txt",
        "nodes/node3/file4.txt"
    ]

    p1 = Process(target=process_files, args=(group1,))
    p2 = Process(target=process_files, args=(group2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Multiprocessing hashing completed.")