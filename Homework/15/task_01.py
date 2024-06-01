import argparse
from collections import namedtuple
import os
import logging



parser = argparse.ArgumentParser(description='Принимаем строку с путем до директории')
parser.add_argument('-p', type=str, default='D:/Users/Andrew/Documents/VirtualBox')
args = parser.parse_args()
Path_dir = namedtuple('Path_dir', ['name', 'extension', 'flag', 'parent'])
logging.basicConfig(filename='project.log.', filemode='w',
encoding='utf-8', level=logging.INFO)
logger = logging.getLogger('Основной файл проекта')

obj_list = []
for dir_path, dir_names, file_names in os.walk(args.p):
    for dir_name in dir_names:
        obj_list.append(Path_dir(dir_name, None, 'dir', dir_path.split('\\')[-1]))
    for file_name in file_names:
        obj_list.append(Path_dir(file_name.split('.')[0], file_name.split('.')[1], 'file', dir_path.split('\\')[-1]))
for item in obj_list:
    logger.info(f'name = {item.name}\next = {item.extension}\nf = {item.flag}\nparent = {item.parent}')
