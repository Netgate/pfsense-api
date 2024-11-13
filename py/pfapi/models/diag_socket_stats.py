from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.os_socket_list import OsSocketList


T = TypeVar("T", bound="DiagSocketStats")


@_attrs_define
class DiagSocketStats:
    """
    Attributes:
        sockets (Union[Unset, OsSocketList]):
    """

    sockets: Union[Unset, "OsSocketList"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sockets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sockets, Unset):
            sockets = self.sockets.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sockets is not UNSET:
            field_dict["sockets"] = sockets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.os_socket_list import OsSocketList

        d = src_dict.copy()
        _sockets = d.pop("sockets", UNSET)
        sockets: Union[Unset, OsSocketList]
        if isinstance(_sockets, Unset):
            sockets = UNSET
        else:
            sockets = OsSocketList.from_dict(_sockets)

        diag_socket_stats = cls(
            sockets=sockets,
        )

        diag_socket_stats.additional_properties = d
        return diag_socket_stats

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
