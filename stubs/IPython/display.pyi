from typing import Union, List, Tuple, Any, Dict

class HTML:
    def __init__(
        self: HTML,
        data: str,
        url: str = None,
        filename: str = None,
        metadata: Dict[Any, Any] = None,
    ): ...

def display(*objs: Any) -> DisplayHandle: ...

class DisplayHandle:
    pass
