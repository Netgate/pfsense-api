from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
        settings (NtpSettings | Unset):
        acls (NtpAcls | Unset):
        serial_gps (NtpSerialGps | Unset):
        pps (NtpPps | Unset):
    """

    settings: NtpSettings | Unset = UNSET
    acls: NtpAcls | Unset = UNSET
    serial_gps: NtpSerialGps | Unset = UNSET
    pps: NtpPps | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        acls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.acls, Unset):
            acls = self.acls.to_dict()

        serial_gps: dict[str, Any] | Unset = UNSET
        if not isinstance(self.serial_gps, Unset):
            serial_gps = self.serial_gps.to_dict()

        pps: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pps, Unset):
            pps = self.pps.to_dict()

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ntp_acls import NtpAcls
        from ..models.ntp_pps import NtpPps
        from ..models.ntp_serial_gps import NtpSerialGps
        from ..models.ntp_settings import NtpSettings

        d = dict(src_dict)
        _settings = d.pop("settings", UNSET)
        settings: NtpSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = NtpSettings.from_dict(_settings)

        _acls = d.pop("acls", UNSET)
        acls: NtpAcls | Unset
        if isinstance(_acls, Unset):
            acls = UNSET
        else:
            acls = NtpAcls.from_dict(_acls)

        _serial_gps = d.pop("serial_gps", UNSET)
        serial_gps: NtpSerialGps | Unset
        if isinstance(_serial_gps, Unset):
            serial_gps = UNSET
        else:
            serial_gps = NtpSerialGps.from_dict(_serial_gps)

        _pps = d.pop("pps", UNSET)
        pps: NtpPps | Unset
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
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
