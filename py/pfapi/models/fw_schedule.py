from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_schedule_range import FWScheduleRange


T = TypeVar("T", bound="FWSchedule")


@_attrs_define
class FWSchedule:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        descr (str | Unset):
        timerange (list[FWScheduleRange] | Unset):
        schedlabel (str | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    timerange: list[FWScheduleRange] | Unset = UNSET
    schedlabel: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        descr = self.descr

        timerange: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.timerange, Unset):
            timerange = []
            for timerange_item_data in self.timerange:
                timerange_item = timerange_item_data.to_dict()
                timerange.append(timerange_item)

        schedlabel = self.schedlabel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if timerange is not UNSET:
            field_dict["timerange"] = timerange
        if schedlabel is not UNSET:
            field_dict["schedlabel"] = schedlabel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fw_schedule_range import FWScheduleRange

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        _timerange = d.pop("timerange", UNSET)
        timerange: list[FWScheduleRange] | Unset = UNSET
        if _timerange is not UNSET:
            timerange = []
            for timerange_item_data in _timerange:
                timerange_item = FWScheduleRange.from_dict(timerange_item_data)

                timerange.append(timerange_item)

        schedlabel = d.pop("schedlabel", UNSET)

        fw_schedule = cls(
            id=id,
            name=name,
            descr=descr,
            timerange=timerange,
            schedlabel=schedlabel,
        )

        fw_schedule.additional_properties = d
        return fw_schedule

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
