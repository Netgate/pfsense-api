from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagAuthTestResult")


@_attrs_define
class DiagAuthTestResult:
    """
    Attributes:
        authtype (Union[Unset, str]):
        groups (Union[Unset, List[str]]):
        authenticated (Union[Unset, bool]):
    """

    authtype: Union[Unset, str] = UNSET
    groups: Union[Unset, List[str]] = UNSET
    authenticated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authtype = self.authtype

        groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        authenticated = self.authenticated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authtype is not UNSET:
            field_dict["authtype"] = authtype
        if groups is not UNSET:
            field_dict["groups"] = groups
        if authenticated is not UNSET:
            field_dict["authenticated"] = authenticated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        authtype = d.pop("authtype", UNSET)

        groups = cast(List[str], d.pop("groups", UNSET))

        authenticated = d.pop("authenticated", UNSET)

        diag_auth_test_result = cls(
            authtype=authtype,
            groups=groups,
            authenticated=authenticated,
        )

        diag_auth_test_result.additional_properties = d
        return diag_auth_test_result

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
