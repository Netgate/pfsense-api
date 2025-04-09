from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wme_setting import WMESetting
    from ..models.wpa_setting import WPASetting


T = TypeVar("T", bound="WirelessInterface")


@_attrs_define
class WirelessInterface:
    """
    Attributes:
        mode (Union[Unset, str]):
        standard (Union[Unset, str]):
        protmode (Union[Unset, str]):
        ssid (Union[Unset, str]):
        channel (Union[Unset, str]):
        authmode (Union[Unset, str]):
        txpower (Union[Unset, str]):
        distance (Union[Unset, str]):
        regdomain (Union[Unset, str]):
        regcountry (Union[Unset, str]):
        reglocation (Union[Unset, str]):
        wpa (Union[Unset, WPASetting]):
        auth_server_addr (Union[Unset, str]):
        auth_server_port (Union[Unset, str]):
        auth_server_shared_secret (Union[Unset, str]):
        auth_server_addr2 (Union[Unset, str]):
        auth_server_port2 (Union[Unset, str]):
        auth_server_shared_secret2 (Union[Unset, str]):
        wme (Union[Unset, WMESetting]):
        channel_width (Union[Unset, str]):
    """

    mode: Union[Unset, str] = UNSET
    standard: Union[Unset, str] = UNSET
    protmode: Union[Unset, str] = UNSET
    ssid: Union[Unset, str] = UNSET
    channel: Union[Unset, str] = UNSET
    authmode: Union[Unset, str] = UNSET
    txpower: Union[Unset, str] = UNSET
    distance: Union[Unset, str] = UNSET
    regdomain: Union[Unset, str] = UNSET
    regcountry: Union[Unset, str] = UNSET
    reglocation: Union[Unset, str] = UNSET
    wpa: Union[Unset, "WPASetting"] = UNSET
    auth_server_addr: Union[Unset, str] = UNSET
    auth_server_port: Union[Unset, str] = UNSET
    auth_server_shared_secret: Union[Unset, str] = UNSET
    auth_server_addr2: Union[Unset, str] = UNSET
    auth_server_port2: Union[Unset, str] = UNSET
    auth_server_shared_secret2: Union[Unset, str] = UNSET
    wme: Union[Unset, "WMESetting"] = UNSET
    channel_width: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mode = self.mode

        standard = self.standard

        protmode = self.protmode

        ssid = self.ssid

        channel = self.channel

        authmode = self.authmode

        txpower = self.txpower

        distance = self.distance

        regdomain = self.regdomain

        regcountry = self.regcountry

        reglocation = self.reglocation

        wpa: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wpa, Unset):
            wpa = self.wpa.to_dict()

        auth_server_addr = self.auth_server_addr

        auth_server_port = self.auth_server_port

        auth_server_shared_secret = self.auth_server_shared_secret

        auth_server_addr2 = self.auth_server_addr2

        auth_server_port2 = self.auth_server_port2

        auth_server_shared_secret2 = self.auth_server_shared_secret2

        wme: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wme, Unset):
            wme = self.wme.to_dict()

        channel_width = self.channel_width

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if standard is not UNSET:
            field_dict["standard"] = standard
        if protmode is not UNSET:
            field_dict["protmode"] = protmode
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if channel is not UNSET:
            field_dict["channel"] = channel
        if authmode is not UNSET:
            field_dict["authmode"] = authmode
        if txpower is not UNSET:
            field_dict["txpower"] = txpower
        if distance is not UNSET:
            field_dict["distance"] = distance
        if regdomain is not UNSET:
            field_dict["regdomain"] = regdomain
        if regcountry is not UNSET:
            field_dict["regcountry"] = regcountry
        if reglocation is not UNSET:
            field_dict["reglocation"] = reglocation
        if wpa is not UNSET:
            field_dict["wpa"] = wpa
        if auth_server_addr is not UNSET:
            field_dict["auth_server_addr"] = auth_server_addr
        if auth_server_port is not UNSET:
            field_dict["auth_server_port"] = auth_server_port
        if auth_server_shared_secret is not UNSET:
            field_dict["auth_server_shared_secret"] = auth_server_shared_secret
        if auth_server_addr2 is not UNSET:
            field_dict["auth_server_addr2"] = auth_server_addr2
        if auth_server_port2 is not UNSET:
            field_dict["auth_server_port2"] = auth_server_port2
        if auth_server_shared_secret2 is not UNSET:
            field_dict["auth_server_shared_secret2"] = auth_server_shared_secret2
        if wme is not UNSET:
            field_dict["wme"] = wme
        if channel_width is not UNSET:
            field_dict["channel_width"] = channel_width

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wme_setting import WMESetting
        from ..models.wpa_setting import WPASetting

        d = src_dict.copy()
        mode = d.pop("mode", UNSET)

        standard = d.pop("standard", UNSET)

        protmode = d.pop("protmode", UNSET)

        ssid = d.pop("ssid", UNSET)

        channel = d.pop("channel", UNSET)

        authmode = d.pop("authmode", UNSET)

        txpower = d.pop("txpower", UNSET)

        distance = d.pop("distance", UNSET)

        regdomain = d.pop("regdomain", UNSET)

        regcountry = d.pop("regcountry", UNSET)

        reglocation = d.pop("reglocation", UNSET)

        _wpa = d.pop("wpa", UNSET)
        wpa: Union[Unset, WPASetting]
        if isinstance(_wpa, Unset):
            wpa = UNSET
        else:
            wpa = WPASetting.from_dict(_wpa)

        auth_server_addr = d.pop("auth_server_addr", UNSET)

        auth_server_port = d.pop("auth_server_port", UNSET)

        auth_server_shared_secret = d.pop("auth_server_shared_secret", UNSET)

        auth_server_addr2 = d.pop("auth_server_addr2", UNSET)

        auth_server_port2 = d.pop("auth_server_port2", UNSET)

        auth_server_shared_secret2 = d.pop("auth_server_shared_secret2", UNSET)

        _wme = d.pop("wme", UNSET)
        wme: Union[Unset, WMESetting]
        if isinstance(_wme, Unset):
            wme = UNSET
        else:
            wme = WMESetting.from_dict(_wme)

        channel_width = d.pop("channel_width", UNSET)

        wireless_interface = cls(
            mode=mode,
            standard=standard,
            protmode=protmode,
            ssid=ssid,
            channel=channel,
            authmode=authmode,
            txpower=txpower,
            distance=distance,
            regdomain=regdomain,
            regcountry=regcountry,
            reglocation=reglocation,
            wpa=wpa,
            auth_server_addr=auth_server_addr,
            auth_server_port=auth_server_port,
            auth_server_shared_secret=auth_server_shared_secret,
            auth_server_addr2=auth_server_addr2,
            auth_server_port2=auth_server_port2,
            auth_server_shared_secret2=auth_server_shared_secret2,
            wme=wme,
            channel_width=channel_width,
        )

        wireless_interface.additional_properties = d
        return wireless_interface

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
