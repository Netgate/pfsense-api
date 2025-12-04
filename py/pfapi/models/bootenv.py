from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Bootenv")


@_attrs_define
class Bootenv:
    """
    Attributes:
        creation_nice (str | Unset):
        used_nice (int | Unset):
        version (str | Unset):
        name (str | Unset):
        mounted (str | Unset):
        activate_title (str | Unset):
        dataset (str | Unset):
        prior (str | Unset):
        creation (str | Unset):
        usedrefreserv (str | Unset):
        used (str | Unset):
        upgrading (bool | Unset):
        active (bool | Unset):
        nextboot (bool | Unset):
        activate_icon (str | Unset):
        lastbooted_nice (str | Unset):
        usedsnap (str | Unset):
        descr (str | Unset):
        failed (bool | Unset):
        referenced (str | Unset):
        mountpoint (str | Unset):
        bootonce (bool | Unset):
        origin (str | Unset):
        useds (str | Unset):
        protect (bool | Unset):
    """

    creation_nice: str | Unset = UNSET
    used_nice: int | Unset = UNSET
    version: str | Unset = UNSET
    name: str | Unset = UNSET
    mounted: str | Unset = UNSET
    activate_title: str | Unset = UNSET
    dataset: str | Unset = UNSET
    prior: str | Unset = UNSET
    creation: str | Unset = UNSET
    usedrefreserv: str | Unset = UNSET
    used: str | Unset = UNSET
    upgrading: bool | Unset = UNSET
    active: bool | Unset = UNSET
    nextboot: bool | Unset = UNSET
    activate_icon: str | Unset = UNSET
    lastbooted_nice: str | Unset = UNSET
    usedsnap: str | Unset = UNSET
    descr: str | Unset = UNSET
    failed: bool | Unset = UNSET
    referenced: str | Unset = UNSET
    mountpoint: str | Unset = UNSET
    bootonce: bool | Unset = UNSET
    origin: str | Unset = UNSET
    useds: str | Unset = UNSET
    protect: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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
