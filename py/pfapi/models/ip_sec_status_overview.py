from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        enabled (Union[Unset, bool]):
        daemon_running (Union[Unset, bool]):
        status (Union[Unset, IPSecStatus]):
        lease (Union[Unset, List['IPSecPool']]):
        sads (Union[Unset, List['IPSecSAD']]):
        spds (Union[Unset, List['IPSecSPD']]):
    """

    enabled: Union[Unset, bool] = UNSET
    daemon_running: Union[Unset, bool] = UNSET
    status: Union[Unset, "IPSecStatus"] = UNSET
    lease: Union[Unset, List["IPSecPool"]] = UNSET
    sads: Union[Unset, List["IPSecSAD"]] = UNSET
    spds: Union[Unset, List["IPSecSPD"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        daemon_running = self.daemon_running

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        lease: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lease, Unset):
            lease = []
            for lease_item_data in self.lease:
                lease_item = lease_item_data.to_dict()
                lease.append(lease_item)

        sads: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sads, Unset):
            sads = []
            for sads_item_data in self.sads:
                sads_item = sads_item_data.to_dict()
                sads.append(sads_item)

        spds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.spds, Unset):
            spds = []
            for spds_item_data in self.spds:
                spds_item = spds_item_data.to_dict()
                spds.append(spds_item)

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ip_sec_pool import IPSecPool
        from ..models.ip_sec_sad import IPSecSAD
        from ..models.ip_sec_spd import IPSecSPD
        from ..models.ip_sec_status import IPSecStatus

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        daemon_running = d.pop("daemon_running", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, IPSecStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IPSecStatus.from_dict(_status)

        lease = []
        _lease = d.pop("lease", UNSET)
        for lease_item_data in _lease or []:
            lease_item = IPSecPool.from_dict(lease_item_data)

            lease.append(lease_item)

        sads = []
        _sads = d.pop("sads", UNSET)
        for sads_item_data in _sads or []:
            sads_item = IPSecSAD.from_dict(sads_item_data)

            sads.append(sads_item)

        spds = []
        _spds = d.pop("spds", UNSET)
        for spds_item_data in _spds or []:
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
