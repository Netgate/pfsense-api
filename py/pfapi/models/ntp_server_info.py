from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NtpServerInfo")


@_attrs_define
class NtpServerInfo:
    """
    Attributes:
        status (str):
        server (str):
        refid (str):
        stratum (str):
        type (str):
        when (str):
        poll (str):
        reach (str):
        delay (str):
        offset (str):
        jitter (str):
    """

    status: str
    server: str
    refid: str
    stratum: str
    type: str
    when: str
    poll: str
    reach: str
    delay: str
    offset: str
    jitter: str
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
        field_dict.update(
            {
                "status": status,
                "server": server,
                "refid": refid,
                "stratum": stratum,
                "type": type,
                "when": when,
                "poll": poll,
                "reach": reach,
                "delay": delay,
                "offset": offset,
                "jitter": jitter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status")

        server = d.pop("server")

        refid = d.pop("refid")

        stratum = d.pop("stratum")

        type = d.pop("type")

        when = d.pop("when")

        poll = d.pop("poll")

        reach = d.pop("reach")

        delay = d.pop("delay")

        offset = d.pop("offset")

        jitter = d.pop("jitter")

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
