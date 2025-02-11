from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.u_pn_p_perm_user import UPnPPermUser


T = TypeVar("T", bound="UPnPConfig")


@_attrs_define
class UPnPConfig:
    """
    Attributes:
        enable (bool):
        enable_upnp (bool):
        enable_natpmp (bool):
        ext_iface (str):
        download (str):
        upload (str):
        overridewanip (str):
        upnpqueue (str):
        logpackets (bool):
        sysuptime (bool):
        permdefault (bool):
        presentationurl (str):
        modelnumber (str):
        enable_stun (bool):
        stun_host (str):
        stun_port (str):
        iface_array (Union[Unset, List[str]]):
        row (Union[Unset, List['UPnPPermUser']]):
    """

    enable: bool
    enable_upnp: bool
    enable_natpmp: bool
    ext_iface: str
    download: str
    upload: str
    overridewanip: str
    upnpqueue: str
    logpackets: bool
    sysuptime: bool
    permdefault: bool
    presentationurl: str
    modelnumber: str
    enable_stun: bool
    stun_host: str
    stun_port: str
    iface_array: Union[Unset, List[str]] = UNSET
    row: Union[Unset, List["UPnPPermUser"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        enable_upnp = self.enable_upnp

        enable_natpmp = self.enable_natpmp

        ext_iface = self.ext_iface

        download = self.download

        upload = self.upload

        overridewanip = self.overridewanip

        upnpqueue = self.upnpqueue

        logpackets = self.logpackets

        sysuptime = self.sysuptime

        permdefault = self.permdefault

        presentationurl = self.presentationurl

        modelnumber = self.modelnumber

        enable_stun = self.enable_stun

        stun_host = self.stun_host

        stun_port = self.stun_port

        iface_array: Union[Unset, List[str]] = UNSET
        if not isinstance(self.iface_array, Unset):
            iface_array = self.iface_array

        row: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.row, Unset):
            row = []
            for row_item_data in self.row:
                row_item = row_item_data.to_dict()
                row.append(row_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "enable_upnp": enable_upnp,
                "enable_natpmp": enable_natpmp,
                "ext_iface": ext_iface,
                "download": download,
                "upload": upload,
                "overridewanip": overridewanip,
                "upnpqueue": upnpqueue,
                "logpackets": logpackets,
                "sysuptime": sysuptime,
                "permdefault": permdefault,
                "presentationurl": presentationurl,
                "modelnumber": modelnumber,
                "enable_stun": enable_stun,
                "stun_host": stun_host,
                "stun_port": stun_port,
            }
        )
        if iface_array is not UNSET:
            field_dict["iface_array"] = iface_array
        if row is not UNSET:
            field_dict["row"] = row

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.u_pn_p_perm_user import UPnPPermUser

        d = src_dict.copy()
        enable = d.pop("enable")

        enable_upnp = d.pop("enable_upnp")

        enable_natpmp = d.pop("enable_natpmp")

        ext_iface = d.pop("ext_iface")

        download = d.pop("download")

        upload = d.pop("upload")

        overridewanip = d.pop("overridewanip")

        upnpqueue = d.pop("upnpqueue")

        logpackets = d.pop("logpackets")

        sysuptime = d.pop("sysuptime")

        permdefault = d.pop("permdefault")

        presentationurl = d.pop("presentationurl")

        modelnumber = d.pop("modelnumber")

        enable_stun = d.pop("enable_stun")

        stun_host = d.pop("stun_host")

        stun_port = d.pop("stun_port")

        iface_array = cast(List[str], d.pop("iface_array", UNSET))

        row = []
        _row = d.pop("row", UNSET)
        for row_item_data in _row or []:
            row_item = UPnPPermUser.from_dict(row_item_data)

            row.append(row_item)

        u_pn_p_config = cls(
            enable=enable,
            enable_upnp=enable_upnp,
            enable_natpmp=enable_natpmp,
            ext_iface=ext_iface,
            download=download,
            upload=upload,
            overridewanip=overridewanip,
            upnpqueue=upnpqueue,
            logpackets=logpackets,
            sysuptime=sysuptime,
            permdefault=permdefault,
            presentationurl=presentationurl,
            modelnumber=modelnumber,
            enable_stun=enable_stun,
            stun_host=stun_host,
            stun_port=stun_port,
            iface_array=iface_array,
            row=row,
        )

        u_pn_p_config.additional_properties = d
        return u_pn_p_config

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
