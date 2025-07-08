from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_sec_bypass_rules import IPSecBypassRules
    from ..models.ip_sec_logging import IPSecLogging


T = TypeVar("T", bound="IPSecConfig")


@_attrs_define
class IPSecConfig:
    """
    Attributes:
        logging (Union[Unset, IPSecLogging]):
        async_crypto (Union[Unset, bool]):
        uniqueids (Union[Unset, str]):
        filtermode (Union[Unset, str]):
        bypassrules (Union[Unset, IPSecBypassRules]):
        pkcs11support (Union[Unset, bool]):
        enableinterfacesuse (Union[Unset, bool]):
        unityplugin (Union[Unset, bool]):
        strictcrlpolicy (Union[Unset, bool]):
        makebeforebreak (Union[Unset, bool]):
        ipsecbypass (Union[Unset, bool]):
        acceptunencryptedmainmode (Union[Unset, bool]):
        maxexchange (Union[Unset, int]):
        port_nat_t (Union[Unset, int]):
        port (Union[Unset, int]):
        compression (Union[Unset, bool]):
        noshuntlaninterfaces (Union[Unset, bool]):
        maxmss (Union[Unset, str]):
        dns_interval (Union[Unset, int]):
        ikev2_retransmit_enable (Union[Unset, bool]):
        ikev2_retransmit_tries (Union[Unset, int]):
        ikev2_retransmit_timeout (Union[Unset, int]):
        ikev2_retransmit_base (Union[Unset, int]):
        ikev2_retransmit_jitter (Union[Unset, int]):
        ikev2_retransmit_limit (Union[Unset, int]):
    """

    logging: Union[Unset, "IPSecLogging"] = UNSET
    async_crypto: Union[Unset, bool] = UNSET
    uniqueids: Union[Unset, str] = UNSET
    filtermode: Union[Unset, str] = UNSET
    bypassrules: Union[Unset, "IPSecBypassRules"] = UNSET
    pkcs11support: Union[Unset, bool] = UNSET
    enableinterfacesuse: Union[Unset, bool] = UNSET
    unityplugin: Union[Unset, bool] = UNSET
    strictcrlpolicy: Union[Unset, bool] = UNSET
    makebeforebreak: Union[Unset, bool] = UNSET
    ipsecbypass: Union[Unset, bool] = UNSET
    acceptunencryptedmainmode: Union[Unset, bool] = UNSET
    maxexchange: Union[Unset, int] = UNSET
    port_nat_t: Union[Unset, int] = UNSET
    port: Union[Unset, int] = UNSET
    compression: Union[Unset, bool] = UNSET
    noshuntlaninterfaces: Union[Unset, bool] = UNSET
    maxmss: Union[Unset, str] = UNSET
    dns_interval: Union[Unset, int] = UNSET
    ikev2_retransmit_enable: Union[Unset, bool] = UNSET
    ikev2_retransmit_tries: Union[Unset, int] = UNSET
    ikev2_retransmit_timeout: Union[Unset, int] = UNSET
    ikev2_retransmit_base: Union[Unset, int] = UNSET
    ikev2_retransmit_jitter: Union[Unset, int] = UNSET
    ikev2_retransmit_limit: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        logging: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.logging, Unset):
            logging = self.logging.to_dict()

        async_crypto = self.async_crypto

        uniqueids = self.uniqueids

        filtermode = self.filtermode

        bypassrules: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bypassrules, Unset):
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

        dns_interval = self.dns_interval

        ikev2_retransmit_enable = self.ikev2_retransmit_enable

        ikev2_retransmit_tries = self.ikev2_retransmit_tries

        ikev2_retransmit_timeout = self.ikev2_retransmit_timeout

        ikev2_retransmit_base = self.ikev2_retransmit_base

        ikev2_retransmit_jitter = self.ikev2_retransmit_jitter

        ikev2_retransmit_limit = self.ikev2_retransmit_limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logging is not UNSET:
            field_dict["logging"] = logging
        if async_crypto is not UNSET:
            field_dict["async_crypto"] = async_crypto
        if uniqueids is not UNSET:
            field_dict["uniqueids"] = uniqueids
        if filtermode is not UNSET:
            field_dict["filtermode"] = filtermode
        if bypassrules is not UNSET:
            field_dict["bypassrules"] = bypassrules
        if pkcs11support is not UNSET:
            field_dict["pkcs11support"] = pkcs11support
        if enableinterfacesuse is not UNSET:
            field_dict["enableinterfacesuse"] = enableinterfacesuse
        if unityplugin is not UNSET:
            field_dict["unityplugin"] = unityplugin
        if strictcrlpolicy is not UNSET:
            field_dict["strictcrlpolicy"] = strictcrlpolicy
        if makebeforebreak is not UNSET:
            field_dict["makebeforebreak"] = makebeforebreak
        if ipsecbypass is not UNSET:
            field_dict["ipsecbypass"] = ipsecbypass
        if acceptunencryptedmainmode is not UNSET:
            field_dict["acceptunencryptedmainmode"] = acceptunencryptedmainmode
        if maxexchange is not UNSET:
            field_dict["maxexchange"] = maxexchange
        if port_nat_t is not UNSET:
            field_dict["port_nat_t"] = port_nat_t
        if port is not UNSET:
            field_dict["port"] = port
        if compression is not UNSET:
            field_dict["compression"] = compression
        if noshuntlaninterfaces is not UNSET:
            field_dict["noshuntlaninterfaces"] = noshuntlaninterfaces
        if maxmss is not UNSET:
            field_dict["maxmss"] = maxmss
        if dns_interval is not UNSET:
            field_dict["dns_interval"] = dns_interval
        if ikev2_retransmit_enable is not UNSET:
            field_dict["ikev2_retransmit_enable"] = ikev2_retransmit_enable
        if ikev2_retransmit_tries is not UNSET:
            field_dict["ikev2_retransmit_tries"] = ikev2_retransmit_tries
        if ikev2_retransmit_timeout is not UNSET:
            field_dict["ikev2_retransmit_timeout"] = ikev2_retransmit_timeout
        if ikev2_retransmit_base is not UNSET:
            field_dict["ikev2_retransmit_base"] = ikev2_retransmit_base
        if ikev2_retransmit_jitter is not UNSET:
            field_dict["ikev2_retransmit_jitter"] = ikev2_retransmit_jitter
        if ikev2_retransmit_limit is not UNSET:
            field_dict["ikev2_retransmit_limit"] = ikev2_retransmit_limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ip_sec_bypass_rules import IPSecBypassRules
        from ..models.ip_sec_logging import IPSecLogging

        d = src_dict.copy()
        _logging = d.pop("logging", UNSET)
        logging: Union[Unset, IPSecLogging]
        if isinstance(_logging, Unset):
            logging = UNSET
        else:
            logging = IPSecLogging.from_dict(_logging)

        async_crypto = d.pop("async_crypto", UNSET)

        uniqueids = d.pop("uniqueids", UNSET)

        filtermode = d.pop("filtermode", UNSET)

        _bypassrules = d.pop("bypassrules", UNSET)
        bypassrules: Union[Unset, IPSecBypassRules]
        if isinstance(_bypassrules, Unset):
            bypassrules = UNSET
        else:
            bypassrules = IPSecBypassRules.from_dict(_bypassrules)

        pkcs11support = d.pop("pkcs11support", UNSET)

        enableinterfacesuse = d.pop("enableinterfacesuse", UNSET)

        unityplugin = d.pop("unityplugin", UNSET)

        strictcrlpolicy = d.pop("strictcrlpolicy", UNSET)

        makebeforebreak = d.pop("makebeforebreak", UNSET)

        ipsecbypass = d.pop("ipsecbypass", UNSET)

        acceptunencryptedmainmode = d.pop("acceptunencryptedmainmode", UNSET)

        maxexchange = d.pop("maxexchange", UNSET)

        port_nat_t = d.pop("port_nat_t", UNSET)

        port = d.pop("port", UNSET)

        compression = d.pop("compression", UNSET)

        noshuntlaninterfaces = d.pop("noshuntlaninterfaces", UNSET)

        maxmss = d.pop("maxmss", UNSET)

        dns_interval = d.pop("dns_interval", UNSET)

        ikev2_retransmit_enable = d.pop("ikev2_retransmit_enable", UNSET)

        ikev2_retransmit_tries = d.pop("ikev2_retransmit_tries", UNSET)

        ikev2_retransmit_timeout = d.pop("ikev2_retransmit_timeout", UNSET)

        ikev2_retransmit_base = d.pop("ikev2_retransmit_base", UNSET)

        ikev2_retransmit_jitter = d.pop("ikev2_retransmit_jitter", UNSET)

        ikev2_retransmit_limit = d.pop("ikev2_retransmit_limit", UNSET)

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
            dns_interval=dns_interval,
            ikev2_retransmit_enable=ikev2_retransmit_enable,
            ikev2_retransmit_tries=ikev2_retransmit_tries,
            ikev2_retransmit_timeout=ikev2_retransmit_timeout,
            ikev2_retransmit_base=ikev2_retransmit_base,
            ikev2_retransmit_jitter=ikev2_retransmit_jitter,
            ikev2_retransmit_limit=ikev2_retransmit_limit,
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
