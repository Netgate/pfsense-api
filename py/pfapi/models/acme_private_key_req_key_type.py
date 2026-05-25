from enum import Enum


class ACMEPrivateKeyReqKeyType(str, Enum):
    EC256 = "ec256"
    EC384 = "ec384"
    RSA2048 = "rsa2048"
    RSA3072 = "rsa3072"
    RSA4096 = "rsa4096"
    RSA8192 = "rsa8192"

    def __str__(self) -> str:
        return str(self.value)
