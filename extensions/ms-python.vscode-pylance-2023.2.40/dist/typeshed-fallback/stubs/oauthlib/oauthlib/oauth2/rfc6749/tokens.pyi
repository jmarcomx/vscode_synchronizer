from _typeshed import Incomplete
from typing import Any

class OAuth2Token(dict[Any, Any]):
    def __init__(self, params, old_scope: Incomplete | None = ...) -> None: ...
    @property
    def scope_changed(self): ...
    @property
    def old_scope(self): ...
    @property
    def old_scopes(self): ...
    @property
    def scope(self): ...
    @property
    def scopes(self): ...
    @property
    def missing_scopes(self): ...
    @property
    def additional_scopes(self): ...

def prepare_mac_header(
    token,
    uri,
    key,
    http_method,
    nonce: Incomplete | None = ...,
    headers: Incomplete | None = ...,
    body: Incomplete | None = ...,
    ext: str = ...,
    hash_algorithm: str = ...,
    issue_time: Incomplete | None = ...,
    draft: int = ...,
): ...
def prepare_bearer_uri(token, uri): ...
def prepare_bearer_headers(token, headers: Incomplete | None = ...): ...
def prepare_bearer_body(token, body: str = ...): ...
def random_token_generator(request, refresh_token: bool = ...): ...
def signed_token_generator(private_pem, **kwargs): ...
def get_token_from_header(request): ...

class TokenBase:
    def __call__(self, request, refresh_token: bool = ...) -> None: ...
    def validate_request(self, request) -> None: ...
    def estimate_type(self, request) -> None: ...

class BearerToken(TokenBase):
    request_validator: Any
    token_generator: Any
    refresh_token_generator: Any
    expires_in: Any
    def __init__(
        self,
        request_validator: Incomplete | None = ...,
        token_generator: Incomplete | None = ...,
        expires_in: Incomplete | None = ...,
        refresh_token_generator: Incomplete | None = ...,
    ) -> None: ...
    def create_token(self, request, refresh_token: bool = ..., **kwargs): ...
    def validate_request(self, request): ...
    def estimate_type(self, request): ...