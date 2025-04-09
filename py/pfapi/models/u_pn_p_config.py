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
        enable (Union[Unset, bool]):
        enable_upnp (Union[Unset, bool]):
        enable_natpmp (Union[Unset, bool]):
        ext_iface (Union[Unset, str]):
        iface_array (Union[Unset, List[str]]):
        download (Union[Unset, str]):
        upload (Union[Unset, str]):
        overridewanip (Union[Unset, str]):
        upnpqueue (Union[Unset, str]):
        logpackets (Union[Unset, bool]):
        sysuptime (Union[Unset, bool]):
        permdefault (Union[Unset, bool]):
        row (Union[Unset, List['UPnPPermUser']]):
        presentationurl (Union[Unset, str]):
        modelnumber (Union[Unset, str]):
        enable_stun (Union[Unset, bool]):
        stun_host (Union[Unset, str]):
        stun_port (Union[Unset, str]):
    """

    enable: Union[Unset, bool] = UNSET
    enable_upnp: Union[Unset, bool] = UNSET
    enable_natpmp: Union[Unset, bool] = UNSET
    ext_iface: Union[Unset, str] = UNSET
    iface_array: Union[Unset, List[str]] = UNSET
    download: Union[Unset, str] = UNSET
    upload: Union[Unset, str] = UNSET
    overridewanip: Union[Unset, str] = UNSET
    upnpqueue: Union[Unset, str] = UNSET
    logpackets: Union[Unset, bool] = UNSET
    sysuptime: Union[Unset, bool] = UNSET
    permdefault: Union[Unset, bool] = UNSET
    row: Union[Unset, List["UPnPPermUser"]] = UNSET
    presentationurl: Union[Unset, str] = UNSET
    modelnumber: Union[Unset, str] = UNSET
    enable_stun: Union[Unset, bool] = UNSET
    stun_host: Union[Unset, str] = UNSET
    stun_port: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        enable_upnp = self.enable_upnp

        enable_natpmp = self.enable_natpmp

        ext_iface = self.ext_iface

        iface_array: Union[Unset, List[str]] = UNSET
        if not isinstance(self.iface_array, Unset):
            iface_array = self.iface_array

        download = self.download

        upload = self.upload

        overridewanip = self.overridewanip

        upnpqueue = self.upnpqueue

        logpackets = self.logpackets

        sysuptime = self.sysuptime

        permdefault = self.permdefault

        row: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.row, Unset):
            row = []
            for row_item_data in self.row:
                row_item = row_item_data.to_dict()
                row.append(row_item)

        presentationurl = self.presentationurl

        modelnumber = self.modelnumber

        enable_stun = self.enable_stun

        stun_host = self.stun_host

        stun_port = self.stun_port

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if enable_upnp is not UNSET:
            field_dict["enable_upnp"] = enable_upnp
        if enable_natpmp is not UNSET:
            field_dict["enable_natpmp"] = enable_natpmp
        if ext_iface is not UNSET:
            field_dict["ext_iface"] = ext_iface
        if iface_array is not UNSET:
            field_dict["iface_array"] = iface_array
        if download is not UNSET:
            field_dict["download"] = download
        if upload is not UNSET:
            field_dict["upload"] = upload
        if overridewanip is not UNSET:
            field_dict["overridewanip"] = overridewanip
        if upnpqueue is not UNSET:
            field_dict["upnpqueue"] = upnpqueue
        if logpackets is not UNSET:
            field_dict["logpackets"] = logpackets
        if sysuptime is not UNSET:
            field_dict["sysuptime"] = sysuptime
        if permdefault is not UNSET:
            field_dict["permdefault"] = permdefault
        if row is not UNSET:
            field_dict["row"] = row
        if presentationurl is not UNSET:
            field_dict["presentationurl"] = presentationurl
        if modelnumber is not UNSET:
            field_dict["modelnumber"] = modelnumber
        if enable_stun is not UNSET:
            field_dict["enable_stun"] = enable_stun
        if stun_host is not UNSET:
            field_dict["stun_host"] = stun_host
        if stun_port is not UNSET:
            field_dict["stun_port"] = stun_port

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.u_pn_p_perm_user import UPnPPermUser

        d = src_dict.copy()
        enable = d.pop("enable", UNSET)

        enable_upnp = d.pop("enable_upnp", UNSET)

        enable_natpmp = d.pop("enable_natpmp", UNSET)

        ext_iface = d.pop("ext_iface", UNSET)

        iface_array = cast(List[str], d.pop("iface_array", UNSET))

        download = d.pop("download", UNSET)

        upload = d.pop("upload", UNSET)

        overridewanip = d.pop("overridewanip", UNSET)

        upnpqueue = d.pop("upnpqueue", UNSET)

        logpackets = d.pop("logpackets", UNSET)

        sysuptime = d.pop("sysuptime", UNSET)

        permdefault = d.pop("permdefault", UNSET)

        row = []
        _row = d.pop("row", UNSET)
        for row_item_data in _row or []:
            row_item = UPnPPermUser.from_dict(row_item_data)

            row.append(row_item)

        presentationurl = d.pop("presentationurl", UNSET)

        modelnumber = d.pop("modelnumber", UNSET)

        enable_stun = d.pop("enable_stun", UNSET)

        stun_host = d.pop("stun_host", UNSET)

        stun_port = d.pop("stun_port", UNSET)

        u_pn_p_config = cls(
            enable=enable,
            enable_upnp=enable_upnp,
            enable_natpmp=enable_natpmp,
            ext_iface=ext_iface,
            iface_array=iface_array,
            download=download,
            upload=upload,
            overridewanip=overridewanip,
            upnpqueue=upnpqueue,
            logpackets=logpackets,
            sysuptime=sysuptime,
            permdefault=permdefault,
            row=row,
            presentationurl=presentationurl,
            modelnumber=modelnumber,
            enable_stun=enable_stun,
            stun_host=stun_host,
            stun_port=stun_port,
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
