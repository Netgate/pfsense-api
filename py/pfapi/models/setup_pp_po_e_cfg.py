from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetupPPPoECfg")


@_attrs_define
class SetupPPPoECfg:
    """
    Attributes:
        service_name (str):
        username (str):
        password (Union[Unset, str]):
        dod (Union[Unset, bool]):
        idletimeout (Union[Unset, str]):
        provider (Union[Unset, str]):
        localip (Union[Unset, str]):
    """

    service_name: str
    username: str
    password: Union[Unset, str] = UNSET
    dod: Union[Unset, bool] = UNSET
    idletimeout: Union[Unset, str] = UNSET
    provider: Union[Unset, str] = UNSET
    localip: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_name = self.service_name

        username = self.username

        password = self.password

        dod = self.dod

        idletimeout = self.idletimeout

        provider = self.provider

        localip = self.localip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "service_name": service_name,
                "username": username,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if dod is not UNSET:
            field_dict["dod"] = dod
        if idletimeout is not UNSET:
            field_dict["idletimeout"] = idletimeout
        if provider is not UNSET:
            field_dict["provider"] = provider
        if localip is not UNSET:
            field_dict["localip"] = localip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service_name = d.pop("service_name")

        username = d.pop("username")

        password = d.pop("password", UNSET)

        dod = d.pop("dod", UNSET)

        idletimeout = d.pop("idletimeout", UNSET)

        provider = d.pop("provider", UNSET)

        localip = d.pop("localip", UNSET)

        setup_pp_po_e_cfg = cls(
            service_name=service_name,
            username=username,
            password=password,
            dod=dod,
            idletimeout=idletimeout,
            provider=provider,
            localip=localip,
        )

        setup_pp_po_e_cfg.additional_properties = d
        return setup_pp_po_e_cfg

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
