from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        username (Union[Unset, str]):
        name (Union[Unset, str]):
        descr (Union[Unset, str]):
        scope (Union[Unset, str]):
        groupname (Union[Unset, str]):
        groups (Union[Unset, List[str]]):
        disabled (Union[Unset, bool]):
        uid (Union[Unset, int]):
        full_name (Union[Unset, str]):
        cert_refids (Union[Unset, List[str]]):
        authorized_keys (Union[Unset, str]):
        privs (Union[Unset, List[str]]):
        keep_cmd_history (Union[Unset, bool]):
        expiration (Union[Unset, int]):
        ipsec_psk (Union[Unset, str]):
        custom_settings (Union[Unset, bool]):
        interfaces_sort (Union[Unset, bool]):
        webguicss (Union[Unset, str]):
        webguifixedmenu (Union[Unset, str]):
        webguihostnamemenu (Union[Unset, str]):
        dashboardcolumns (Union[Unset, int]):
        dashboardavailablewidgetspanel (Union[Unset, bool]):
        systemlogsfilterpanel (Union[Unset, bool]):
        systemlogsmanagelogpanel (Union[Unset, bool]):
        statusmonitoringsettingspanel (Union[Unset, bool]):
        webguileftcolumnhyper (Union[Unset, bool]):
        disablealiaspopupdetail (Union[Unset, bool]):
        pagenamefirst (Union[Unset, bool]):
    """

    username: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    groupname: Union[Unset, str] = UNSET
    groups: Union[Unset, List[str]] = UNSET
    disabled: Union[Unset, bool] = UNSET
    uid: Union[Unset, int] = UNSET
    full_name: Union[Unset, str] = UNSET
    cert_refids: Union[Unset, List[str]] = UNSET
    authorized_keys: Union[Unset, str] = UNSET
    privs: Union[Unset, List[str]] = UNSET
    keep_cmd_history: Union[Unset, bool] = UNSET
    expiration: Union[Unset, int] = UNSET
    ipsec_psk: Union[Unset, str] = UNSET
    custom_settings: Union[Unset, bool] = UNSET
    interfaces_sort: Union[Unset, bool] = UNSET
    webguicss: Union[Unset, str] = UNSET
    webguifixedmenu: Union[Unset, str] = UNSET
    webguihostnamemenu: Union[Unset, str] = UNSET
    dashboardcolumns: Union[Unset, int] = UNSET
    dashboardavailablewidgetspanel: Union[Unset, bool] = UNSET
    systemlogsfilterpanel: Union[Unset, bool] = UNSET
    systemlogsmanagelogpanel: Union[Unset, bool] = UNSET
    statusmonitoringsettingspanel: Union[Unset, bool] = UNSET
    webguileftcolumnhyper: Union[Unset, bool] = UNSET
    disablealiaspopupdetail: Union[Unset, bool] = UNSET
    pagenamefirst: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username

        name = self.name

        descr = self.descr

        scope = self.scope

        groupname = self.groupname

        groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        disabled = self.disabled

        uid = self.uid

        full_name = self.full_name

        cert_refids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cert_refids, Unset):
            cert_refids = self.cert_refids

        authorized_keys = self.authorized_keys

        privs: Union[Unset, List[str]] = UNSET
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        scope = d.pop("scope", UNSET)

        groupname = d.pop("groupname", UNSET)

        groups = cast(List[str], d.pop("groups", UNSET))

        disabled = d.pop("disabled", UNSET)

        uid = d.pop("uid", UNSET)

        full_name = d.pop("full_name", UNSET)

        cert_refids = cast(List[str], d.pop("cert_refids", UNSET))

        authorized_keys = d.pop("authorized_keys", UNSET)

        privs = cast(List[str], d.pop("privs", UNSET))

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
