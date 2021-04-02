import os
import sys
import unittest

# Add the parent directory to the pythonpath
test_dir_path = os.path.dirname(os.path.realpath(__file__))
project_path = os.path.dirname(test_dir_path)
sys.path.append(project_path)

from pipeline.runner import run_pipeline


class TestPipeline(unittest.TestCase):

    def test_pipeline(self):
        # Run the pipeline via the runner
        run_pipeline(os.path.join(test_dir_path, "data"))


if __name__ == '__main__':
    unittest.main()
