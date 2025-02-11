from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserGeneric")


@_attrs_define
class UserGeneric:
    """
    Attributes:
        username (str):
        descr (str):
        scope (str):
        groupname (str):
        disabled (bool):
        uid (int):
        full_name (str):
        authorized_keys (str):
        keep_cmd_history (bool):
        name (Union[Unset, str]):
        groups (Union[Unset, List[str]]):
        cert_refids (Union[Unset, List[str]]):
        privs (Union[Unset, List[str]]):
        expiration (Union[Unset, int]):
    """

    username: str
    descr: str
    scope: str
    groupname: str
    disabled: bool
    uid: int
    full_name: str
    authorized_keys: str
    keep_cmd_history: bool
    name: Union[Unset, str] = UNSET
    groups: Union[Unset, List[str]] = UNSET
    cert_refids: Union[Unset, List[str]] = UNSET
    privs: Union[Unset, List[str]] = UNSET
    expiration: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username

        descr = self.descr

        scope = self.scope

        groupname = self.groupname

        disabled = self.disabled

        uid = self.uid

        full_name = self.full_name

        authorized_keys = self.authorized_keys

        keep_cmd_history = self.keep_cmd_history

        name = self.name

        groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        cert_refids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cert_refids, Unset):
            cert_refids = self.cert_refids

        privs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.privs, Unset):
            privs = self.privs

        expiration = self.expiration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "descr": descr,
                "scope": scope,
                "groupname": groupname,
                "disabled": disabled,
                "uid": uid,
                "full_name": full_name,
                "authorized_keys": authorized_keys,
                "keep_cmd_history": keep_cmd_history,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if groups is not UNSET:
            field_dict["groups"] = groups
        if cert_refids is not UNSET:
            field_dict["cert_refids"] = cert_refids
        if privs is not UNSET:
            field_dict["privs"] = privs
        if expiration is not UNSET:
            field_dict["expiration"] = expiration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username")

        descr = d.pop("descr")

        scope = d.pop("scope")

        groupname = d.pop("groupname")

        disabled = d.pop("disabled")

        uid = d.pop("uid")

        full_name = d.pop("full_name")

        authorized_keys = d.pop("authorized_keys")

        keep_cmd_history = d.pop("keep_cmd_history")

        name = d.pop("name", UNSET)

        groups = cast(List[str], d.pop("groups", UNSET))

        cert_refids = cast(List[str], d.pop("cert_refids", UNSET))

        privs = cast(List[str], d.pop("privs", UNSET))

        expiration = d.pop("expiration", UNSET)

        user_generic = cls(
            username=username,
            descr=descr,
            scope=scope,
            groupname=groupname,
            disabled=disabled,
            uid=uid,
            full_name=full_name,
            authorized_keys=authorized_keys,
            keep_cmd_history=keep_cmd_history,
            name=name,
            groups=groups,
            cert_refids=cert_refids,
            privs=privs,
            expiration=expiration,
        )

        user_generic.additional_properties = d
        return user_generic

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
