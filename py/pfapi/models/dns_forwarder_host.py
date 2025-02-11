from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_forwarder_alias import DNSForwarderAlias


T = TypeVar("T", bound="DNSForwarderHost")


@_attrs_define
class DNSForwarderHost:
    """
    Attributes:
        host (str):
        domain (str):
        ip (str):
        descr (str):
        aliases (Union[Unset, List['DNSForwarderAlias']]):
    """

    host: str
    domain: str
    ip: str
    descr: str
    aliases: Union[Unset, List["DNSForwarderAlias"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host

        domain = self.domain

        ip = self.ip

        descr = self.descr

        aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()
                aliases.append(aliases_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "domain": domain,
                "ip": ip,
                "descr": descr,
            }
        )
        if aliases is not UNSET:
            field_dict["aliases"] = aliases

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dns_forwarder_alias import DNSForwarderAlias

        d = src_dict.copy()
        host = d.pop("host")

        domain = d.pop("domain")

        ip = d.pop("ip")

        descr = d.pop("descr")

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = DNSForwarderAlias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        dns_forwarder_host = cls(
            host=host,
            domain=domain,
            ip=ip,
            descr=descr,
            aliases=aliases,
        )

        dns_forwarder_host.additional_properties = d
        return dns_forwarder_host

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
