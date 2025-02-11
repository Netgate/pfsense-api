from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DHCPLease")


@_attrs_define
class DHCPLease:
    """
    Attributes:
        host (str):
        lifetime (int):
        ip (str):
        mac (str):
        cltt (str):
        state (str):
        start (str):
        end (str):
        iaid (int):
        duid (str):
    """

    host: str
    lifetime: int
    ip: str
    mac: str
    cltt: str
    state: str
    start: str
    end: str
    iaid: int
    duid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host

        lifetime = self.lifetime

        ip = self.ip

        mac = self.mac

        cltt = self.cltt

        state = self.state

        start = self.start

        end = self.end

        iaid = self.iaid

        duid = self.duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "lifetime": lifetime,
                "ip": ip,
                "mac": mac,
                "cltt": cltt,
                "state": state,
                "start": start,
                "end": end,
                "iaid": iaid,
                "duid": duid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host")

        lifetime = d.pop("lifetime")

        ip = d.pop("ip")

        mac = d.pop("mac")

        cltt = d.pop("cltt")

        state = d.pop("state")

        start = d.pop("start")

        end = d.pop("end")

        iaid = d.pop("iaid")

        duid = d.pop("duid")

        dhcp_lease = cls(
            host=host,
            lifetime=lifetime,
            ip=ip,
            mac=mac,
            cltt=cltt,
            state=state,
            start=start,
            end=end,
            iaid=iaid,
            duid=duid,
        )

        dhcp_lease.additional_properties = d
        return dhcp_lease

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
