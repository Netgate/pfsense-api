from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_sec_disconnect_req_phase import IPSecDisconnectReqPhase
from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecDisconnectReq")


@_attrs_define
class IPSecDisconnectReq:
    """
    Attributes:
        phase (Union[Unset, IPSecDisconnectReqPhase]):
        conid (Union[Unset, str]):
        uniqueid (Union[Unset, str]):
    """

    phase: Union[Unset, IPSecDisconnectReqPhase] = UNSET
    conid: Union[Unset, str] = UNSET
    uniqueid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        phase: Union[Unset, str] = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.value

        conid = self.conid

        uniqueid = self.uniqueid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phase is not UNSET:
            field_dict["phase"] = phase
        if conid is not UNSET:
            field_dict["conid"] = conid
        if uniqueid is not UNSET:
            field_dict["uniqueid"] = uniqueid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _phase = d.pop("phase", UNSET)
        phase: Union[Unset, IPSecDisconnectReqPhase]
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = IPSecDisconnectReqPhase(_phase)

        conid = d.pop("conid", UNSET)

        uniqueid = d.pop("uniqueid", UNSET)

        ip_sec_disconnect_req = cls(
            phase=phase,
            conid=conid,
            uniqueid=uniqueid,
        )

        ip_sec_disconnect_req.additional_properties = d
        return ip_sec_disconnect_req

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
