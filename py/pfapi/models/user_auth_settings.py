from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAuthSettings")


@_attrs_define
class UserAuthSettings:
    """
    Attributes:
        session_timeout (int): session timeout in minutes
        authentication_server (str): current value
        password_hash (str): current value
        shell_auth (bool): user is able to access shell
        auth_refresh_time (int): duration to cache authentication results from remote auth servers in seconds
        authentication_servers (Union[Unset, List[str]]):
        password_hashes (Union[Unset, List[str]]):
    """

    session_timeout: int
    authentication_server: str
    password_hash: str
    shell_auth: bool
    auth_refresh_time: int
    authentication_servers: Union[Unset, List[str]] = UNSET
    password_hashes: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        session_timeout = self.session_timeout

        authentication_server = self.authentication_server

        password_hash = self.password_hash

        shell_auth = self.shell_auth

        auth_refresh_time = self.auth_refresh_time

        authentication_servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authentication_servers, Unset):
            authentication_servers = self.authentication_servers

        password_hashes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.password_hashes, Unset):
            password_hashes = self.password_hashes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_timeout": session_timeout,
                "authentication_server": authentication_server,
                "password_hash": password_hash,
                "shell_auth": shell_auth,
                "auth_refresh_time": auth_refresh_time,
            }
        )
        if authentication_servers is not UNSET:
            field_dict["authentication_servers"] = authentication_servers
        if password_hashes is not UNSET:
            field_dict["password_hashes"] = password_hashes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        session_timeout = d.pop("session_timeout")

        authentication_server = d.pop("authentication_server")

        password_hash = d.pop("password_hash")

        shell_auth = d.pop("shell_auth")

        auth_refresh_time = d.pop("auth_refresh_time")

        authentication_servers = cast(List[str], d.pop("authentication_servers", UNSET))

        password_hashes = cast(List[str], d.pop("password_hashes", UNSET))

        user_auth_settings = cls(
            session_timeout=session_timeout,
            authentication_server=authentication_server,
            password_hash=password_hash,
            shell_auth=shell_auth,
            auth_refresh_time=auth_refresh_time,
            authentication_servers=authentication_servers,
            password_hashes=password_hashes,
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
