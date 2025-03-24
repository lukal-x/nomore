"""list helper"""

from nomore.deps.helpers.contracts import HelperContract


class L(HelperContract):

    @staticmethod
    def joined(parts: list[str], sep: str = ", ") -> str:
        return sep.join(parts)

    def join(self, sep: str = ", ") -> "L":
        self.v = L.joined(self.v, sep)
        return self
