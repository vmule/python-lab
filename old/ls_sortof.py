import argparse
import os
import sys

class WalkDirs(object):

    def __init__(self, path):
          self.path = path

    def dir_walk(self, dot_files=False, recursive=False):
        path = os.path.abspath(self.path)
        try:
            file_list = os.listdir(path)
        except FileNotFoundError:
            print("Error: %s is not a valid path" % path)
            exit(1)
        except PermissionError:
            print("Error: invalid permission for %s" % path)
            exit(1)

        if dot_files:
            print('.')
            print('..')
        for entry in file_list:
            filename = entry
            abs_filename = os.path.join(path, entry)
            if os.path.isfile(abs_filename):
                if not dot_files and '.' in filename[0]:
                    continue
                print(abs_filename)
            elif os.path.isdir(abs_filename):
                if not dot_files and '.' in filename[0]:
                    continue
                elif recursive:
                    # call itself
                    print("\n%s:" % abs_filename)
                    instance = WalkDirs(abs_filename)
                    instance.dir_walk(dot_files=dot_files, recursive=recursive)
                else:
                    print(abs_filename + '/')
            else:
                print("%s is not file nor dir." % abs_filename)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", action="store_true", help="Print dot files")
    parser.add_argument("-r", action="store_true", help="Recursive")
    parser.add_argument("Path", help="Path to folder")
    args = parser.parse_args()

    instance = WalkDirs(args.Path)
    instance.dir_walk(dot_files=args.a, recursive=args.r)

if __name__ == '__main__':
    main()
