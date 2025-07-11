from __future__ import annotations

from pydantic import BaseModel


class Todo(BaseModel):
    """Ein einzelner Todo-Eintrag."""

    id: int
    text: str
    done: bool = False
