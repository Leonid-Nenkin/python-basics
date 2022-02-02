import os


def create_folders(start_folder, child_folders):
    if not os.path.exists(start_folder):
        os.mkdir(start_folder)

    for i in child_folders:
        os.mkdir(os.path.join(start_folder, i))


if __name__ == "__main__":
    start_dir_name = 'my_project'
    child_folders = ['settings', 'mainapp', 'adminapp', 'authapp']
    create_folders(start_dir_name, child_folders)

