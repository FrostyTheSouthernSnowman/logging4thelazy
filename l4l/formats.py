import traceback
from .base import BaseLogFormat


class ErrorLogFormat(BaseLogFormat):
    template = "{frame.filename}:{frame.lineno}:{frame.name}:\n" "    {frame.line}"

    def __init__(self, value) -> None:
        summary = traceback.StackSummary.extract(traceback.walk_stack(None))

        formated_summary = [self.template.format(frame=frame) for frame in summary]
        formated_summary.append(value)
        final = "\n".join(formated_summary)

        self.value = final
