from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AllowedIP")


@_attrs_define
class AllowedIP:
    """
    Attributes:
        ip (str):
        sn (str):
        descr (str):
        dir_ (str):
        bw_up (str):
        bw_down (str):
    """

    ip: str
    sn: str
    descr: str
    dir_: str
    bw_up: str
    bw_down: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ip = self.ip

        sn = self.sn

        descr = self.descr

        dir_ = self.dir_

        bw_up = self.bw_up

        bw_down = self.bw_down

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip": ip,
                "sn": sn,
                "descr": descr,
                "dir": dir_,
                "bw_up": bw_up,
                "bw_down": bw_down,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip = d.pop("ip")

        sn = d.pop("sn")

        descr = d.pop("descr")

        dir_ = d.pop("dir")

        bw_up = d.pop("bw_up")

        bw_down = d.pop("bw_down")

        allowed_ip = cls(
            ip=ip,
            sn=sn,
            descr=descr,
            dir_=dir_,
            bw_up=bw_up,
            bw_down=bw_down,
        )

        allowed_ip.additional_properties = d
        return allowed_ip

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
