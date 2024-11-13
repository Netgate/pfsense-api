from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyslogConfigOverride")


@_attrs_define
class SyslogConfigOverride:
    """
    Attributes:
        override_reverse (Union[Unset, bool]):
        reverse (Union[Unset, bool]):
        override_nentries (Union[Unset, bool]):
        nentries (Union[Unset, int]):
        override_logfilesize (Union[Unset, bool]):
        logfilesize (Union[Unset, int]):
        override_rotatecount (Union[Unset, bool]):
        rotatecount (Union[Unset, int]):
        override_format (Union[Unset, bool]):
        format_ (Union[Unset, str]):
        web_server_log (Union[Unset, bool]):
        logdefaultblock (Union[Unset, bool]):
        logdefaultpass (Union[Unset, bool]):
        logbogons (Union[Unset, bool]):
        logprivatenets (Union[Unset, bool]):
        filterdescriptions (Union[Unset, int]):
    """

    override_reverse: Union[Unset, bool] = UNSET
    reverse: Union[Unset, bool] = UNSET
    override_nentries: Union[Unset, bool] = UNSET
    nentries: Union[Unset, int] = UNSET
    override_logfilesize: Union[Unset, bool] = UNSET
    logfilesize: Union[Unset, int] = UNSET
    override_rotatecount: Union[Unset, bool] = UNSET
    rotatecount: Union[Unset, int] = UNSET
    override_format: Union[Unset, bool] = UNSET
    format_: Union[Unset, str] = UNSET
    web_server_log: Union[Unset, bool] = UNSET
    logdefaultblock: Union[Unset, bool] = UNSET
    logdefaultpass: Union[Unset, bool] = UNSET
    logbogons: Union[Unset, bool] = UNSET
    logprivatenets: Union[Unset, bool] = UNSET
    filterdescriptions: Union[Unset, int] = UNSET
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

        web_server_log = self.web_server_log

        logdefaultblock = self.logdefaultblock

        logdefaultpass = self.logdefaultpass

        logbogons = self.logbogons

        logprivatenets = self.logprivatenets

        filterdescriptions = self.filterdescriptions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if override_reverse is not UNSET:
            field_dict["override_reverse"] = override_reverse
        if reverse is not UNSET:
            field_dict["reverse"] = reverse
        if override_nentries is not UNSET:
            field_dict["override_nentries"] = override_nentries
        if nentries is not UNSET:
            field_dict["nentries"] = nentries
        if override_logfilesize is not UNSET:
            field_dict["override_logfilesize"] = override_logfilesize
        if logfilesize is not UNSET:
            field_dict["logfilesize"] = logfilesize
        if override_rotatecount is not UNSET:
            field_dict["override_rotatecount"] = override_rotatecount
        if rotatecount is not UNSET:
            field_dict["rotatecount"] = rotatecount
        if override_format is not UNSET:
            field_dict["override_format"] = override_format
        if format_ is not UNSET:
            field_dict["format"] = format_
        if web_server_log is not UNSET:
            field_dict["web_server_log"] = web_server_log
        if logdefaultblock is not UNSET:
            field_dict["logdefaultblock"] = logdefaultblock
        if logdefaultpass is not UNSET:
            field_dict["logdefaultpass"] = logdefaultpass
        if logbogons is not UNSET:
            field_dict["logbogons"] = logbogons
        if logprivatenets is not UNSET:
            field_dict["logprivatenets"] = logprivatenets
        if filterdescriptions is not UNSET:
            field_dict["filterdescriptions"] = filterdescriptions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        override_reverse = d.pop("override_reverse", UNSET)

        reverse = d.pop("reverse", UNSET)

        override_nentries = d.pop("override_nentries", UNSET)

        nentries = d.pop("nentries", UNSET)

        override_logfilesize = d.pop("override_logfilesize", UNSET)

        logfilesize = d.pop("logfilesize", UNSET)

        override_rotatecount = d.pop("override_rotatecount", UNSET)

        rotatecount = d.pop("rotatecount", UNSET)

        override_format = d.pop("override_format", UNSET)

        format_ = d.pop("format", UNSET)

        web_server_log = d.pop("web_server_log", UNSET)

        logdefaultblock = d.pop("logdefaultblock", UNSET)

        logdefaultpass = d.pop("logdefaultpass", UNSET)

        logbogons = d.pop("logbogons", UNSET)

        logprivatenets = d.pop("logprivatenets", UNSET)

        filterdescriptions = d.pop("filterdescriptions", UNSET)

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
            web_server_log=web_server_log,
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
