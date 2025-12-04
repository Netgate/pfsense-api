from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_login_session import AdminLoginSession
    from ..models.mesh_stats import MeshStats
    from ..models.storage_stats import StorageStats


T = TypeVar("T", bound="ControllerStats")


@_attrs_define
class ControllerStats:
    """
    Attributes:
        uptime (int | Unset): uptime in seconds
        started (int | Unset): time controller was started/restarted
        mem_total (int | Unset): host physical memory in bytes
        mem_used (int | Unset): controller current memory usage
        storage (list[StorageStats] | Unset):
        cpu_load (list[int] | Unset):
        admin_logins (int | Unset): number of logged in admins
        systems_total (int | Unset): total number of systems being managed
        systems_online (int | Unset): number of systems that are online
        systems_failed (int | Unset): number of systems in failure/error state
        mesh (MeshStats | Unset):
        admin_sessions (list[AdminLoginSession] | Unset):
        timestamp (int | Unset): current millisecond timestamp of the controller
    """

    uptime: int | Unset = UNSET
    started: int | Unset = UNSET
    mem_total: int | Unset = UNSET
    mem_used: int | Unset = UNSET
    storage: list[StorageStats] | Unset = UNSET
    cpu_load: list[int] | Unset = UNSET
    admin_logins: int | Unset = UNSET
    systems_total: int | Unset = UNSET
    systems_online: int | Unset = UNSET
    systems_failed: int | Unset = UNSET
    mesh: MeshStats | Unset = UNSET
    admin_sessions: list[AdminLoginSession] | Unset = UNSET
    timestamp: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uptime = self.uptime

        started = self.started

        mem_total = self.mem_total

        mem_used = self.mem_used

        storage: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.storage, Unset):
            storage = []
            for storage_item_data in self.storage:
                storage_item = storage_item_data.to_dict()
                storage.append(storage_item)

        cpu_load: list[int] | Unset = UNSET
        if not isinstance(self.cpu_load, Unset):
            cpu_load = self.cpu_load

        admin_logins = self.admin_logins

        systems_total = self.systems_total

        systems_online = self.systems_online

        systems_failed = self.systems_failed

        mesh: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mesh, Unset):
            mesh = self.mesh.to_dict()

        admin_sessions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.admin_sessions, Unset):
            admin_sessions = []
            for admin_sessions_item_data in self.admin_sessions:
                admin_sessions_item = admin_sessions_item_data.to_dict()
                admin_sessions.append(admin_sessions_item)

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if started is not UNSET:
            field_dict["started"] = started
        if mem_total is not UNSET:
            field_dict["mem_total"] = mem_total
        if mem_used is not UNSET:
            field_dict["mem_used"] = mem_used
        if storage is not UNSET:
            field_dict["storage"] = storage
        if cpu_load is not UNSET:
            field_dict["cpu_load"] = cpu_load
        if admin_logins is not UNSET:
            field_dict["admin_logins"] = admin_logins
        if systems_total is not UNSET:
            field_dict["systems_total"] = systems_total
        if systems_online is not UNSET:
            field_dict["systems_online"] = systems_online
        if systems_failed is not UNSET:
            field_dict["systems_failed"] = systems_failed
        if mesh is not UNSET:
            field_dict["mesh"] = mesh
        if admin_sessions is not UNSET:
            field_dict["admin_sessions"] = admin_sessions
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_login_session import AdminLoginSession
        from ..models.mesh_stats import MeshStats
        from ..models.storage_stats import StorageStats

        d = dict(src_dict)
        uptime = d.pop("uptime", UNSET)

        started = d.pop("started", UNSET)

        mem_total = d.pop("mem_total", UNSET)

        mem_used = d.pop("mem_used", UNSET)

        _storage = d.pop("storage", UNSET)
        storage: list[StorageStats] | Unset = UNSET
        if _storage is not UNSET:
            storage = []
            for storage_item_data in _storage:
                storage_item = StorageStats.from_dict(storage_item_data)

                storage.append(storage_item)

        cpu_load = cast(list[int], d.pop("cpu_load", UNSET))

        admin_logins = d.pop("admin_logins", UNSET)

        systems_total = d.pop("systems_total", UNSET)

        systems_online = d.pop("systems_online", UNSET)

        systems_failed = d.pop("systems_failed", UNSET)

        _mesh = d.pop("mesh", UNSET)
        mesh: MeshStats | Unset
        if isinstance(_mesh, Unset):
            mesh = UNSET
        else:
            mesh = MeshStats.from_dict(_mesh)

        _admin_sessions = d.pop("admin_sessions", UNSET)
        admin_sessions: list[AdminLoginSession] | Unset = UNSET
        if _admin_sessions is not UNSET:
            admin_sessions = []
            for admin_sessions_item_data in _admin_sessions:
                admin_sessions_item = AdminLoginSession.from_dict(admin_sessions_item_data)

                admin_sessions.append(admin_sessions_item)

        timestamp = d.pop("timestamp", UNSET)

        controller_stats = cls(
            uptime=uptime,
            started=started,
            mem_total=mem_total,
            mem_used=mem_used,
            storage=storage,
            cpu_load=cpu_load,
            admin_logins=admin_logins,
            systems_total=systems_total,
            systems_online=systems_online,
            systems_failed=systems_failed,
            mesh=mesh,
            admin_sessions=admin_sessions,
            timestamp=timestamp,
        )

        controller_stats.additional_properties = d
        return controller_stats

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
