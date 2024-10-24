
"""
Create a dict in which the keys are the names of files in a directory and the values are 
the sizes of those files. 

To calculate the file size, you can use os.stat or Path.stat()

Example directory - 'dir_path_url'
"""

from pathlib import Path 
import sys

def get_filesizes(directory):
	"""Walk through the directory and create a dict with filenames as keys and the file sizes 
	as values. Can skip subfolders."""
	folder_dict = {}

	# Convert the directory path to a Path object
	dir_path = Path(directory)

	# Iterate through all the files in the directory (excluding subfolders)
	print(f"Directory being processed: {dir_path}")

	for file_path in dir_path.iterdir():
		# Check if it's a file (not a directory)
		if file_path.is_file():
			folder_dict[file_path.name] = file_path.stat().st_size

	return folder_dict

"""
Recursive Version:

If you want to recursively walk through all subdirectories as well, use Path.rglob('*') 
instead of Path.iterdir():
"""

def get_filesizes_incl_subfolders(directory):
	"""Walk through the directory and all subdirectories recursively and create a dict with 
	filenames as keys and the file sizes as values."""
	folder_dict = {}
	filename_count = {}

	# Convert the directory path to a Path object
	dir_path = Path(directory)

	# Iterate through all the files in the directory (excluding subfolders)
	for file_path in dir_path.rglob('*'):
		# Check if it's a file (not a directory)
		if file_path.is_file():
			# Extract the base filename
			base_filename = file_path.name 

			# If the filename has been encountered before increment the count and add a suffix
			if base_filename in filename_count:
				filename_count[base_filename] += 1
				new_filename = f"{base_filename}-{filename_count[base_filename]}"
			else:
				# First occurance of the filename
				filename_count[base_filename] = 1 
				new_filename = base_filename

			# Use the relative path as the key to avoid filename conflicts
			folder_dict[new_filename] = file_path.stat().st_size

	return folder_dict

print()

def print_largest_files(directory, n=10):
	"""Print the n largest files in a directory, including subdirectories with size and 
	folder path."""

	# Get all file sizes using the get_filesizes_and_subfolders function
	file_sizes = get_filesizes_incl_subfolders(directory)

	# Sort the files by size in descending order
	sorted_files = sorted(file_sizes.items(), key=lambda x: x[1], reverse=True)

	# Get the top n largest files
	largest_files = sorted_files[:n]

	# Neatly print the results
	print(f"\nThe {n} largest files in '{directory}' are:\n")
	for i, (filename, size) in enumerate(largest_files, 1):
		# Print the filename and size in KB
		print(f"{i}. {filename} - {size/1024:.2f} KB")


if __name__ == "__main__":
	# Check if a command-line argument is provided
	if len(sys.argv) != 2: 
		print("Usage: python3 file_sizes.py directory_path")
		sys.exit(1)

	# Get the directory path from the command-line argument
	directory = sys.argv[1]

	# Print the largest files in the specified directory
	print_largest_files(directory)






