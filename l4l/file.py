from .base import BaseLogFormat, BaseLogger
import typing


class FileLogger(BaseLogger):
    """
    # FileLogger
    FileLogger logs values to a file.
    Define the file path with the path argument when you initialize a FileLogger.
    """

    file = None

    def __init__(self, name: str = "FileLogger", path: str = None) -> None:
        if path == None:
            raise ValueError(f"path can't be none")

        if type(path) != str:
            raise TypeError(f"path must be a string, but got {path}")

        if type(name) != str:
            raise TypeError(f"name should be string, but got {type(name)}")

        self.file = open(path, "a+")
        print(f"{name}: all logs logged by logger, {name}", file=self.file)

        self.name = name
        self.logs = [f"{name}: all logs logged by logger, {name}"]

    def log(
        self, value: typing.Type[BaseLogFormat], stdout: bool = False, stderr=False
    ) -> None:
        """
        logs value to a path. Additionally, if you also want the value to go to stdout or stderr,
        you only need to set stdout or stderr to True.
        """
        print(f"{self.name}: {value.value}", file=self.file)

        if stdout or stderr:
            return super().log(value, stdout, stderr)

    def __del__(self):
        if self.file != None:
            self.file.close()
