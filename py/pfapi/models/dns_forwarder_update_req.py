from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_forwarder_config import DNSForwarderConfig


T = TypeVar("T", bound="DNSForwarderUpdateReq")


@_attrs_define
class DNSForwarderUpdateReq:
    """
    Attributes:
        config (Union[Unset, DNSForwarderConfig]):
    """

    config: Union[Unset, "DNSForwarderConfig"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config

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

        dns_forwarder_update_req = cls(
            config=config,
        )

        dns_forwarder_update_req.additional_properties = d
        return dns_forwarder_update_req

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
