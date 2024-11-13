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
        config (Union[Unset, CaptivePortalConfig]):
        interfaces (Union[Unset, List[str]]):
        certificates (Union[Unset, List['ServiceCertificate']]):
        vouch (Union[Unset, Voucher]):
    """

    config: Union[Unset, "CaptivePortalConfig"] = UNSET
    interfaces: Union[Unset, List[str]] = UNSET
    certificates: Union[Unset, List["ServiceCertificate"]] = UNSET
    vouch: Union[Unset, "Voucher"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        interfaces: Union[Unset, List[str]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        certificates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.certificates, Unset):
            certificates = []
            for certificates_item_data in self.certificates:
                certificates_item = certificates_item_data.to_dict()
                certificates.append(certificates_item)

        vouch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vouch, Unset):
            vouch = self.vouch.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if certificates is not UNSET:
            field_dict["certificates"] = certificates
        if vouch is not UNSET:
            field_dict["vouch"] = vouch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.captive_portal_config import CaptivePortalConfig
        from ..models.service_certificate import ServiceCertificate
        from ..models.voucher import Voucher

        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, CaptivePortalConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = CaptivePortalConfig.from_dict(_config)

        interfaces = cast(List[str], d.pop("interfaces", UNSET))

        certificates = []
        _certificates = d.pop("certificates", UNSET)
        for certificates_item_data in _certificates or []:
            certificates_item = ServiceCertificate.from_dict(certificates_item_data)

            certificates.append(certificates_item)

        _vouch = d.pop("vouch", UNSET)
        vouch: Union[Unset, Voucher]
        if isinstance(_vouch, Unset):
            vouch = UNSET
        else:
            vouch = Voucher.from_dict(_vouch)

        captive_portal_info = cls(
            config=config,
            interfaces=interfaces,
            certificates=certificates,
            vouch=vouch,
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
