from os import getenv

auth_server_url = getenv("AUTH_SERVER_URL")

class Auth:
    def __init__(self, error: bool, code: int | None = None, detail: str | None = None) -> None:
        self.error = error
        self.code = code
        self.detail = detail

    @classmethod
    def validate(cls, header: str):
        # TODO request to auth server
        
        return cls(False)
