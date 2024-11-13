from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FWScheduleRange")


@_attrs_define
class FWScheduleRange:
    """
    Attributes:
        position (Union[Unset, str]):
        month (Union[Unset, str]):
        day (Union[Unset, str]):
        hour (Union[Unset, str]):
        rangedescr (Union[Unset, str]):
    """

    position: Union[Unset, str] = UNSET
    month: Union[Unset, str] = UNSET
    day: Union[Unset, str] = UNSET
    hour: Union[Unset, str] = UNSET
    rangedescr: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position

        month = self.month

        day = self.day

        hour = self.hour

        rangedescr = self.rangedescr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if month is not UNSET:
            field_dict["month"] = month
        if day is not UNSET:
            field_dict["day"] = day
        if hour is not UNSET:
            field_dict["hour"] = hour
        if rangedescr is not UNSET:
            field_dict["rangedescr"] = rangedescr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        position = d.pop("position", UNSET)

        month = d.pop("month", UNSET)

        day = d.pop("day", UNSET)

        hour = d.pop("hour", UNSET)

        rangedescr = d.pop("rangedescr", UNSET)

        fw_schedule_range = cls(
            position=position,
            month=month,
            day=day,
            hour=hour,
            rangedescr=rangedescr,
        )

        fw_schedule_range.additional_properties = d
        return fw_schedule_range

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
