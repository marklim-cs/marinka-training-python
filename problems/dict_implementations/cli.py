import argparse
import timeit
from pathlib import Path
from .compare_dicts import ArrayMap, TreeMap, PythonDict, Node

parser = argparse.ArgumentParser()

parser.add_argument("storage")
parser.add_argument("path")

args = parser.parse_args()
file_path = Path(args.path)

if not file_path.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

def count_words(path, storage):
    with open(path, "r", encoding="utf-8") as f:
        textfile = f.read()

    words = textfile.split()
    tree_map = TreeMap()

    for word in words:
        value = tree_map.find(word) or 0
        tree_map.insert(word, value + 1)


def execution_time():
    code = count_words
    time_taken = timeit.timeit(code)
    print(time_taken)