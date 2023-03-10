from _typeshed import Self
from collections.abc import Iterable
from re import Pattern
from typing import IO

from paramiko.ssh_exception import ConfigParseError as ConfigParseError, CouldNotCanonicalize as CouldNotCanonicalize

SSH_PORT: int

class SSHConfig:
    SETTINGS_REGEX: Pattern[str]
    TOKENS_BY_CONFIG_KEY: dict[str, list[str]]
    def __init__(self) -> None: ...
    @classmethod
    def from_text(cls: type[Self], text: str) -> Self: ...
    @classmethod
    def from_path(cls: type[Self], path: str) -> Self: ...
    @classmethod
    def from_file(cls: type[Self], flo: IO[str]) -> Self: ...
    def parse(self, file_obj: IO[str]) -> None: ...
    def lookup(self, hostname: str) -> SSHConfigDict: ...
    def canonicalize(self, hostname: str, options: SSHConfigDict, domains: Iterable[str]) -> str: ...
    def get_hostnames(self) -> set[str]: ...

class LazyFqdn:
    fqdn: str | None
    config: SSHConfig
    host: str | None
    def __init__(self, config: SSHConfigDict, host: str | None = ...) -> None: ...

class SSHConfigDict(dict[str, str]):
    def as_bool(self, key: str) -> bool: ...
    def as_int(self, key: str) -> int: ...
