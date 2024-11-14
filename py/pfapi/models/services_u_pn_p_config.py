from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.u_pn_p_config import UPnPConfig


T = TypeVar("T", bound="ServicesUPnPConfig")


@_attrs_define
class ServicesUPnPConfig:
    """
    Attributes:
        config (Union[Unset, UPnPConfig]):
        interfaces (Union[Unset, List[str]]):
    """

    config: Union[Unset, "UPnPConfig"] = UNSET
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
        from ..models.u_pn_p_config import UPnPConfig

        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, UPnPConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = UPnPConfig.from_dict(_config)

        interfaces = cast(List[str], d.pop("interfaces", UNSET))

        services_u_pn_p_config = cls(
            config=config,
            interfaces=interfaces,
        )

        services_u_pn_p_config.additional_properties = d
        return services_u_pn_p_config

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
