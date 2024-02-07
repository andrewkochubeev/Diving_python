from pathlib import Path
import os

def rename_files(desired_name, num_digits, source_ext, target_ext):
    os.chdir('test_folder')
    list_files = os.listdir()
    count = 1
    for name in list_files:
        if name.split('.')[-1] == source_ext:
            p = Path(name)
            p.rename(desired_name + str(count).zfill(num_digits) + '.' + target_ext)
            count += 1
