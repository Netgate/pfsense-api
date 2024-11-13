from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controller_service_config import ControllerServiceConfig


T = TypeVar("T", bound="ControllerService")


@_attrs_define
class ControllerService:
    """
    Attributes:
        listening (Union[Unset, List[str]]):
        config (Union[Unset, ControllerServiceConfig]):
        license_ (Union[Unset, str]):
    """

    listening: Union[Unset, List[str]] = UNSET
    config: Union[Unset, "ControllerServiceConfig"] = UNSET
    license_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        listening: Union[Unset, List[str]] = UNSET
        if not isinstance(self.listening, Unset):
            listening = self.listening

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        license_ = self.license_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if listening is not UNSET:
            field_dict["listening"] = listening
        if config is not UNSET:
            field_dict["config"] = config
        if license_ is not UNSET:
            field_dict["license"] = license_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controller_service_config import ControllerServiceConfig

        d = src_dict.copy()
        listening = cast(List[str], d.pop("listening", UNSET))

        _config = d.pop("config", UNSET)
        config: Union[Unset, ControllerServiceConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ControllerServiceConfig.from_dict(_config)

        license_ = d.pop("license", UNSET)

        controller_service = cls(
            listening=listening,
            config=config,
            license_=license_,
        )

        controller_service.additional_properties = d
        return controller_service

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
