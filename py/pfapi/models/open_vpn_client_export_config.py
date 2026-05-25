from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.open_vpn_client_export_config_bindmode import OpenVPNClientExportConfigBindmode
from ..models.open_vpn_client_export_config_p12_encryption import OpenVPNClientExportConfigP12Encryption
from ..models.open_vpn_client_export_config_verifyservercn import OpenVPNClientExportConfigVerifyservercn
from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenVPNClientExportConfig")


@_attrs_define
class OpenVPNClientExportConfig:
    """
    Attributes:
        server (str | Unset): vpnid of a openvpn server in remote access mode
        useaddr (str | Unset): host name resolution, the format of remote directive entries uses in client configuration
            files
        useaddr_hostname (str | Unset): when useaddr is "other", this specify the hostname or ip address the client will
            use to connect to this server
        verifyservercn (OpenVPNClientExportConfigVerifyservercn | Unset): verify server common name
        blockoutsidedns (bool | Unset): block outside dns
        legacy (bool | Unset): do not include openvpn 2.5 and later settings in the client configuration
        silent (bool | Unset): create a silent windows installer for unattended deploy
        bindmode (OpenVPNClientExportConfigBindmode | Unset): bind mode
        usepkcs11 (bool | Unset): use pkcs11 storage device
        pkcs11providers (list[str] | Unset):
        pkcs11id (str | Unset): when usepkcs11 is true, specify the object's id on the pkcs11 device
        usetoken (bool | Unset): use microsoft certificate storage instead of local files
        usepass (bool | Unset): use a password to protect the pkcs12 file contents or key in viscosity bundle
        pass_ (str | Unset): when usepass is true, specify the password used to protect the certificate file contents
        p12encryption (OpenVPNClientExportConfigP12Encryption | Unset): level of encryption
        useproxy (bool | Unset): use proxy to communicate with the openvpn server
        useproxytype (str | Unset): when useproxy is true, specify proxy type (http or socks)
        proxyaddr (str | Unset): when useproxy is true, specify hostname or ip address of proxy server
        proxyport (str | Unset): when useproxy is true, specify proxy server's port
        useproxypass (str | Unset): when useproxy is true, specify proxy authentication method (none, basic, ntlm)
        proxyuser (str | Unset): when useproxy is true, specify username for authentication to proxy
        proxypass (str | Unset): when useproxy is true, specify password for authentication to proxy
        advancedoptions (str | Unset): base64 encoded of additional options to add to the openvpn client export
            configuration
    """

    server: str | Unset = UNSET
    useaddr: str | Unset = UNSET
    useaddr_hostname: str | Unset = UNSET
    verifyservercn: OpenVPNClientExportConfigVerifyservercn | Unset = UNSET
    blockoutsidedns: bool | Unset = UNSET
    legacy: bool | Unset = UNSET
    silent: bool | Unset = UNSET
    bindmode: OpenVPNClientExportConfigBindmode | Unset = UNSET
    usepkcs11: bool | Unset = UNSET
    pkcs11providers: list[str] | Unset = UNSET
    pkcs11id: str | Unset = UNSET
    usetoken: bool | Unset = UNSET
    usepass: bool | Unset = UNSET
    pass_: str | Unset = UNSET
    p12encryption: OpenVPNClientExportConfigP12Encryption | Unset = UNSET
    useproxy: bool | Unset = UNSET
    useproxytype: str | Unset = UNSET
    proxyaddr: str | Unset = UNSET
    proxyport: str | Unset = UNSET
    useproxypass: str | Unset = UNSET
    proxyuser: str | Unset = UNSET
    proxypass: str | Unset = UNSET
    advancedoptions: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server = self.server

        useaddr = self.useaddr

        useaddr_hostname = self.useaddr_hostname

        verifyservercn: str | Unset = UNSET
        if not isinstance(self.verifyservercn, Unset):
            verifyservercn = self.verifyservercn.value

        blockoutsidedns = self.blockoutsidedns

        legacy = self.legacy

        silent = self.silent

        bindmode: str | Unset = UNSET
        if not isinstance(self.bindmode, Unset):
            bindmode = self.bindmode.value

        usepkcs11 = self.usepkcs11

        pkcs11providers: list[str] | Unset = UNSET
        if not isinstance(self.pkcs11providers, Unset):
            pkcs11providers = self.pkcs11providers

        pkcs11id = self.pkcs11id

        usetoken = self.usetoken

        usepass = self.usepass

        pass_ = self.pass_

        p12encryption: str | Unset = UNSET
        if not isinstance(self.p12encryption, Unset):
            p12encryption = self.p12encryption.value

        useproxy = self.useproxy

        useproxytype = self.useproxytype

        proxyaddr = self.proxyaddr

        proxyport = self.proxyport

        useproxypass = self.useproxypass

        proxyuser = self.proxyuser

        proxypass = self.proxypass

        advancedoptions = self.advancedoptions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server is not UNSET:
            field_dict["server"] = server
        if useaddr is not UNSET:
            field_dict["useaddr"] = useaddr
        if useaddr_hostname is not UNSET:
            field_dict["useaddr_hostname"] = useaddr_hostname
        if verifyservercn is not UNSET:
            field_dict["verifyservercn"] = verifyservercn
        if blockoutsidedns is not UNSET:
            field_dict["blockoutsidedns"] = blockoutsidedns
        if legacy is not UNSET:
            field_dict["legacy"] = legacy
        if silent is not UNSET:
            field_dict["silent"] = silent
        if bindmode is not UNSET:
            field_dict["bindmode"] = bindmode
        if usepkcs11 is not UNSET:
            field_dict["usepkcs11"] = usepkcs11
        if pkcs11providers is not UNSET:
            field_dict["pkcs11providers"] = pkcs11providers
        if pkcs11id is not UNSET:
            field_dict["pkcs11id"] = pkcs11id
        if usetoken is not UNSET:
            field_dict["usetoken"] = usetoken
        if usepass is not UNSET:
            field_dict["usepass"] = usepass
        if pass_ is not UNSET:
            field_dict["pass"] = pass_
        if p12encryption is not UNSET:
            field_dict["p12encryption"] = p12encryption
        if useproxy is not UNSET:
            field_dict["useproxy"] = useproxy
        if useproxytype is not UNSET:
            field_dict["useproxytype"] = useproxytype
        if proxyaddr is not UNSET:
            field_dict["proxyaddr"] = proxyaddr
        if proxyport is not UNSET:
            field_dict["proxyport"] = proxyport
        if useproxypass is not UNSET:
            field_dict["useproxypass"] = useproxypass
        if proxyuser is not UNSET:
            field_dict["proxyuser"] = proxyuser
        if proxypass is not UNSET:
            field_dict["proxypass"] = proxypass
        if advancedoptions is not UNSET:
            field_dict["advancedoptions"] = advancedoptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server = d.pop("server", UNSET)

        useaddr = d.pop("useaddr", UNSET)

        useaddr_hostname = d.pop("useaddr_hostname", UNSET)

        _verifyservercn = d.pop("verifyservercn", UNSET)
        verifyservercn: OpenVPNClientExportConfigVerifyservercn | Unset
        if isinstance(_verifyservercn, Unset):
            verifyservercn = UNSET
        else:
            verifyservercn = OpenVPNClientExportConfigVerifyservercn(_verifyservercn)

        blockoutsidedns = d.pop("blockoutsidedns", UNSET)

        legacy = d.pop("legacy", UNSET)

        silent = d.pop("silent", UNSET)

        _bindmode = d.pop("bindmode", UNSET)
        bindmode: OpenVPNClientExportConfigBindmode | Unset
        if isinstance(_bindmode, Unset):
            bindmode = UNSET
        else:
            bindmode = OpenVPNClientExportConfigBindmode(_bindmode)

        usepkcs11 = d.pop("usepkcs11", UNSET)

        pkcs11providers = cast(list[str], d.pop("pkcs11providers", UNSET))

        pkcs11id = d.pop("pkcs11id", UNSET)

        usetoken = d.pop("usetoken", UNSET)

        usepass = d.pop("usepass", UNSET)

        pass_ = d.pop("pass", UNSET)

        _p12encryption = d.pop("p12encryption", UNSET)
        p12encryption: OpenVPNClientExportConfigP12Encryption | Unset
        if isinstance(_p12encryption, Unset):
            p12encryption = UNSET
        else:
            p12encryption = OpenVPNClientExportConfigP12Encryption(_p12encryption)

        useproxy = d.pop("useproxy", UNSET)

        useproxytype = d.pop("useproxytype", UNSET)

        proxyaddr = d.pop("proxyaddr", UNSET)

        proxyport = d.pop("proxyport", UNSET)

        useproxypass = d.pop("useproxypass", UNSET)

        proxyuser = d.pop("proxyuser", UNSET)

        proxypass = d.pop("proxypass", UNSET)

        advancedoptions = d.pop("advancedoptions", UNSET)

        open_vpn_client_export_config = cls(
            server=server,
            useaddr=useaddr,
            useaddr_hostname=useaddr_hostname,
            verifyservercn=verifyservercn,
            blockoutsidedns=blockoutsidedns,
            legacy=legacy,
            silent=silent,
            bindmode=bindmode,
            usepkcs11=usepkcs11,
            pkcs11providers=pkcs11providers,
            pkcs11id=pkcs11id,
            usetoken=usetoken,
            usepass=usepass,
            pass_=pass_,
            p12encryption=p12encryption,
            useproxy=useproxy,
            useproxytype=useproxytype,
            proxyaddr=proxyaddr,
            proxyport=proxyport,
            useproxypass=useproxypass,
            proxyuser=proxyuser,
            proxypass=proxypass,
            advancedoptions=advancedoptions,
        )

        open_vpn_client_export_config.additional_properties = d
        return open_vpn_client_export_config

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
