from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CheckIPService")


@_attrs_define
class CheckIPService:
    """
    Attributes:
        enable (bool):
        name (str):
        url (str):
        username (str):
        password (str):
        verifysslpeer (bool):
        curl_proxy (bool):
        descr (str):
    """

    enable: bool
    name: str
    url: str
    username: str
    password: str
    verifysslpeer: bool
    curl_proxy: bool
    descr: str
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
                "name": name,
                "url": url,
                "username": username,
                "password": password,
                "verifysslpeer": verifysslpeer,
                "curl_proxy": curl_proxy,
                "descr": descr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("enable")

        name = d.pop("name")

        url = d.pop("url")

        username = d.pop("username")

        password = d.pop("password")

        verifysslpeer = d.pop("verifysslpeer")

        curl_proxy = d.pop("curl_proxy")

        descr = d.pop("descr")

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
