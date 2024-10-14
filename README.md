# File Size Dictionary Generator

This Python program generates a dictionary where the keys are the filenames in a specified directory (folder) and the values are their respective file sizes in bytes. 

The program supports two modes: one that skips subdirectories and one that includes them.

## Features

- **Basic Mode**: Collects file sizes for all files in the specified directory, excluding subfolders.

- **Recursive Mode**: Recursively collects file sizes from all files in the specified directory and its subdirectories.

- **Largest Files Report**: Prints the top `n` largest files within the directory and its subfolders.

## Use Cases

This program can be useful in various scenarios where managing or analyzing file sizes in a directory structure is required. Below are some practical examples:

- Disk Space Management
- Backup Preparation
- File Inventory
- Automated Reports
- Detecting Duplicate Files

### Prerequisites

- Python 3.x
- `pathlib` module (comes pre-installed with Python 3)

### Installation

1. Clone the repository or copy the script to your local machine.

2. Make sure Python is installed and properly set up on your system.

### Running the Program

1. Set the target directory by modifying the `directory` variable in the script. For example:

   directory = 'dir_path_url'

2. To get a dictionary of file sizes for files in the specified directory:

   file_sizes = get_filesizes(directory)
   print(file_sizes)

3. To get file sizes for all files in the directory and its subdirectories:

   directory_size = get_filesizes_incl_subfolders(directory)

4. To print the top n largest files:

   print_largest_files(directory, n=10)



