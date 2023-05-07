# Modified from https://stackoverflow.com/a/21341209
from __future__ import annotations
import sys, logging
from typing import Optional

class ListStream:
    def __init__(self) -> None:
        self._curr_index = 0
        self.data = []

    def write(self, s) -> None:
        self.data.append(s)

    def readline(self) -> Optional[str]:
        if len(self.data) - 1 >= self._curr_index:
            self._curr_index += 1
            return self.data[self._curr_index - 1]
        return None
        
    def reset_index(self) -> None:
        self._curr_index = 0

    @property
    def index(self) -> int:
        return self._curr_index
    
    def __len__(self) -> int:
        return self.data.__len__()

    def __enter__(self) -> ListStream:
        sys.stdout = self
        return self
    
    def __exit__(self, ext_type, exc_value, traceback) -> None:
        sys.stdout = sys.__stdout__  

    def flush(self) -> None:
        pass

liststream = ListStream()
liststream_handler = logging.StreamHandler(liststream)