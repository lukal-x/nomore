import typing as T


class KeyringContract(T.Protocol):

    def set_password(self, svc: str, usr: str, pwd: str | None) -> None:
        """?"""

    def get_password(self, svc: str, usr: str) -> str | None:
        """?"""
