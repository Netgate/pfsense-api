from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Bootenv")


@_attrs_define
class Bootenv:
    """
    Attributes:
        creation_nice (str):
        used_nice (int):
        version (str):
        name (str):
        mounted (str):
        activate_title (str):
        dataset (str):
        prior (str):
        creation (str):
        usedrefreserv (str):
        used (str):
        upgrading (bool):
        active (bool):
        nextboot (bool):
        activate_icon (str):
        lastbooted_nice (str):
        usedsnap (str):
        descr (str):
        failed (bool):
        referenced (str):
        mountpoint (str):
        bootonce (bool):
        origin (str):
        useds (str):
        protect (bool):
    """

    creation_nice: str
    used_nice: int
    version: str
    name: str
    mounted: str
    activate_title: str
    dataset: str
    prior: str
    creation: str
    usedrefreserv: str
    used: str
    upgrading: bool
    active: bool
    nextboot: bool
    activate_icon: str
    lastbooted_nice: str
    usedsnap: str
    descr: str
    failed: bool
    referenced: str
    mountpoint: str
    bootonce: bool
    origin: str
    useds: str
    protect: bool
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
        field_dict.update(
            {
                "creation_nice": creation_nice,
                "used_nice": used_nice,
                "version": version,
                "name": name,
                "mounted": mounted,
                "activate_title": activate_title,
                "dataset": dataset,
                "prior": prior,
                "creation": creation,
                "usedrefreserv": usedrefreserv,
                "used": used,
                "upgrading": upgrading,
                "active": active,
                "nextboot": nextboot,
                "activate_icon": activate_icon,
                "lastbooted_nice": lastbooted_nice,
                "usedsnap": usedsnap,
                "descr": descr,
                "failed": failed,
                "referenced": referenced,
                "mountpoint": mountpoint,
                "bootonce": bootonce,
                "origin": origin,
                "useds": useds,
                "protect": protect,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        creation_nice = d.pop("creation_nice")

        used_nice = d.pop("used_nice")

        version = d.pop("version")

        name = d.pop("name")

        mounted = d.pop("mounted")

        activate_title = d.pop("activate_title")

        dataset = d.pop("dataset")

        prior = d.pop("prior")

        creation = d.pop("creation")

        usedrefreserv = d.pop("usedrefreserv")

        used = d.pop("used")

        upgrading = d.pop("upgrading")

        active = d.pop("active")

        nextboot = d.pop("nextboot")

        activate_icon = d.pop("activate_icon")

        lastbooted_nice = d.pop("lastbooted_nice")

        usedsnap = d.pop("usedsnap")

        descr = d.pop("descr")

        failed = d.pop("failed")

        referenced = d.pop("referenced")

        mountpoint = d.pop("mountpoint")

        bootonce = d.pop("bootonce")

        origin = d.pop("origin")

        useds = d.pop("useds")

        protect = d.pop("protect")

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
