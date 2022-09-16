import json
from argparse import ArgumentParser
from pathlib import Path


def merge(in_dir, out_fn):
    fnames = list(Path(in_dir).glob("*.json"))
    breakpoint()
    data = {}
    data['wines'] = []

    n_files = len(fnames)

    for fn in fnames:
        with open(fn, "r") as f:
            tmp_data = json.load(f)
            data["wines"] += tmp_data["wines"]
        f.close()

    unique_data = list({row['seo_name']: row for row in data['wines']}.values())

    with open(out_fn, 'w') as f:
        # Dumps the merged data
        json.dump(unique_data, f)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("in_dir")
    parser.add_argument("output_filename")
    args = parser.parse_args()
    merge(args.in_dir, args.output_filename)
