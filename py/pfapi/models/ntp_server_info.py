from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NtpServerInfo")


@_attrs_define
class NtpServerInfo:
    """
    Attributes:
        status (Union[Unset, str]):
        server (Union[Unset, str]):
        refid (Union[Unset, str]):
        stratum (Union[Unset, str]):
        type (Union[Unset, str]):
        when (Union[Unset, str]):
        poll (Union[Unset, str]):
        reach (Union[Unset, str]):
        delay (Union[Unset, str]):
        offset (Union[Unset, str]):
        jitter (Union[Unset, str]):
    """

    status: Union[Unset, str] = UNSET
    server: Union[Unset, str] = UNSET
    refid: Union[Unset, str] = UNSET
    stratum: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    when: Union[Unset, str] = UNSET
    poll: Union[Unset, str] = UNSET
    reach: Union[Unset, str] = UNSET
    delay: Union[Unset, str] = UNSET
    offset: Union[Unset, str] = UNSET
    jitter: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        server = self.server

        refid = self.refid

        stratum = self.stratum

        type = self.type

        when = self.when

        poll = self.poll

        reach = self.reach

        delay = self.delay

        offset = self.offset

        jitter = self.jitter

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if server is not UNSET:
            field_dict["server"] = server
        if refid is not UNSET:
            field_dict["refid"] = refid
        if stratum is not UNSET:
            field_dict["stratum"] = stratum
        if type is not UNSET:
            field_dict["type"] = type
        if when is not UNSET:
            field_dict["when"] = when
        if poll is not UNSET:
            field_dict["poll"] = poll
        if reach is not UNSET:
            field_dict["reach"] = reach
        if delay is not UNSET:
            field_dict["delay"] = delay
        if offset is not UNSET:
            field_dict["offset"] = offset
        if jitter is not UNSET:
            field_dict["jitter"] = jitter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status", UNSET)

        server = d.pop("server", UNSET)

        refid = d.pop("refid", UNSET)

        stratum = d.pop("stratum", UNSET)

        type = d.pop("type", UNSET)

        when = d.pop("when", UNSET)

        poll = d.pop("poll", UNSET)

        reach = d.pop("reach", UNSET)

        delay = d.pop("delay", UNSET)

        offset = d.pop("offset", UNSET)

        jitter = d.pop("jitter", UNSET)

        ntp_server_info = cls(
            status=status,
            server=server,
            refid=refid,
            stratum=stratum,
            type=type,
            when=when,
            poll=poll,
            reach=reach,
            delay=delay,
            offset=offset,
            jitter=jitter,
        )

        ntp_server_info.additional_properties = d
        return ntp_server_info

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
