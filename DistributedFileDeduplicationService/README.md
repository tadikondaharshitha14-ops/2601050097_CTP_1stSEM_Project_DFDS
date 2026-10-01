# Distributed File Deduplication Service

A Python-based distributed file deduplication system that detects duplicate files across multiple storage nodes using **SHA-256 content hashing**, **Object-Oriented Programming**, **Divide-and-Conquer**, and **Multiprocessing**.

---

## 📌 Problem Statement

**Detect and eliminate duplicate files across a large distributed file store.**

In distributed storage systems, the same file may be stored multiple times on different nodes. This results in unnecessary storage usage.

This project identifies duplicate files by comparing their content hashes and generates reports showing duplicate files and storage space that can be saved.

---

## 🎯 Objectives

* Scan files from multiple distributed nodes.
* Calculate SHA-256 hashes for files.
* Detect duplicate files based on content.
* Apply Object-Oriented Programming (OOP).
* Divide files into smaller groups using Divide-and-Conquer.
* Use multiprocessing for parallel file processing.
* Generate a deduplication report.
* Calculate storage space before and after deduplication.
* Provide safe deletion of duplicate files with user confirmation.

---

## 🛠️ Technologies Used

* **Python 3**
* **SHA-256 Hashing**
* **Object-Oriented Programming (OOP)**
* **Divide-and-Conquer**
* **Multiprocessing**
* **VS Code**
* **Git / GitHub**

---

## 📂 Project Structure

```text
DistributedFileDeduplication/
│
├── nodes/
│   ├── node1/
│   │   └── file1.txt
│   │
│   ├── node2/
│   │   ├── file2.txt
│   │   └── file3.txt
│   │
│   └── node3/
│       └── file4.txt
│
├── storage/
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
│
├── README.md
└── venv/
```

---

## 📄 Description of Files

### `file_scanner.py`

Scans the storage folder and finds all available files.

### `file_hasher.py`

Calculates the SHA-256 hash of a file using its content.

### `duplicate_detector.py`

Detects duplicate files by comparing their SHA-256 hashes.

### `deduplication_service.py`

Provides an OOP-based service for running duplicate detection.

### `distributed_scanner.py`

Scans multiple distributed nodes and collects all file paths.

### `distributed_deduplication.py`

Detects duplicate files across different distributed nodes.

### `divide_files.py`

Divides the collected files into smaller groups using the divide-and-conquer approach.

### `multiprocessing_hash.py`

Uses multiprocessing to calculate hashes for files in different groups.

### `multiprocessing_deduplication.py`

Combines multiprocessing and SHA-256 hashing to detect duplicate files.

### `deduplication_report.py`

Generates a report containing:

* Total files
* Unique files
* Duplicate files
* Duplicate file list

### `storage_report.py`

Calculates:

* Storage before deduplication
* Storage after deduplication
* Storage space saved

### `remove_duplicates.py`

Displays duplicate files and asks the user for confirmation before deleting them.

---

## ⚙️ How the System Works

The system follows the process below:

```text
Distributed Nodes
       │
       ↓
Scan Files
       │
       ↓
Collect File Paths
       │
       ↓
Divide Files into Groups
       │
       ↓
Multiprocessing
       │
       ↓
Calculate SHA-256 Hash
       │
       ↓
Compare Hashes
       │
       ↓
Identify Duplicate Files
       │
       ↓
Generate Report
       │
       ↓
Calculate Storage Saved
       │
       ↓
Ask User Before Deletion
```

---

## 🔐 SHA-256 Hashing

The project uses SHA-256 to generate a content hash for every file.

For example:

```text
node1/file1.txt
Content: Hello World

        ↓

SHA-256 Hash

        ↓

a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
```

If another file contains the same content, it produces the same hash.

Example:

```text
node1/file1.txt → Hello World → Hash A

node2/file3.txt → Hello World → Hash A
```

Therefore, `file3.txt` is identified as a duplicate.

> Note: In a production system, a matching hash should ideally be followed by a byte-for-byte comparison before treating two files as definitively identical.

---

## 🔀 Divide-and-Conquer

The project divides a large collection of files into smaller groups.

Example:

```text
All Files
    │
    ├───────────────┐
    ↓               ↓
 Group 1         Group 2
    │               │
 file1            file3
 file2            file4
```

This approach makes the files easier to process and prepares the system for parallel execution.

---

## ⚡ Multiprocessing

Python multiprocessing is used to process different groups of files using separate processes.

