from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snmp_config import SNMPConfig


T = TypeVar("T", bound="ServicesSNMPConfigReq")


@_attrs_define
class ServicesSNMPConfigReq:
    """
    Attributes:
        config (Union[Unset, SNMPConfig]):
    """

    config: Union[Unset, "SNMPConfig"] = UNSET
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
        from ..models.snmp_config import SNMPConfig

        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, SNMPConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = SNMPConfig.from_dict(_config)

        services_snmp_config_req = cls(
            config=config,
        )

        services_snmp_config_req.additional_properties = d
        return services_snmp_config_req

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
