import dbus

from nomore.deps.helpers.l import L
from nomore.deps.services.keyrings.contracts import KeyringContract

bus: dbus.SessionBus = dbus.SessionBus()
keys: dbus.proxies.ProxyObject = bus.get_object(
    "org.gnome.Keyring", "/org/gnome/Keyring"
)


class LinuxKeyring(KeyringContract):
    def set_password(svc: str, usr: str, pwd: str | None = None) -> None:
        if pwd is None:
            pwd = input()

        keys.StoreSecret(
            L.joined([svc, usr], sep="_"), pwd, dbus_interface="org.gnome.Keyring"
        )

    def get_password(svc: str, usr: str) -> str | None:
        return keys.GetSecret(
            L.joined([svc, usr], sep="_"), dbus_interface="org.gnome.Keyring"
        )