```text
                 Files
                   │
          ┌────────┴────────┐
          ↓                 ↓
      Process 1          Process 2
       Group 1            Group 2
          │                 │
          ↓                 ↓
       Hashing            Hashing
          │                 │
          └────────┬────────┘
                   ↓
          Duplicate Detection
```

This approach can improve processing efficiency for large collections of files.

---

## 📊 Sample Distributed Storage

The project uses three nodes:

```text
node1/
└── file1.txt → Hello World

node2/
├── file2.txt → Python is easy
└── file3.txt → Hello World

node3/
└── file4.txt → Distributed Systems
```

Here:

```text
file1.txt = file3.txt
```

because both contain:

```text
Hello World
```

Therefore:

```text
node2/file3.txt
```

is detected as a duplicate.

---

## 📈 Deduplication Report

The project produced the following result:

```text
Deduplication Report
--------------------
Total Files: 4
Unique Files: 3
Duplicate Files: 1

Duplicate File List:
nodes\node2\file3.txt
```

---

## 💾 Storage Report

For the test data:

```text
Storage Report
--------------
Total Files: 4
Unique Files: 3
Duplicate Files: 1

Storage Before: 55 bytes
Storage After: 44 bytes
Space Saved: 11 bytes
```

Therefore, the duplicate file accounts for **11 bytes** of storage that could be saved if the duplicate copy is removed.

---

## 🧪 Testing

The project was tested using different file contents.

### Test 1 — Duplicate Files

```text
file1.txt → Hello World
file3.txt → Hello World
```

Result:

```text
Duplicate Files: 1
```

✅ Test Passed

---

### Test 2 — Different Files

`file3.txt` was changed to:

```text
Different Content
```

Result:

```text
Total Files: 4
Unique Files: 4
Duplicate Files: 0
```

✅ Test Passed

---

### Test 3 — Duplicate Restored

`file3.txt` was changed back to:

```text
Hello World
```

Result:

```text
Total Files: 4
Unique Files: 3
Duplicate Files: 1
```

✅ Test Passed

---

## 🗑️ Safe Duplicate Removal

The project does not immediately delete duplicate files.

It first asks the user:

```text
Delete duplicate files? (yes/no):
```

If the user enters:

```text
no
```

the files remain unchanged.

If the user enters:

```text
yes
```

the detected duplicate files are deleted.

This provides a confirmation step before file removal.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project

```bash
cd DistributedFileDeduplication
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 5. Run the distributed scanner

```bash
python distributed_scanner.py
```

### 6. Run duplicate detection

```bash
python distributed_deduplication.py
```

### 7. Run multiprocessing

```bash
python multiprocessing_deduplication.py
```

### 8. Generate deduplication report

```bash
python deduplication_report.py
```

### 9. Generate storage report

```bash
python storage_report.py
```

### 10. Run safe duplicate removal

```bash
python remove_duplicates.py
```

---

## 🧠 Main Concepts Used

### 1. Content Hashing

Used to identify files with the same content.

### 2. Object-Oriented Programming

Used to organize the project into classes such as:

```python
FileHasher
DistributedScanner
DuplicateDetector
DeduplicationService
```

### 3. Divide-and-Conquer

Used to divide files into smaller groups.

### 4. Multiprocessing

Used to process different groups of files in parallel.

### 5. File System Operations

Python's `os` module is used for scanning files, checking file sizes, and handling duplicate files.

---

## 🌟 Advantages

* Detects duplicate files across multiple nodes.
* Reduces unnecessary storage usage.
* Uses content-based hashing.
* Supports parallel file processing.
* Provides storage and deduplication reports.
* Uses object-oriented design.
* Provides confirmation before deleting files.
* Can be extended for larger distributed storage systems.

---

## 🔮 Future Enhancements

The project can be extended with:

* Database-based metadata storage.
* Cloud storage support.
* Distributed worker nodes.
* Progress monitoring.
* Improved parallel processing.
* File recovery and backup.
* Web-based monitoring dashboard.
* Large-scale distributed storage support.

---

## 📝 Conclusion

The **Distributed File Deduplication Service** successfully detects duplicate files across multiple distributed nodes using SHA-256 content hashing.

The project demonstrates important concepts including:

* Distributed file scanning
* Content hashing
* Object-Oriented Programming
* Divide-and-Conquer
* Multiprocessing
* Duplicate detection
* Storage optimization
* Safe file deletion

The system successfully identified duplicate files in the test environment and calculated the storage space that could be saved through deduplication.
