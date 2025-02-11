from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ip_sec_bypass_rules import IPSecBypassRules
    from ..models.ip_sec_logging import IPSecLogging


T = TypeVar("T", bound="IPSecConfig")


@_attrs_define
class IPSecConfig:
    """
    Attributes:
        logging (IPSecLogging):
        async_crypto (bool):
        uniqueids (str):
        filtermode (str):
        bypassrules (IPSecBypassRules):
        pkcs11support (bool):
        enableinterfacesuse (bool):
        unityplugin (bool):
        strictcrlpolicy (bool):
        makebeforebreak (bool):
        ipsecbypass (bool):
        acceptunencryptedmainmode (bool):
        maxexchange (int):
        port_nat_t (int):
        port (int):
        compression (bool):
        noshuntlaninterfaces (bool):
        maxmss (str):
    """

    logging: "IPSecLogging"
    async_crypto: bool
    uniqueids: str
    filtermode: str
    bypassrules: "IPSecBypassRules"
    pkcs11support: bool
    enableinterfacesuse: bool
    unityplugin: bool
    strictcrlpolicy: bool
    makebeforebreak: bool
    ipsecbypass: bool
    acceptunencryptedmainmode: bool
    maxexchange: int
    port_nat_t: int
    port: int
    compression: bool
    noshuntlaninterfaces: bool
    maxmss: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        logging = self.logging.to_dict()

        async_crypto = self.async_crypto

        uniqueids = self.uniqueids

        filtermode = self.filtermode

        bypassrules = self.bypassrules.to_dict()

        pkcs11support = self.pkcs11support

        enableinterfacesuse = self.enableinterfacesuse

        unityplugin = self.unityplugin

        strictcrlpolicy = self.strictcrlpolicy

        makebeforebreak = self.makebeforebreak

        ipsecbypass = self.ipsecbypass

        acceptunencryptedmainmode = self.acceptunencryptedmainmode

        maxexchange = self.maxexchange

        port_nat_t = self.port_nat_t

        port = self.port

        compression = self.compression

        noshuntlaninterfaces = self.noshuntlaninterfaces

        maxmss = self.maxmss

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logging": logging,
                "async_crypto": async_crypto,
                "uniqueids": uniqueids,
                "filtermode": filtermode,
                "bypassrules": bypassrules,
                "pkcs11support": pkcs11support,
                "enableinterfacesuse": enableinterfacesuse,
                "unityplugin": unityplugin,
                "strictcrlpolicy": strictcrlpolicy,
                "makebeforebreak": makebeforebreak,
                "ipsecbypass": ipsecbypass,
                "acceptunencryptedmainmode": acceptunencryptedmainmode,
                "maxexchange": maxexchange,
                "port_nat_t": port_nat_t,
                "port": port,
                "compression": compression,
                "noshuntlaninterfaces": noshuntlaninterfaces,
                "maxmss": maxmss,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ip_sec_bypass_rules import IPSecBypassRules
        from ..models.ip_sec_logging import IPSecLogging

        d = src_dict.copy()
        logging = IPSecLogging.from_dict(d.pop("logging"))

        async_crypto = d.pop("async_crypto")

        uniqueids = d.pop("uniqueids")

        filtermode = d.pop("filtermode")

        bypassrules = IPSecBypassRules.from_dict(d.pop("bypassrules"))

        pkcs11support = d.pop("pkcs11support")

        enableinterfacesuse = d.pop("enableinterfacesuse")

        unityplugin = d.pop("unityplugin")

        strictcrlpolicy = d.pop("strictcrlpolicy")

        makebeforebreak = d.pop("makebeforebreak")

        ipsecbypass = d.pop("ipsecbypass")

        acceptunencryptedmainmode = d.pop("acceptunencryptedmainmode")

        maxexchange = d.pop("maxexchange")

        port_nat_t = d.pop("port_nat_t")

        port = d.pop("port")

        compression = d.pop("compression")

        noshuntlaninterfaces = d.pop("noshuntlaninterfaces")

        maxmss = d.pop("maxmss")

        ip_sec_config = cls(
            logging=logging,
            async_crypto=async_crypto,
            uniqueids=uniqueids,
            filtermode=filtermode,
            bypassrules=bypassrules,
            pkcs11support=pkcs11support,
            enableinterfacesuse=enableinterfacesuse,
            unityplugin=unityplugin,
            strictcrlpolicy=strictcrlpolicy,
            makebeforebreak=makebeforebreak,
            ipsecbypass=ipsecbypass,
            acceptunencryptedmainmode=acceptunencryptedmainmode,
            maxexchange=maxexchange,
            port_nat_t=port_nat_t,
            port=port,
            compression=compression,
            noshuntlaninterfaces=noshuntlaninterfaces,
            maxmss=maxmss,
        )

        ip_sec_config.additional_properties = d
        return ip_sec_config

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
