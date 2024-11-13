from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderPlanSetting")


@_attrs_define
class ProviderPlanSetting:
    """
    Attributes:
        name (Union[Unset, str]):
        apn (Union[Unset, str]):
        username (Union[Unset, str]):
        password (Union[Unset, str]):
        number (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    apn: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        apn = self.apn

        username = self.username

        password = self.password

        number = self.number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if apn is not UNSET:
            field_dict["apn"] = apn
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        apn = d.pop("apn", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        number = d.pop("number", UNSET)

        provider_plan_setting = cls(
            name=name,
            apn=apn,
            username=username,
            password=password,
            number=number,
        )

        provider_plan_setting.additional_properties = d
        return provider_plan_setting

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
