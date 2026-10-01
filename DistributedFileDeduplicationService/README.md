**Distributed File Deduplication Service**
 
**1. Project Title**

Distributed File Deduplication Service

**2. Problem Statement**

Detect and eliminate duplicate files across a large distributed file store.

**3. Objective**

The main objective of this project is to find duplicate files stored across different distributed nodes and reduce unnecessary storage usage.

**4. Technologies Used**

Python

SHA-256 Hashing

Object-Oriented Programming (OOP)

Divide-and-Conquer

Multiprocessing

**5. How the Project Works**

**The project follows these steps:**

Distributed Nodes

       ↓
       
Scan Files

       ↓
       
Calculate SHA-256 Hash
       ↓
Divide Files into Groups
       ↓
Multiprocessing
       ↓
Compare Hashes
       ↓
Find Duplicate Files
       ↓
Generate Report
6. Project Structure
DistributedFileDeduplication
│
├── nodes
│   ├── node1
│   │   └── file1.txt
│   ├── node2
│   │   ├── file2.txt
│   │   └── file3.txt
│   └── node3
│       └── file4.txt
│
├── file_scanner.py
├── file_hasher.py
├── duplicate_detector.py
├── deduplication_service.py
├── distributed_scanner.py
├── distributed_deduplication.py
├── divide_files.py
├── multiprocessing_hash.py
├── multiprocessing_deduplication.py
├── deduplication_report.py
├── storage_report.py
├── remove_duplicates.py
└── README.md
7. File Description
file_scanner.py

Scans the storage folder and finds files.

file_hasher.py

Calculates the SHA-256 hash of each file.

duplicate_detector.py

Detects duplicate files by comparing their hashes.

distributed_scanner.py

Scans files from multiple distributed nodes.

distributed_deduplication.py

Finds duplicate files across distributed nodes.

divide_files.py

Divides the files into smaller groups using divide-and-conquer.

multiprocessing_hash.py

Calculates file hashes using multiprocessing.

multiprocessing_deduplication.py

Uses multiprocessing and hashing to detect duplicate files.

deduplication_report.py

Displays total, unique, and duplicate file counts.

storage_report.py

Calculates storage used and storage saved.

remove_duplicates.py

Asks for user confirmation before deleting duplicate files.

8. Duplicate Detection Method

The project uses SHA-256 content hashing.

If two files have the same content:

Same Content
     ↓
Same SHA-256 Hash
     ↓
Duplicate File

For example:

node1/file1.txt → Hello World
node2/file3.txt → Hello World

Both files produce the same hash, so file3.txt is detected as a duplicate.

9. Divide-and-Conquer

The files are divided into smaller groups before processing.

All Files
    ↓
Group 1     Group 2

This makes the system easier to process and prepares it for parallel execution.

10. Multiprocessing

Python multiprocessing is used to process different groups of files in parallel.

             Files
               ↓
       ┌───────┴───────┐
       ↓               ↓
   Process 1        Process 2
   Group 1          Group 2

This can improve processing efficiency for large file collections.

11. Sample Result

For the current test data:

Total Files: 4
Unique Files: 3
Duplicate Files: 1

Duplicate file:

nodes/node2/file3.txt
12. Storage Result

The current test produced:

Storage Before: 55 bytes
Storage After: 44 bytes
Space Saved: 11 bytes
13. Testing

The project was tested with:

Duplicate files
Different files
Duplicate files restored again

All tests produced the expected results.

14. Conclusion

The Distributed File Deduplication Service successfully detects duplicate files across multiple nodes using SHA-256 hashing. Divide-and-conquer and multiprocessing are used to organize and process files efficiently. The system also generates deduplication and storage reports.
