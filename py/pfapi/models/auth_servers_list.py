from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuthServersList")


@_attrs_define
class AuthServersList:
    """
    Attributes:
        svrlist (List[str]):
        authtype (str):
    """

    svrlist: List[str]
    authtype: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        svrlist = self.svrlist

        authtype = self.authtype

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "svrlist": svrlist,
                "authtype": authtype,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        svrlist = cast(List[str], d.pop("svrlist"))

        authtype = d.pop("authtype")

        auth_servers_list = cls(
            svrlist=svrlist,
            authtype=authtype,
        )

        auth_servers_list.additional_properties = d
        return auth_servers_list

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
