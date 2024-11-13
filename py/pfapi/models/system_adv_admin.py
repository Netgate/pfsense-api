from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_cert import SystemCert


T = TypeVar("T", bound="SystemAdvAdmin")


@_attrs_define
class SystemAdvAdmin:
    """
    Attributes:
        webguiproto (Union[Unset, str]):
        webguiport (Union[Unset, str]):
        max_procs (Union[Unset, int]):
        disablehttpredirect (Union[Unset, bool]):
        disablehsts (Union[Unset, bool]):
        ocsp_staple (Union[Unset, bool]):
        disableconsolemenu (Union[Unset, bool]):
        noantilockout (Union[Unset, bool]):
        nodnsrebindcheck (Union[Unset, bool]):
        nohttpreferercheck (Union[Unset, bool]):
        pagenamefirst (Union[Unset, bool]):
        loginautocomplete (Union[Unset, bool]):
        althostnames (Union[Unset, str]):
        enableserial (Union[Unset, bool]):
        serialspeed (Union[Unset, str]):
        primaryconsole (Union[Unset, str]):
        sshport (Union[Unset, str]):
        enablesshd (Union[Unset, bool]):
        sshdkeyonly (Union[Unset, str]):
        sshdagentforwarding (Union[Unset, bool]):
        quietlogin (Union[Unset, bool]):
        roaming (Union[Unset, bool]):
        sshguard_threshold (Union[Unset, str]):
        sshguard_blocktime (Union[Unset, str]):
        sshguard_detection_time (Union[Unset, str]):
        sshguard_whitelist (Union[Unset, str]):
        ssl_certref (Union[Unset, str]):
        certsavailable (Union[Unset, bool]):
        certlist (Union[Unset, List['SystemCert']]):
    """

    webguiproto: Union[Unset, str] = UNSET
    webguiport: Union[Unset, str] = UNSET
    max_procs: Union[Unset, int] = UNSET
    disablehttpredirect: Union[Unset, bool] = UNSET
    disablehsts: Union[Unset, bool] = UNSET
    ocsp_staple: Union[Unset, bool] = UNSET
    disableconsolemenu: Union[Unset, bool] = UNSET
    noantilockout: Union[Unset, bool] = UNSET
    nodnsrebindcheck: Union[Unset, bool] = UNSET
    nohttpreferercheck: Union[Unset, bool] = UNSET
    pagenamefirst: Union[Unset, bool] = UNSET
    loginautocomplete: Union[Unset, bool] = UNSET
    althostnames: Union[Unset, str] = UNSET
    enableserial: Union[Unset, bool] = UNSET
    serialspeed: Union[Unset, str] = UNSET
    primaryconsole: Union[Unset, str] = UNSET
    sshport: Union[Unset, str] = UNSET
    enablesshd: Union[Unset, bool] = UNSET
    sshdkeyonly: Union[Unset, str] = UNSET
    sshdagentforwarding: Union[Unset, bool] = UNSET
    quietlogin: Union[Unset, bool] = UNSET
    roaming: Union[Unset, bool] = UNSET
    sshguard_threshold: Union[Unset, str] = UNSET
    sshguard_blocktime: Union[Unset, str] = UNSET
    sshguard_detection_time: Union[Unset, str] = UNSET
    sshguard_whitelist: Union[Unset, str] = UNSET
    ssl_certref: Union[Unset, str] = UNSET
    certsavailable: Union[Unset, bool] = UNSET
    certlist: Union[Unset, List["SystemCert"]] = UNSET
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

        certlist: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.certlist, Unset):
            certlist = []
            for certlist_item_data in self.certlist:
                certlist_item = certlist_item_data.to_dict()
                certlist.append(certlist_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webguiproto is not UNSET:
            field_dict["webguiproto"] = webguiproto
        if webguiport is not UNSET:
            field_dict["webguiport"] = webguiport
        if max_procs is not UNSET:
            field_dict["max_procs"] = max_procs
        if disablehttpredirect is not UNSET:
            field_dict["disablehttpredirect"] = disablehttpredirect
        if disablehsts is not UNSET:
            field_dict["disablehsts"] = disablehsts
        if ocsp_staple is not UNSET:
            field_dict["ocsp_staple"] = ocsp_staple
        if disableconsolemenu is not UNSET:
            field_dict["disableconsolemenu"] = disableconsolemenu
        if noantilockout is not UNSET:
            field_dict["noantilockout"] = noantilockout
        if nodnsrebindcheck is not UNSET:
            field_dict["nodnsrebindcheck"] = nodnsrebindcheck
        if nohttpreferercheck is not UNSET:
            field_dict["nohttpreferercheck"] = nohttpreferercheck
        if pagenamefirst is not UNSET:
            field_dict["pagenamefirst"] = pagenamefirst
        if loginautocomplete is not UNSET:
            field_dict["loginautocomplete"] = loginautocomplete
        if althostnames is not UNSET:
            field_dict["althostnames"] = althostnames
        if enableserial is not UNSET:
            field_dict["enableserial"] = enableserial
        if serialspeed is not UNSET:
            field_dict["serialspeed"] = serialspeed
        if primaryconsole is not UNSET:
            field_dict["primaryconsole"] = primaryconsole
        if sshport is not UNSET:
            field_dict["sshport"] = sshport
        if enablesshd is not UNSET:
            field_dict["enablesshd"] = enablesshd
        if sshdkeyonly is not UNSET:
            field_dict["sshdkeyonly"] = sshdkeyonly
        if sshdagentforwarding is not UNSET:
            field_dict["sshdagentforwarding"] = sshdagentforwarding
        if quietlogin is not UNSET:
            field_dict["quietlogin"] = quietlogin
        if roaming is not UNSET:
            field_dict["roaming"] = roaming
        if sshguard_threshold is not UNSET:
            field_dict["sshguard_threshold"] = sshguard_threshold
        if sshguard_blocktime is not UNSET:
            field_dict["sshguard_blocktime"] = sshguard_blocktime
        if sshguard_detection_time is not UNSET:
            field_dict["sshguard_detection_time"] = sshguard_detection_time
        if sshguard_whitelist is not UNSET:
            field_dict["sshguard_whitelist"] = sshguard_whitelist
        if ssl_certref is not UNSET:
            field_dict["ssl_certref"] = ssl_certref
        if certsavailable is not UNSET:
            field_dict["certsavailable"] = certsavailable
        if certlist is not UNSET:
            field_dict["certlist"] = certlist

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_cert import SystemCert

        d = src_dict.copy()
        webguiproto = d.pop("webguiproto", UNSET)

        webguiport = d.pop("webguiport", UNSET)

        max_procs = d.pop("max_procs", UNSET)

        disablehttpredirect = d.pop("disablehttpredirect", UNSET)

        disablehsts = d.pop("disablehsts", UNSET)

        ocsp_staple = d.pop("ocsp_staple", UNSET)

        disableconsolemenu = d.pop("disableconsolemenu", UNSET)

        noantilockout = d.pop("noantilockout", UNSET)

        nodnsrebindcheck = d.pop("nodnsrebindcheck", UNSET)

        nohttpreferercheck = d.pop("nohttpreferercheck", UNSET)

        pagenamefirst = d.pop("pagenamefirst", UNSET)

        loginautocomplete = d.pop("loginautocomplete", UNSET)

        althostnames = d.pop("althostnames", UNSET)

        enableserial = d.pop("enableserial", UNSET)

        serialspeed = d.pop("serialspeed", UNSET)

        primaryconsole = d.pop("primaryconsole", UNSET)

        sshport = d.pop("sshport", UNSET)

        enablesshd = d.pop("enablesshd", UNSET)

        sshdkeyonly = d.pop("sshdkeyonly", UNSET)

        sshdagentforwarding = d.pop("sshdagentforwarding", UNSET)

        quietlogin = d.pop("quietlogin", UNSET)

        roaming = d.pop("roaming", UNSET)

        sshguard_threshold = d.pop("sshguard_threshold", UNSET)

        sshguard_blocktime = d.pop("sshguard_blocktime", UNSET)

        sshguard_detection_time = d.pop("sshguard_detection_time", UNSET)

        sshguard_whitelist = d.pop("sshguard_whitelist", UNSET)

        ssl_certref = d.pop("ssl_certref", UNSET)

        certsavailable = d.pop("certsavailable", UNSET)

        certlist = []
        _certlist = d.pop("certlist", UNSET)
        for certlist_item_data in _certlist or []:
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
