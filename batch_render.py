import os
import subprocess
import glob
import argparse
parser = argparse.ArgumentParser(
    description="Batch imports and renders models from 4 angles using Blender")
parser.add_argument(
    "glob", help="Use a glob with ** or * to select files", type=str)
parser.add_argument(
    "-b", "--blender", help="Specify the path to blender executable, defaults to path for Blender installed through Steam on Windows", type=str, default="C:\\Program Files (x86)\\Steam\\steamapps\\common\\Blender\\blender.exe")
args = parser.parse_args()

file_list = sorted(glob.glob(
    args.glob, recursive=True))
for filename in file_list:
    # print(item)
    subprocess.run([args.blender, "-b", "./import.blend",
                    "-P", "import.py", "--", filename])
