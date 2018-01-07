import glob
import os

paths = glob.glob("*.output.xml")

for path in paths:
    root, ext = os.path.splitext(path)
    root, ext = os.path.splitext(root)
    path2 = "{}.xml".format(root)
    s = "diff -w {} {}".format(path2, path)
    print(s)
    os.system(s)
