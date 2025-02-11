from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.net_if_assign_owner_req_owner_type import NetIfAssignOwnerReqOwnerType

T = TypeVar("T", bound="NetIfAssignOwnerReq")


@_attrs_define
class NetIfAssignOwnerReq:
    """owner_id is the identifier of the subsystem taking ownership of the
    interface.

    If the owner_type is set to "host", then it is returned
    to the host.

        Attributes:
            owner_type (NetIfAssignOwnerReqOwnerType):
            owner_id (str):
    """

    owner_type: NetIfAssignOwnerReqOwnerType
    owner_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owner_type = self.owner_type.value

        owner_id = self.owner_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner_type": owner_type,
                "owner_id": owner_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        owner_type = NetIfAssignOwnerReqOwnerType(d.pop("owner_type"))

        owner_id = d.pop("owner_id")

        net_if_assign_owner_req = cls(
            owner_type=owner_type,
            owner_id=owner_id,
        )

        net_if_assign_owner_req.additional_properties = d
        return net_if_assign_owner_req

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
