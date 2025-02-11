from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.wme_setting import WMESetting
    from ..models.wpa_setting import WPASetting


T = TypeVar("T", bound="WirelessInterface")


@_attrs_define
class WirelessInterface:
    """
    Attributes:
        mode (str):
        standard (str):
        protmode (str):
        ssid (str):
        channel (str):
        authmode (str):
        txpower (str):
        distance (str):
        regdomain (str):
        regcountry (str):
        reglocation (str):
        wpa (WPASetting):
        auth_server_addr (str):
        auth_server_port (str):
        auth_server_shared_secret (str):
        auth_server_addr2 (str):
        auth_server_port2 (str):
        auth_server_shared_secret2 (str):
        wme (WMESetting):
        channel_width (str):
    """

    mode: str
    standard: str
    protmode: str
    ssid: str
    channel: str
    authmode: str
    txpower: str
    distance: str
    regdomain: str
    regcountry: str
    reglocation: str
    wpa: "WPASetting"
    auth_server_addr: str
    auth_server_port: str
    auth_server_shared_secret: str
    auth_server_addr2: str
    auth_server_port2: str
    auth_server_shared_secret2: str
    wme: "WMESetting"
    channel_width: str
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

        wpa = self.wpa.to_dict()

        auth_server_addr = self.auth_server_addr

        auth_server_port = self.auth_server_port

        auth_server_shared_secret = self.auth_server_shared_secret

        auth_server_addr2 = self.auth_server_addr2

        auth_server_port2 = self.auth_server_port2

        auth_server_shared_secret2 = self.auth_server_shared_secret2

        wme = self.wme.to_dict()

        channel_width = self.channel_width

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "standard": standard,
                "protmode": protmode,
                "ssid": ssid,
                "channel": channel,
                "authmode": authmode,
                "txpower": txpower,
                "distance": distance,
                "regdomain": regdomain,
                "regcountry": regcountry,
                "reglocation": reglocation,
                "wpa": wpa,
                "auth_server_addr": auth_server_addr,
                "auth_server_port": auth_server_port,
                "auth_server_shared_secret": auth_server_shared_secret,
                "auth_server_addr2": auth_server_addr2,
                "auth_server_port2": auth_server_port2,
                "auth_server_shared_secret2": auth_server_shared_secret2,
                "wme": wme,
                "channel_width": channel_width,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wme_setting import WMESetting
        from ..models.wpa_setting import WPASetting

        d = src_dict.copy()
        mode = d.pop("mode")

        standard = d.pop("standard")

        protmode = d.pop("protmode")

        ssid = d.pop("ssid")

        channel = d.pop("channel")

        authmode = d.pop("authmode")

        txpower = d.pop("txpower")

        distance = d.pop("distance")

        regdomain = d.pop("regdomain")

        regcountry = d.pop("regcountry")

        reglocation = d.pop("reglocation")

        wpa = WPASetting.from_dict(d.pop("wpa"))

        auth_server_addr = d.pop("auth_server_addr")

        auth_server_port = d.pop("auth_server_port")

        auth_server_shared_secret = d.pop("auth_server_shared_secret")

        auth_server_addr2 = d.pop("auth_server_addr2")

        auth_server_port2 = d.pop("auth_server_port2")

        auth_server_shared_secret2 = d.pop("auth_server_shared_secret2")

        wme = WMESetting.from_dict(d.pop("wme"))

        channel_width = d.pop("channel_width")

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
