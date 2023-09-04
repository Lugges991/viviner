import json
from argparse import ArgumentParser
from pathlib import Path
import pandas as pd 


def merge(in_dir, out_fn):
    fnames = sorted(list(Path(in_dir).glob("*.json")))

    all_wines = []

    for fn in fnames:
        print(f"Processing {fn.name}")
        with open(fn, "r") as f:
            j = json.load(f)
            all_wines.extend(j["wines"])


    with open(out_fn, "w") as f:
        json.dump(all_wines, f)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("in_dir")
    parser.add_argument("output_filename")
    args = parser.parse_args()
    merge(args.in_dir, args.output_filename)
