import os

def recurse_dir(root):
    root = os.path.abspath(root)
    for item in os.listdir(root):
        item_full_path = os.path.join(root, item)
        if os.path.isdir(item_full_path):
            recurse_dir(item_full_path)
        else:
            print("%s - %s" % (item_full_path, os.stat(item_full_path).st_size))


