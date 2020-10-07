import os


def removeFiles(ext):

    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            path = os.path.join(root, name)
            if path.endswith(ext):
                os.remove(path)

    print("All srt files removed successfully 😁😁😁")


removeFiles(".srt")
