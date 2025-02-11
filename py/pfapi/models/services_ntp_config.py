from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
        settings (NtpSettings):
        acls (NtpAcls):
        serial_gps (NtpSerialGps):
        pps (NtpPps):
    """

    settings: "NtpSettings"
    acls: "NtpAcls"
    serial_gps: "NtpSerialGps"
    pps: "NtpPps"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        settings = self.settings.to_dict()

        acls = self.acls.to_dict()

        serial_gps = self.serial_gps.to_dict()

        pps = self.pps.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "settings": settings,
                "acls": acls,
                "serial_gps": serial_gps,
                "pps": pps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ntp_acls import NtpAcls
        from ..models.ntp_pps import NtpPps
        from ..models.ntp_serial_gps import NtpSerialGps
        from ..models.ntp_settings import NtpSettings

        d = src_dict.copy()
        settings = NtpSettings.from_dict(d.pop("settings"))

        acls = NtpAcls.from_dict(d.pop("acls"))

        serial_gps = NtpSerialGps.from_dict(d.pop("serial_gps"))

        pps = NtpPps.from_dict(d.pop("pps"))

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
