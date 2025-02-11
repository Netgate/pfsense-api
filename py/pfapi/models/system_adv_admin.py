from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.system_cert import SystemCert


T = TypeVar("T", bound="SystemAdvAdmin")


@_attrs_define
class SystemAdvAdmin:
    """
    Attributes:
        webguiproto (str):
        webguiport (str):
        max_procs (int):
        disablehttpredirect (bool):
        disablehsts (bool):
        ocsp_staple (bool):
        disableconsolemenu (bool):
        noantilockout (bool):
        nodnsrebindcheck (bool):
        nohttpreferercheck (bool):
        pagenamefirst (bool):
        loginautocomplete (bool):
        althostnames (str):
        enableserial (bool):
        serialspeed (str):
        primaryconsole (str):
        sshport (str):
        enablesshd (bool):
        sshdkeyonly (str):
        sshdagentforwarding (bool):
        quietlogin (bool):
        roaming (bool):
        sshguard_threshold (str):
        sshguard_blocktime (str):
        sshguard_detection_time (str):
        sshguard_whitelist (str):
        ssl_certref (str):
        certsavailable (bool):
        certlist (List['SystemCert']):
    """

    webguiproto: str
    webguiport: str
    max_procs: int
    disablehttpredirect: bool
    disablehsts: bool
    ocsp_staple: bool
    disableconsolemenu: bool
    noantilockout: bool
    nodnsrebindcheck: bool
    nohttpreferercheck: bool
    pagenamefirst: bool
    loginautocomplete: bool
    althostnames: str
    enableserial: bool
    serialspeed: str
    primaryconsole: str
    sshport: str
    enablesshd: bool
    sshdkeyonly: str
    sshdagentforwarding: bool
    quietlogin: bool
    roaming: bool
    sshguard_threshold: str
    sshguard_blocktime: str
    sshguard_detection_time: str
    sshguard_whitelist: str
    ssl_certref: str
    certsavailable: bool
    certlist: List["SystemCert"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        webguiproto = self.webguiproto

        webguiport = self.webguiport

        max_procs = self.max_procs

        disablehttpredirect = self.disablehttpredirect

        disablehsts = self.disablehsts

        ocsp_staple = self.ocsp_staple

        disableconsolemenu = self.disableconsolemenu

        noantilockout = self.noantilockout

        nodnsrebindcheck = self.nodnsrebindcheck

        nohttpreferercheck = self.nohttpreferercheck

        pagenamefirst = self.pagenamefirst

        loginautocomplete = self.loginautocomplete

        althostnames = self.althostnames

        enableserial = self.enableserial

        serialspeed = self.serialspeed

        primaryconsole = self.primaryconsole

        sshport = self.sshport

        enablesshd = self.enablesshd

        sshdkeyonly = self.sshdkeyonly

        sshdagentforwarding = self.sshdagentforwarding

        quietlogin = self.quietlogin

        roaming = self.roaming

        sshguard_threshold = self.sshguard_threshold

        sshguard_blocktime = self.sshguard_blocktime

        sshguard_detection_time = self.sshguard_detection_time

        sshguard_whitelist = self.sshguard_whitelist

        ssl_certref = self.ssl_certref

        certsavailable = self.certsavailable

        certlist = []
        for certlist_item_data in self.certlist:
            certlist_item = certlist_item_data.to_dict()
            certlist.append(certlist_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "webguiproto": webguiproto,
                "webguiport": webguiport,
                "max_procs": max_procs,
                "disablehttpredirect": disablehttpredirect,
                "disablehsts": disablehsts,
                "ocsp_staple": ocsp_staple,
                "disableconsolemenu": disableconsolemenu,
                "noantilockout": noantilockout,
                "nodnsrebindcheck": nodnsrebindcheck,
                "nohttpreferercheck": nohttpreferercheck,
                "pagenamefirst": pagenamefirst,
                "loginautocomplete": loginautocomplete,
                "althostnames": althostnames,
                "enableserial": enableserial,
                "serialspeed": serialspeed,
                "primaryconsole": primaryconsole,
                "sshport": sshport,
                "enablesshd": enablesshd,
                "sshdkeyonly": sshdkeyonly,
                "sshdagentforwarding": sshdagentforwarding,
                "quietlogin": quietlogin,
                "roaming": roaming,
                "sshguard_threshold": sshguard_threshold,
                "sshguard_blocktime": sshguard_blocktime,
                "sshguard_detection_time": sshguard_detection_time,
                "sshguard_whitelist": sshguard_whitelist,
                "ssl_certref": ssl_certref,
                "certsavailable": certsavailable,
                "certlist": certlist,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_cert import SystemCert

        d = src_dict.copy()
        webguiproto = d.pop("webguiproto")

        webguiport = d.pop("webguiport")

        max_procs = d.pop("max_procs")

        disablehttpredirect = d.pop("disablehttpredirect")

        disablehsts = d.pop("disablehsts")

        ocsp_staple = d.pop("ocsp_staple")

        disableconsolemenu = d.pop("disableconsolemenu")

        noantilockout = d.pop("noantilockout")

        nodnsrebindcheck = d.pop("nodnsrebindcheck")

        nohttpreferercheck = d.pop("nohttpreferercheck")

        pagenamefirst = d.pop("pagenamefirst")

        loginautocomplete = d.pop("loginautocomplete")

        althostnames = d.pop("althostnames")

        enableserial = d.pop("enableserial")

        serialspeed = d.pop("serialspeed")

        primaryconsole = d.pop("primaryconsole")

        sshport = d.pop("sshport")

        enablesshd = d.pop("enablesshd")

        sshdkeyonly = d.pop("sshdkeyonly")

        sshdagentforwarding = d.pop("sshdagentforwarding")

        quietlogin = d.pop("quietlogin")

        roaming = d.pop("roaming")

        sshguard_threshold = d.pop("sshguard_threshold")

        sshguard_blocktime = d.pop("sshguard_blocktime")

        sshguard_detection_time = d.pop("sshguard_detection_time")

        sshguard_whitelist = d.pop("sshguard_whitelist")

        ssl_certref = d.pop("ssl_certref")

        certsavailable = d.pop("certsavailable")

        certlist = []
        _certlist = d.pop("certlist")
        for certlist_item_data in _certlist:
            certlist_item = SystemCert.from_dict(certlist_item_data)

            certlist.append(certlist_item)

        system_adv_admin = cls(
            webguiproto=webguiproto,
            webguiport=webguiport,
            max_procs=max_procs,
            disablehttpredirect=disablehttpredirect,
            disablehsts=disablehsts,
            ocsp_staple=ocsp_staple,
            disableconsolemenu=disableconsolemenu,
            noantilockout=noantilockout,
            nodnsrebindcheck=nodnsrebindcheck,
            nohttpreferercheck=nohttpreferercheck,
            pagenamefirst=pagenamefirst,
            loginautocomplete=loginautocomplete,
            althostnames=althostnames,
            enableserial=enableserial,
            serialspeed=serialspeed,
            primaryconsole=primaryconsole,
            sshport=sshport,
            enablesshd=enablesshd,
            sshdkeyonly=sshdkeyonly,
            sshdagentforwarding=sshdagentforwarding,
            quietlogin=quietlogin,
            roaming=roaming,
            sshguard_threshold=sshguard_threshold,
            sshguard_blocktime=sshguard_blocktime,
            sshguard_detection_time=sshguard_detection_time,
            sshguard_whitelist=sshguard_whitelist,
            ssl_certref=ssl_certref,
            certsavailable=certsavailable,
            certlist=certlist,
        )

        system_adv_admin.additional_properties = d
        return system_adv_admin

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
