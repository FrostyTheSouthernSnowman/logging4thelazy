import typing


class BaseLogFormat:
    def __init__(self, value) -> None:
        self.value = value


class BaseLogger:
    def __init__(self, name: str = "BaseLogger") -> None:
        """
        # BaseLogger
        BaseLogger is a simple logging class.
        Define a name for BaseLogger to use in its logs.
        """
        if type(name) != str:
            raise TypeError(
                f"Argument name must be of type string, but got {type(name)}"
            )

        self.logs: typing.List[str] = [
            f"{name}: List of all logs logged by logger, {name}"
        ]
        print(self.logs[0])
        self.name = name

    def log(
        self, value: typing.Type[BaseLogFormat], stdout: bool = False, stderr=False
    ) -> None:
        """
        Logs a value.
        The value argument should be a LogFormat.
        The stdout argument tells wether the log should go to stdout.
        The stderr argument tells wether the log should go to stderr.
        Only stdout or stderr can be true. NOT BOTH!
        """

        if type(stdout) != bool or type(stderr) != bool:
            raise TypeError(
                f"stdout and stderr must both be of type boolean but got stdout: {type(stdout)}, and stderr: {type(stderr)}"
            )

        if stdout and stderr:
            raise ValueError("stdout and stderr cannot both be True.")

        if stdout:
            print(f"{self.name}: {value.value}")
            self.logs.append(f"{self.name}: {value.value}")

        if stderr:
            self.logs.append(f"{self.name}: {value.value}")
            raise Exception(f"{self.name}: {value.value}")

        return


def from_value(value: str):
    return BaseLogFormat(value)
