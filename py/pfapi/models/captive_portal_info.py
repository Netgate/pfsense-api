from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.captive_portal_config import CaptivePortalConfig
    from ..models.service_certificate import ServiceCertificate
    from ..models.voucher import Voucher


T = TypeVar("T", bound="CaptivePortalInfo")


@_attrs_define
class CaptivePortalInfo:
    """
    Attributes:
        config (CaptivePortalConfig):
        vouch (Voucher):
        interfaces (Union[Unset, List[str]]):
        certificates (Union[Unset, List['ServiceCertificate']]):
    """

    config: "CaptivePortalConfig"
    vouch: "Voucher"
    interfaces: Union[Unset, List[str]] = UNSET
    certificates: Union[Unset, List["ServiceCertificate"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config = self.config.to_dict()

        vouch = self.vouch.to_dict()

        interfaces: Union[Unset, List[str]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        certificates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.certificates, Unset):
            certificates = []
            for certificates_item_data in self.certificates:
                certificates_item = certificates_item_data.to_dict()
                certificates.append(certificates_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "vouch": vouch,
            }
        )
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if certificates is not UNSET:
            field_dict["certificates"] = certificates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.captive_portal_config import CaptivePortalConfig
        from ..models.service_certificate import ServiceCertificate
        from ..models.voucher import Voucher

        d = src_dict.copy()
        config = CaptivePortalConfig.from_dict(d.pop("config"))

        vouch = Voucher.from_dict(d.pop("vouch"))

        interfaces = cast(List[str], d.pop("interfaces", UNSET))

        certificates = []
        _certificates = d.pop("certificates", UNSET)
        for certificates_item_data in _certificates or []:
            certificates_item = ServiceCertificate.from_dict(certificates_item_data)

            certificates.append(certificates_item)

        captive_portal_info = cls(
            config=config,
            vouch=vouch,
            interfaces=interfaces,
            certificates=certificates,
        )

        captive_portal_info.additional_properties = d
        return captive_portal_info

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
