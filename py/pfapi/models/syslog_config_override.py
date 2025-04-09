from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyslogConfigOverride")


@_attrs_define
class SyslogConfigOverride:
    """
    Attributes:
        cronorder (Union[Unset, str]): reverse, forward, or empty for default
        nentries (Union[Unset, int]):
        logfilesize (Union[Unset, int]):
        rotatecount (Union[Unset, int]):
        format_ (Union[Unset, str]): formatted, raw
        lognginx (Union[Unset, bool]):
        logdefaultblock (Union[Unset, bool]):
        logdefaultpass (Union[Unset, bool]):
        logbogons (Union[Unset, bool]):
        logprivatenets (Union[Unset, bool]):
        loglinklocal4 (Union[Unset, bool]):
        logsnort2c (Union[Unset, bool]):
        filterdescriptions (Union[Unset, int]):
    """

    cronorder: Union[Unset, str] = UNSET
    nentries: Union[Unset, int] = UNSET
    logfilesize: Union[Unset, int] = UNSET
    rotatecount: Union[Unset, int] = UNSET
    format_: Union[Unset, str] = UNSET
    lognginx: Union[Unset, bool] = UNSET
    logdefaultblock: Union[Unset, bool] = UNSET
    logdefaultpass: Union[Unset, bool] = UNSET
    logbogons: Union[Unset, bool] = UNSET
    logprivatenets: Union[Unset, bool] = UNSET
    loglinklocal4: Union[Unset, bool] = UNSET
    logsnort2c: Union[Unset, bool] = UNSET
    filterdescriptions: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cronorder = self.cronorder

        nentries = self.nentries

        logfilesize = self.logfilesize

        rotatecount = self.rotatecount

        format_ = self.format_

        lognginx = self.lognginx

        logdefaultblock = self.logdefaultblock

        logdefaultpass = self.logdefaultpass

        logbogons = self.logbogons

        logprivatenets = self.logprivatenets

        loglinklocal4 = self.loglinklocal4

        logsnort2c = self.logsnort2c

        filterdescriptions = self.filterdescriptions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cronorder is not UNSET:
            field_dict["cronorder"] = cronorder
        if nentries is not UNSET:
            field_dict["nentries"] = nentries
        if logfilesize is not UNSET:
            field_dict["logfilesize"] = logfilesize
        if rotatecount is not UNSET:
            field_dict["rotatecount"] = rotatecount
        if format_ is not UNSET:
            field_dict["format"] = format_
        if lognginx is not UNSET:
            field_dict["lognginx"] = lognginx
        if logdefaultblock is not UNSET:
            field_dict["logdefaultblock"] = logdefaultblock
        if logdefaultpass is not UNSET:
            field_dict["logdefaultpass"] = logdefaultpass
        if logbogons is not UNSET:
            field_dict["logbogons"] = logbogons
        if logprivatenets is not UNSET:
            field_dict["logprivatenets"] = logprivatenets
        if loglinklocal4 is not UNSET:
            field_dict["loglinklocal4"] = loglinklocal4
        if logsnort2c is not UNSET:
            field_dict["logsnort2c"] = logsnort2c
        if filterdescriptions is not UNSET:
            field_dict["filterdescriptions"] = filterdescriptions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cronorder = d.pop("cronorder", UNSET)

        nentries = d.pop("nentries", UNSET)

        logfilesize = d.pop("logfilesize", UNSET)

        rotatecount = d.pop("rotatecount", UNSET)

        format_ = d.pop("format", UNSET)

        lognginx = d.pop("lognginx", UNSET)

        logdefaultblock = d.pop("logdefaultblock", UNSET)

        logdefaultpass = d.pop("logdefaultpass", UNSET)

        logbogons = d.pop("logbogons", UNSET)

        logprivatenets = d.pop("logprivatenets", UNSET)

        loglinklocal4 = d.pop("loglinklocal4", UNSET)

        logsnort2c = d.pop("logsnort2c", UNSET)

        filterdescriptions = d.pop("filterdescriptions", UNSET)

        syslog_config_override = cls(
            cronorder=cronorder,
            nentries=nentries,
            logfilesize=logfilesize,
            rotatecount=rotatecount,
            format_=format_,
            lognginx=lognginx,
            logdefaultblock=logdefaultblock,
            logdefaultpass=logdefaultpass,
            logbogons=logbogons,
            logprivatenets=logprivatenets,
            loglinklocal4=loglinklocal4,
            logsnort2c=logsnort2c,
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
