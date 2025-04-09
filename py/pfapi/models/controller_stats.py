from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mesh_stats import MeshStats
    from ..models.storage_stats import StorageStats


T = TypeVar("T", bound="ControllerStats")


@_attrs_define
class ControllerStats:
    """
    Attributes:
        uptime (Union[Unset, int]): uptime in seconds
        started (Union[Unset, int]): time controller was started/restarted
        mem_total (Union[Unset, int]): host physical memory in bytes
        mem_used (Union[Unset, int]): controller current memory usage
        storage (Union[Unset, List['StorageStats']]):
        cpu_load (Union[Unset, List[int]]):
        admin_logins (Union[Unset, int]): number of logged in admins
        systems_total (Union[Unset, int]): total number of systems being managed
        systems_online (Union[Unset, int]): number of systems that are online
        systems_failed (Union[Unset, int]): number of systems in failure/error state
        mesh (Union[Unset, MeshStats]):
    """

    uptime: Union[Unset, int] = UNSET
    started: Union[Unset, int] = UNSET
    mem_total: Union[Unset, int] = UNSET
    mem_used: Union[Unset, int] = UNSET
    storage: Union[Unset, List["StorageStats"]] = UNSET
    cpu_load: Union[Unset, List[int]] = UNSET
    admin_logins: Union[Unset, int] = UNSET
    systems_total: Union[Unset, int] = UNSET
    systems_online: Union[Unset, int] = UNSET
    systems_failed: Union[Unset, int] = UNSET
    mesh: Union[Unset, "MeshStats"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uptime = self.uptime

        started = self.started

        mem_total = self.mem_total

        mem_used = self.mem_used

        storage: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.storage, Unset):
            storage = []
            for storage_item_data in self.storage:
                storage_item = storage_item_data.to_dict()
                storage.append(storage_item)

        cpu_load: Union[Unset, List[int]] = UNSET
        if not isinstance(self.cpu_load, Unset):
            cpu_load = self.cpu_load

        admin_logins = self.admin_logins

        systems_total = self.systems_total

        systems_online = self.systems_online

        systems_failed = self.systems_failed

        mesh: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mesh, Unset):
            mesh = self.mesh.to_dict()

        field_dict: Dict[str, Any] = {}
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.mesh_stats import MeshStats
        from ..models.storage_stats import StorageStats

        d = src_dict.copy()
        uptime = d.pop("uptime", UNSET)

        started = d.pop("started", UNSET)

        mem_total = d.pop("mem_total", UNSET)

        mem_used = d.pop("mem_used", UNSET)

        storage = []
        _storage = d.pop("storage", UNSET)
        for storage_item_data in _storage or []:
            storage_item = StorageStats.from_dict(storage_item_data)

            storage.append(storage_item)

        cpu_load = cast(List[int], d.pop("cpu_load", UNSET))

        admin_logins = d.pop("admin_logins", UNSET)

        systems_total = d.pop("systems_total", UNSET)

        systems_online = d.pop("systems_online", UNSET)

        systems_failed = d.pop("systems_failed", UNSET)

        _mesh = d.pop("mesh", UNSET)
        mesh: Union[Unset, MeshStats]
        if isinstance(_mesh, Unset):
            mesh = UNSET
        else:
            mesh = MeshStats.from_dict(_mesh)

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
        )

        controller_stats.additional_properties = d
        return controller_stats

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
