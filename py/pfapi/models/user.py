from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        username (str):
        name (str | Unset):
        descr (str | Unset):
        scope (str | Unset):
        groupname (str | Unset):
        groups (list[str] | Unset):
        disabled (bool | Unset):
        uid (int | Unset):
        full_name (str | Unset):
        cert_refids (list[str] | Unset):
        authorized_keys (str | Unset):
        privs (list[str] | Unset):
        keep_cmd_history (bool | Unset):
        expiration (int | Unset):
        ipsec_psk (str | Unset):
        custom_settings (bool | Unset):
        interfaces_sort (bool | Unset):
        webguicss (str | Unset):
        webguifixedmenu (str | Unset):
        webguihostnamemenu (str | Unset):
        dashboardcolumns (int | Unset):
        dashboardavailablewidgetspanel (bool | Unset):
        systemlogsfilterpanel (bool | Unset):
        systemlogsmanagelogpanel (bool | Unset):
        statusmonitoringsettingspanel (bool | Unset):
        webguileftcolumnhyper (bool | Unset):
        disablealiaspopupdetail (bool | Unset):
        pagenamefirst (bool | Unset):
    """

    username: str
    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    scope: str | Unset = UNSET
    groupname: str | Unset = UNSET
    groups: list[str] | Unset = UNSET
    disabled: bool | Unset = UNSET
    uid: int | Unset = UNSET
    full_name: str | Unset = UNSET
    cert_refids: list[str] | Unset = UNSET
    authorized_keys: str | Unset = UNSET
    privs: list[str] | Unset = UNSET
    keep_cmd_history: bool | Unset = UNSET
    expiration: int | Unset = UNSET
    ipsec_psk: str | Unset = UNSET
    custom_settings: bool | Unset = UNSET
    interfaces_sort: bool | Unset = UNSET
    webguicss: str | Unset = UNSET
    webguifixedmenu: str | Unset = UNSET
    webguihostnamemenu: str | Unset = UNSET
    dashboardcolumns: int | Unset = UNSET
    dashboardavailablewidgetspanel: bool | Unset = UNSET
    systemlogsfilterpanel: bool | Unset = UNSET
    systemlogsmanagelogpanel: bool | Unset = UNSET
    statusmonitoringsettingspanel: bool | Unset = UNSET
    webguileftcolumnhyper: bool | Unset = UNSET
    disablealiaspopupdetail: bool | Unset = UNSET
    pagenamefirst: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        name = self.name

        descr = self.descr

        scope = self.scope

        groupname = self.groupname

        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        disabled = self.disabled

        uid = self.uid

        full_name = self.full_name

        cert_refids: list[str] | Unset = UNSET
        if not isinstance(self.cert_refids, Unset):
            cert_refids = self.cert_refids

        authorized_keys = self.authorized_keys

        privs: list[str] | Unset = UNSET
        if not isinstance(self.privs, Unset):
            privs = self.privs

        keep_cmd_history = self.keep_cmd_history

        expiration = self.expiration

        ipsec_psk = self.ipsec_psk

        custom_settings = self.custom_settings

        interfaces_sort = self.interfaces_sort

        webguicss = self.webguicss

        webguifixedmenu = self.webguifixedmenu

        webguihostnamemenu = self.webguihostnamemenu

        dashboardcolumns = self.dashboardcolumns

        dashboardavailablewidgetspanel = self.dashboardavailablewidgetspanel

        systemlogsfilterpanel = self.systemlogsfilterpanel

        systemlogsmanagelogpanel = self.systemlogsmanagelogpanel

        statusmonitoringsettingspanel = self.statusmonitoringsettingspanel

        webguileftcolumnhyper = self.webguileftcolumnhyper

        disablealiaspopupdetail = self.disablealiaspopupdetail

        pagenamefirst = self.pagenamefirst

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if scope is not UNSET:
            field_dict["scope"] = scope
        if groupname is not UNSET:
            field_dict["groupname"] = groupname
        if groups is not UNSET:
            field_dict["groups"] = groups
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if uid is not UNSET:
            field_dict["uid"] = uid
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if cert_refids is not UNSET:
            field_dict["cert_refids"] = cert_refids
        if authorized_keys is not UNSET:
            field_dict["authorized_keys"] = authorized_keys
        if privs is not UNSET:
            field_dict["privs"] = privs
        if keep_cmd_history is not UNSET:
            field_dict["keep_cmd_history"] = keep_cmd_history
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if ipsec_psk is not UNSET:
            field_dict["ipsec_psk"] = ipsec_psk
        if custom_settings is not UNSET:
            field_dict["custom_settings"] = custom_settings
        if interfaces_sort is not UNSET:
            field_dict["interfaces_sort"] = interfaces_sort
        if webguicss is not UNSET:
            field_dict["webguicss"] = webguicss
        if webguifixedmenu is not UNSET:
            field_dict["webguifixedmenu"] = webguifixedmenu
        if webguihostnamemenu is not UNSET:
            field_dict["webguihostnamemenu"] = webguihostnamemenu
        if dashboardcolumns is not UNSET:
            field_dict["dashboardcolumns"] = dashboardcolumns
        if dashboardavailablewidgetspanel is not UNSET:
            field_dict["dashboardavailablewidgetspanel"] = dashboardavailablewidgetspanel
        if systemlogsfilterpanel is not UNSET:
            field_dict["systemlogsfilterpanel"] = systemlogsfilterpanel
        if systemlogsmanagelogpanel is not UNSET:
            field_dict["systemlogsmanagelogpanel"] = systemlogsmanagelogpanel
        if statusmonitoringsettingspanel is not UNSET:
            field_dict["statusmonitoringsettingspanel"] = statusmonitoringsettingspanel
        if webguileftcolumnhyper is not UNSET:
            field_dict["webguileftcolumnhyper"] = webguileftcolumnhyper
        if disablealiaspopupdetail is not UNSET:
            field_dict["disablealiaspopupdetail"] = disablealiaspopupdetail
        if pagenamefirst is not UNSET:
            field_dict["pagenamefirst"] = pagenamefirst

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        scope = d.pop("scope", UNSET)

        groupname = d.pop("groupname", UNSET)

        groups = cast(list[str], d.pop("groups", UNSET))

        disabled = d.pop("disabled", UNSET)

        uid = d.pop("uid", UNSET)

        full_name = d.pop("full_name", UNSET)

        cert_refids = cast(list[str], d.pop("cert_refids", UNSET))

        authorized_keys = d.pop("authorized_keys", UNSET)

        privs = cast(list[str], d.pop("privs", UNSET))

        keep_cmd_history = d.pop("keep_cmd_history", UNSET)

        expiration = d.pop("expiration", UNSET)

        ipsec_psk = d.pop("ipsec_psk", UNSET)

        custom_settings = d.pop("custom_settings", UNSET)

        interfaces_sort = d.pop("interfaces_sort", UNSET)

        webguicss = d.pop("webguicss", UNSET)

        webguifixedmenu = d.pop("webguifixedmenu", UNSET)

        webguihostnamemenu = d.pop("webguihostnamemenu", UNSET)

        dashboardcolumns = d.pop("dashboardcolumns", UNSET)

        dashboardavailablewidgetspanel = d.pop("dashboardavailablewidgetspanel", UNSET)

        systemlogsfilterpanel = d.pop("systemlogsfilterpanel", UNSET)

        systemlogsmanagelogpanel = d.pop("systemlogsmanagelogpanel", UNSET)

        statusmonitoringsettingspanel = d.pop("statusmonitoringsettingspanel", UNSET)

        webguileftcolumnhyper = d.pop("webguileftcolumnhyper", UNSET)

        disablealiaspopupdetail = d.pop("disablealiaspopupdetail", UNSET)

        pagenamefirst = d.pop("pagenamefirst", UNSET)

        user = cls(
            username=username,
            name=name,
            descr=descr,
            scope=scope,
            groupname=groupname,
            groups=groups,
            disabled=disabled,
            uid=uid,
            full_name=full_name,
            cert_refids=cert_refids,
            authorized_keys=authorized_keys,
            privs=privs,
            keep_cmd_history=keep_cmd_history,
            expiration=expiration,
            ipsec_psk=ipsec_psk,
            custom_settings=custom_settings,
            interfaces_sort=interfaces_sort,
            webguicss=webguicss,
            webguifixedmenu=webguifixedmenu,
            webguihostnamemenu=webguihostnamemenu,
            dashboardcolumns=dashboardcolumns,
            dashboardavailablewidgetspanel=dashboardavailablewidgetspanel,
            systemlogsfilterpanel=systemlogsfilterpanel,
            systemlogsmanagelogpanel=systemlogsmanagelogpanel,
            statusmonitoringsettingspanel=statusmonitoringsettingspanel,
            webguileftcolumnhyper=webguileftcolumnhyper,
            disablealiaspopupdetail=disablealiaspopupdetail,
            pagenamefirst=pagenamefirst,
        )

        user.additional_properties = d
        return user

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
