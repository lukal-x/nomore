import dbus

from nomore.deps.helpers.l import L
from nomore.deps.services.keyrings.contracts import KeyringContract


class Secrets(KeyringContract):
    __bus: dbus.SessionBus
    __interface: str
    __name: str
    __iface: dbus.proxies.ProxyObject

    def __init__(self) -> None:
        self.__bus = dbus.SessionBus()

        self.__name = "org.freedesktop.secrets"
        self.__interface = "org.freedesktop.Secret.Service"
        self.__objpath = "/org/freedesktop/secrets"

        self.__iface = self.__bus.get_object(self.__name, self.__objpath)

    @property
    def iface(self) -> dbus.proxies.ProxyObject:
        return self.__iface

    def __get_ref(self, svc: str, usr: str) -> dbus.proxies.ProxyObject | None:
        items = self.iface.SearchItems(
            dict(service=svc, username=usr), dbus_interface=self.__interface
        )

        if not any(items):
            return None

        item: dbus.proxies.ProxyObject | None = next(iter(items), None)

        if item is None:
            raise AssertionError("?2")

        return item

    def set_password(self, svc: str, usr: str, pwd: str | None = None) -> None:
        if pwd is None:
            pwd = input()

        result = self.__get_ref(svc, usr).StoreSecret(
            dict(service=svc, username=usr), pwd, dbus_interface=self.__interface
        )
        print(result)

    def get_password(self, svc: str, usr: str) -> str | None:
        """?

        todo: encrypt the value!
        """
        item = self.__get_ref(svc, usr)
        if item is None:
            return None

        return item.GetSecret(dbus_interface=self.__interface)


class LinuxKeyring(KeyringContract):
    __impl: KeyringContract

    def __init__(self) -> None:
        try:
            self.__impl = Secrets()
        except Exception as ex:
            raise

    def set_password(self, svc: str, usr: str, pwd: str | None = None) -> None:
        return self.__impl.set_password(svc, usr, pwd)

    def get_password(self, svc: str, usr: str) -> str | None:
        return self.__impl.get_password(svc, usr)
