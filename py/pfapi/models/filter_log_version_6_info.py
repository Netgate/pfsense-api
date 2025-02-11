from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FilterLogVersion6Info")


@_attrs_define
class FilterLogVersion6Info:
    """
    Attributes:
        class_ (str):
        flow_label (str):
        hlim (str):
    """

    class_: str
    flow_label: str
    hlim: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        class_ = self.class_

        flow_label = self.flow_label

        hlim = self.hlim

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "class": class_,
                "flow_label": flow_label,
                "hlim": hlim,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        class_ = d.pop("class")

        flow_label = d.pop("flow_label")

        hlim = d.pop("hlim")

        filter_log_version_6_info = cls(
            class_=class_,
            flow_label=flow_label,
            hlim=hlim,
        )

        filter_log_version_6_info.additional_properties = d
        return filter_log_version_6_info

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
