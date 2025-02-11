from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SyslogConfigOverride")


@_attrs_define
class SyslogConfigOverride:
    """
    Attributes:
        override_reverse (bool):
        reverse (bool):
        override_nentries (bool):
        nentries (int):
        override_logfilesize (bool):
        logfilesize (int):
        override_rotatecount (bool):
        rotatecount (int):
        override_format (bool):
        format_ (str):
        lognginx (bool):
        logdefaultblock (bool):
        logdefaultpass (bool):
        logbogons (bool):
        logprivatenets (bool):
        filterdescriptions (int):
    """

    override_reverse: bool
    reverse: bool
    override_nentries: bool
    nentries: int
    override_logfilesize: bool
    logfilesize: int
    override_rotatecount: bool
    rotatecount: int
    override_format: bool
    format_: str
    lognginx: bool
    logdefaultblock: bool
    logdefaultpass: bool
    logbogons: bool
    logprivatenets: bool
    filterdescriptions: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        override_reverse = self.override_reverse

        reverse = self.reverse

        override_nentries = self.override_nentries

        nentries = self.nentries

        override_logfilesize = self.override_logfilesize

        logfilesize = self.logfilesize

        override_rotatecount = self.override_rotatecount

        rotatecount = self.rotatecount

        override_format = self.override_format

        format_ = self.format_

        lognginx = self.lognginx

        logdefaultblock = self.logdefaultblock

        logdefaultpass = self.logdefaultpass

        logbogons = self.logbogons

        logprivatenets = self.logprivatenets

        filterdescriptions = self.filterdescriptions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "override_reverse": override_reverse,
                "reverse": reverse,
                "override_nentries": override_nentries,
                "nentries": nentries,
                "override_logfilesize": override_logfilesize,
                "logfilesize": logfilesize,
                "override_rotatecount": override_rotatecount,
                "rotatecount": rotatecount,
                "override_format": override_format,
                "format": format_,
                "lognginx": lognginx,
                "logdefaultblock": logdefaultblock,
                "logdefaultpass": logdefaultpass,
                "logbogons": logbogons,
                "logprivatenets": logprivatenets,
                "filterdescriptions": filterdescriptions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        override_reverse = d.pop("override_reverse")

        reverse = d.pop("reverse")

        override_nentries = d.pop("override_nentries")

        nentries = d.pop("nentries")

        override_logfilesize = d.pop("override_logfilesize")

        logfilesize = d.pop("logfilesize")

        override_rotatecount = d.pop("override_rotatecount")

        rotatecount = d.pop("rotatecount")

        override_format = d.pop("override_format")

        format_ = d.pop("format")

        lognginx = d.pop("lognginx")

        logdefaultblock = d.pop("logdefaultblock")

        logdefaultpass = d.pop("logdefaultpass")

        logbogons = d.pop("logbogons")

        logprivatenets = d.pop("logprivatenets")

        filterdescriptions = d.pop("filterdescriptions")

        syslog_config_override = cls(
            override_reverse=override_reverse,
            reverse=reverse,
            override_nentries=override_nentries,
            nentries=nentries,
            override_logfilesize=override_logfilesize,
            logfilesize=logfilesize,
            override_rotatecount=override_rotatecount,
            rotatecount=rotatecount,
            override_format=override_format,
            format_=format_,
            lognginx=lognginx,
            logdefaultblock=logdefaultblock,
            logdefaultpass=logdefaultpass,
            logbogons=logbogons,
            logprivatenets=logprivatenets,
            filterdescriptions=filterdescriptions,
        )

        syslog_config_override.additional_properties = d
        return syslog_config_override

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
