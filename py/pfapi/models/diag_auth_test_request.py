from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagAuthTestRequest")


@_attrs_define
class DiagAuthTestRequest:
    """
    Attributes:
        authtype (Union[Unset, str]):
        username (Union[Unset, str]):
        password (Union[Unset, str]):
    """

    authtype: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authtype = self.authtype

        username = self.username

        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authtype is not UNSET:
            field_dict["authtype"] = authtype
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        authtype = d.pop("authtype", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        diag_auth_test_request = cls(
            authtype=authtype,
            username=username,
            password=password,
        )

        diag_auth_test_request.additional_properties = d
        return diag_auth_test_request

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
