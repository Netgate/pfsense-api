from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaptivePortalDisconnectRequest")


@_attrs_define
class CaptivePortalDisconnectRequest:
    """
    Attributes:
        all_ (Union[Unset, bool]):
        session_id (Union[Unset, str]):
    """

    all_: Union[Unset, bool] = UNSET
    session_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        all_ = self.all_

        session_id = self.session_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if session_id is not UNSET:
            field_dict["session_id"] = session_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        all_ = d.pop("all", UNSET)

        session_id = d.pop("session_id", UNSET)

        captive_portal_disconnect_request = cls(
            all_=all_,
            session_id=session_id,
        )

        captive_portal_disconnect_request.additional_properties = d
        return captive_portal_disconnect_request

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