from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_sec_pool import IPSecPool
    from ..models.ip_sec_sad import IPSecSAD
    from ..models.ip_sec_spd import IPSecSPD
    from ..models.ip_sec_status import IPSecStatus


T = TypeVar("T", bound="IPSecStatusOverview")


@_attrs_define
class IPSecStatusOverview:
    """
    Attributes:
        enabled (bool | Unset):
        daemon_running (bool | Unset):
        status (IPSecStatus | Unset):
        lease (list[IPSecPool] | Unset):
        sads (list[IPSecSAD] | Unset):
        spds (list[IPSecSPD] | Unset):
    """

    enabled: bool | Unset = UNSET
    daemon_running: bool | Unset = UNSET
    status: IPSecStatus | Unset = UNSET
    lease: list[IPSecPool] | Unset = UNSET
    sads: list[IPSecSAD] | Unset = UNSET
    spds: list[IPSecSPD] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        daemon_running = self.daemon_running

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        lease: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lease, Unset):
            lease = []
            for lease_item_data in self.lease:
                lease_item = lease_item_data.to_dict()
                lease.append(lease_item)

        sads: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sads, Unset):
            sads = []
            for sads_item_data in self.sads:
                sads_item = sads_item_data.to_dict()
                sads.append(sads_item)

        spds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.spds, Unset):
            spds = []
            for spds_item_data in self.spds:
                spds_item = spds_item_data.to_dict()
                spds.append(spds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if daemon_running is not UNSET:
            field_dict["daemon_running"] = daemon_running
        if status is not UNSET:
            field_dict["status"] = status
        if lease is not UNSET:
            field_dict["lease"] = lease
        if sads is not UNSET:
            field_dict["sads"] = sads
        if spds is not UNSET:
            field_dict["spds"] = spds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_sec_pool import IPSecPool
        from ..models.ip_sec_sad import IPSecSAD
        from ..models.ip_sec_spd import IPSecSPD
        from ..models.ip_sec_status import IPSecStatus

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        daemon_running = d.pop("daemon_running", UNSET)

        _status = d.pop("status", UNSET)
        status: IPSecStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IPSecStatus.from_dict(_status)

        _lease = d.pop("lease", UNSET)
        lease: list[IPSecPool] | Unset = UNSET
        if _lease is not UNSET:
            lease = []
            for lease_item_data in _lease:
                lease_item = IPSecPool.from_dict(lease_item_data)

                lease.append(lease_item)

        _sads = d.pop("sads", UNSET)
        sads: list[IPSecSAD] | Unset = UNSET
        if _sads is not UNSET:
            sads = []
            for sads_item_data in _sads:
                sads_item = IPSecSAD.from_dict(sads_item_data)

                sads.append(sads_item)

        _spds = d.pop("spds", UNSET)
        spds: list[IPSecSPD] | Unset = UNSET
        if _spds is not UNSET:
            spds = []
            for spds_item_data in _spds:
                spds_item = IPSecSPD.from_dict(spds_item_data)

                spds.append(spds_item)

        ip_sec_status_overview = cls(
            enabled=enabled,
            daemon_running=daemon_running,
            status=status,
            lease=lease,
            sads=sads,
            spds=spds,
        )

        ip_sec_status_overview.additional_properties = d
        return ip_sec_status_overview

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
