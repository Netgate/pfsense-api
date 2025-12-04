from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.captive_allowed_host import CaptiveAllowedHost
    from ..models.captive_allowed_ip import CaptiveAllowedIP
    from ..models.captive_element import CaptiveElement
    from ..models.captive_passthru_mac import CaptivePassthruMac


T = TypeVar("T", bound="CaptivePortalConfig")


@_attrs_define
class CaptivePortalConfig:
    """
    Attributes:
        zone (str):
        zoneid (str | Unset): optional, 0-57535
        descr (str | Unset):
        localauth_priv (bool | Unset):
        interface (str | Unset):
        maxproc (str | Unset):
        maxprocperip (str | Unset):
        timeout (str | Unset):
        idletimeout (str | Unset):
        trafficquota (str | Unset):
        freelogins_count (str | Unset):
        freelogins_resettimeout (str | Unset):
        freelogins_updatetimeouts (bool | Unset):
        logoutwin_enable (bool | Unset):
        enable (bool | Unset):
        auth_method (str | Unset):
        auth_server (str | Unset):
        auth_server2 (str | Unset):
        radmac_secret (str | Unset):
        radmac_fallback (bool | Unset):
        radiussession_timeout (bool | Unset):
        radiustraffic_quota (bool | Unset):
        radiusperuserbw (bool | Unset):
        radacct_enable (bool | Unset):
        radacct_server (str | Unset):
        reverseacct (bool | Unset):
        includeidletime (bool | Unset):
        reauthenticate (bool | Unset):
        preservedb (bool | Unset):
        reauthenticateacct (str | Unset):
        httpslogin (bool | Unset):
        httpsname (str | Unset):
        preauthurl (str | Unset):
        blockedmacsurl (str | Unset):
        certref (str | Unset):
        nohttpsforwards (bool | Unset):
        nomacfilter (bool | Unset):
        redirurl (str | Unset):
        passthrumacadd (bool | Unset):
        radmac_format (str | Unset):
        radiusnasid (str | Unset):
        customlogo (bool | Unset):
        custombg (bool | Unset):
        customhtml (bool | Unset):
        termsconditions (str | Unset):
        page (str | Unset):
        noconcurrentlogins (str | Unset):
        peruserbw (bool | Unset):
        bwdefaultdn (str | Unset):
        bwdefaultup (str | Unset):
        enablebackwardsync (bool | Unset):
        backwardsyncip (str | Unset):
        backwardsyncuser (str | Unset):
        backwardsyncpassword (str | Unset):
        passthrumac (list[CaptivePassthruMac] | Unset):
        allowedip (list[CaptiveAllowedIP] | Unset):
        allowedhostname (list[CaptiveAllowedHost] | Unset):
        element (list[CaptiveElement] | Unset):
    """

    zone: str
    zoneid: str | Unset = UNSET
    descr: str | Unset = UNSET
    localauth_priv: bool | Unset = UNSET
    interface: str | Unset = UNSET
    maxproc: str | Unset = UNSET
    maxprocperip: str | Unset = UNSET
    timeout: str | Unset = UNSET
    idletimeout: str | Unset = UNSET
    trafficquota: str | Unset = UNSET
    freelogins_count: str | Unset = UNSET
    freelogins_resettimeout: str | Unset = UNSET
    freelogins_updatetimeouts: bool | Unset = UNSET
    logoutwin_enable: bool | Unset = UNSET
    enable: bool | Unset = UNSET
    auth_method: str | Unset = UNSET
    auth_server: str | Unset = UNSET
    auth_server2: str | Unset = UNSET
    radmac_secret: str | Unset = UNSET
    radmac_fallback: bool | Unset = UNSET
    radiussession_timeout: bool | Unset = UNSET
    radiustraffic_quota: bool | Unset = UNSET
    radiusperuserbw: bool | Unset = UNSET
    radacct_enable: bool | Unset = UNSET
    radacct_server: str | Unset = UNSET
    reverseacct: bool | Unset = UNSET
    includeidletime: bool | Unset = UNSET
    reauthenticate: bool | Unset = UNSET
    preservedb: bool | Unset = UNSET
    reauthenticateacct: str | Unset = UNSET
    httpslogin: bool | Unset = UNSET
    httpsname: str | Unset = UNSET
    preauthurl: str | Unset = UNSET
    blockedmacsurl: str | Unset = UNSET
    certref: str | Unset = UNSET
    nohttpsforwards: bool | Unset = UNSET
    nomacfilter: bool | Unset = UNSET
    redirurl: str | Unset = UNSET
    passthrumacadd: bool | Unset = UNSET
    radmac_format: str | Unset = UNSET
    radiusnasid: str | Unset = UNSET
    customlogo: bool | Unset = UNSET
    custombg: bool | Unset = UNSET
    customhtml: bool | Unset = UNSET
    termsconditions: str | Unset = UNSET
    page: str | Unset = UNSET
    noconcurrentlogins: str | Unset = UNSET
    peruserbw: bool | Unset = UNSET
    bwdefaultdn: str | Unset = UNSET
    bwdefaultup: str | Unset = UNSET
    enablebackwardsync: bool | Unset = UNSET
    backwardsyncip: str | Unset = UNSET
    backwardsyncuser: str | Unset = UNSET
    backwardsyncpassword: str | Unset = UNSET
    passthrumac: list[CaptivePassthruMac] | Unset = UNSET
    allowedip: list[CaptiveAllowedIP] | Unset = UNSET
    allowedhostname: list[CaptiveAllowedHost] | Unset = UNSET
    element: list[CaptiveElement] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        zone = self.zone

        zoneid = self.zoneid

        descr = self.descr

        localauth_priv = self.localauth_priv

        interface = self.interface

        maxproc = self.maxproc

        maxprocperip = self.maxprocperip

        timeout = self.timeout

        idletimeout = self.idletimeout

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

        enablebackwardsync = self.enablebackwardsync

        backwardsyncip = self.backwardsyncip

        backwardsyncuser = self.backwardsyncuser

        backwardsyncpassword = self.backwardsyncpassword

        passthrumac: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.passthrumac, Unset):
            passthrumac = []
            for passthrumac_item_data in self.passthrumac:
                passthrumac_item = passthrumac_item_data.to_dict()
                passthrumac.append(passthrumac_item)

        allowedip: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allowedip, Unset):
            allowedip = []
            for allowedip_item_data in self.allowedip:
                allowedip_item = allowedip_item_data.to_dict()
                allowedip.append(allowedip_item)

        allowedhostname: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allowedhostname, Unset):
            allowedhostname = []
            for allowedhostname_item_data in self.allowedhostname:
                allowedhostname_item = allowedhostname_item_data.to_dict()
                allowedhostname.append(allowedhostname_item)

        element: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.element, Unset):
            element = []
            for element_item_data in self.element:
                element_item = element_item_data.to_dict()
                element.append(element_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "zone": zone,
            }
        )
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
        if idletimeout is not UNSET:
            field_dict["idletimeout"] = idletimeout
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
        if enablebackwardsync is not UNSET:
            field_dict["enablebackwardsync"] = enablebackwardsync
        if backwardsyncip is not UNSET:
            field_dict["backwardsyncip"] = backwardsyncip
        if backwardsyncuser is not UNSET:
            field_dict["backwardsyncuser"] = backwardsyncuser
        if backwardsyncpassword is not UNSET:
            field_dict["backwardsyncpassword"] = backwardsyncpassword
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.captive_allowed_host import CaptiveAllowedHost
        from ..models.captive_allowed_ip import CaptiveAllowedIP
        from ..models.captive_element import CaptiveElement
        from ..models.captive_passthru_mac import CaptivePassthruMac

        d = dict(src_dict)
        zone = d.pop("zone")

        zoneid = d.pop("zoneid", UNSET)

        descr = d.pop("descr", UNSET)

        localauth_priv = d.pop("localauth_priv", UNSET)

        interface = d.pop("interface", UNSET)

        maxproc = d.pop("maxproc", UNSET)

        maxprocperip = d.pop("maxprocperip", UNSET)

        timeout = d.pop("timeout", UNSET)

        idletimeout = d.pop("idletimeout", UNSET)

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

        enablebackwardsync = d.pop("enablebackwardsync", UNSET)

        backwardsyncip = d.pop("backwardsyncip", UNSET)

        backwardsyncuser = d.pop("backwardsyncuser", UNSET)

        backwardsyncpassword = d.pop("backwardsyncpassword", UNSET)

        _passthrumac = d.pop("passthrumac", UNSET)
        passthrumac: list[CaptivePassthruMac] | Unset = UNSET
        if _passthrumac is not UNSET:
            passthrumac = []
            for passthrumac_item_data in _passthrumac:
                passthrumac_item = CaptivePassthruMac.from_dict(passthrumac_item_data)

                passthrumac.append(passthrumac_item)

        _allowedip = d.pop("allowedip", UNSET)
        allowedip: list[CaptiveAllowedIP] | Unset = UNSET
        if _allowedip is not UNSET:
            allowedip = []
            for allowedip_item_data in _allowedip:
                allowedip_item = CaptiveAllowedIP.from_dict(allowedip_item_data)

                allowedip.append(allowedip_item)

        _allowedhostname = d.pop("allowedhostname", UNSET)
        allowedhostname: list[CaptiveAllowedHost] | Unset = UNSET
        if _allowedhostname is not UNSET:
            allowedhostname = []
            for allowedhostname_item_data in _allowedhostname:
                allowedhostname_item = CaptiveAllowedHost.from_dict(allowedhostname_item_data)

                allowedhostname.append(allowedhostname_item)

        _element = d.pop("element", UNSET)
        element: list[CaptiveElement] | Unset = UNSET
        if _element is not UNSET:
            element = []
            for element_item_data in _element:
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
            idletimeout=idletimeout,
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
            enablebackwardsync=enablebackwardsync,
            backwardsyncip=backwardsyncip,
            backwardsyncuser=backwardsyncuser,
            backwardsyncpassword=backwardsyncpassword,
            passthrumac=passthrumac,
            allowedip=allowedip,
            allowedhostname=allowedhostname,
            element=element,
        )

        captive_portal_config.additional_properties = d
        return captive_portal_config

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
