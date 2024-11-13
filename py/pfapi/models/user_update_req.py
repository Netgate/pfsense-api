from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserUpdateReq")


@_attrs_define
class UserUpdateReq:
    """
    Attributes:
        password (Union[Unset, str]):
        full_name (Union[Unset, str]):
        groups (Union[Unset, List[str]]):
        cert_refids (Union[Unset, List[str]]):
        authorized_keys (Union[Unset, str]):
        ipsec_psk (Union[Unset, str]):
        privs (Union[Unset, List[str]]):
        keep_cmd_history (Union[Unset, bool]):
        expiration (Union[Unset, int]):
        disabled (Union[Unset, bool]):
    """

    password: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    groups: Union[Unset, List[str]] = UNSET
    cert_refids: Union[Unset, List[str]] = UNSET
    authorized_keys: Union[Unset, str] = UNSET
    ipsec_psk: Union[Unset, str] = UNSET
    privs: Union[Unset, List[str]] = UNSET
    keep_cmd_history: Union[Unset, bool] = UNSET
    expiration: Union[Unset, int] = UNSET
    disabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password

        full_name = self.full_name

        groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        cert_refids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cert_refids, Unset):
            cert_refids = self.cert_refids

        authorized_keys = self.authorized_keys

        ipsec_psk = self.ipsec_psk

        privs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.privs, Unset):
            privs = self.privs

        keep_cmd_history = self.keep_cmd_history

        expiration = self.expiration

        disabled = self.disabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if ipsec_psk is not UNSET:
            field_dict["ipsec_psk"] = ipsec_psk
        if privs is not UNSET:
            field_dict["privs"] = privs
        if keep_cmd_history is not UNSET:
            field_dict["keep_cmd_history"] = keep_cmd_history
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("password", UNSET)

        full_name = d.pop("full_name", UNSET)

        groups = cast(List[str], d.pop("groups", UNSET))

        cert_refids = cast(List[str], d.pop("cert_refids", UNSET))

        authorized_keys = d.pop("authorized_keys", UNSET)

        ipsec_psk = d.pop("ipsec_psk", UNSET)

        privs = cast(List[str], d.pop("privs", UNSET))

        keep_cmd_history = d.pop("keep_cmd_history", UNSET)

        expiration = d.pop("expiration", UNSET)

        disabled = d.pop("disabled", UNSET)

        user_update_req = cls(
            password=password,
            full_name=full_name,
            groups=groups,
            cert_refids=cert_refids,
            authorized_keys=authorized_keys,
            ipsec_psk=ipsec_psk,
            privs=privs,
            keep_cmd_history=keep_cmd_history,
            expiration=expiration,
            disabled=disabled,
        )

        user_update_req.additional_properties = d
        return user_update_req

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
