import os


def rename_images(directory, file_type):
    """
    Rename all files in the given directory to sequential names.

    :param directory: The directory containing the files.
    :param file_type: The file extension of the files to be renamed (e.g., '.jpg').
    """
    files = [
        file for file in os.listdir(directory)
        if file.lower().endswith(file_type.lower())
    ]
    i = 0
    for file in files:
        print(f'{file}\t-->  ', end='')
        old_path = os.path.join(directory, file)
        new_file_name = f'{i}.{file_type}'  # 1.jpg, 2.jpg etc
        new_renamed_path = os.path.join(directory, new_file_name)
        os.rename(old_path, new_renamed_path)
        new_files = [
            file for file in os.listdir(directory)
            if file.lower().endswith(file_type.lower())
        ]

        print(new_files[i])
        i += 1


rename_images('F:\\test', '.jpg')
