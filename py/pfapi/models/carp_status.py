from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.carpvip_status import CARPVIPStatus


T = TypeVar("T", bound="CARPStatus")


@_attrs_define
class CARPStatus:
    """
    Attributes:
        enabled (bool):
        maintenancemode_enabled (bool):
        vips (Union[Unset, List['CARPVIPStatus']]):
    """

    enabled: bool
    maintenancemode_enabled: bool
    vips: Union[Unset, List["CARPVIPStatus"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        maintenancemode_enabled = self.maintenancemode_enabled

        vips: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vips, Unset):
            vips = []
            for vips_item_data in self.vips:
                vips_item = vips_item_data.to_dict()
                vips.append(vips_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "maintenancemode_enabled": maintenancemode_enabled,
            }
        )
        if vips is not UNSET:
            field_dict["vips"] = vips

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.carpvip_status import CARPVIPStatus

        d = src_dict.copy()
        enabled = d.pop("enabled")

        maintenancemode_enabled = d.pop("maintenancemode_enabled")

        vips = []
        _vips = d.pop("vips", UNSET)
        for vips_item_data in _vips or []:
            vips_item = CARPVIPStatus.from_dict(vips_item_data)

            vips.append(vips_item)

        carp_status = cls(
            enabled=enabled,
            maintenancemode_enabled=maintenancemode_enabled,
            vips=vips,
        )

        carp_status.additional_properties = d
        return carp_status

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
