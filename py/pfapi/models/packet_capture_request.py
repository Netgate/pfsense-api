from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
            action (str | Unset): start, stop
            interface (str | Unset): assigned network interface name
            promiscuous (bool | Unset):
            count (int | Unset): how many packets to capture
            snaplen (int | Unset): packet length
            detail (str | Unset): level of detail - normal, medium, high, full
            viewtype (str | Unset): interpret captured traffic as specified type:
                default, aodv, carp, cnfp, lmp, pgm, pgm_zmtp1, resp, radius,
                rpc, rtp, rtcp snmp, tftp, vat, wb, vxlan, zmtp1
            dnsquery (bool | Unset): reverse DNS lookup
            untagged_filter (PacketCaptureFilter | Unset): Additional packet capture filter. These are common options for
                both
                tagged and untagged filters, with the exception of the vlan_*
                values which are only used by the tagged_filter.
            tagged_filter (PacketCaptureFilter | Unset): Additional packet capture filter. These are common options for both
                tagged and untagged filters, with the exception of the vlan_*
                values which are only used by the tagged_filter.
    """

    action: str | Unset = UNSET
    interface: str | Unset = UNSET
    promiscuous: bool | Unset = UNSET
    count: int | Unset = UNSET
    snaplen: int | Unset = UNSET
    detail: str | Unset = UNSET
    viewtype: str | Unset = UNSET
    dnsquery: bool | Unset = UNSET
    untagged_filter: PacketCaptureFilter | Unset = UNSET
    tagged_filter: PacketCaptureFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        interface = self.interface

        promiscuous = self.promiscuous

        count = self.count

        snaplen = self.snaplen

        detail = self.detail

        viewtype = self.viewtype

        dnsquery = self.dnsquery

        untagged_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.untagged_filter, Unset):
            untagged_filter = self.untagged_filter.to_dict()

        tagged_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tagged_filter, Unset):
            tagged_filter = self.tagged_filter.to_dict()

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.packet_capture_filter import PacketCaptureFilter

        d = dict(src_dict)
        action = d.pop("action", UNSET)

        interface = d.pop("interface", UNSET)

        promiscuous = d.pop("promiscuous", UNSET)

        count = d.pop("count", UNSET)

        snaplen = d.pop("snaplen", UNSET)

        detail = d.pop("detail", UNSET)

        viewtype = d.pop("viewtype", UNSET)

        dnsquery = d.pop("dnsquery", UNSET)

        _untagged_filter = d.pop("untagged_filter", UNSET)
        untagged_filter: PacketCaptureFilter | Unset
        if isinstance(_untagged_filter, Unset):
            untagged_filter = UNSET
        else:
            untagged_filter = PacketCaptureFilter.from_dict(_untagged_filter)

        _tagged_filter = d.pop("tagged_filter", UNSET)
        tagged_filter: PacketCaptureFilter | Unset
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
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
