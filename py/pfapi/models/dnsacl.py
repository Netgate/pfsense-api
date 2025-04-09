from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dnsacl_network import DNSACLNetwork


T = TypeVar("T", bound="DNSACL")


@_attrs_define
class DNSACL:
    """
    Attributes:
        aclid (str):
        aclname (str):
        aclaction (Union[Unset, str]):
        description (Union[Unset, str]):
        row (Union[Unset, List['DNSACLNetwork']]):
    """

    aclid: str
    aclname: str
    aclaction: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    row: Union[Unset, List["DNSACLNetwork"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aclid = self.aclid

        aclname = self.aclname

        aclaction = self.aclaction

        description = self.description

        row: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.row, Unset):
            row = []
            for row_item_data in self.row:
                row_item = row_item_data.to_dict()
                row.append(row_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aclid": aclid,
                "aclname": aclname,
            }
        )
        if aclaction is not UNSET:
            field_dict["aclaction"] = aclaction
        if description is not UNSET:
            field_dict["description"] = description
        if row is not UNSET:
            field_dict["row"] = row

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dnsacl_network import DNSACLNetwork

        d = src_dict.copy()
        aclid = d.pop("aclid")

        aclname = d.pop("aclname")

        aclaction = d.pop("aclaction", UNSET)

        description = d.pop("description", UNSET)

        row = []
        _row = d.pop("row", UNSET)
        for row_item_data in _row or []:
            row_item = DNSACLNetwork.from_dict(row_item_data)

            row.append(row_item)

        dnsacl = cls(
            aclid=aclid,
            aclname=aclname,
            aclaction=aclaction,
            description=description,
            row=row,
        )

        dnsacl.additional_properties = d
        return dnsacl

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
