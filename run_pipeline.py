#!/usr/bin/env python
"""-----------------------------------------------------------------------
  Python script for running the custom tsdat package defined by this
  package.
---------------------------------------------------------------------------"""
import argparse
import sys
import os

# Add the parent directory to the pythonpath
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

from pipeline.runner import run_pipeline


def main():
    """-------------------------------------------------------------------
    Main function.
    -------------------------------------------------------------------"""

    # Parse arguments - a file or list of files
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='+', type=str)
    args = parser.parse_args()
    files = []

    for f in args.file:
        files.append(f)

    # run the pipeline
    run_pipeline(files)


if __name__ == "__main__":
    main()
