# File-Integrity-Checker

COMPANY: CODETECH IT SOLUTION

NAME: YOKESH R

INTERN ID: CT04DH39

DOMAIN: CYBER SECURITY AND ETHICAL HACKING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

File Integrity Monitoring Tool Descrption:
This project is a File Integrity Monitoring (FIM) Tool built using Python. Its main purpose is to detect unauthorized or unexpected changes in files by calculating and comparing their cryptographic hash values. By monitoring changes in hash values, the tool helps ensure that sensitive or important files have not been altered, corrupted, or tampered with.

The tool uses the SHA-256 hashing algorithm from Python’s built-in hashlib library. On the first run, it calculates and stores the hash values of specified files in a JSON file. On subsequent runs, it recalculates the hash values of those files and compares them with the previously stored values. If the hash has changed, the tool flags the file as “modified”; if not found, it is marked as “new”; and if unchanged, it is reported as “OK”.

This solution is especially useful for basic security auditing, data protection, and file validation tasks, where it’s crucial to verify that files remain unaltered over time. It works completely offline and requires no third-party packages.

🔧 Features:
Monitors specific files for any changes.

Uses SHA-256 to ensure file integrity.

Saves hash history in a JSON file.

Provides clear status output: NEW, MODIFIED, UNCHANGED.

💡 Use Cases:
Verifying backups and critical files.

Detecting unauthorized changes to scripts, logs, or configurations.

Lightweight local file integrity checker for developers or administrators.

The tool is simple to use and only requires Python. It serves as a foundational security utility and can be extended for real-time monitoring or notifications.

OUTPUT:
