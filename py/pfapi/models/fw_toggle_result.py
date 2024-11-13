from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.toggle_resp_status import ToggleRespStatus


T = TypeVar("T", bound="FWToggleResult")


@_attrs_define
class FWToggleResult:
    """
    Attributes:
        status (Union[Unset, ToggleRespStatus]):
    """

    status: Union[Unset, "ToggleRespStatus"] = UNSET
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
        from ..models.toggle_resp_status import ToggleRespStatus

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, ToggleRespStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ToggleRespStatus.from_dict(_status)

        fw_toggle_result = cls(
            status=status,
        )

        fw_toggle_result.additional_properties = d
        return fw_toggle_result

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
