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
        zone (Union[Unset, str]):
        zoneid (Union[Unset, str]):
        descr (Union[Unset, str]):
        localauth_priv (Union[Unset, bool]):
        interface (Union[Unset, str]):
        maxproc (Union[Unset, str]):
        maxprocperip (Union[Unset, str]):
        timeout (Union[Unset, str]):
        idletime (Union[Unset, str]):
        trafficquota (Union[Unset, str]):
        freelogins_count (Union[Unset, str]):
        freelogins_resettimeout (Union[Unset, str]):
        freelogins_updatetimeouts (Union[Unset, bool]):
        logoutwin_enable (Union[Unset, bool]):
        enable (Union[Unset, bool]):
        auth_method (Union[Unset, str]):
        auth_server (Union[Unset, str]):
        auth_server2 (Union[Unset, str]):
        radmac_secret (Union[Unset, str]):
        radmac_fallback (Union[Unset, bool]):
        radiussession_timeout (Union[Unset, bool]):
        radiustraffic_quota (Union[Unset, bool]):
        radiusperuserbw (Union[Unset, bool]):
        radacct_enable (Union[Unset, bool]):
        radacct_server (Union[Unset, str]):
        reverseacct (Union[Unset, bool]):
        includeidletime (Union[Unset, bool]):
        reauthenticate (Union[Unset, bool]):
        preservedb (Union[Unset, bool]):
        reauthenticateacct (Union[Unset, str]):
        httpslogin (Union[Unset, bool]):
        httpsname (Union[Unset, str]):
        preauthurl (Union[Unset, str]):
        blockedmacsurl (Union[Unset, str]):
        certref (Union[Unset, str]):
        nohttpsforwards (Union[Unset, bool]):
        nomacfilter (Union[Unset, bool]):
        redirurl (Union[Unset, str]):
        passthrumacadd (Union[Unset, bool]):
        radmac_format (Union[Unset, str]):
        radiusnasid (Union[Unset, str]):
        customlogo (Union[Unset, bool]):
        custombg (Union[Unset, bool]):
        customhtml (Union[Unset, bool]):
        termsconditions (Union[Unset, str]):
        page (Union[Unset, str]):
        noconcurrentlogins (Union[Unset, str]):
        peruserbw (Union[Unset, bool]):
        bwdefaultdn (Union[Unset, str]):
        bwdefaultup (Union[Unset, str]):
        passthrumac (Union[Unset, List['PassthruMac']]):
        allowedip (Union[Unset, List['AllowedIP']]):
        allowedhostname (Union[Unset, List['AllowedHost']]):
        element (Union[Unset, List['CaptiveElement']]):
    """

    zone: Union[Unset, str] = UNSET
    zoneid: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    localauth_priv: Union[Unset, bool] = UNSET
    interface: Union[Unset, str] = UNSET
    maxproc: Union[Unset, str] = UNSET
    maxprocperip: Union[Unset, str] = UNSET
    timeout: Union[Unset, str] = UNSET
    idletime: Union[Unset, str] = UNSET
    trafficquota: Union[Unset, str] = UNSET
    freelogins_count: Union[Unset, str] = UNSET
    freelogins_resettimeout: Union[Unset, str] = UNSET
    freelogins_updatetimeouts: Union[Unset, bool] = UNSET
    logoutwin_enable: Union[Unset, bool] = UNSET
    enable: Union[Unset, bool] = UNSET
    auth_method: Union[Unset, str] = UNSET
    auth_server: Union[Unset, str] = UNSET
    auth_server2: Union[Unset, str] = UNSET
    radmac_secret: Union[Unset, str] = UNSET
    radmac_fallback: Union[Unset, bool] = UNSET
    radiussession_timeout: Union[Unset, bool] = UNSET
    radiustraffic_quota: Union[Unset, bool] = UNSET
    radiusperuserbw: Union[Unset, bool] = UNSET
    radacct_enable: Union[Unset, bool] = UNSET
    radacct_server: Union[Unset, str] = UNSET
    reverseacct: Union[Unset, bool] = UNSET
    includeidletime: Union[Unset, bool] = UNSET
    reauthenticate: Union[Unset, bool] = UNSET
    preservedb: Union[Unset, bool] = UNSET
    reauthenticateacct: Union[Unset, str] = UNSET
    httpslogin: Union[Unset, bool] = UNSET
    httpsname: Union[Unset, str] = UNSET
    preauthurl: Union[Unset, str] = UNSET
    blockedmacsurl: Union[Unset, str] = UNSET
    certref: Union[Unset, str] = UNSET
    nohttpsforwards: Union[Unset, bool] = UNSET
    nomacfilter: Union[Unset, bool] = UNSET
    redirurl: Union[Unset, str] = UNSET
    passthrumacadd: Union[Unset, bool] = UNSET
    radmac_format: Union[Unset, str] = UNSET
    radiusnasid: Union[Unset, str] = UNSET
    customlogo: Union[Unset, bool] = UNSET
    custombg: Union[Unset, bool] = UNSET
    customhtml: Union[Unset, bool] = UNSET
    termsconditions: Union[Unset, str] = UNSET
    page: Union[Unset, str] = UNSET
    noconcurrentlogins: Union[Unset, str] = UNSET
    peruserbw: Union[Unset, bool] = UNSET
    bwdefaultdn: Union[Unset, str] = UNSET
    bwdefaultup: Union[Unset, str] = UNSET
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
        field_dict.update({})
        if zone is not UNSET:
            field_dict["zone"] = zone
        if zoneid is not UNSET:
            field_dict["zoneid"] = zoneid
        if descr is not UNSET:
            field_dict["descr"] = descr
        if localauth_priv is not UNSET:
            field_dict["localauth_priv"] = localauth_priv
        if interface is not UNSET:
            field_dict["interface"] = interface
        if maxproc is not UNSET:
            field_dict["maxproc"] = maxproc
        if maxprocperip is not UNSET:
            field_dict["maxprocperip"] = maxprocperip
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if idletime is not UNSET:
            field_dict["idletime"] = idletime
        if trafficquota is not UNSET:
            field_dict["trafficquota"] = trafficquota
        if freelogins_count is not UNSET:
            field_dict["freelogins_count"] = freelogins_count
        if freelogins_resettimeout is not UNSET:
            field_dict["freelogins_resettimeout"] = freelogins_resettimeout
        if freelogins_updatetimeouts is not UNSET:
            field_dict["freelogins_updatetimeouts"] = freelogins_updatetimeouts
        if logoutwin_enable is not UNSET:
            field_dict["logoutwin_enable"] = logoutwin_enable
        if enable is not UNSET:
            field_dict["enable"] = enable
        if auth_method is not UNSET:
            field_dict["auth_method"] = auth_method
        if auth_server is not UNSET:
            field_dict["auth_server"] = auth_server
        if auth_server2 is not UNSET:
            field_dict["auth_server2"] = auth_server2
        if radmac_secret is not UNSET:
            field_dict["radmac_secret"] = radmac_secret
        if radmac_fallback is not UNSET:
            field_dict["radmac_fallback"] = radmac_fallback
        if radiussession_timeout is not UNSET:
            field_dict["radiussession_timeout"] = radiussession_timeout
        if radiustraffic_quota is not UNSET:
            field_dict["radiustraffic_quota"] = radiustraffic_quota
        if radiusperuserbw is not UNSET:
            field_dict["radiusperuserbw"] = radiusperuserbw
        if radacct_enable is not UNSET:
            field_dict["radacct_enable"] = radacct_enable
        if radacct_server is not UNSET:
            field_dict["radacct_server"] = radacct_server
        if reverseacct is not UNSET:
            field_dict["reverseacct"] = reverseacct
        if includeidletime is not UNSET:
            field_dict["includeidletime"] = includeidletime
        if reauthenticate is not UNSET:
            field_dict["reauthenticate"] = reauthenticate
        if preservedb is not UNSET:
            field_dict["preservedb"] = preservedb
        if reauthenticateacct is not UNSET:
            field_dict["reauthenticateacct"] = reauthenticateacct
        if httpslogin is not UNSET:
            field_dict["httpslogin"] = httpslogin
        if httpsname is not UNSET:
            field_dict["httpsname"] = httpsname
        if preauthurl is not UNSET:
            field_dict["preauthurl"] = preauthurl
        if blockedmacsurl is not UNSET:
            field_dict["blockedmacsurl"] = blockedmacsurl
        if certref is not UNSET:
            field_dict["certref"] = certref
        if nohttpsforwards is not UNSET:
            field_dict["nohttpsforwards"] = nohttpsforwards
        if nomacfilter is not UNSET:
            field_dict["nomacfilter"] = nomacfilter
        if redirurl is not UNSET:
            field_dict["redirurl"] = redirurl
        if passthrumacadd is not UNSET:
            field_dict["passthrumacadd"] = passthrumacadd
        if radmac_format is not UNSET:
            field_dict["radmac_format"] = radmac_format
        if radiusnasid is not UNSET:
            field_dict["radiusnasid"] = radiusnasid
        if customlogo is not UNSET:
            field_dict["customlogo"] = customlogo
        if custombg is not UNSET:
            field_dict["custombg"] = custombg
        if customhtml is not UNSET:
            field_dict["customhtml"] = customhtml
        if termsconditions is not UNSET:
            field_dict["termsconditions"] = termsconditions
        if page is not UNSET:
            field_dict["page"] = page
        if noconcurrentlogins is not UNSET:
            field_dict["noconcurrentlogins"] = noconcurrentlogins
        if peruserbw is not UNSET:
            field_dict["peruserbw"] = peruserbw
        if bwdefaultdn is not UNSET:
            field_dict["bwdefaultdn"] = bwdefaultdn
        if bwdefaultup is not UNSET:
            field_dict["bwdefaultup"] = bwdefaultup
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
        zone = d.pop("zone", UNSET)

        zoneid = d.pop("zoneid", UNSET)

        descr = d.pop("descr", UNSET)

        localauth_priv = d.pop("localauth_priv", UNSET)

        interface = d.pop("interface", UNSET)

        maxproc = d.pop("maxproc", UNSET)

        maxprocperip = d.pop("maxprocperip", UNSET)

        timeout = d.pop("timeout", UNSET)

        idletime = d.pop("idletime", UNSET)

        trafficquota = d.pop("trafficquota", UNSET)

        freelogins_count = d.pop("freelogins_count", UNSET)

        freelogins_resettimeout = d.pop("freelogins_resettimeout", UNSET)

        freelogins_updatetimeouts = d.pop("freelogins_updatetimeouts", UNSET)

        logoutwin_enable = d.pop("logoutwin_enable", UNSET)

        enable = d.pop("enable", UNSET)

        auth_method = d.pop("auth_method", UNSET)

        auth_server = d.pop("auth_server", UNSET)

        auth_server2 = d.pop("auth_server2", UNSET)

        radmac_secret = d.pop("radmac_secret", UNSET)

        radmac_fallback = d.pop("radmac_fallback", UNSET)

        radiussession_timeout = d.pop("radiussession_timeout", UNSET)

        radiustraffic_quota = d.pop("radiustraffic_quota", UNSET)

        radiusperuserbw = d.pop("radiusperuserbw", UNSET)

        radacct_enable = d.pop("radacct_enable", UNSET)

        radacct_server = d.pop("radacct_server", UNSET)

        reverseacct = d.pop("reverseacct", UNSET)

        includeidletime = d.pop("includeidletime", UNSET)

        reauthenticate = d.pop("reauthenticate", UNSET)

        preservedb = d.pop("preservedb", UNSET)

        reauthenticateacct = d.pop("reauthenticateacct", UNSET)

        httpslogin = d.pop("httpslogin", UNSET)

        httpsname = d.pop("httpsname", UNSET)

        preauthurl = d.pop("preauthurl", UNSET)

        blockedmacsurl = d.pop("blockedmacsurl", UNSET)

        certref = d.pop("certref", UNSET)

        nohttpsforwards = d.pop("nohttpsforwards", UNSET)

        nomacfilter = d.pop("nomacfilter", UNSET)

        redirurl = d.pop("redirurl", UNSET)

        passthrumacadd = d.pop("passthrumacadd", UNSET)

        radmac_format = d.pop("radmac_format", UNSET)

        radiusnasid = d.pop("radiusnasid", UNSET)

        customlogo = d.pop("customlogo", UNSET)

        custombg = d.pop("custombg", UNSET)

        customhtml = d.pop("customhtml", UNSET)

        termsconditions = d.pop("termsconditions", UNSET)

        page = d.pop("page", UNSET)

        noconcurrentlogins = d.pop("noconcurrentlogins", UNSET)

        peruserbw = d.pop("peruserbw", UNSET)

        bwdefaultdn = d.pop("bwdefaultdn", UNSET)

        bwdefaultup = d.pop("bwdefaultup", UNSET)

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
