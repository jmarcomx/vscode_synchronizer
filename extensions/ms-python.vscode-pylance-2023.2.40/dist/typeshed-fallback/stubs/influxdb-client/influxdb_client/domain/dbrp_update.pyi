from _typeshed import Incomplete

class DBRPUpdate:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, retention_policy: Incomplete | None = ..., default: Incomplete | None = ...) -> None: ...
    @property
    def retention_policy(self): ...
    @retention_policy.setter
    def retention_policy(self, retention_policy) -> None: ...
    @property
    def default(self): ...
    @default.setter
    def default(self, default) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
