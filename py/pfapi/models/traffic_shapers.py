from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.altq_capable_interface import ALTQCapableInterface
    from ..models.altq_root_queue import ALTQRootQueue
    from ..models.limiter import Limiter


T = TypeVar("T", bound="TrafficShapers")


@_attrs_define
class TrafficShapers:
    """
    Attributes:
        altq (Union[Unset, List['ALTQRootQueue']]):
        altq_capable_ifs (Union[Unset, List['ALTQCapableInterface']]):
        limiter (Union[Unset, List['Limiter']]):
    """

    altq: Union[Unset, List["ALTQRootQueue"]] = UNSET
    altq_capable_ifs: Union[Unset, List["ALTQCapableInterface"]] = UNSET
    limiter: Union[Unset, List["Limiter"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        altq: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.altq, Unset):
            altq = []
            for altq_item_data in self.altq:
                altq_item = altq_item_data.to_dict()
                altq.append(altq_item)

        altq_capable_ifs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.altq_capable_ifs, Unset):
            altq_capable_ifs = []
            for altq_capable_ifs_item_data in self.altq_capable_ifs:
                altq_capable_ifs_item = altq_capable_ifs_item_data.to_dict()
                altq_capable_ifs.append(altq_capable_ifs_item)

        limiter: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.limiter, Unset):
            limiter = []
            for limiter_item_data in self.limiter:
                limiter_item = limiter_item_data.to_dict()
                limiter.append(limiter_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if altq is not UNSET:
            field_dict["altq"] = altq
        if altq_capable_ifs is not UNSET:
            field_dict["altq_capable_ifs"] = altq_capable_ifs
        if limiter is not UNSET:
            field_dict["limiter"] = limiter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.altq_capable_interface import ALTQCapableInterface
        from ..models.altq_root_queue import ALTQRootQueue
        from ..models.limiter import Limiter

        d = src_dict.copy()
        altq = []
        _altq = d.pop("altq", UNSET)
        for altq_item_data in _altq or []:
            altq_item = ALTQRootQueue.from_dict(altq_item_data)

            altq.append(altq_item)

        altq_capable_ifs = []
        _altq_capable_ifs = d.pop("altq_capable_ifs", UNSET)
        for altq_capable_ifs_item_data in _altq_capable_ifs or []:
            altq_capable_ifs_item = ALTQCapableInterface.from_dict(altq_capable_ifs_item_data)

            altq_capable_ifs.append(altq_capable_ifs_item)

        limiter = []
        _limiter = d.pop("limiter", UNSET)
        for limiter_item_data in _limiter or []:
            limiter_item = Limiter.from_dict(limiter_item_data)

            limiter.append(limiter_item)

        traffic_shapers = cls(
            altq=altq,
            altq_capable_ifs=altq_capable_ifs,
            limiter=limiter,
        )

        traffic_shapers.additional_properties = d
        return traffic_shapers

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
