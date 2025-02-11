from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.fw_schedule_range import FWScheduleRange


T = TypeVar("T", bound="FWSchedule")


@_attrs_define
class FWSchedule:
    """
    Attributes:
        id (str):
        name (str):
        descr (str):
        timerange (List['FWScheduleRange']):
        schedlabel (str):
    """

    id: str
    name: str
    descr: str
    timerange: List["FWScheduleRange"]
    schedlabel: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        descr = self.descr

        timerange = []
        for timerange_item_data in self.timerange:
            timerange_item = timerange_item_data.to_dict()
            timerange.append(timerange_item)

        schedlabel = self.schedlabel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "descr": descr,
                "timerange": timerange,
                "schedlabel": schedlabel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_schedule_range import FWScheduleRange

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        descr = d.pop("descr")

        timerange = []
        _timerange = d.pop("timerange")
        for timerange_item_data in _timerange:
            timerange_item = FWScheduleRange.from_dict(timerange_item_data)

            timerange.append(timerange_item)

        schedlabel = d.pop("schedlabel")

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
