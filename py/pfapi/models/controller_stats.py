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
        uptime (int): uptime in seconds
        started (int): time controller was started/restarted
        mem_total (int): host physical memory in bytes
        mem_used (int): controller current memory usage
        cpu_load (List[int]):
        admin_logins (int): number of logged in admins
        systems_total (int): total number of systems being managed
        systems_online (int): number of systems that are online
        systems_failed (int): number of systems in failure/error state
        mesh (MeshStats):
        storage (Union[Unset, List['StorageStats']]):
    """

    uptime: int
    started: int
    mem_total: int
    mem_used: int
    cpu_load: List[int]
    admin_logins: int
    systems_total: int
    systems_online: int
    systems_failed: int
    mesh: "MeshStats"
    storage: Union[Unset, List["StorageStats"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uptime = self.uptime

        started = self.started

        mem_total = self.mem_total

        mem_used = self.mem_used

        cpu_load = self.cpu_load

        admin_logins = self.admin_logins

        systems_total = self.systems_total

        systems_online = self.systems_online

        systems_failed = self.systems_failed

        mesh = self.mesh.to_dict()

        storage: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.storage, Unset):
            storage = []
            for storage_item_data in self.storage:
                storage_item = storage_item_data.to_dict()
                storage.append(storage_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uptime": uptime,
                "started": started,
                "mem_total": mem_total,
                "mem_used": mem_used,
                "cpu_load": cpu_load,
                "admin_logins": admin_logins,
                "systems_total": systems_total,
                "systems_online": systems_online,
                "systems_failed": systems_failed,
                "mesh": mesh,
            }
        )
        if storage is not UNSET:
            field_dict["storage"] = storage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.mesh_stats import MeshStats
        from ..models.storage_stats import StorageStats

        d = src_dict.copy()
        uptime = d.pop("uptime")

        started = d.pop("started")

        mem_total = d.pop("mem_total")

        mem_used = d.pop("mem_used")

        cpu_load = cast(List[int], d.pop("cpu_load"))

        admin_logins = d.pop("admin_logins")

        systems_total = d.pop("systems_total")

        systems_online = d.pop("systems_online")

        systems_failed = d.pop("systems_failed")

        mesh = MeshStats.from_dict(d.pop("mesh"))

        storage = []
        _storage = d.pop("storage", UNSET)
        for storage_item_data in _storage or []:
            storage_item = StorageStats.from_dict(storage_item_data)

            storage.append(storage_item)

        controller_stats = cls(
            uptime=uptime,
            started=started,
            mem_total=mem_total,
            mem_used=mem_used,
            cpu_load=cpu_load,
            admin_logins=admin_logins,
            systems_total=systems_total,
            systems_online=systems_online,
            systems_failed=systems_failed,
            mesh=mesh,
            storage=storage,
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
