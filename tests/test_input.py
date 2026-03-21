import pytest
from app.io.input import read_from_file, read_from_file_with_pandas


class TestReadFromFile:

    def test_success(self, tmp_path):
        file = tmp_path / "test.txt"
        file.write_text("Hello", encoding="utf-8")

        assert read_from_file(file) == "Hello"

    def test_empty(self, tmp_path):
        file = tmp_path / "empty.txt"
        file.write_text("", encoding="utf-8")

        assert read_from_file(file) == ""

    def test_not_found(self):
        with pytest.raises(FileNotFoundError):
            read_from_file("no_file.txt")
