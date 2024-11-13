from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wire_guard_tunnel_status import WireGuardTunnelStatus


T = TypeVar("T", bound="WireGuardStatus")


@_attrs_define
class WireGuardStatus:
    """
    Attributes:
        status (Union[Unset, List['WireGuardTunnelStatus']]):
    """

    status: Union[Unset, List["WireGuardTunnelStatus"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.status, Unset):
            status = []
            for status_item_data in self.status:
                status_item = status_item_data.to_dict()
                status.append(status_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wire_guard_tunnel_status import WireGuardTunnelStatus

        d = src_dict.copy()
        status = []
        _status = d.pop("status", UNSET)
        for status_item_data in _status or []:
            status_item = WireGuardTunnelStatus.from_dict(status_item_data)

            status.append(status_item)

        wire_guard_status = cls(
            status=status,
        )

        wire_guard_status.additional_properties = d
        return wire_guard_status

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
