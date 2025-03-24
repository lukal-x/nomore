import sys
import typing as T

from nomore.deps.services.keyrings.linux import LinuxKeyring

impl: KeyringContract | None = None

match sys.platform:
    case "linux":
         impl = LinuxKeyring()
    case _:
        logging.warning(f"Keyring implementation for {sys.platform} not implemented yet!")
        pass


def set_password(svc: str, usr: str, pwd: str | None = None) -> None:
    return impl.set_password(svc, usr, pwd)


def get_password(svc: str, usr: str) -> str | None:
    return impl.get_password(svc, usr)
