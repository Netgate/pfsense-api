from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAuthSettings")


@_attrs_define
class UserAuthSettings:
    """
    Attributes:
        session_timeout (Union[Unset, str]): session timeout in minutes, empty string is default 240
        authentication_server (Union[Unset, str]): current value
        authentication_servers (Union[Unset, List[str]]):
        password_hash (Union[Unset, str]): current value
        password_hashes (Union[Unset, List[str]]):
        shell_auth (Union[Unset, bool]): user is able to access shell
        auth_refresh_time (Union[Unset, str]): duration to cache authentication results from remote auth servers in
            seconds, empty string is default 30, max 3600
    """

    session_timeout: Union[Unset, str] = UNSET
    authentication_server: Union[Unset, str] = UNSET
    authentication_servers: Union[Unset, List[str]] = UNSET
    password_hash: Union[Unset, str] = UNSET
    password_hashes: Union[Unset, List[str]] = UNSET
    shell_auth: Union[Unset, bool] = UNSET
    auth_refresh_time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        session_timeout = self.session_timeout

        authentication_server = self.authentication_server

        authentication_servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authentication_servers, Unset):
            authentication_servers = self.authentication_servers

        password_hash = self.password_hash

        password_hashes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.password_hashes, Unset):
            password_hashes = self.password_hashes

        shell_auth = self.shell_auth

        auth_refresh_time = self.auth_refresh_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_timeout is not UNSET:
            field_dict["session_timeout"] = session_timeout
        if authentication_server is not UNSET:
            field_dict["authentication_server"] = authentication_server
        if authentication_servers is not UNSET:
            field_dict["authentication_servers"] = authentication_servers
        if password_hash is not UNSET:
            field_dict["password_hash"] = password_hash
        if password_hashes is not UNSET:
            field_dict["password_hashes"] = password_hashes
        if shell_auth is not UNSET:
            field_dict["shell_auth"] = shell_auth
        if auth_refresh_time is not UNSET:
            field_dict["auth_refresh_time"] = auth_refresh_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        session_timeout = d.pop("session_timeout", UNSET)

        authentication_server = d.pop("authentication_server", UNSET)

        authentication_servers = cast(List[str], d.pop("authentication_servers", UNSET))

        password_hash = d.pop("password_hash", UNSET)

        password_hashes = cast(List[str], d.pop("password_hashes", UNSET))

        shell_auth = d.pop("shell_auth", UNSET)

        auth_refresh_time = d.pop("auth_refresh_time", UNSET)

        user_auth_settings = cls(
            session_timeout=session_timeout,
            authentication_server=authentication_server,
            authentication_servers=authentication_servers,
            password_hash=password_hash,
            password_hashes=password_hashes,
            shell_auth=shell_auth,
            auth_refresh_time=auth_refresh_time,
        )

        user_auth_settings.additional_properties = d
        return user_auth_settings

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
