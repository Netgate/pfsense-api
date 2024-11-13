from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_sec_ikesa import IPSecIKESA
    from ..models.ip_sec_phase_list import IPSecPhaseList


T = TypeVar("T", bound="IPSecStatus")


@_attrs_define
class IPSecStatus:
    """
    Attributes:
        list_sa (Union[Unset, List['IPSecIKESA']]):
        phases (Union[Unset, IPSecPhaseList]):
    """

    list_sa: Union[Unset, List["IPSecIKESA"]] = UNSET
    phases: Union[Unset, "IPSecPhaseList"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        list_sa: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.list_sa, Unset):
            list_sa = []
            for list_sa_item_data in self.list_sa:
                list_sa_item = list_sa_item_data.to_dict()
                list_sa.append(list_sa_item)

        phases: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.phases, Unset):
            phases = self.phases.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if list_sa is not UNSET:
            field_dict["list_sa"] = list_sa
        if phases is not UNSET:
            field_dict["phases"] = phases

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ip_sec_ikesa import IPSecIKESA
        from ..models.ip_sec_phase_list import IPSecPhaseList

        d = src_dict.copy()
        list_sa = []
        _list_sa = d.pop("list_sa", UNSET)
        for list_sa_item_data in _list_sa or []:
            list_sa_item = IPSecIKESA.from_dict(list_sa_item_data)

            list_sa.append(list_sa_item)

        _phases = d.pop("phases", UNSET)
        phases: Union[Unset, IPSecPhaseList]
        if isinstance(_phases, Unset):
            phases = UNSET
        else:
            phases = IPSecPhaseList.from_dict(_phases)

        ip_sec_status = cls(
            list_sa=list_sa,
            phases=phases,
        )

        ip_sec_status.additional_properties = d
        return ip_sec_status

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
