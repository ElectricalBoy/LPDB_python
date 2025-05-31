from typing import Any, NotRequired, Required, TypedDict

class LpdbResponse(TypedDict):
    result: Required[list[dict[str, Any]]]
    error: NotRequired[list[str]]
    warning: NotRequired[list[str]]
