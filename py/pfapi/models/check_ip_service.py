from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckIPService")


@_attrs_define
class CheckIPService:
    """
    Attributes:
        enable (bool):
        name (Union[Unset, str]):
        url (Union[Unset, str]):
        username (Union[Unset, str]):
        password (Union[Unset, str]):
        verifysslpeer (Union[Unset, bool]):
        curl_proxy (Union[Unset, bool]):
        descr (Union[Unset, str]):
    """

    enable: bool
    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    verifysslpeer: Union[Unset, bool] = UNSET
    curl_proxy: Union[Unset, bool] = UNSET
    descr: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        name = self.name

        url = self.url

        username = self.username

        password = self.password

        verifysslpeer = self.verifysslpeer

        curl_proxy = self.curl_proxy

        descr = self.descr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if verifysslpeer is not UNSET:
            field_dict["verifysslpeer"] = verifysslpeer
        if curl_proxy is not UNSET:
            field_dict["curl_proxy"] = curl_proxy
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("enable")

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        verifysslpeer = d.pop("verifysslpeer", UNSET)

        curl_proxy = d.pop("curl_proxy", UNSET)

        descr = d.pop("descr", UNSET)

        check_ip_service = cls(
            enable=enable,
            name=name,
            url=url,
            username=username,
            password=password,
            verifysslpeer=verifysslpeer,
            curl_proxy=curl_proxy,
            descr=descr,
        )

        check_ip_service.additional_properties = d
        return check_ip_service

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
