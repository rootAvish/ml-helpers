#!/bin/env python3
import json
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="File containing the list required to be converted.",
        type=str)
    filename = parser.parse_args().filename

    json_list = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line:
                json_list.append(line)

    with open(".".join(filename.split(".")[:-1]) + ".json", "w") as o:
        o.write(json.dumps(json_list))

if __name__ == '__main__':
    main()
