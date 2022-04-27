import pytest

from l4l import BaseLogFormat, BaseLogger, from_value


def test_base_log_format():
    log_format = BaseLogFormat("test")
    assert log_format.value == "test"


def test_base_logger_init(capsys):
    logger = BaseLogger("logger")
    out, _ = capsys.readouterr()
    assert out == "logger: List of all logs logged by logger, logger\n"
    assert logger.name == "logger"
    assert logger.logs == ["logger: List of all logs logged by logger, logger"]


def test_base_logger_with_wrong_init_args():
    with pytest.raises(TypeError):
        logger = BaseLogger(42)


def test_base_logger_log_raises_error_when_stdout_is_not_bool():
    with pytest.raises(TypeError):
        logger = BaseLogger("logger")
        logger.log(from_value("test"), "asdf", False)


def test_base_logger_log_raises_error_when_stderr_is_not_bool():
    with pytest.raises(TypeError):
        logger = BaseLogger("logger")
        logger.log(from_value("test"), True, "asdf")


def test_base_logger_log_raises_error_when_stdout_and_stderr_are_true():
    with pytest.raises(ValueError):
        logger = BaseLogger("logger")
        logger.log(from_value("test"), True, True)


def test_base_logger_logs_to_stdout(capsys):
    logger = BaseLogger("logger")
    _, _ = capsys.readouterr()  # clear capsys
    logger.log(from_value("test"), stdout=True, stderr=False)
    out, _ = capsys.readouterr()
    assert out == "logger: test\n"
    assert logger.logs[1] == "logger: test"


def test_base_logger_logs_to_stderr(capsys):
    with pytest.raises(Exception):
        logger = BaseLogger("logger")
        _, _ = capsys.readouterr()  # clear capsys
        logger.log(from_value("test"), stdout=False, stderr=True)
        _, err = capsys.readouterr()
        assert err == "logger: test\n"
        assert logger.logs[1] == "logger: test"


def test_from_value():
    assert from_value("test").value == BaseLogFormat("test").value
    assert isinstance(from_value("test"), BaseLogFormat)
