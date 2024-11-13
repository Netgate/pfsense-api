from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CARPResetDemotionResult")


@_attrs_define
class CARPResetDemotionResult:
    """
    Attributes:
        carp_detected_problems (Union[Unset, int]):
    """

    carp_detected_problems: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        carp_detected_problems = self.carp_detected_problems

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carp_detected_problems is not UNSET:
            field_dict["carp_detected_problems"] = carp_detected_problems

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        carp_detected_problems = d.pop("carp_detected_problems", UNSET)

        carp_reset_demotion_result = cls(
            carp_detected_problems=carp_detected_problems,
        )

        carp_reset_demotion_result.additional_properties = d
        return carp_reset_demotion_result

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
