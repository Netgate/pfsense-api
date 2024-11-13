from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_status import SystemStatus


T = TypeVar("T", bound="StatusSummary")


@_attrs_define
class StatusSummary:
    """
    Attributes:
        status (Union[Unset, SystemStatus]):
    """

    status: Union[Unset, "SystemStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_status import SystemStatus

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, SystemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SystemStatus.from_dict(_status)

        status_summary = cls(
            status=status,
        )

        status_summary.additional_properties = d
        return status_summary

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
