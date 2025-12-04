from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAddReq")


@_attrs_define
class UserAddReq:
    """
    Attributes:
        username (str):
        uid (int | Unset):
        password (str | Unset):
        full_name (str | Unset):
        groups (list[str] | Unset):
        cert_refids (list[str] | Unset):
        authorized_keys (str | Unset):
        privs (list[str] | Unset):
        scope (str | Unset):
        keep_cmd_history (bool | Unset):
        expiration (int | Unset):
        disabled (bool | Unset):
        ipsec_psk (str | Unset):
    """

    username: str
    uid: int | Unset = UNSET
    password: str | Unset = UNSET
    full_name: str | Unset = UNSET
    groups: list[str] | Unset = UNSET
    cert_refids: list[str] | Unset = UNSET
    authorized_keys: str | Unset = UNSET
    privs: list[str] | Unset = UNSET
    scope: str | Unset = UNSET
    keep_cmd_history: bool | Unset = UNSET
    expiration: int | Unset = UNSET
    disabled: bool | Unset = UNSET
    ipsec_psk: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        uid = self.uid

        password = self.password

        full_name = self.full_name

        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        cert_refids: list[str] | Unset = UNSET
        if not isinstance(self.cert_refids, Unset):
            cert_refids = self.cert_refids

        authorized_keys = self.authorized_keys

        privs: list[str] | Unset = UNSET
        if not isinstance(self.privs, Unset):
            privs = self.privs

        scope = self.scope

        keep_cmd_history = self.keep_cmd_history

        expiration = self.expiration

        disabled = self.disabled

        ipsec_psk = self.ipsec_psk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if password is not UNSET:
            field_dict["password"] = password
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if groups is not UNSET:
            field_dict["groups"] = groups
        if cert_refids is not UNSET:
            field_dict["cert_refids"] = cert_refids
        if authorized_keys is not UNSET:
            field_dict["authorized_keys"] = authorized_keys
        if privs is not UNSET:
            field_dict["privs"] = privs
        if scope is not UNSET:
            field_dict["scope"] = scope
        if keep_cmd_history is not UNSET:
            field_dict["keep_cmd_history"] = keep_cmd_history
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if ipsec_psk is not UNSET:
            field_dict["ipsec_psk"] = ipsec_psk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        uid = d.pop("uid", UNSET)

        password = d.pop("password", UNSET)

        full_name = d.pop("full_name", UNSET)

        groups = cast(list[str], d.pop("groups", UNSET))

        cert_refids = cast(list[str], d.pop("cert_refids", UNSET))

        authorized_keys = d.pop("authorized_keys", UNSET)

        privs = cast(list[str], d.pop("privs", UNSET))

        scope = d.pop("scope", UNSET)

        keep_cmd_history = d.pop("keep_cmd_history", UNSET)

        expiration = d.pop("expiration", UNSET)

        disabled = d.pop("disabled", UNSET)

        ipsec_psk = d.pop("ipsec_psk", UNSET)

        user_add_req = cls(
            username=username,
            uid=uid,
            password=password,
            full_name=full_name,
            groups=groups,
            cert_refids=cert_refids,
            authorized_keys=authorized_keys,
            privs=privs,
            scope=scope,
            keep_cmd_history=keep_cmd_history,
            expiration=expiration,
            disabled=disabled,
            ipsec_psk=ipsec_psk,
        )

        user_add_req.additional_properties = d
        return user_add_req

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
