from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_forwarder_config import DNSForwarderConfig


T = TypeVar("T", bound="DNSForwarderConfigInfo")


@_attrs_define
class DNSForwarderConfigInfo:
    """
    Attributes:
        config (Union[Unset, DNSForwarderConfig]):
        interfaces (Union[Unset, List[str]]):
    """

    config: Union[Unset, "DNSForwarderConfig"] = UNSET
    interfaces: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        interfaces: Union[Unset, List[str]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dns_forwarder_config import DNSForwarderConfig

        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, DNSForwarderConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = DNSForwarderConfig.from_dict(_config)

        interfaces = cast(List[str], d.pop("interfaces", UNSET))

        dns_forwarder_config_info = cls(
            config=config,
            interfaces=interfaces,
        )

        dns_forwarder_config_info.additional_properties = d
        return dns_forwarder_config_info

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
