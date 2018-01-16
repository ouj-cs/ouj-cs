import glob
import os

paths = glob.glob("*.jack")

for path in paths:
    root, ext = os.path.splitext(path)
    path1 = "{}.vm".format(root)
    path2 = "{}_org.vm".format(root)
    s = "diff -w {} {}".format(path1, path2)
    print(s)
    os.system(s)
