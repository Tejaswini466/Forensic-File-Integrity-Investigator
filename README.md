# Forensic File Integrity & Metadata Investigator

A Python-based digital forensics tool that automates file integrity verification, metadata extraction, anomaly detection, and forensic report generation.

The tool helps investigators and system administrators identify unauthorized file modifications by comparing cryptographic hashes, analyzing file metadata, and detecting suspicious file behavior using statistical methods.

---

## 📌 Problem Statement

Manually verifying thousands of files for unauthorized changes is time-consuming and inefficient.

Files may be modified, replaced, or manipulated without obvious signs. Traditional manual checks make it difficult to quickly identify suspicious changes or abnormal file behavior.

This project provides an automated solution to scan directories, collect forensic evidence, detect anomalies, and generate structured reports.

---

## Features

### 1. File Integrity Verification
- Generates cryptographic hashes using:
  - MD5
  - SHA-256
- Compares current file states against previously stored baselines
- Detects files that have been modified or tampered with

### 2. Metadata Extraction
Collects important forensic information:

- File name
- File path
- File size
- File extension
- Last modified timestamp
- File permissions
- Cryptographic hash

### 3. Statistical Anomaly Detection

Uses NumPy-based analysis to identify unusual files:

- Calculates average file size
- Measures standard deviation
- Flags files that significantly differ from normal behavior

Example:
> A text file that suddenly becomes hundreds of megabytes may indicate suspicious activity.

### 4. Automated Reporting

Generates structured forensic reports using Pandas:

- Converts scan results into DataFrames
- Categorizes files based on modification age
- Exports reports to Excel format

Generated report:
![Screenshot of sample report](<Screenshot (526).png>)


### 5. Baseline Persistence

Uses Pickle to store a "Known Good" snapshot of a directory.

Future scans compare against this baseline to identify:

- Modified files
- Changed hashes
- New files
- Missing files

---

## 6. Project Architecture

Forensic-File-Integrity-Investigator
│
├── main.py # Program entry point
│
├── scanner.py # File scanning and metadata collection
│
├── analyzer.py # Statistical anomaly detection
│
├── reporter.py # Report generation using Pandas
│
├── utils.py # Hashing and helper functions
│
├── baselines/ # Stored forensic snapshots
│
├── reports/ # Generated reports
│
└── requirements.txt # Required Python packages


## Technologies Used

### Programming Language
- Python 3.x

### Data Science
- NumPy
- Pandas

### Security & System Modules
- hashlib
- os
- time

### Data Persistence
- Pickle

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Tejaswini466/Forensic-File-Integrity-Investigator.git

cd Forensic-File-Integrity-Investigator

pip install -r requirements.txt

python main.py
```

## Output

The tool generates:
Forensic_Report.xlsx

The report contains:

- File details
- Integrity status
- Anomaly detection results
- Modification information


## Possible enhancements:

- Real-time file monitoring
- Malware signature detection
- Digital evidence timeline generation
- GUI interface
- Database-based evidence storage
- Advanced anomaly detection using machine learning