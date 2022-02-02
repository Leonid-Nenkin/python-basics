import os
import shutil
from os import scandir, path, mkdir

def collect_templates(start_folder, child_folders):

    if not path.exists('templates'):
        mkdir(path.join(start_folder, 'templaes'))
    
    for i in child_folders:
        mkdir(path.join(start_folder, 'templaes', i))

    for i in child_folders:
        for item in scandir(path.join(start_folder, i, 'templates')):
            shutil.copy(item, path.join(start_folder, 'templaes', i))


if __name__== "__main__":
    start_dir_name = 'my_project'
    child_folders = ['settings', 'mainapp', 'adminapp', 'authapp']
    collect_templates(start_dir_name, child_folders)