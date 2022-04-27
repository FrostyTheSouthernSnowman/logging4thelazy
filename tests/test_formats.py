from l4l import ErrorLogFormat
import re


def test_error_log_format():
    error_log = ErrorLogFormat("some log")
    assert (
        re.search("some log$", error_log.value) != None
    )  # TODO: find a better way to match with a string that ends in 'some logs' and includes something that looks like a traceback
