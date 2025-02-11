from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAuthSettingsReq")


@_attrs_define
class UserAuthSettingsReq:
    """
    Attributes:
        authentication_server (str):
        save_and_test (bool):
        session_timeout (Union[Unset, int]):
        password_hash (Union[Unset, str]):
        shell_auth (Union[Unset, bool]):
        auth_refresh_time (Union[Unset, int]):
    """

    authentication_server: str
    save_and_test: bool
    session_timeout: Union[Unset, int] = UNSET
    password_hash: Union[Unset, str] = UNSET
    shell_auth: Union[Unset, bool] = UNSET
    auth_refresh_time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authentication_server = self.authentication_server

        save_and_test = self.save_and_test

        session_timeout = self.session_timeout

        password_hash = self.password_hash

        shell_auth = self.shell_auth

        auth_refresh_time = self.auth_refresh_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authentication_server": authentication_server,
                "save_and_test": save_and_test,
            }
        )
        if session_timeout is not UNSET:
            field_dict["session_timeout"] = session_timeout
        if password_hash is not UNSET:
            field_dict["password_hash"] = password_hash
        if shell_auth is not UNSET:
            field_dict["shell_auth"] = shell_auth
        if auth_refresh_time is not UNSET:
            field_dict["auth_refresh_time"] = auth_refresh_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        authentication_server = d.pop("authentication_server")

        save_and_test = d.pop("save_and_test")

        session_timeout = d.pop("session_timeout", UNSET)

        password_hash = d.pop("password_hash", UNSET)

        shell_auth = d.pop("shell_auth", UNSET)

        auth_refresh_time = d.pop("auth_refresh_time", UNSET)

        user_auth_settings_req = cls(
            authentication_server=authentication_server,
            save_and_test=save_and_test,
            session_timeout=session_timeout,
            password_hash=password_hash,
            shell_auth=shell_auth,
            auth_refresh_time=auth_refresh_time,
        )

        user_auth_settings_req.additional_properties = d
        return user_auth_settings_req

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
