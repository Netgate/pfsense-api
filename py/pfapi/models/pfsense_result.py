from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PfsenseResult")


@_attrs_define
class PfsenseResult:
    """
    Attributes:
        msg (str):
        alrt (Union[Unset, bool]):
        sb (Union[Unset, bool]):
        alrtoln (Union[Unset, bool]):
        alrtclr (Union[Unset, str]):
        auth (Union[Unset, bool]):
        status (Union[Unset, str]):
        message (Union[Unset, str]):
    """

    msg: str
    alrt: Union[Unset, bool] = UNSET
    sb: Union[Unset, bool] = UNSET
    alrtoln: Union[Unset, bool] = UNSET
    alrtclr: Union[Unset, str] = UNSET
    auth: Union[Unset, bool] = UNSET
    status: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        msg = self.msg

        alrt = self.alrt

        sb = self.sb

        alrtoln = self.alrtoln

        alrtclr = self.alrtclr

        auth = self.auth

        status = self.status

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "msg": msg,
            }
        )
        if alrt is not UNSET:
            field_dict["alrt"] = alrt
        if sb is not UNSET:
            field_dict["sb"] = sb
        if alrtoln is not UNSET:
            field_dict["alrtoln"] = alrtoln
        if alrtclr is not UNSET:
            field_dict["alrtclr"] = alrtclr
        if auth is not UNSET:
            field_dict["auth"] = auth
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        msg = d.pop("msg")

        alrt = d.pop("alrt", UNSET)

        sb = d.pop("sb", UNSET)

        alrtoln = d.pop("alrtoln", UNSET)

        alrtclr = d.pop("alrtclr", UNSET)

        auth = d.pop("auth", UNSET)

        status = d.pop("status", UNSET)

        message = d.pop("message", UNSET)

        pfsense_result = cls(
            msg=msg,
            alrt=alrt,
            sb=sb,
            alrtoln=alrtoln,
            alrtclr=alrtclr,
            auth=auth,
            status=status,
            message=message,
        )

        pfsense_result.additional_properties = d
        return pfsense_result

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
