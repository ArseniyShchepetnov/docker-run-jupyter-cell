"""Default tests for build to pass."""
import os
import tempfile

from src.helloworld import write_helloworld


def test_default():
    """Test hello world funciton."""
    with tempfile.TemporaryDirectory() as tmpdir:
        file = os.path.join(tmpdir, "helloworld")

        write_helloworld(file=file)
        assert os.path.isfile(file)

        with open(file, "r", encoding="UTF-8") as fobj:
            string = fobj.read()
            assert string == "Hello World!"
