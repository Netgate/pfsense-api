from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.packet_capture_filter import PacketCaptureFilter


T = TypeVar("T", bound="PacketCaptureRequest")


@_attrs_define
class PacketCaptureRequest:
    """valid values:
    action = "start", "stop"

        Attributes:
            action (Union[Unset, str]): start, stop
            interface (Union[Unset, str]): assigned network interface name
            promiscuous (Union[Unset, bool]):
            count (Union[Unset, int]): how many packets to capture
            snaplen (Union[Unset, int]): packet length
            detail (Union[Unset, str]): level of detail - normal, medium, high, full
            viewtype (Union[Unset, str]): interpret captured traffic as specified type:
                default, aodv, carp, cnfp, lmp, pgm, pgm_zmtp1, resp, radius,
                rpc, rtp, rtcp snmp, tftp, vat, wb, vxlan, zmtp1
            dnsquery (Union[Unset, bool]): reverse DNS lookup
            untagged_filter (Union[Unset, PacketCaptureFilter]): Additional packet capture filter. These are common options
                for both
                tagged and untagged filters, with the exception of the vlan_*
                values which are only used by the tagged_filter.
            tagged_filter (Union[Unset, PacketCaptureFilter]): Additional packet capture filter. These are common options
                for both
                tagged and untagged filters, with the exception of the vlan_*
                values which are only used by the tagged_filter.
    """

    action: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    promiscuous: Union[Unset, bool] = UNSET
    count: Union[Unset, int] = UNSET
    snaplen: Union[Unset, int] = UNSET
    detail: Union[Unset, str] = UNSET
    viewtype: Union[Unset, str] = UNSET
    dnsquery: Union[Unset, bool] = UNSET
    untagged_filter: Union[Unset, "PacketCaptureFilter"] = UNSET
    tagged_filter: Union[Unset, "PacketCaptureFilter"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action

        interface = self.interface

        promiscuous = self.promiscuous

        count = self.count

        snaplen = self.snaplen

        detail = self.detail

        viewtype = self.viewtype

        dnsquery = self.dnsquery

        untagged_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.untagged_filter, Unset):
            untagged_filter = self.untagged_filter.to_dict()

        tagged_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tagged_filter, Unset):
            tagged_filter = self.tagged_filter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if interface is not UNSET:
            field_dict["interface"] = interface
        if promiscuous is not UNSET:
            field_dict["promiscuous"] = promiscuous
        if count is not UNSET:
            field_dict["count"] = count
        if snaplen is not UNSET:
            field_dict["snaplen"] = snaplen
        if detail is not UNSET:
            field_dict["detail"] = detail
        if viewtype is not UNSET:
            field_dict["viewtype"] = viewtype
        if dnsquery is not UNSET:
            field_dict["dnsquery"] = dnsquery
        if untagged_filter is not UNSET:
            field_dict["untagged_filter"] = untagged_filter
        if tagged_filter is not UNSET:
            field_dict["tagged_filter"] = tagged_filter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.packet_capture_filter import PacketCaptureFilter

        d = src_dict.copy()
        action = d.pop("action", UNSET)

        interface = d.pop("interface", UNSET)

        promiscuous = d.pop("promiscuous", UNSET)

        count = d.pop("count", UNSET)

        snaplen = d.pop("snaplen", UNSET)

        detail = d.pop("detail", UNSET)

        viewtype = d.pop("viewtype", UNSET)

        dnsquery = d.pop("dnsquery", UNSET)

        _untagged_filter = d.pop("untagged_filter", UNSET)
        untagged_filter: Union[Unset, PacketCaptureFilter]
        if isinstance(_untagged_filter, Unset):
            untagged_filter = UNSET
        else:
            untagged_filter = PacketCaptureFilter.from_dict(_untagged_filter)

        _tagged_filter = d.pop("tagged_filter", UNSET)
        tagged_filter: Union[Unset, PacketCaptureFilter]
        if isinstance(_tagged_filter, Unset):
            tagged_filter = UNSET
        else:
            tagged_filter = PacketCaptureFilter.from_dict(_tagged_filter)

        packet_capture_request = cls(
            action=action,
            interface=interface,
            promiscuous=promiscuous,
            count=count,
            snaplen=snaplen,
            detail=detail,
            viewtype=viewtype,
            dnsquery=dnsquery,
            untagged_filter=untagged_filter,
            tagged_filter=tagged_filter,
        )

        packet_capture_request.additional_properties = d
        return packet_capture_request

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
