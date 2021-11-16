"""--------------------------------------------------------------------------
Python script for running the custom tsdat pipeline defined by this project.
---------------------------------------------------------------------------"""
import argparse
from pipeline.runner import run_pipeline


def main():
    """-------------------------------------------------------------------
    Main function.
    -------------------------------------------------------------------"""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m",
        "--mode",
        default="dev",
        help="Identify the configuration to use.  Default is dev.",
    )
    parser.add_argument("file", nargs="*", type=str)
    args = parser.parse_args()

    files = []
    for f in args.file:
        files.append(f)

    run_pipeline(mode=args.mode, input_files=files)


if __name__ == "__main__":
    main()
