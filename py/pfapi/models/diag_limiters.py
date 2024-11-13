from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.limiter_info import LimiterInfo


T = TypeVar("T", bound="DiagLimiters")


@_attrs_define
class DiagLimiters:
    """
    Attributes:
        limiters (Union[Unset, LimiterInfo]):
    """

    limiters: Union[Unset, "LimiterInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        limiters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.limiters, Unset):
            limiters = self.limiters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limiters is not UNSET:
            field_dict["limiters"] = limiters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.limiter_info import LimiterInfo

        d = src_dict.copy()
        _limiters = d.pop("limiters", UNSET)
        limiters: Union[Unset, LimiterInfo]
        if isinstance(_limiters, Unset):
            limiters = UNSET
        else:
            limiters = LimiterInfo.from_dict(_limiters)

        diag_limiters = cls(
            limiters=limiters,
        )

        diag_limiters.additional_properties = d
        return diag_limiters

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
