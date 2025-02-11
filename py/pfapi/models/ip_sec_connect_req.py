from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IPSecConnectReq")


@_attrs_define
class IPSecConnectReq:
    """
    Attributes:
        connect_p1 (bool):
        p1_ikeid (str):
        connect_p2 (bool):
        p2_reqid (str):
    """

    connect_p1: bool
    p1_ikeid: str
    connect_p2: bool
    p2_reqid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connect_p1 = self.connect_p1

        p1_ikeid = self.p1_ikeid

        connect_p2 = self.connect_p2

        p2_reqid = self.p2_reqid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connect_p1": connect_p1,
                "p1_ikeid": p1_ikeid,
                "connect_p2": connect_p2,
                "p2_reqid": p2_reqid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connect_p1 = d.pop("connect_p1")

        p1_ikeid = d.pop("p1_ikeid")

        connect_p2 = d.pop("connect_p2")

        p2_reqid = d.pop("p2_reqid")

        ip_sec_connect_req = cls(
            connect_p1=connect_p1,
            p1_ikeid=p1_ikeid,
            connect_p2=connect_p2,
            p2_reqid=p2_reqid,
        )

        ip_sec_connect_req.additional_properties = d
        return ip_sec_connect_req

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
