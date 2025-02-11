from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allowed_host import AllowedHost
    from ..models.allowed_ip import AllowedIP
    from ..models.captive_element import CaptiveElement
    from ..models.passthru_mac import PassthruMac


T = TypeVar("T", bound="CaptivePortalConfig")


@_attrs_define
class CaptivePortalConfig:
    """
    Attributes:
        zone (str):
        zoneid (str):
        descr (str):
        localauth_priv (bool):
        interface (str):
        maxproc (str):
        maxprocperip (str):
        timeout (str):
        idletime (str):
        trafficquota (str):
        freelogins_count (str):
        freelogins_resettimeout (str):
        freelogins_updatetimeouts (bool):
        logoutwin_enable (bool):
        enable (bool):
        auth_method (str):
        auth_server (str):
        auth_server2 (str):
        radmac_secret (str):
        radmac_fallback (bool):
        radiussession_timeout (bool):
        radiustraffic_quota (bool):
        radiusperuserbw (bool):
        radacct_enable (bool):
        radacct_server (str):
        reverseacct (bool):
        includeidletime (bool):
        reauthenticate (bool):
        preservedb (bool):
        reauthenticateacct (str):
        httpslogin (bool):
        httpsname (str):
        preauthurl (str):
        blockedmacsurl (str):
        certref (str):
        nohttpsforwards (bool):
        nomacfilter (bool):
        redirurl (str):
        passthrumacadd (bool):
        radmac_format (str):
        radiusnasid (str):
        customlogo (bool):
        custombg (bool):
        customhtml (bool):
        termsconditions (str):
        page (str):
        noconcurrentlogins (str):
        peruserbw (bool):
        bwdefaultdn (str):
        bwdefaultup (str):
        passthrumac (Union[Unset, List['PassthruMac']]):
        allowedip (Union[Unset, List['AllowedIP']]):
        allowedhostname (Union[Unset, List['AllowedHost']]):
        element (Union[Unset, List['CaptiveElement']]):
    """

    zone: str
    zoneid: str
    descr: str
    localauth_priv: bool
    interface: str
    maxproc: str
    maxprocperip: str
    timeout: str
    idletime: str
    trafficquota: str
    freelogins_count: str
    freelogins_resettimeout: str
    freelogins_updatetimeouts: bool
    logoutwin_enable: bool
    enable: bool
    auth_method: str
    auth_server: str
    auth_server2: str
    radmac_secret: str
    radmac_fallback: bool
    radiussession_timeout: bool
    radiustraffic_quota: bool
    radiusperuserbw: bool
    radacct_enable: bool
    radacct_server: str
    reverseacct: bool
    includeidletime: bool
    reauthenticate: bool
    preservedb: bool
    reauthenticateacct: str
    httpslogin: bool
    httpsname: str
    preauthurl: str
    blockedmacsurl: str
    certref: str
    nohttpsforwards: bool
    nomacfilter: bool
    redirurl: str
    passthrumacadd: bool
    radmac_format: str
    radiusnasid: str
    customlogo: bool
    custombg: bool
    customhtml: bool
    termsconditions: str
    page: str
    noconcurrentlogins: str
    peruserbw: bool
    bwdefaultdn: str
    bwdefaultup: str
    passthrumac: Union[Unset, List["PassthruMac"]] = UNSET
    allowedip: Union[Unset, List["AllowedIP"]] = UNSET
    allowedhostname: Union[Unset, List["AllowedHost"]] = UNSET
    element: Union[Unset, List["CaptiveElement"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        zone = self.zone

        zoneid = self.zoneid

        descr = self.descr

        localauth_priv = self.localauth_priv

        interface = self.interface

        maxproc = self.maxproc

        maxprocperip = self.maxprocperip

        timeout = self.timeout

        idletime = self.idletime

        trafficquota = self.trafficquota

        freelogins_count = self.freelogins_count

        freelogins_resettimeout = self.freelogins_resettimeout

        freelogins_updatetimeouts = self.freelogins_updatetimeouts

        logoutwin_enable = self.logoutwin_enable

        enable = self.enable

        auth_method = self.auth_method

        auth_server = self.auth_server

        auth_server2 = self.auth_server2

        radmac_secret = self.radmac_secret

        radmac_fallback = self.radmac_fallback

        radiussession_timeout = self.radiussession_timeout

        radiustraffic_quota = self.radiustraffic_quota

        radiusperuserbw = self.radiusperuserbw

        radacct_enable = self.radacct_enable

        radacct_server = self.radacct_server

        reverseacct = self.reverseacct

        includeidletime = self.includeidletime

        reauthenticate = self.reauthenticate

        preservedb = self.preservedb

        reauthenticateacct = self.reauthenticateacct

        httpslogin = self.httpslogin

        httpsname = self.httpsname

        preauthurl = self.preauthurl

        blockedmacsurl = self.blockedmacsurl

        certref = self.certref

        nohttpsforwards = self.nohttpsforwards

        nomacfilter = self.nomacfilter

        redirurl = self.redirurl

        passthrumacadd = self.passthrumacadd

        radmac_format = self.radmac_format

        radiusnasid = self.radiusnasid

        customlogo = self.customlogo

        custombg = self.custombg

        customhtml = self.customhtml

        termsconditions = self.termsconditions

        page = self.page

        noconcurrentlogins = self.noconcurrentlogins

        peruserbw = self.peruserbw

        bwdefaultdn = self.bwdefaultdn

        bwdefaultup = self.bwdefaultup

        passthrumac: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.passthrumac, Unset):
            passthrumac = []
            for passthrumac_item_data in self.passthrumac:
                passthrumac_item = passthrumac_item_data.to_dict()
                passthrumac.append(passthrumac_item)

        allowedip: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.allowedip, Unset):
            allowedip = []
            for allowedip_item_data in self.allowedip:
                allowedip_item = allowedip_item_data.to_dict()
                allowedip.append(allowedip_item)

        allowedhostname: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.allowedhostname, Unset):
            allowedhostname = []
            for allowedhostname_item_data in self.allowedhostname:
                allowedhostname_item = allowedhostname_item_data.to_dict()
                allowedhostname.append(allowedhostname_item)

        element: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.element, Unset):
            element = []
            for element_item_data in self.element:
                element_item = element_item_data.to_dict()
                element.append(element_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "zone": zone,
                "zoneid": zoneid,
                "descr": descr,
                "localauth_priv": localauth_priv,
                "interface": interface,
                "maxproc": maxproc,
                "maxprocperip": maxprocperip,
                "timeout": timeout,
                "idletime": idletime,
                "trafficquota": trafficquota,
                "freelogins_count": freelogins_count,
                "freelogins_resettimeout": freelogins_resettimeout,
                "freelogins_updatetimeouts": freelogins_updatetimeouts,
                "logoutwin_enable": logoutwin_enable,
                "enable": enable,
                "auth_method": auth_method,
                "auth_server": auth_server,
                "auth_server2": auth_server2,
                "radmac_secret": radmac_secret,
                "radmac_fallback": radmac_fallback,
                "radiussession_timeout": radiussession_timeout,
                "radiustraffic_quota": radiustraffic_quota,
                "radiusperuserbw": radiusperuserbw,
                "radacct_enable": radacct_enable,
                "radacct_server": radacct_server,
                "reverseacct": reverseacct,
                "includeidletime": includeidletime,
                "reauthenticate": reauthenticate,
                "preservedb": preservedb,
                "reauthenticateacct": reauthenticateacct,
                "httpslogin": httpslogin,
                "httpsname": httpsname,
                "preauthurl": preauthurl,
                "blockedmacsurl": blockedmacsurl,
                "certref": certref,
                "nohttpsforwards": nohttpsforwards,
                "nomacfilter": nomacfilter,
                "redirurl": redirurl,
                "passthrumacadd": passthrumacadd,
                "radmac_format": radmac_format,
                "radiusnasid": radiusnasid,
                "customlogo": customlogo,
                "custombg": custombg,
                "customhtml": customhtml,
                "termsconditions": termsconditions,
                "page": page,
                "noconcurrentlogins": noconcurrentlogins,
                "peruserbw": peruserbw,
                "bwdefaultdn": bwdefaultdn,
                "bwdefaultup": bwdefaultup,
            }
        )
        if passthrumac is not UNSET:
            field_dict["passthrumac"] = passthrumac
        if allowedip is not UNSET:
            field_dict["allowedip"] = allowedip
        if allowedhostname is not UNSET:
            field_dict["allowedhostname"] = allowedhostname
        if element is not UNSET:
            field_dict["element"] = element

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.allowed_host import AllowedHost
        from ..models.allowed_ip import AllowedIP
        from ..models.captive_element import CaptiveElement
        from ..models.passthru_mac import PassthruMac

        d = src_dict.copy()
        zone = d.pop("zone")

        zoneid = d.pop("zoneid")

        descr = d.pop("descr")

        localauth_priv = d.pop("localauth_priv")

        interface = d.pop("interface")

        maxproc = d.pop("maxproc")

        maxprocperip = d.pop("maxprocperip")

        timeout = d.pop("timeout")

        idletime = d.pop("idletime")

        trafficquota = d.pop("trafficquota")

        freelogins_count = d.pop("freelogins_count")

        freelogins_resettimeout = d.pop("freelogins_resettimeout")

        freelogins_updatetimeouts = d.pop("freelogins_updatetimeouts")

        logoutwin_enable = d.pop("logoutwin_enable")

        enable = d.pop("enable")

        auth_method = d.pop("auth_method")

        auth_server = d.pop("auth_server")

        auth_server2 = d.pop("auth_server2")

        radmac_secret = d.pop("radmac_secret")

        radmac_fallback = d.pop("radmac_fallback")

        radiussession_timeout = d.pop("radiussession_timeout")

        radiustraffic_quota = d.pop("radiustraffic_quota")

        radiusperuserbw = d.pop("radiusperuserbw")

        radacct_enable = d.pop("radacct_enable")

        radacct_server = d.pop("radacct_server")

        reverseacct = d.pop("reverseacct")

        includeidletime = d.pop("includeidletime")

        reauthenticate = d.pop("reauthenticate")

        preservedb = d.pop("preservedb")

        reauthenticateacct = d.pop("reauthenticateacct")

        httpslogin = d.pop("httpslogin")

        httpsname = d.pop("httpsname")

        preauthurl = d.pop("preauthurl")

        blockedmacsurl = d.pop("blockedmacsurl")

        certref = d.pop("certref")

        nohttpsforwards = d.pop("nohttpsforwards")

        nomacfilter = d.pop("nomacfilter")

        redirurl = d.pop("redirurl")

        passthrumacadd = d.pop("passthrumacadd")

        radmac_format = d.pop("radmac_format")

        radiusnasid = d.pop("radiusnasid")

        customlogo = d.pop("customlogo")

        custombg = d.pop("custombg")

        customhtml = d.pop("customhtml")

        termsconditions = d.pop("termsconditions")

        page = d.pop("page")

        noconcurrentlogins = d.pop("noconcurrentlogins")

        peruserbw = d.pop("peruserbw")

        bwdefaultdn = d.pop("bwdefaultdn")

        bwdefaultup = d.pop("bwdefaultup")

        passthrumac = []
        _passthrumac = d.pop("passthrumac", UNSET)
        for passthrumac_item_data in _passthrumac or []:
            passthrumac_item = PassthruMac.from_dict(passthrumac_item_data)

            passthrumac.append(passthrumac_item)

        allowedip = []
        _allowedip = d.pop("allowedip", UNSET)
        for allowedip_item_data in _allowedip or []:
            allowedip_item = AllowedIP.from_dict(allowedip_item_data)

            allowedip.append(allowedip_item)

        allowedhostname = []
        _allowedhostname = d.pop("allowedhostname", UNSET)
        for allowedhostname_item_data in _allowedhostname or []:
            allowedhostname_item = AllowedHost.from_dict(allowedhostname_item_data)

            allowedhostname.append(allowedhostname_item)

        element = []
        _element = d.pop("element", UNSET)
        for element_item_data in _element or []:
            element_item = CaptiveElement.from_dict(element_item_data)

            element.append(element_item)

        captive_portal_config = cls(
            zone=zone,
            zoneid=zoneid,
            descr=descr,
            localauth_priv=localauth_priv,
            interface=interface,
            maxproc=maxproc,
            maxprocperip=maxprocperip,
            timeout=timeout,
            idletime=idletime,
            trafficquota=trafficquota,
            freelogins_count=freelogins_count,
            freelogins_resettimeout=freelogins_resettimeout,
            freelogins_updatetimeouts=freelogins_updatetimeouts,
            logoutwin_enable=logoutwin_enable,
            enable=enable,
            auth_method=auth_method,
            auth_server=auth_server,
            auth_server2=auth_server2,
            radmac_secret=radmac_secret,
            radmac_fallback=radmac_fallback,
            radiussession_timeout=radiussession_timeout,
            radiustraffic_quota=radiustraffic_quota,
            radiusperuserbw=radiusperuserbw,
            radacct_enable=radacct_enable,
            radacct_server=radacct_server,
            reverseacct=reverseacct,
            includeidletime=includeidletime,
            reauthenticate=reauthenticate,
            preservedb=preservedb,
            reauthenticateacct=reauthenticateacct,
            httpslogin=httpslogin,
            httpsname=httpsname,
            preauthurl=preauthurl,
            blockedmacsurl=blockedmacsurl,
            certref=certref,
            nohttpsforwards=nohttpsforwards,
            nomacfilter=nomacfilter,
            redirurl=redirurl,
            passthrumacadd=passthrumacadd,
            radmac_format=radmac_format,
            radiusnasid=radiusnasid,
            customlogo=customlogo,
            custombg=custombg,
            customhtml=customhtml,
            termsconditions=termsconditions,
            page=page,
            noconcurrentlogins=noconcurrentlogins,
            peruserbw=peruserbw,
            bwdefaultdn=bwdefaultdn,
            bwdefaultup=bwdefaultup,
            passthrumac=passthrumac,
            allowedip=allowedip,
            allowedhostname=allowedhostname,
            element=element,
        )

        captive_portal_config.additional_properties = d
        return captive_portal_config

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
