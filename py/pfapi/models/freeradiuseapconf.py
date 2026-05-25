from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_value import TextValue


T = TypeVar("T", bound="Freeradiuseapconf")


@_attrs_define
class Freeradiuseapconf:
    """
    Attributes:
        eapconfdisableweakeaptypes (bool | Unset): (EAP) Disable Weak EAP Types
            When enabled, only stronger EAP types like TLS, TTLS, PEAP, and MSCHAPv2 are allowed. This option does not
            affect tunneled EAP sessions.

            Disables weak EAP types: MD5, and GTC
        eapconfdefaulteaptype (str | Unset): (EAP) Default EAP Type (md5, gtc, leap, tls, ttls, peap, mschapv2)

            Invoke the default supported EAP type when EAP-Identity response is received.

            Important: Do not select the weak types if 'Disable Weak EAP Types' is checked above; try PEAP instead.
            (Default: md5)
        eapconftimerexpire (str | Unset): (EAP) Expiration of EAP-Response / EAP-Request List

            A list is maintained to correlate EAP-Response packets with EAP-Request packets. Define the expire time of the
            list here.
            (Default: 60)
        eapconfignoreunknowneaptypes (str | Unset): (EAP) Ignore Unknown EAP Types (no, yes)

            If the RADIUS server does not know the EAP type, it rejects it.
            If set to "yes", a module must be configured to proxy the request to another RADIUS server.
            (Default: No)
        eapconfciscoaccountingusernamebug (str | Unset): (EAP) CISCO Accounting Username Bug (no, yes)

            CISCO AP1230B firmware 12.2(13)JA1 has a bug which can be workaround by setting this to "yes".
            (Default: No)
        eapconfmaxsessions (str | Unset): (EAP) Maximum Sessions Tracking Per Server

            Help to prevent DoS attacks by limiting the number of sessions that the server is tracking.
            (Default: 4096)
        eapconftlsminversion (str | Unset): (EAP) Minimum TLS version (1.0, 1.1, 1.2)

            Set minimum TLS version. Leave 1.0 if you have old clients.
        ssl_ca_cert (str | Unset): (Certificates for TLS) SSL CA Certificate

            Choose the SSL CA Certficate here which you created with 'System > Cert Manager'.

            IMPORTANT: Configuring a valid CA certificate here is required!
        ssl_ca_crl (str | Unset): (Certificates for TLS) SSL Revocation List

            Choose the SSL CA Certficate revocation list here which you created with 'System > Cert Manager'.

            Important:
            You need to restart FreeRADIUS service after adding a certificate to the CRL.


            Choose 'none' if you do not use any CRL.
            (Default: none)
        ssl_server_cert (str | Unset): (Certificates for TLS) SSL Server Certificate

            Choose the SSL Server Certficate here which you created with 'System > Cert Manager'.

            IMPORTANT: Configuring a valid server certificate here is required!
        eapconfincludelength (str | Unset): (EAP-TLS) Include Length (yes, no)

            If set to 'Yes', Total Length of the message is included in every packet we send.

            If set to 'No' Total Length of the message is included only in the first packet of a fragment series.
            (Default: Yes)
        eapconffragmentsize (str | Unset): (EAP-TLS) Fragment Size

            'Fragment Size' can never exceed the size of a RADIUS packet (4096 bytes), and is preferably half of that,
            to accomodate other attributes in RADIUS packet.
            On most APs, the max. packet length is configured between 1500 - 1600. In these cases, fragment size should be
            1024 or less.

            (Default: 1024)
        eapconfenablecheckcertissuer (bool | Unset): (EAP-TLS) Check Cert Issuer
            When enabled, the server/client certificate must match the CA issuer. (Default: false)

            Validate the certificate against the CA
        eapconfcasubject (str | Unset): (EAP-TLS) CA Subject

            Enter the subject of the CA to validate, or leave blank to assume the subject of SSL CA Certificate chosen
            above.
            (Example: /C=US/ST=Texas/L=Austin/O=Example Co/emailAddress=certs@example.com/CN=example-ca)
        eapconfenablecheckcertcn (bool | Unset): (EAP-TLS) Check Client Certificate CN
            When enabled, the Common Name of the client certificate must match the username set in 'FreeRADIUS > Users'.
            (Default: false)

            Validate the Client Certificate Common Name
        eapconfcacheenablecache (str | Unset): (EAP-TLS Cache) Enable cache (yes, no)

            Session resumption / fast reauthentication cache.
            Click Info for details. (Default: Disable)

            The cache contains the following information:

            - Session Id: Unique identifier, managed by SSL
            - User-Name: From the Access-Accept
            - Stripped-User-Name: From the Access-Request
            - Cached-Session-Policy: From the Access-Accept

            The "Cached-Session-Policy" is the name of a policy which should be applied to the cached session.
            This policy can be used to assign VLANs, IP addresses, etc.
            It serves as a useful way to re-apply the policy from the original Access-Accept to the subsequent Access-Accept
            for the cached session.

            On session resumption, these attributes are copied from the cache, and placed into the reply list.
            You probably also want use_tunneled_reply = yes when using fast session resumption.
        eapconfcachelifetime (str | Unset): (EAP-TLS Cache) Lifetime

            Lifetime of the cached entries, in hours.
            The sessions will be deleted after this time.
            (Default: 24)
        eapconfcachemaxentries (str | Unset): (EAP-TLS Cache) Max Entries

            The maximum number of entries in the cache. Set to "0" for "infinite."
            (Default: 255)
        eapconfocspenable (str | Unset): (EAP-TLS with OCSP support) Enable OCSP (no, yes)

            Choose whether you like to enable or disable OCSP support.
            (Default: Disable)
        eapconfocspoverridecerturl (str | Unset): (EAP-TLS with OCSP support) Override OCSP Responder URL (no, yes)

            The OCSP responder URL is extracted from the certificate. You can override it below.
            (Default: No)
        eapconfocspurl (str | Unset): (EAP-TLS with OCSP support) OCSP Responder

            Enter the URL of the OCSP responder. OCSP must be enabled for this to work.
            (Default: http://127.0.0.1/ocsp/)
        eapconfttlsdefaulteaptype (str | Unset): (EAP-TTLS) Default EAP Type (md5, gtc, otp, tls, mschapv2)

            The tunneled EAP session needs a default EAP type which is separate from the one for the non-tunneled EAP
            module.
            Inside of the TTLS tunnel, using EAP-MD5 is recommended.
            If the request does not contain an EAP conversation, then this configuration entry is ignored.
            (Default: MD5)
        eapconfttlscopyrequesttotunnel (str | Unset): (EAP-TTLS) Copy Request to Tunnel (no, yes)

            The tunneled authentication request does not usually contain useful attributes like 'Calling-Station-Id', etc.
            These attributes are outside of the tunnel, and normally unavailable to the tunneled authentication request.
            By setting this configuration entry to 'Yes', any attribute which is not available in the tunneled
            authentication request,
            but which is available outside of the tunnel, is copied to the tunneled request.
            (Default: No)
        eapconfttlsusetunneledreply (str | Unset): (EAP-TTLS) Use Tunneled Reply (no, yes)

            The reply attributes sent to the NAS are usually based on the name of the user 'outside' of the tunnel (usually
            'anonymous').

            If you want to send the reply attributes based on the user name inside of the tunnel, then set 'Use Tunneled
            Reply' to 'Yes';
            the reply to the NAS will be taken from the reply to the tunneled request.
            (Default: No)
        eapconfttlsincludelength (str | Unset): (EAP-TTLS) Include Length (yes, no)

            If set to 'Yes', Total Length of the message is included in every packet we send.

            If set to 'No', Total Length of the message is included only in the first packet of a fragment series.
            (Default: Yes)
        eapconfpeapdefaulteaptype (str | Unset): (EAP-PEAP) Default EAP Type (md5, gtc, otp, tls, mschapv2)

            The tunneled EAP session needs a default EAP type which is separate from the one for the non-tunneled EAP
            module.
            Inside of the PEAP tunnel, using MS-CHAPv2 is recommended, as that is the default type supported by Windows
            clients.
            (Default: MSCHAPv2)
        eapconfpeapcopyrequesttotunnel (str | Unset): (EAP-PEAP) Copy Request to Tunnel (no, yes)

            The tunneled authentication request does not usually contain useful attributes like 'Calling-Station-Id', etc.
            These attributes are outside of the tunnel, and normally unavailable to the tunneled authentication request.
            By setting this configuration entry to 'Yes', any attribute which is not available in the tunneled
            authentication request,
            but which is available outside of the tunnel, is copied to the tunneled request.
            (Default: No)
        eapconfpeapusetunneledreply (str | Unset): (EAP-PEAP) Use Tunneled Reply (no, yes)

            The reply attributes sent to the NAS are usually based on the name of the user 'outside' of the tunnel (usually
            'anonymous').
            If you want to send the reply attributes based on the user name inside of the tunnel, then set this
            configuration entry to 'Yes';
            the reply to the NAS will be taken from the reply to the tunneled request.
            (Default: No)
        eapconfpeapsohenable (str | Unset): (EAP-PEAP) Microsoft Statement of Health (SoH) Support (Disable, Enable)

            You can accept/reject clients based on Microsoft's Statement of Health, e.g. if they are missing Windows
            Updates,
            don't have a firewall enabled, antivirus is not in line with policy, etc.
            You need to change /usr/local/etc/raddb/sites-available/soh for your needs.
            It cannot be changed from GUI and will be deleted after package reinstallation.
            (Default: Disable)
        ssl_ca_cert_options (list[TextValue] | Unset):
        ssl_ca_crl_options (list[TextValue] | Unset):
        ssl_server_cert_options (list[TextValue] | Unset):
    """

    eapconfdisableweakeaptypes: bool | Unset = UNSET
    eapconfdefaulteaptype: str | Unset = UNSET
    eapconftimerexpire: str | Unset = UNSET
    eapconfignoreunknowneaptypes: str | Unset = UNSET
    eapconfciscoaccountingusernamebug: str | Unset = UNSET
    eapconfmaxsessions: str | Unset = UNSET
    eapconftlsminversion: str | Unset = UNSET
    ssl_ca_cert: str | Unset = UNSET
    ssl_ca_crl: str | Unset = UNSET
    ssl_server_cert: str | Unset = UNSET
    eapconfincludelength: str | Unset = UNSET
    eapconffragmentsize: str | Unset = UNSET
    eapconfenablecheckcertissuer: bool | Unset = UNSET
    eapconfcasubject: str | Unset = UNSET
    eapconfenablecheckcertcn: bool | Unset = UNSET
    eapconfcacheenablecache: str | Unset = UNSET
    eapconfcachelifetime: str | Unset = UNSET
    eapconfcachemaxentries: str | Unset = UNSET
    eapconfocspenable: str | Unset = UNSET
    eapconfocspoverridecerturl: str | Unset = UNSET
    eapconfocspurl: str | Unset = UNSET
    eapconfttlsdefaulteaptype: str | Unset = UNSET
    eapconfttlscopyrequesttotunnel: str | Unset = UNSET
    eapconfttlsusetunneledreply: str | Unset = UNSET
    eapconfttlsincludelength: str | Unset = UNSET
    eapconfpeapdefaulteaptype: str | Unset = UNSET
    eapconfpeapcopyrequesttotunnel: str | Unset = UNSET
    eapconfpeapusetunneledreply: str | Unset = UNSET
    eapconfpeapsohenable: str | Unset = UNSET
    ssl_ca_cert_options: list[TextValue] | Unset = UNSET
    ssl_ca_crl_options: list[TextValue] | Unset = UNSET
    ssl_server_cert_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eapconfdisableweakeaptypes = self.eapconfdisableweakeaptypes

        eapconfdefaulteaptype = self.eapconfdefaulteaptype

        eapconftimerexpire = self.eapconftimerexpire

        eapconfignoreunknowneaptypes = self.eapconfignoreunknowneaptypes

        eapconfciscoaccountingusernamebug = self.eapconfciscoaccountingusernamebug

        eapconfmaxsessions = self.eapconfmaxsessions

        eapconftlsminversion = self.eapconftlsminversion

        ssl_ca_cert = self.ssl_ca_cert

        ssl_ca_crl = self.ssl_ca_crl

        ssl_server_cert = self.ssl_server_cert

        eapconfincludelength = self.eapconfincludelength

        eapconffragmentsize = self.eapconffragmentsize

        eapconfenablecheckcertissuer = self.eapconfenablecheckcertissuer

        eapconfcasubject = self.eapconfcasubject

        eapconfenablecheckcertcn = self.eapconfenablecheckcertcn

        eapconfcacheenablecache = self.eapconfcacheenablecache

        eapconfcachelifetime = self.eapconfcachelifetime

        eapconfcachemaxentries = self.eapconfcachemaxentries

        eapconfocspenable = self.eapconfocspenable

        eapconfocspoverridecerturl = self.eapconfocspoverridecerturl

        eapconfocspurl = self.eapconfocspurl

        eapconfttlsdefaulteaptype = self.eapconfttlsdefaulteaptype

        eapconfttlscopyrequesttotunnel = self.eapconfttlscopyrequesttotunnel

        eapconfttlsusetunneledreply = self.eapconfttlsusetunneledreply

        eapconfttlsincludelength = self.eapconfttlsincludelength

        eapconfpeapdefaulteaptype = self.eapconfpeapdefaulteaptype

        eapconfpeapcopyrequesttotunnel = self.eapconfpeapcopyrequesttotunnel

        eapconfpeapusetunneledreply = self.eapconfpeapusetunneledreply

        eapconfpeapsohenable = self.eapconfpeapsohenable

        ssl_ca_cert_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssl_ca_cert_options, Unset):
            ssl_ca_cert_options = []
            for ssl_ca_cert_options_item_data in self.ssl_ca_cert_options:
                ssl_ca_cert_options_item = ssl_ca_cert_options_item_data.to_dict()
                ssl_ca_cert_options.append(ssl_ca_cert_options_item)

        ssl_ca_crl_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssl_ca_crl_options, Unset):
            ssl_ca_crl_options = []
            for ssl_ca_crl_options_item_data in self.ssl_ca_crl_options:
                ssl_ca_crl_options_item = ssl_ca_crl_options_item_data.to_dict()
                ssl_ca_crl_options.append(ssl_ca_crl_options_item)

        ssl_server_cert_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssl_server_cert_options, Unset):
            ssl_server_cert_options = []
            for ssl_server_cert_options_item_data in self.ssl_server_cert_options:
                ssl_server_cert_options_item = ssl_server_cert_options_item_data.to_dict()
                ssl_server_cert_options.append(ssl_server_cert_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eapconfdisableweakeaptypes is not UNSET:
            field_dict["eapconfdisableweakeaptypes"] = eapconfdisableweakeaptypes
        if eapconfdefaulteaptype is not UNSET:
            field_dict["eapconfdefaulteaptype"] = eapconfdefaulteaptype
        if eapconftimerexpire is not UNSET:
            field_dict["eapconftimerexpire"] = eapconftimerexpire
        if eapconfignoreunknowneaptypes is not UNSET:
            field_dict["eapconfignoreunknowneaptypes"] = eapconfignoreunknowneaptypes
        if eapconfciscoaccountingusernamebug is not UNSET:
            field_dict["eapconfciscoaccountingusernamebug"] = eapconfciscoaccountingusernamebug
        if eapconfmaxsessions is not UNSET:
            field_dict["eapconfmaxsessions"] = eapconfmaxsessions
        if eapconftlsminversion is not UNSET:
            field_dict["eapconftlsminversion"] = eapconftlsminversion
        if ssl_ca_cert is not UNSET:
            field_dict["ssl_ca_cert"] = ssl_ca_cert
        if ssl_ca_crl is not UNSET:
            field_dict["ssl_ca_crl"] = ssl_ca_crl
        if ssl_server_cert is not UNSET:
            field_dict["ssl_server_cert"] = ssl_server_cert
        if eapconfincludelength is not UNSET:
            field_dict["eapconfincludelength"] = eapconfincludelength
        if eapconffragmentsize is not UNSET:
            field_dict["eapconffragmentsize"] = eapconffragmentsize
        if eapconfenablecheckcertissuer is not UNSET:
            field_dict["eapconfenablecheckcertissuer"] = eapconfenablecheckcertissuer
        if eapconfcasubject is not UNSET:
            field_dict["eapconfcasubject"] = eapconfcasubject
        if eapconfenablecheckcertcn is not UNSET:
            field_dict["eapconfenablecheckcertcn"] = eapconfenablecheckcertcn
        if eapconfcacheenablecache is not UNSET:
            field_dict["eapconfcacheenablecache"] = eapconfcacheenablecache
        if eapconfcachelifetime is not UNSET:
            field_dict["eapconfcachelifetime"] = eapconfcachelifetime
        if eapconfcachemaxentries is not UNSET:
            field_dict["eapconfcachemaxentries"] = eapconfcachemaxentries
        if eapconfocspenable is not UNSET:
            field_dict["eapconfocspenable"] = eapconfocspenable
        if eapconfocspoverridecerturl is not UNSET:
            field_dict["eapconfocspoverridecerturl"] = eapconfocspoverridecerturl
        if eapconfocspurl is not UNSET:
            field_dict["eapconfocspurl"] = eapconfocspurl
        if eapconfttlsdefaulteaptype is not UNSET:
            field_dict["eapconfttlsdefaulteaptype"] = eapconfttlsdefaulteaptype
        if eapconfttlscopyrequesttotunnel is not UNSET:
            field_dict["eapconfttlscopyrequesttotunnel"] = eapconfttlscopyrequesttotunnel
        if eapconfttlsusetunneledreply is not UNSET:
            field_dict["eapconfttlsusetunneledreply"] = eapconfttlsusetunneledreply
        if eapconfttlsincludelength is not UNSET:
            field_dict["eapconfttlsincludelength"] = eapconfttlsincludelength
        if eapconfpeapdefaulteaptype is not UNSET:
            field_dict["eapconfpeapdefaulteaptype"] = eapconfpeapdefaulteaptype
        if eapconfpeapcopyrequesttotunnel is not UNSET:
            field_dict["eapconfpeapcopyrequesttotunnel"] = eapconfpeapcopyrequesttotunnel
        if eapconfpeapusetunneledreply is not UNSET:
            field_dict["eapconfpeapusetunneledreply"] = eapconfpeapusetunneledreply
        if eapconfpeapsohenable is not UNSET:
            field_dict["eapconfpeapsohenable"] = eapconfpeapsohenable
        if ssl_ca_cert_options is not UNSET:
            field_dict["ssl_ca_cert_options"] = ssl_ca_cert_options
        if ssl_ca_crl_options is not UNSET:
            field_dict["ssl_ca_crl_options"] = ssl_ca_crl_options
        if ssl_server_cert_options is not UNSET:
            field_dict["ssl_server_cert_options"] = ssl_server_cert_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_value import TextValue

        d = dict(src_dict)
        eapconfdisableweakeaptypes = d.pop("eapconfdisableweakeaptypes", UNSET)

        eapconfdefaulteaptype = d.pop("eapconfdefaulteaptype", UNSET)

        eapconftimerexpire = d.pop("eapconftimerexpire", UNSET)

        eapconfignoreunknowneaptypes = d.pop("eapconfignoreunknowneaptypes", UNSET)

        eapconfciscoaccountingusernamebug = d.pop("eapconfciscoaccountingusernamebug", UNSET)

        eapconfmaxsessions = d.pop("eapconfmaxsessions", UNSET)

        eapconftlsminversion = d.pop("eapconftlsminversion", UNSET)

        ssl_ca_cert = d.pop("ssl_ca_cert", UNSET)

        ssl_ca_crl = d.pop("ssl_ca_crl", UNSET)

        ssl_server_cert = d.pop("ssl_server_cert", UNSET)

        eapconfincludelength = d.pop("eapconfincludelength", UNSET)

        eapconffragmentsize = d.pop("eapconffragmentsize", UNSET)

        eapconfenablecheckcertissuer = d.pop("eapconfenablecheckcertissuer", UNSET)

        eapconfcasubject = d.pop("eapconfcasubject", UNSET)

        eapconfenablecheckcertcn = d.pop("eapconfenablecheckcertcn", UNSET)

        eapconfcacheenablecache = d.pop("eapconfcacheenablecache", UNSET)

        eapconfcachelifetime = d.pop("eapconfcachelifetime", UNSET)

        eapconfcachemaxentries = d.pop("eapconfcachemaxentries", UNSET)

        eapconfocspenable = d.pop("eapconfocspenable", UNSET)

        eapconfocspoverridecerturl = d.pop("eapconfocspoverridecerturl", UNSET)

        eapconfocspurl = d.pop("eapconfocspurl", UNSET)

        eapconfttlsdefaulteaptype = d.pop("eapconfttlsdefaulteaptype", UNSET)

        eapconfttlscopyrequesttotunnel = d.pop("eapconfttlscopyrequesttotunnel", UNSET)

        eapconfttlsusetunneledreply = d.pop("eapconfttlsusetunneledreply", UNSET)

        eapconfttlsincludelength = d.pop("eapconfttlsincludelength", UNSET)

        eapconfpeapdefaulteaptype = d.pop("eapconfpeapdefaulteaptype", UNSET)

        eapconfpeapcopyrequesttotunnel = d.pop("eapconfpeapcopyrequesttotunnel", UNSET)

        eapconfpeapusetunneledreply = d.pop("eapconfpeapusetunneledreply", UNSET)

        eapconfpeapsohenable = d.pop("eapconfpeapsohenable", UNSET)

        _ssl_ca_cert_options = d.pop("ssl_ca_cert_options", UNSET)
        ssl_ca_cert_options: list[TextValue] | Unset = UNSET
        if _ssl_ca_cert_options is not UNSET:
            ssl_ca_cert_options = []
            for ssl_ca_cert_options_item_data in _ssl_ca_cert_options:
                ssl_ca_cert_options_item = TextValue.from_dict(ssl_ca_cert_options_item_data)

                ssl_ca_cert_options.append(ssl_ca_cert_options_item)

        _ssl_ca_crl_options = d.pop("ssl_ca_crl_options", UNSET)
        ssl_ca_crl_options: list[TextValue] | Unset = UNSET
        if _ssl_ca_crl_options is not UNSET:
            ssl_ca_crl_options = []
            for ssl_ca_crl_options_item_data in _ssl_ca_crl_options:
                ssl_ca_crl_options_item = TextValue.from_dict(ssl_ca_crl_options_item_data)

                ssl_ca_crl_options.append(ssl_ca_crl_options_item)

        _ssl_server_cert_options = d.pop("ssl_server_cert_options", UNSET)
        ssl_server_cert_options: list[TextValue] | Unset = UNSET
        if _ssl_server_cert_options is not UNSET:
            ssl_server_cert_options = []
            for ssl_server_cert_options_item_data in _ssl_server_cert_options:
                ssl_server_cert_options_item = TextValue.from_dict(ssl_server_cert_options_item_data)

                ssl_server_cert_options.append(ssl_server_cert_options_item)

        freeradiuseapconf = cls(
            eapconfdisableweakeaptypes=eapconfdisableweakeaptypes,
            eapconfdefaulteaptype=eapconfdefaulteaptype,
            eapconftimerexpire=eapconftimerexpire,
            eapconfignoreunknowneaptypes=eapconfignoreunknowneaptypes,
            eapconfciscoaccountingusernamebug=eapconfciscoaccountingusernamebug,
            eapconfmaxsessions=eapconfmaxsessions,
            eapconftlsminversion=eapconftlsminversion,
            ssl_ca_cert=ssl_ca_cert,
            ssl_ca_crl=ssl_ca_crl,
            ssl_server_cert=ssl_server_cert,
            eapconfincludelength=eapconfincludelength,
            eapconffragmentsize=eapconffragmentsize,
            eapconfenablecheckcertissuer=eapconfenablecheckcertissuer,
            eapconfcasubject=eapconfcasubject,
            eapconfenablecheckcertcn=eapconfenablecheckcertcn,
            eapconfcacheenablecache=eapconfcacheenablecache,
            eapconfcachelifetime=eapconfcachelifetime,
            eapconfcachemaxentries=eapconfcachemaxentries,
            eapconfocspenable=eapconfocspenable,
            eapconfocspoverridecerturl=eapconfocspoverridecerturl,
            eapconfocspurl=eapconfocspurl,
            eapconfttlsdefaulteaptype=eapconfttlsdefaulteaptype,
            eapconfttlscopyrequesttotunnel=eapconfttlscopyrequesttotunnel,
            eapconfttlsusetunneledreply=eapconfttlsusetunneledreply,
            eapconfttlsincludelength=eapconfttlsincludelength,
            eapconfpeapdefaulteaptype=eapconfpeapdefaulteaptype,
            eapconfpeapcopyrequesttotunnel=eapconfpeapcopyrequesttotunnel,
            eapconfpeapusetunneledreply=eapconfpeapusetunneledreply,
            eapconfpeapsohenable=eapconfpeapsohenable,
            ssl_ca_cert_options=ssl_ca_cert_options,
            ssl_ca_crl_options=ssl_ca_crl_options,
            ssl_server_cert_options=ssl_server_cert_options,
        )

        freeradiuseapconf.additional_properties = d
        return freeradiuseapconf

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
