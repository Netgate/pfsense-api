from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_resolver_config import DNSResolverConfig
    from ..models.service_certificate import ServiceCertificate


T = TypeVar("T", bound="DNSResolverConfigInfo")


@_attrs_define
class DNSResolverConfigInfo:
    """
    Attributes:
        config (Union[Unset, DNSResolverConfig]):
        interfaces (Union[Unset, List[str]]):
        certs (Union[Unset, List['ServiceCertificate']]):
        scripts (Union[Unset, List[str]]):
    """

    config: Union[Unset, "DNSResolverConfig"] = UNSET
    interfaces: Union[Unset, List[str]] = UNSET
    certs: Union[Unset, List["ServiceCertificate"]] = UNSET
    scripts: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        interfaces: Union[Unset, List[str]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        certs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.certs, Unset):
            certs = []
            for certs_item_data in self.certs:
                certs_item = certs_item_data.to_dict()
                certs.append(certs_item)

        scripts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.scripts, Unset):
            scripts = self.scripts

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if certs is not UNSET:
            field_dict["certs"] = certs
        if scripts is not UNSET:
            field_dict["scripts"] = scripts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dns_resolver_config import DNSResolverConfig
        from ..models.service_certificate import ServiceCertificate

        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, DNSResolverConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = DNSResolverConfig.from_dict(_config)

        interfaces = cast(List[str], d.pop("interfaces", UNSET))

        certs = []
        _certs = d.pop("certs", UNSET)
        for certs_item_data in _certs or []:
            certs_item = ServiceCertificate.from_dict(certs_item_data)

            certs.append(certs_item)

        scripts = cast(List[str], d.pop("scripts", UNSET))

        dns_resolver_config_info = cls(
            config=config,
            interfaces=interfaces,
            certs=certs,
            scripts=scripts,
        )

        dns_resolver_config_info.additional_properties = d
        return dns_resolver_config_info

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
