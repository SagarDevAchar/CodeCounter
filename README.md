# CodeCounter
A Basic Newline-checking Python CLI to measure Code Work

## How to Use

1. Run the Python Script
2. Provide the **ABSOLUTE FOLDER PATHS** as input when asked 
    - Multiple Folders can be scanned at once
    - Seperate the paths by the character **`|`** and hit `ENTER`
3. On successful execution, the results are displayed
4. A **scan_list.txt** is generated, consisting the paths of all the files scanned

## Supported Filetypes

- **Python Files** : `*.py` and `*.pyw`
- **C Files** : `*.c`
- **C++ Files** : `*.cpp`
- **Java Files** : `*.java`
- **Arduino Files** : `*.ino`

Feel free to make changes to the code (particularly `scanCodeFiles()` and `SCAN_LIST`) to customize the working for other filetypes

## Requirements

- **OS** : Windows
- A Proper installation of Python 3
