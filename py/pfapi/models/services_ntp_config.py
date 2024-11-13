from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ntp_acls import NtpAcls
    from ..models.ntp_pps import NtpPps
    from ..models.ntp_serial_gps import NtpSerialGps
    from ..models.ntp_settings import NtpSettings


T = TypeVar("T", bound="ServicesNtpConfig")


@_attrs_define
class ServicesNtpConfig:
    """
    Attributes:
        settings (Union[Unset, NtpSettings]):
        acls (Union[Unset, NtpAcls]):
        serial_gps (Union[Unset, NtpSerialGps]):
        pps (Union[Unset, NtpPps]):
    """

    settings: Union[Unset, "NtpSettings"] = UNSET
    acls: Union[Unset, "NtpAcls"] = UNSET
    serial_gps: Union[Unset, "NtpSerialGps"] = UNSET
    pps: Union[Unset, "NtpPps"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        acls: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.acls, Unset):
            acls = self.acls.to_dict()

        serial_gps: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.serial_gps, Unset):
            serial_gps = self.serial_gps.to_dict()

        pps: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pps, Unset):
            pps = self.pps.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if settings is not UNSET:
            field_dict["settings"] = settings
        if acls is not UNSET:
            field_dict["acls"] = acls
        if serial_gps is not UNSET:
            field_dict["serial_gps"] = serial_gps
        if pps is not UNSET:
            field_dict["pps"] = pps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ntp_acls import NtpAcls
        from ..models.ntp_pps import NtpPps
        from ..models.ntp_serial_gps import NtpSerialGps
        from ..models.ntp_settings import NtpSettings

        d = src_dict.copy()
        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, NtpSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = NtpSettings.from_dict(_settings)

        _acls = d.pop("acls", UNSET)
        acls: Union[Unset, NtpAcls]
        if isinstance(_acls, Unset):
            acls = UNSET
        else:
            acls = NtpAcls.from_dict(_acls)

        _serial_gps = d.pop("serial_gps", UNSET)
        serial_gps: Union[Unset, NtpSerialGps]
        if isinstance(_serial_gps, Unset):
            serial_gps = UNSET
        else:
            serial_gps = NtpSerialGps.from_dict(_serial_gps)

        _pps = d.pop("pps", UNSET)
        pps: Union[Unset, NtpPps]
        if isinstance(_pps, Unset):
            pps = UNSET
        else:
            pps = NtpPps.from_dict(_pps)

        services_ntp_config = cls(
            settings=settings,
            acls=acls,
            serial_gps=serial_gps,
            pps=pps,
        )

        services_ntp_config.additional_properties = d
        return services_ntp_config

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
