from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tier import Tier


T = TypeVar("T", bound="GroupStatus")


@_attrs_define
class GroupStatus:
    """
    Attributes:
        name (str):
        descr (str):
        tier1 (Union[Unset, List['Tier']]):
        tier2 (Union[Unset, List['Tier']]):
        tier3 (Union[Unset, List['Tier']]):
        tier4 (Union[Unset, List['Tier']]):
        tier5 (Union[Unset, List['Tier']]):
    """

    name: str
    descr: str
    tier1: Union[Unset, List["Tier"]] = UNSET
    tier2: Union[Unset, List["Tier"]] = UNSET
    tier3: Union[Unset, List["Tier"]] = UNSET
    tier4: Union[Unset, List["Tier"]] = UNSET
    tier5: Union[Unset, List["Tier"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        descr = self.descr

        tier1: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tier1, Unset):
            tier1 = []
            for tier1_item_data in self.tier1:
                tier1_item = tier1_item_data.to_dict()
                tier1.append(tier1_item)

        tier2: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tier2, Unset):
            tier2 = []
            for tier2_item_data in self.tier2:
                tier2_item = tier2_item_data.to_dict()
                tier2.append(tier2_item)

        tier3: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tier3, Unset):
            tier3 = []
            for tier3_item_data in self.tier3:
                tier3_item = tier3_item_data.to_dict()
                tier3.append(tier3_item)

        tier4: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tier4, Unset):
            tier4 = []
            for tier4_item_data in self.tier4:
                tier4_item = tier4_item_data.to_dict()
                tier4.append(tier4_item)

        tier5: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tier5, Unset):
            tier5 = []
            for tier5_item_data in self.tier5:
                tier5_item = tier5_item_data.to_dict()
                tier5.append(tier5_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "descr": descr,
            }
        )
        if tier1 is not UNSET:
            field_dict["tier1"] = tier1
        if tier2 is not UNSET:
            field_dict["tier2"] = tier2
        if tier3 is not UNSET:
            field_dict["tier3"] = tier3
        if tier4 is not UNSET:
            field_dict["tier4"] = tier4
        if tier5 is not UNSET:
            field_dict["tier5"] = tier5

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tier import Tier

        d = src_dict.copy()
        name = d.pop("name")

        descr = d.pop("descr")

        tier1 = []
        _tier1 = d.pop("tier1", UNSET)
        for tier1_item_data in _tier1 or []:
            tier1_item = Tier.from_dict(tier1_item_data)

            tier1.append(tier1_item)

        tier2 = []
        _tier2 = d.pop("tier2", UNSET)
        for tier2_item_data in _tier2 or []:
            tier2_item = Tier.from_dict(tier2_item_data)

            tier2.append(tier2_item)

        tier3 = []
        _tier3 = d.pop("tier3", UNSET)
        for tier3_item_data in _tier3 or []:
            tier3_item = Tier.from_dict(tier3_item_data)

            tier3.append(tier3_item)

        tier4 = []
        _tier4 = d.pop("tier4", UNSET)
        for tier4_item_data in _tier4 or []:
            tier4_item = Tier.from_dict(tier4_item_data)

            tier4.append(tier4_item)

        tier5 = []
        _tier5 = d.pop("tier5", UNSET)
        for tier5_item_data in _tier5 or []:
            tier5_item = Tier.from_dict(tier5_item_data)

            tier5.append(tier5_item)

        group_status = cls(
            name=name,
            descr=descr,
            tier1=tier1,
            tier2=tier2,
            tier3=tier3,
            tier4=tier4,
            tier5=tier5,
        )

        group_status.additional_properties = d
        return group_status

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
