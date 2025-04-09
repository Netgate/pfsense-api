from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginResponse")


@_attrs_define
class LoginResponse:
    """
    Attributes:
        token (Union[Unset, str]):
        user (Union[Unset, str]):
        version (Union[Unset, str]):
        alerts (Union[Unset, List[str]]):
    """

    token: Union[Unset, str] = UNSET
    user: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    alerts: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token

        user = self.user

        version = self.version

        alerts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = self.alerts

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if user is not UNSET:
            field_dict["user"] = user
        if version is not UNSET:
            field_dict["version"] = version
        if alerts is not UNSET:
            field_dict["alerts"] = alerts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        user = d.pop("user", UNSET)

        version = d.pop("version", UNSET)

        alerts = cast(List[str], d.pop("alerts", UNSET))

        login_response = cls(
            token=token,
            user=user,
            version=version,
            alerts=alerts,
        )

        login_response.additional_properties = d
        return login_response

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
