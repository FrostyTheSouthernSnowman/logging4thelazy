import pytest
import os

from l4l import FileLogger, from_value


def test_file_logger_with_no_path():
    with pytest.raises(ValueError):
        logger = FileLogger()


def test_file_logger_with_non_string_path():
    with pytest.raises(TypeError):
        logger = FileLogger(path=134)


def test_file_logger_with_non_string_name():
    with pytest.raises(TypeError):
        logger = FileLogger(name=134, path="logs.log")


def test_file_logger_logs_to_file():
    path = "./logs.log"
    logger = FileLogger(name="TestFileLogger", path=path)
    logger.log(from_value("A test log"))
    del logger  # closes the log file
    with open("./logs.log", "r") as f:
        assert (
            f.readline()
            == "TestFileLogger: all logs logged by logger, TestFileLogger\n"
        )
        assert f.readline() == "TestFileLogger: A test log\n"

    os.remove(path)


def test_file_logger_also_logs_to_stdout(capsys):
    path = "./logs.log"
    logger = FileLogger(name="TestFileLogger", path=path)
    logger.log(from_value("A test log"), stdout=True)
    out, _ = capsys.readouterr()
    assert out == "TestFileLogger: A test log\n"
    del logger  # closes the log file
    os.remove(path)
