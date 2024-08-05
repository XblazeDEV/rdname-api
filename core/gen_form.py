from pydantic import BaseModel


class RefGen(BaseModel):
    ref1: list[str]
    ref2: list[str]