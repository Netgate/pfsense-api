from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acb_config import ACBConfig


T = TypeVar("T", bound="ACBConfigInfo")


@_attrs_define
class ACBConfigInfo:
    """
    Attributes:
        config (Union[Unset, ACBConfig]): valid values:
            frequency = "cron", "every"
            reverse = "yes", "no"
        userkey (Union[Unset, str]):
    """

    config: Union[Unset, "ACBConfig"] = UNSET
    userkey: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        userkey = self.userkey

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if userkey is not UNSET:
            field_dict["userkey"] = userkey

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acb_config import ACBConfig

        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, ACBConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ACBConfig.from_dict(_config)

        userkey = d.pop("userkey", UNSET)

        acb_config_info = cls(
            config=config,
            userkey=userkey,
        )

        acb_config_info.additional_properties = d
        return acb_config_info

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
