from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseFeature")


@_attrs_define
class LicenseFeature:
    """
    Attributes:
        name (Union[Unset, str]):
        value (Union[Unset, str]):
        source (Union[Unset, str]):
        stop (Union[Unset, int]):
    """

    name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    stop: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        value = self.value

        source = self.source

        stop = self.stop

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value
        if source is not UNSET:
            field_dict["source"] = source
        if stop is not UNSET:
            field_dict["stop"] = stop

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        source = d.pop("source", UNSET)

        stop = d.pop("stop", UNSET)

        license_feature = cls(
            name=name,
            value=value,
            source=source,
            stop=stop,
        )

        license_feature.additional_properties = d
        return license_feature

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
