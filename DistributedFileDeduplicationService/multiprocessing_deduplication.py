from multiprocessing import Process, Queue
from file_hasher import FileHasher


def process_files(files, queue):

    hasher = FileHasher()
    results = []

    for file in files:

        file_hash = hasher.get_hash(file)
        results.append((file, file_hash))

    queue.put(results)


if __name__ == "__main__":

    group1 = [
        "nodes/node1/file1.txt",
        "nodes/node2/file2.txt"
    ]

    group2 = [
        "nodes/node2/file3.txt",
        "nodes/node3/file4.txt"
    ]

    queue = Queue()

    p1 = Process(target=process_files, args=(group1, queue))
    p2 = Process(target=process_files, args=(group2, queue))

    p1.start()
    p2.start()

    results1 = queue.get()
    results2 = queue.get()

    p1.join()
    p2.join()

    all_results = results1 + results2

    hash_map = {}
    duplicates = []

    for file, file_hash in all_results:

        if file_hash in hash_map:
            duplicates.append(file)
        else:
            hash_map[file_hash] = file

    print("\nDuplicate Files")
    print("----------------")

    for file in duplicates:
        print(file)

    print("\nMultiprocessing Deduplication Completed.")