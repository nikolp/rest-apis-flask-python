import pytest
import pathlib
from unittest import mock 

@pytest.fixture
def common_file():
    with open('some_data.txt') as dt:
        return dt.read()

def test_one(tmp_path):
    print(tmp_path)

def test_two(tmp_path):
    print(tmp_path)

def test_three(common_file):
    print(common_file)

def count_current_dir_files():
    counter = 0
    print()
    for c in pathlib.Path('.').iterdir():
        print(c)
        counter += 1
    return counter

def test_count_current_dir_files_v1(monkeypatch):
    def mock_file_list(_mock_self):
        return ["file1", "file2", "file3"]
    
    monkeypatch.setattr(pathlib.Path, 'iterdir', mock_file_list)
    assert count_current_dir_files() == 3

def test_count_current_dir_files_v2():
    with mock.patch('pathlib.Path', spec=True) as m:
        # The first "return_value" is needed since we mock Path but code under test calls Path()
        m.return_value.iterdir.return_value = ["file1", "file2", "file3"];
        assert count_current_dir_files() == 3