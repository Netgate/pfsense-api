from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Bootenv")


@_attrs_define
class Bootenv:
    """
    Attributes:
        creation_nice (Union[Unset, str]):
        used_nice (Union[Unset, int]):
        version (Union[Unset, str]):
        name (Union[Unset, str]):
        mounted (Union[Unset, str]):
        activate_title (Union[Unset, str]):
        dataset (Union[Unset, str]):
        prior (Union[Unset, str]):
        creation (Union[Unset, str]):
        usedrefreserv (Union[Unset, str]):
        used (Union[Unset, str]):
        upgrading (Union[Unset, bool]):
        active (Union[Unset, bool]):
        nextboot (Union[Unset, bool]):
        activate_icon (Union[Unset, str]):
        lastbooted_nice (Union[Unset, str]):
        usedsnap (Union[Unset, str]):
        descr (Union[Unset, str]):
        failed (Union[Unset, bool]):
        referenced (Union[Unset, str]):
        mountpoint (Union[Unset, str]):
        bootonce (Union[Unset, bool]):
        origin (Union[Unset, str]):
        useds (Union[Unset, str]):
        protect (Union[Unset, bool]):
    """

    creation_nice: Union[Unset, str] = UNSET
    used_nice: Union[Unset, int] = UNSET
    version: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    mounted: Union[Unset, str] = UNSET
    activate_title: Union[Unset, str] = UNSET
    dataset: Union[Unset, str] = UNSET
    prior: Union[Unset, str] = UNSET
    creation: Union[Unset, str] = UNSET
    usedrefreserv: Union[Unset, str] = UNSET
    used: Union[Unset, str] = UNSET
    upgrading: Union[Unset, bool] = UNSET
    active: Union[Unset, bool] = UNSET
    nextboot: Union[Unset, bool] = UNSET
    activate_icon: Union[Unset, str] = UNSET
    lastbooted_nice: Union[Unset, str] = UNSET
    usedsnap: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    failed: Union[Unset, bool] = UNSET
    referenced: Union[Unset, str] = UNSET
    mountpoint: Union[Unset, str] = UNSET
    bootonce: Union[Unset, bool] = UNSET
    origin: Union[Unset, str] = UNSET
    useds: Union[Unset, str] = UNSET
    protect: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        creation_nice = self.creation_nice

        used_nice = self.used_nice

        version = self.version

        name = self.name

        mounted = self.mounted

        activate_title = self.activate_title

        dataset = self.dataset

        prior = self.prior

        creation = self.creation

        usedrefreserv = self.usedrefreserv

        used = self.used

        upgrading = self.upgrading

        active = self.active

        nextboot = self.nextboot

        activate_icon = self.activate_icon

        lastbooted_nice = self.lastbooted_nice

        usedsnap = self.usedsnap

        descr = self.descr

        failed = self.failed

        referenced = self.referenced

        mountpoint = self.mountpoint

        bootonce = self.bootonce

        origin = self.origin

        useds = self.useds

        protect = self.protect

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creation_nice is not UNSET:
            field_dict["creation_nice"] = creation_nice
        if used_nice is not UNSET:
            field_dict["used_nice"] = used_nice
        if version is not UNSET:
            field_dict["version"] = version
        if name is not UNSET:
            field_dict["name"] = name
        if mounted is not UNSET:
            field_dict["mounted"] = mounted
        if activate_title is not UNSET:
            field_dict["activate_title"] = activate_title
        if dataset is not UNSET:
            field_dict["dataset"] = dataset
        if prior is not UNSET:
            field_dict["prior"] = prior
        if creation is not UNSET:
            field_dict["creation"] = creation
        if usedrefreserv is not UNSET:
            field_dict["usedrefreserv"] = usedrefreserv
        if used is not UNSET:
            field_dict["used"] = used
        if upgrading is not UNSET:
            field_dict["upgrading"] = upgrading
        if active is not UNSET:
            field_dict["active"] = active
        if nextboot is not UNSET:
            field_dict["nextboot"] = nextboot
        if activate_icon is not UNSET:
            field_dict["activate_icon"] = activate_icon
        if lastbooted_nice is not UNSET:
            field_dict["lastbooted_nice"] = lastbooted_nice
        if usedsnap is not UNSET:
            field_dict["usedsnap"] = usedsnap
        if descr is not UNSET:
            field_dict["descr"] = descr
        if failed is not UNSET:
            field_dict["failed"] = failed
        if referenced is not UNSET:
            field_dict["referenced"] = referenced
        if mountpoint is not UNSET:
            field_dict["mountpoint"] = mountpoint
        if bootonce is not UNSET:
            field_dict["bootonce"] = bootonce
        if origin is not UNSET:
            field_dict["origin"] = origin
        if useds is not UNSET:
            field_dict["useds"] = useds
        if protect is not UNSET:
            field_dict["protect"] = protect

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        creation_nice = d.pop("creation_nice", UNSET)

        used_nice = d.pop("used_nice", UNSET)

        version = d.pop("version", UNSET)

        name = d.pop("name", UNSET)

        mounted = d.pop("mounted", UNSET)

        activate_title = d.pop("activate_title", UNSET)

        dataset = d.pop("dataset", UNSET)

        prior = d.pop("prior", UNSET)

        creation = d.pop("creation", UNSET)

        usedrefreserv = d.pop("usedrefreserv", UNSET)

        used = d.pop("used", UNSET)

        upgrading = d.pop("upgrading", UNSET)

        active = d.pop("active", UNSET)

        nextboot = d.pop("nextboot", UNSET)

        activate_icon = d.pop("activate_icon", UNSET)

        lastbooted_nice = d.pop("lastbooted_nice", UNSET)

        usedsnap = d.pop("usedsnap", UNSET)

        descr = d.pop("descr", UNSET)

        failed = d.pop("failed", UNSET)

        referenced = d.pop("referenced", UNSET)

        mountpoint = d.pop("mountpoint", UNSET)

        bootonce = d.pop("bootonce", UNSET)

        origin = d.pop("origin", UNSET)

        useds = d.pop("useds", UNSET)

        protect = d.pop("protect", UNSET)

        bootenv = cls(
            creation_nice=creation_nice,
            used_nice=used_nice,
            version=version,
            name=name,
            mounted=mounted,
            activate_title=activate_title,
            dataset=dataset,
            prior=prior,
            creation=creation,
            usedrefreserv=usedrefreserv,
            used=used,
            upgrading=upgrading,
            active=active,
            nextboot=nextboot,
            activate_icon=activate_icon,
            lastbooted_nice=lastbooted_nice,
            usedsnap=usedsnap,
            descr=descr,
            failed=failed,
            referenced=referenced,
            mountpoint=mountpoint,
            bootonce=bootonce,
            origin=origin,
            useds=useds,
            protect=protect,
        )

        bootenv.additional_properties = d
        return bootenv

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
