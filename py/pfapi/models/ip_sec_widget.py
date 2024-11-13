from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_sec_widget_mobile import IPSecWidgetMobile
    from ..models.ip_sec_widget_tunnel import IPSecWidgetTunnel


T = TypeVar("T", bound="IPSecWidget")


@_attrs_define
class IPSecWidget:
    """
    Attributes:
        phase1s_active (Union[Unset, int]):
        phase1s_total (Union[Unset, int]):
        phase2s_active (Union[Unset, int]):
        phase2s_total (Union[Unset, int]):
        total_active (Union[Unset, int]):
        total_inactive (Union[Unset, int]):
        mobile_users (Union[Unset, int]):
        mobile_active (Union[Unset, int]):
        mobile_total (Union[Unset, int]):
        tunnels (Union[Unset, List['IPSecWidgetTunnel']]):
        mobile (Union[Unset, List['IPSecWidgetMobile']]):
    """

    phase1s_active: Union[Unset, int] = UNSET
    phase1s_total: Union[Unset, int] = UNSET
    phase2s_active: Union[Unset, int] = UNSET
    phase2s_total: Union[Unset, int] = UNSET
    total_active: Union[Unset, int] = UNSET
    total_inactive: Union[Unset, int] = UNSET
    mobile_users: Union[Unset, int] = UNSET
    mobile_active: Union[Unset, int] = UNSET
    mobile_total: Union[Unset, int] = UNSET
    tunnels: Union[Unset, List["IPSecWidgetTunnel"]] = UNSET
    mobile: Union[Unset, List["IPSecWidgetMobile"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        phase1s_active = self.phase1s_active

        phase1s_total = self.phase1s_total

        phase2s_active = self.phase2s_active

        phase2s_total = self.phase2s_total

        total_active = self.total_active

        total_inactive = self.total_inactive

        mobile_users = self.mobile_users

        mobile_active = self.mobile_active

        mobile_total = self.mobile_total

        tunnels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tunnels, Unset):
            tunnels = []
            for tunnels_item_data in self.tunnels:
                tunnels_item = tunnels_item_data.to_dict()
                tunnels.append(tunnels_item)

        mobile: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.mobile, Unset):
            mobile = []
            for mobile_item_data in self.mobile:
                mobile_item = mobile_item_data.to_dict()
                mobile.append(mobile_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phase1s_active is not UNSET:
            field_dict["phase1s_active"] = phase1s_active
        if phase1s_total is not UNSET:
            field_dict["phase1s_total"] = phase1s_total
        if phase2s_active is not UNSET:
            field_dict["phase2s_active"] = phase2s_active
        if phase2s_total is not UNSET:
            field_dict["phase2s_total"] = phase2s_total
        if total_active is not UNSET:
            field_dict["total_active"] = total_active
        if total_inactive is not UNSET:
            field_dict["total_inactive"] = total_inactive
        if mobile_users is not UNSET:
            field_dict["mobile_users"] = mobile_users
        if mobile_active is not UNSET:
            field_dict["mobile_active"] = mobile_active
        if mobile_total is not UNSET:
            field_dict["mobile_total"] = mobile_total
        if tunnels is not UNSET:
            field_dict["tunnels"] = tunnels
        if mobile is not UNSET:
            field_dict["mobile"] = mobile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ip_sec_widget_mobile import IPSecWidgetMobile
        from ..models.ip_sec_widget_tunnel import IPSecWidgetTunnel

        d = src_dict.copy()
        phase1s_active = d.pop("phase1s_active", UNSET)

        phase1s_total = d.pop("phase1s_total", UNSET)

        phase2s_active = d.pop("phase2s_active", UNSET)

        phase2s_total = d.pop("phase2s_total", UNSET)

        total_active = d.pop("total_active", UNSET)

        total_inactive = d.pop("total_inactive", UNSET)

        mobile_users = d.pop("mobile_users", UNSET)

        mobile_active = d.pop("mobile_active", UNSET)

        mobile_total = d.pop("mobile_total", UNSET)

        tunnels = []
        _tunnels = d.pop("tunnels", UNSET)
        for tunnels_item_data in _tunnels or []:
            tunnels_item = IPSecWidgetTunnel.from_dict(tunnels_item_data)

            tunnels.append(tunnels_item)

        mobile = []
        _mobile = d.pop("mobile", UNSET)
        for mobile_item_data in _mobile or []:
            mobile_item = IPSecWidgetMobile.from_dict(mobile_item_data)

            mobile.append(mobile_item)

        ip_sec_widget = cls(
            phase1s_active=phase1s_active,
            phase1s_total=phase1s_total,
            phase2s_active=phase2s_active,
            phase2s_total=phase2s_total,
            total_active=total_active,
            total_inactive=total_inactive,
            mobile_users=mobile_users,
            mobile_active=mobile_active,
            mobile_total=mobile_total,
            tunnels=tunnels,
            mobile=mobile,
        )

        ip_sec_widget.additional_properties = d
        return ip_sec_widget

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
