from _typeshed import Incomplete, Self
from typing import Any

class Settings:
    def __new__(cls: type[Self], *args, **kw) -> Self: ...
    def __init__(self, settings: Incomplete | None = ...) -> None: ...
    @classmethod
    def get_key(cls, settings: Incomplete | None = ...): ...
    def replace(self, mod_settings: Incomplete | None = ..., **kwds): ...

settings: Any

def apply_settings(f): ...

class SettingValidationError(ValueError): ...

def check_settings(settings) -> None: ...