from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_value import TextValue


T = TypeVar("T", bound="Freeradiusmodulesldap")


@_attrs_define
class Freeradiusmodulesldap:
    """
    Attributes:
        modulesldapenableauthorize (bool | Unset): (Enable LDAP Support - Server 1) LDAP Authorization Support
            Enables LDAP in the authorize section. The ldap module will set Auth-Type to LDAP if it has not already been
            set. (Default: Disabled)

            Enable LDAP For Authorization
        modulesldapenableauthenticate (bool | Unset): (Enable LDAP Support - Server 1) LDAP Authentication Support
            Enables LDAP in the authenticate section. Note that this means "check plain-text password against the LDAP
            database", which means that EAP won't work, as it does not supply a plain-text password.

            Enable LDAP For Authentication
        modulesldapserver (str | Unset): (General Configuration - Server 1) Server Address

            LDAP server FQDN or IP address.
            (Example: ldap.example.com)
        modulesldapserverport (str | Unset): (General Configuration - Server 1) Server Port

            LDAP server port.
            (Default: 389)
        modulesldapidentity (str | Unset): (General Configuration - Server 1) Identity

            LDAP ID for authentication.
            (Example: cn=admin,o=My Company Ltd,c=US)
        modulesldappassword (str | Unset): (General Configuration - Server 1) Password

            LDAP password for authentication.
            (Default: mypass)
        modulesldapbasedn (str | Unset): (General Configuration - Server 1) Base DN

            Base DN for LDAP search.
            (Example: o=My Company Ltd,c=US)
        modulesldapfilter (str | Unset): (General Configuration - Server 1) Filter

            LDAP search filter.
            Default: (uid=%{%{Stripped-User-Name}:-%{User-Name}})
        modulesldapbasefilter (str | Unset): (General Configuration - Server 1) Base Filter

            Default: (objectclass=radiusprofile)
        modulesldapldapconnectionsnumber (str | Unset): (General Configuration - Server 1) LDAP Connections Number

            How many connections to keep open to the LDAP server.

            This saves time over opening a new LDAP socket for every authentication request.
            (Default: 5)
        modulesldaptimeout (str | Unset): (General Configuration - Server 1) Timeout

            Seconds to wait for LDAP query to finish.
            (Default: 4)
        modulesldaptimelimit (str | Unset): (General Configuration - Server 1) Time Limit

            Seconds the LDAP server has to process the query (server-side time limit).
            (Default: 3)
        modulesldapnettimeout (str | Unset): (General Configuration - Server 1) Network Timeout

            Seconds to wait for response of the server because of network failures.
            (Default: 1)
        modulesldapmsadcompatibilityenable (str | Unset): (Miscellaneous Configuration - Server 1) Active Directory
            Compatibility (Disable, Enable)

            If you see the helpful "operations error" being returned to the LDAP module, enable this.
            (Default: Disable)
        modulesldapdmiscenable (bool | Unset): (Miscellaneous Configuration - Server 1) Misc Configuration - Server 1
            By default, the options below are not active in the configuration.

            Enable Miscellaneous Configuration for Server 1
        modulesldapdefaultprofile (str | Unset): (Miscellaneous Configuration - Server 1) Default Profile

            (Example: cn=radprofile,ou=dialup,o=My Company Ltd,c=US)
        modulesldapprofileattribute (str | Unset): (Miscellaneous Configuration - Server 1) Profile Attribute

            (Default: radiusProfileDn)
        modulesldapaccessattr (str | Unset): (Miscellaneous Configuration - Server 1) Access Attribute

            (Default: dialupAccess)
        modulesldapgroupenable (bool | Unset): (Group Membership Options - Server 1) Group Membership Options
            By default, the options below are not active in the configuration.

            Enable Group Membership Options
        modulesldapgroupnameattribute (str | Unset): (Group Membership Options - Server 1) Groupname Attribute

            (Default: cn)
        modulesldapgroupmembershipfilter (str | Unset): (Group Membership Options - Server 1) Group Membership Filter

            Default: (|(&(objectClass=GroupOfNames)(member=%{control:Ldap-
            UserDn}))(&(objectClass=GroupOfUniqueNames)(uniquemember=%{control:Ldap-UserDn})))
        modulesldapgroupmembershipattribute (str | Unset): (Group Membership Options - Server 1) Group Membership
            Attribute

            (Default: radiusGroupName)
        modulesldapcomparecheckitems (str | Unset): (Group Membership Options - Server 1) Compare Check Items (yes, no)

            (Default: Yes)
        modulesldapdoxlat (str | Unset): (Group Membership Options - Server 1) Do XLAT (yes, no)

            (Default: Yes)
        modulesldapaccessattrusedforallow (str | Unset): (Group Membership Options - Server 1) Access Attribute Used For
            Allow (yes, no)

            (Default: Yes)
        modulesldapkeepaliveidle (str | Unset): (KeepAlive Configuration - Server 1) LDAP OPT X KeepAlive Idle

            (Default: 60)
        modulesldapkeepaliveprobes (str | Unset): (KeepAlive Configuration - Server 1) LDAP OPT X KeepAlive Probes

            (Default: 3)
        modulesldapkeepaliveinterval (str | Unset): (KeepAlive Configuration - Server 1) LDAP OPT X KeepAlive Interval

            (Default: 3)
        modulesldapenabletlssupport (bool | Unset): (LDAP TLS Support - Server 1) TLS Support
            If enabled, certificates in ../raddb/certs/ will be checked against the LDAP server certificates.

            Enable TLS support for LDAP server 1
        modulesldapenablestarttls (bool | Unset): (LDAP TLS Support - Server 1) Use STARTTLS
            If enabled, STARTTLS will be used instead of LDAPS.

            Enable STARTTLS for LDAP server 1
        ssl_ca_cert1 (str | Unset): (LDAP TLS Support - Server 1) SSL CA Certificate

            Choose the SSL CA Certficate here which you created with 'System > Cert Manager'.

            Choose 'none' if you do not use any kind of certificates.
            (Default: none)
        ssl_server_cert1 (str | Unset): (LDAP TLS Support - Server 1) SSL Server Certificate

            Choose the SSL Server Certficate here which you created with 'System > Cert Manager'.

            Choose 'none' if you do not use any kind of certificates.
            (Default: none)
        modulesldaprequirecert (str | Unset): (LDAP TLS Support - Server 1) Choose Certificate Verification Method
            (never, allow, demand)

            Choose how the certs should be checked.
            Click Info for details. (Default: never)

            - Never: Don't even bother trying.
            - Allow: Try but don't fail if the certificate can't be verified.
            - Demand: Fail if the certificate doesn't verify.
        modulesldap2failover (str | Unset): (Enable Redundant LDAP Server Support) Choose Failover/Load Balancing Mode
            (redundant, load-balance, redundant-load-balance)

            Choose the interaction of the two LDAP servers.
            Click Info for details. (Default: Redundant)

            - Redundant: Failover to server2 if server1 fails.
            - Load-Balance: The load is balanced 50:50 between both servers.
            - Redundant-Load-Balance: The load is balanced 50:50 between both servers. If one is down, the other does 100%.
        modulesldap2enableauthorize (bool | Unset): (Enable LDAP Support - Server 2) LDAP Authorization Support
            Enables LDAP in the authorize section. The ldap module will set Auth-Type to LDAP if it has not already been
            set. (Default: Disabled)

            Enable LDAP For Authorization (Default: unchecked)
        modulesldap2enableauthenticate (bool | Unset): (Enable LDAP Support - Server 2) LDAP Authentication Support
            Enables LDAP in the authenticate section. Note that this means "check plain-text password against the LDAP
            database", which means that EAP won't work, as it does not supply a plain-text password.

            Enable LDAP For Authentication
        modulesldap2server (str | Unset): (General Configuration - Server 2) Server Address

            LDAP server FQDN or IP address.
            (Example: ldap.example.com)
        modulesldap2serverport (str | Unset): (General Configuration - Server 2) Server Port

            LDAP server port.
            (Default: 389)
        modulesldap2identity (str | Unset): (General Configuration - Server 2) Identity

            LDAP ID for authentication.
            (Example: cn=admin,o=My Company Ltd,c=US)
        modulesldap2password (str | Unset): (General Configuration - Server 2) Password

            LDAP password for authentication.
            (Default: mypass)
        modulesldap2basedn (str | Unset): (General Configuration - Server 2) Base DN

            Base DN for LDAP search.
            (Example: o=My Company Ltd,c=US)
        modulesldap2filter (str | Unset): (General Configuration - Server 2) Filter

            LDAP search filter.
            Default: (uid=%{%{Stripped-User-Name}:-%{User-Name}})
        modulesldap2basefilter (str | Unset): (General Configuration - Server 2) Base Filter

            Default: (objectclass=radiusprofile)
        modulesldap2ldapconnectionsnumber (str | Unset): (General Configuration - Server 2) LDAP Connections Number

            How many connections to keep open to the LDAP server.

            This saves time over opening a new LDAP socket for every authentication request.
            (Default: 5)
        modulesldap2timeout (str | Unset): (General Configuration - Server 2) Timeout

            Seconds to wait for LDAP query to finish.
            (Default: 4)
        modulesldap2timelimit (str | Unset): (General Configuration - Server 2) Time Limit

            Seconds the LDAP server has to process the query (server-side time limit).
            (Default: 3)
        modulesldap2nettimeout (str | Unset): (General Configuration - Server 2) Network Timeout

            Seconds to wait for response of the server because of network failures.
            (Default: 1)
        modulesldap2msadcompatibilityenable (str | Unset): (Miscellaneous Configuration - Server 2) Active Directory
            Compatibility (Disable, Enable)

            If you see the helpful "operations error" being returned to the LDAP module, enable this.
            (Default: Disable)
        modulesldap2dmiscenable (bool | Unset): (Miscellaneous Configuration - Server 2) Misc Configuration
            By default, the options below are not active in the configuration.

            Enable Miscellaneous Configuration for Server 2
        modulesldap2defaultprofile (str | Unset): (Miscellaneous Configuration - Server 2) Default Profile

            (Example: cn=radprofile,ou=dialup,o=My Company Ltd,c=US)
        modulesldap2profileattribute (str | Unset): (Miscellaneous Configuration - Server 2) Profile Attribute

            (Default: radiusProfileDn)
        modulesldap2accessattr (str | Unset): (Miscellaneous Configuration - Server 2) Access Attribute

            (Default: dialupAccess)
        modulesldap2groupenable (bool | Unset): (Group Membership Options - Server 2) Enable Group Membership Options
            By default, the options below are not active in the configuration.

            Enable Group Membership Options
        modulesldap2groupnameattribute (str | Unset): (Group Membership Options - Server 2) Groupname Attribute

            (Default: cn)
        modulesldap2groupmembershipfilter (str | Unset): (Group Membership Options - Server 2) Group Membership Filter

            Default: (|(&(objectClass=GroupOfNames)(member=%{control:Ldap-
            UserDn}))(&(objectClass=GroupOfUniqueNames)(uniquemember=%{control:Ldap-UserDn})))
        modulesldap2groupmembershipattribute (str | Unset): (Group Membership Options - Server 2) Group Membership
            Attribute

            (Default: radiusGroupName)
        modulesldap2comparecheckitems (str | Unset): (Group Membership Options - Server 2) Compare Check Items (yes, no)

            (Default: Yes)
        modulesldap2doxlat (str | Unset): (Group Membership Options - Server 2) Do XLAT (yes, no)

            (Default: Yes)
        modulesldap2accessattrusedforallow (str | Unset): (Group Membership Options - Server 2) Access Attribute Used
            For Allow (yes, no)

            (Default: Yes)
        modulesldap2keepaliveidle (str | Unset): (KeepAlive Configuration - Server 2) LDAP OPT X KeepAlive Idle

            (Default: 60)
        modulesldap2keepaliveprobes (str | Unset): (KeepAlive Configuration - Server 2) LDAP OPT X KeepAlive Probes

            (Default: 3)
        modulesldap2keepaliveinterval (str | Unset): (KeepAlive Configuration - Server 2) LDAP OPT X KeepAlive Interval

            (Default: 3)
        modulesldap2enabletlssupport (bool | Unset): (LDAP TLS Support - Server 2) TLS Support
            If enabled, certificates in ../raddb/certs/ will be checked against the LDAP server certificates.

            Enable TLS support for LDAP server 2
        modulesldap2enablestarttls (bool | Unset): (LDAP TLS Support - Server 2) Use STARTTLS
            If enabled, STARTTLS will be used instead of LDAPS.

            Enable STARTTLS for LDAP server 2
        ssl_ca_cert2 (str | Unset): (LDAP TLS Support - Server 2) SSL CA Certificate

            Choose the SSL CA Certficate here which you created with 'System > Cert Manager'.

            Choose 'none' if you do not use any kind of certificates.
            (Default: none)
        ssl_server_cert2 (str | Unset): (LDAP TLS Support - Server 2) SSL Server Certificate

            Choose the SSL Server Certficate here which you created with 'System > Cert Manager'.


            Choose 'none' if you do not use any kind of certificates.
            (Default: none)
        modulesldap2requirecert (str | Unset): (LDAP TLS Support - Server 2) Choose Certificate Verification Method
            (never, allow, demand)

            Choose how the certs should be checked.
            Click Info for details. (Default: never)

            - Never: Don't even bother trying.
            - Allow: Try but don't fail if the certificate can't be verified.
            - Demand: Fail if the certificate doesn't verify.
        ssl_ca_cert1_options (list[TextValue] | Unset):
        ssl_server_cert1_options (list[TextValue] | Unset):
        ssl_ca_cert2_options (list[TextValue] | Unset):
        ssl_server_cert2_options (list[TextValue] | Unset):
    """

    modulesldapenableauthorize: bool | Unset = UNSET
    modulesldapenableauthenticate: bool | Unset = UNSET
    modulesldapserver: str | Unset = UNSET
    modulesldapserverport: str | Unset = UNSET
    modulesldapidentity: str | Unset = UNSET
    modulesldappassword: str | Unset = UNSET
    modulesldapbasedn: str | Unset = UNSET
    modulesldapfilter: str | Unset = UNSET
    modulesldapbasefilter: str | Unset = UNSET
    modulesldapldapconnectionsnumber: str | Unset = UNSET
    modulesldaptimeout: str | Unset = UNSET
    modulesldaptimelimit: str | Unset = UNSET
    modulesldapnettimeout: str | Unset = UNSET
    modulesldapmsadcompatibilityenable: str | Unset = UNSET
    modulesldapdmiscenable: bool | Unset = UNSET
    modulesldapdefaultprofile: str | Unset = UNSET
    modulesldapprofileattribute: str | Unset = UNSET
    modulesldapaccessattr: str | Unset = UNSET
    modulesldapgroupenable: bool | Unset = UNSET
    modulesldapgroupnameattribute: str | Unset = UNSET
    modulesldapgroupmembershipfilter: str | Unset = UNSET
    modulesldapgroupmembershipattribute: str | Unset = UNSET
    modulesldapcomparecheckitems: str | Unset = UNSET
    modulesldapdoxlat: str | Unset = UNSET
    modulesldapaccessattrusedforallow: str | Unset = UNSET
    modulesldapkeepaliveidle: str | Unset = UNSET
    modulesldapkeepaliveprobes: str | Unset = UNSET
    modulesldapkeepaliveinterval: str | Unset = UNSET
    modulesldapenabletlssupport: bool | Unset = UNSET
    modulesldapenablestarttls: bool | Unset = UNSET
    ssl_ca_cert1: str | Unset = UNSET
    ssl_server_cert1: str | Unset = UNSET
    modulesldaprequirecert: str | Unset = UNSET
    modulesldap2failover: str | Unset = UNSET
    modulesldap2enableauthorize: bool | Unset = UNSET
    modulesldap2enableauthenticate: bool | Unset = UNSET
    modulesldap2server: str | Unset = UNSET
    modulesldap2serverport: str | Unset = UNSET
    modulesldap2identity: str | Unset = UNSET
    modulesldap2password: str | Unset = UNSET
    modulesldap2basedn: str | Unset = UNSET
    modulesldap2filter: str | Unset = UNSET
    modulesldap2basefilter: str | Unset = UNSET
    modulesldap2ldapconnectionsnumber: str | Unset = UNSET
    modulesldap2timeout: str | Unset = UNSET
    modulesldap2timelimit: str | Unset = UNSET
    modulesldap2nettimeout: str | Unset = UNSET
    modulesldap2msadcompatibilityenable: str | Unset = UNSET
    modulesldap2dmiscenable: bool | Unset = UNSET
    modulesldap2defaultprofile: str | Unset = UNSET
    modulesldap2profileattribute: str | Unset = UNSET
    modulesldap2accessattr: str | Unset = UNSET
    modulesldap2groupenable: bool | Unset = UNSET
    modulesldap2groupnameattribute: str | Unset = UNSET
    modulesldap2groupmembershipfilter: str | Unset = UNSET
    modulesldap2groupmembershipattribute: str | Unset = UNSET
    modulesldap2comparecheckitems: str | Unset = UNSET
    modulesldap2doxlat: str | Unset = UNSET
    modulesldap2accessattrusedforallow: str | Unset = UNSET
    modulesldap2keepaliveidle: str | Unset = UNSET
    modulesldap2keepaliveprobes: str | Unset = UNSET
    modulesldap2keepaliveinterval: str | Unset = UNSET
    modulesldap2enabletlssupport: bool | Unset = UNSET
    modulesldap2enablestarttls: bool | Unset = UNSET
    ssl_ca_cert2: str | Unset = UNSET
    ssl_server_cert2: str | Unset = UNSET
    modulesldap2requirecert: str | Unset = UNSET
    ssl_ca_cert1_options: list[TextValue] | Unset = UNSET
    ssl_server_cert1_options: list[TextValue] | Unset = UNSET
    ssl_ca_cert2_options: list[TextValue] | Unset = UNSET
    ssl_server_cert2_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        modulesldapenableauthorize = self.modulesldapenableauthorize

        modulesldapenableauthenticate = self.modulesldapenableauthenticate

        modulesldapserver = self.modulesldapserver

        modulesldapserverport = self.modulesldapserverport

        modulesldapidentity = self.modulesldapidentity

        modulesldappassword = self.modulesldappassword

        modulesldapbasedn = self.modulesldapbasedn

        modulesldapfilter = self.modulesldapfilter

        modulesldapbasefilter = self.modulesldapbasefilter

        modulesldapldapconnectionsnumber = self.modulesldapldapconnectionsnumber

        modulesldaptimeout = self.modulesldaptimeout

        modulesldaptimelimit = self.modulesldaptimelimit

        modulesldapnettimeout = self.modulesldapnettimeout

        modulesldapmsadcompatibilityenable = self.modulesldapmsadcompatibilityenable

        modulesldapdmiscenable = self.modulesldapdmiscenable

        modulesldapdefaultprofile = self.modulesldapdefaultprofile

        modulesldapprofileattribute = self.modulesldapprofileattribute

        modulesldapaccessattr = self.modulesldapaccessattr

        modulesldapgroupenable = self.modulesldapgroupenable

        modulesldapgroupnameattribute = self.modulesldapgroupnameattribute

        modulesldapgroupmembershipfilter = self.modulesldapgroupmembershipfilter

        modulesldapgroupmembershipattribute = self.modulesldapgroupmembershipattribute

        modulesldapcomparecheckitems = self.modulesldapcomparecheckitems

        modulesldapdoxlat = self.modulesldapdoxlat

        modulesldapaccessattrusedforallow = self.modulesldapaccessattrusedforallow

        modulesldapkeepaliveidle = self.modulesldapkeepaliveidle

        modulesldapkeepaliveprobes = self.modulesldapkeepaliveprobes

        modulesldapkeepaliveinterval = self.modulesldapkeepaliveinterval

        modulesldapenabletlssupport = self.modulesldapenabletlssupport

        modulesldapenablestarttls = self.modulesldapenablestarttls

        ssl_ca_cert1 = self.ssl_ca_cert1

        ssl_server_cert1 = self.ssl_server_cert1

        modulesldaprequirecert = self.modulesldaprequirecert

        modulesldap2failover = self.modulesldap2failover

        modulesldap2enableauthorize = self.modulesldap2enableauthorize

        modulesldap2enableauthenticate = self.modulesldap2enableauthenticate

        modulesldap2server = self.modulesldap2server

        modulesldap2serverport = self.modulesldap2serverport

        modulesldap2identity = self.modulesldap2identity

        modulesldap2password = self.modulesldap2password

        modulesldap2basedn = self.modulesldap2basedn

        modulesldap2filter = self.modulesldap2filter

        modulesldap2basefilter = self.modulesldap2basefilter

        modulesldap2ldapconnectionsnumber = self.modulesldap2ldapconnectionsnumber

        modulesldap2timeout = self.modulesldap2timeout

        modulesldap2timelimit = self.modulesldap2timelimit

        modulesldap2nettimeout = self.modulesldap2nettimeout

        modulesldap2msadcompatibilityenable = self.modulesldap2msadcompatibilityenable

        modulesldap2dmiscenable = self.modulesldap2dmiscenable

        modulesldap2defaultprofile = self.modulesldap2defaultprofile

        modulesldap2profileattribute = self.modulesldap2profileattribute

        modulesldap2accessattr = self.modulesldap2accessattr

        modulesldap2groupenable = self.modulesldap2groupenable

        modulesldap2groupnameattribute = self.modulesldap2groupnameattribute

        modulesldap2groupmembershipfilter = self.modulesldap2groupmembershipfilter

        modulesldap2groupmembershipattribute = self.modulesldap2groupmembershipattribute

        modulesldap2comparecheckitems = self.modulesldap2comparecheckitems

        modulesldap2doxlat = self.modulesldap2doxlat

        modulesldap2accessattrusedforallow = self.modulesldap2accessattrusedforallow

        modulesldap2keepaliveidle = self.modulesldap2keepaliveidle

        modulesldap2keepaliveprobes = self.modulesldap2keepaliveprobes

        modulesldap2keepaliveinterval = self.modulesldap2keepaliveinterval

        modulesldap2enabletlssupport = self.modulesldap2enabletlssupport

        modulesldap2enablestarttls = self.modulesldap2enablestarttls

        ssl_ca_cert2 = self.ssl_ca_cert2

        ssl_server_cert2 = self.ssl_server_cert2

        modulesldap2requirecert = self.modulesldap2requirecert

        ssl_ca_cert1_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssl_ca_cert1_options, Unset):
            ssl_ca_cert1_options = []
            for ssl_ca_cert1_options_item_data in self.ssl_ca_cert1_options:
                ssl_ca_cert1_options_item = ssl_ca_cert1_options_item_data.to_dict()
                ssl_ca_cert1_options.append(ssl_ca_cert1_options_item)

        ssl_server_cert1_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssl_server_cert1_options, Unset):
            ssl_server_cert1_options = []
            for ssl_server_cert1_options_item_data in self.ssl_server_cert1_options:
                ssl_server_cert1_options_item = ssl_server_cert1_options_item_data.to_dict()
                ssl_server_cert1_options.append(ssl_server_cert1_options_item)

        ssl_ca_cert2_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssl_ca_cert2_options, Unset):
            ssl_ca_cert2_options = []
            for ssl_ca_cert2_options_item_data in self.ssl_ca_cert2_options:
                ssl_ca_cert2_options_item = ssl_ca_cert2_options_item_data.to_dict()
                ssl_ca_cert2_options.append(ssl_ca_cert2_options_item)

        ssl_server_cert2_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssl_server_cert2_options, Unset):
            ssl_server_cert2_options = []
            for ssl_server_cert2_options_item_data in self.ssl_server_cert2_options:
                ssl_server_cert2_options_item = ssl_server_cert2_options_item_data.to_dict()
                ssl_server_cert2_options.append(ssl_server_cert2_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modulesldapenableauthorize is not UNSET:
            field_dict["modulesldapenableauthorize"] = modulesldapenableauthorize
        if modulesldapenableauthenticate is not UNSET:
            field_dict["modulesldapenableauthenticate"] = modulesldapenableauthenticate
        if modulesldapserver is not UNSET:
            field_dict["modulesldapserver"] = modulesldapserver
        if modulesldapserverport is not UNSET:
            field_dict["modulesldapserverport"] = modulesldapserverport
        if modulesldapidentity is not UNSET:
            field_dict["modulesldapidentity"] = modulesldapidentity
        if modulesldappassword is not UNSET:
            field_dict["modulesldappassword"] = modulesldappassword
        if modulesldapbasedn is not UNSET:
            field_dict["modulesldapbasedn"] = modulesldapbasedn
        if modulesldapfilter is not UNSET:
            field_dict["modulesldapfilter"] = modulesldapfilter
        if modulesldapbasefilter is not UNSET:
            field_dict["modulesldapbasefilter"] = modulesldapbasefilter
        if modulesldapldapconnectionsnumber is not UNSET:
            field_dict["modulesldapldapconnectionsnumber"] = modulesldapldapconnectionsnumber
        if modulesldaptimeout is not UNSET:
            field_dict["modulesldaptimeout"] = modulesldaptimeout
        if modulesldaptimelimit is not UNSET:
            field_dict["modulesldaptimelimit"] = modulesldaptimelimit
        if modulesldapnettimeout is not UNSET:
            field_dict["modulesldapnettimeout"] = modulesldapnettimeout
        if modulesldapmsadcompatibilityenable is not UNSET:
            field_dict["modulesldapmsadcompatibilityenable"] = modulesldapmsadcompatibilityenable
        if modulesldapdmiscenable is not UNSET:
            field_dict["modulesldapdmiscenable"] = modulesldapdmiscenable
        if modulesldapdefaultprofile is not UNSET:
            field_dict["modulesldapdefaultprofile"] = modulesldapdefaultprofile
        if modulesldapprofileattribute is not UNSET:
            field_dict["modulesldapprofileattribute"] = modulesldapprofileattribute
        if modulesldapaccessattr is not UNSET:
            field_dict["modulesldapaccessattr"] = modulesldapaccessattr
        if modulesldapgroupenable is not UNSET:
            field_dict["modulesldapgroupenable"] = modulesldapgroupenable
        if modulesldapgroupnameattribute is not UNSET:
            field_dict["modulesldapgroupnameattribute"] = modulesldapgroupnameattribute
        if modulesldapgroupmembershipfilter is not UNSET:
            field_dict["modulesldapgroupmembershipfilter"] = modulesldapgroupmembershipfilter
        if modulesldapgroupmembershipattribute is not UNSET:
            field_dict["modulesldapgroupmembershipattribute"] = modulesldapgroupmembershipattribute
        if modulesldapcomparecheckitems is not UNSET:
            field_dict["modulesldapcomparecheckitems"] = modulesldapcomparecheckitems
        if modulesldapdoxlat is not UNSET:
            field_dict["modulesldapdoxlat"] = modulesldapdoxlat
        if modulesldapaccessattrusedforallow is not UNSET:
            field_dict["modulesldapaccessattrusedforallow"] = modulesldapaccessattrusedforallow
        if modulesldapkeepaliveidle is not UNSET:
            field_dict["modulesldapkeepaliveidle"] = modulesldapkeepaliveidle
        if modulesldapkeepaliveprobes is not UNSET:
            field_dict["modulesldapkeepaliveprobes"] = modulesldapkeepaliveprobes
        if modulesldapkeepaliveinterval is not UNSET:
            field_dict["modulesldapkeepaliveinterval"] = modulesldapkeepaliveinterval
        if modulesldapenabletlssupport is not UNSET:
            field_dict["modulesldapenabletlssupport"] = modulesldapenabletlssupport
        if modulesldapenablestarttls is not UNSET:
            field_dict["modulesldapenablestarttls"] = modulesldapenablestarttls
        if ssl_ca_cert1 is not UNSET:
            field_dict["ssl_ca_cert1"] = ssl_ca_cert1
        if ssl_server_cert1 is not UNSET:
            field_dict["ssl_server_cert1"] = ssl_server_cert1
        if modulesldaprequirecert is not UNSET:
            field_dict["modulesldaprequirecert"] = modulesldaprequirecert
        if modulesldap2failover is not UNSET:
            field_dict["modulesldap2failover"] = modulesldap2failover
        if modulesldap2enableauthorize is not UNSET:
            field_dict["modulesldap2enableauthorize"] = modulesldap2enableauthorize
        if modulesldap2enableauthenticate is not UNSET:
            field_dict["modulesldap2enableauthenticate"] = modulesldap2enableauthenticate
        if modulesldap2server is not UNSET:
            field_dict["modulesldap2server"] = modulesldap2server
        if modulesldap2serverport is not UNSET:
            field_dict["modulesldap2serverport"] = modulesldap2serverport
        if modulesldap2identity is not UNSET:
            field_dict["modulesldap2identity"] = modulesldap2identity
        if modulesldap2password is not UNSET:
            field_dict["modulesldap2password"] = modulesldap2password
        if modulesldap2basedn is not UNSET:
            field_dict["modulesldap2basedn"] = modulesldap2basedn
        if modulesldap2filter is not UNSET:
            field_dict["modulesldap2filter"] = modulesldap2filter
        if modulesldap2basefilter is not UNSET:
            field_dict["modulesldap2basefilter"] = modulesldap2basefilter
        if modulesldap2ldapconnectionsnumber is not UNSET:
            field_dict["modulesldap2ldapconnectionsnumber"] = modulesldap2ldapconnectionsnumber
        if modulesldap2timeout is not UNSET:
            field_dict["modulesldap2timeout"] = modulesldap2timeout
        if modulesldap2timelimit is not UNSET:
            field_dict["modulesldap2timelimit"] = modulesldap2timelimit
        if modulesldap2nettimeout is not UNSET:
            field_dict["modulesldap2nettimeout"] = modulesldap2nettimeout
        if modulesldap2msadcompatibilityenable is not UNSET:
            field_dict["modulesldap2msadcompatibilityenable"] = modulesldap2msadcompatibilityenable
        if modulesldap2dmiscenable is not UNSET:
            field_dict["modulesldap2dmiscenable"] = modulesldap2dmiscenable
        if modulesldap2defaultprofile is not UNSET:
            field_dict["modulesldap2defaultprofile"] = modulesldap2defaultprofile
        if modulesldap2profileattribute is not UNSET:
            field_dict["modulesldap2profileattribute"] = modulesldap2profileattribute
        if modulesldap2accessattr is not UNSET:
            field_dict["modulesldap2accessattr"] = modulesldap2accessattr
        if modulesldap2groupenable is not UNSET:
            field_dict["modulesldap2groupenable"] = modulesldap2groupenable
        if modulesldap2groupnameattribute is not UNSET:
            field_dict["modulesldap2groupnameattribute"] = modulesldap2groupnameattribute
        if modulesldap2groupmembershipfilter is not UNSET:
            field_dict["modulesldap2groupmembershipfilter"] = modulesldap2groupmembershipfilter
        if modulesldap2groupmembershipattribute is not UNSET:
            field_dict["modulesldap2groupmembershipattribute"] = modulesldap2groupmembershipattribute
        if modulesldap2comparecheckitems is not UNSET:
            field_dict["modulesldap2comparecheckitems"] = modulesldap2comparecheckitems
        if modulesldap2doxlat is not UNSET:
            field_dict["modulesldap2doxlat"] = modulesldap2doxlat
        if modulesldap2accessattrusedforallow is not UNSET:
            field_dict["modulesldap2accessattrusedforallow"] = modulesldap2accessattrusedforallow
        if modulesldap2keepaliveidle is not UNSET:
            field_dict["modulesldap2keepaliveidle"] = modulesldap2keepaliveidle
        if modulesldap2keepaliveprobes is not UNSET:
            field_dict["modulesldap2keepaliveprobes"] = modulesldap2keepaliveprobes
        if modulesldap2keepaliveinterval is not UNSET:
            field_dict["modulesldap2keepaliveinterval"] = modulesldap2keepaliveinterval
        if modulesldap2enabletlssupport is not UNSET:
            field_dict["modulesldap2enabletlssupport"] = modulesldap2enabletlssupport
        if modulesldap2enablestarttls is not UNSET:
            field_dict["modulesldap2enablestarttls"] = modulesldap2enablestarttls
        if ssl_ca_cert2 is not UNSET:
            field_dict["ssl_ca_cert2"] = ssl_ca_cert2
        if ssl_server_cert2 is not UNSET:
            field_dict["ssl_server_cert2"] = ssl_server_cert2
        if modulesldap2requirecert is not UNSET:
            field_dict["modulesldap2requirecert"] = modulesldap2requirecert
        if ssl_ca_cert1_options is not UNSET:
            field_dict["ssl_ca_cert1_options"] = ssl_ca_cert1_options
        if ssl_server_cert1_options is not UNSET:
            field_dict["ssl_server_cert1_options"] = ssl_server_cert1_options
        if ssl_ca_cert2_options is not UNSET:
            field_dict["ssl_ca_cert2_options"] = ssl_ca_cert2_options
        if ssl_server_cert2_options is not UNSET:
            field_dict["ssl_server_cert2_options"] = ssl_server_cert2_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_value import TextValue

        d = dict(src_dict)
        modulesldapenableauthorize = d.pop("modulesldapenableauthorize", UNSET)

        modulesldapenableauthenticate = d.pop("modulesldapenableauthenticate", UNSET)

        modulesldapserver = d.pop("modulesldapserver", UNSET)

        modulesldapserverport = d.pop("modulesldapserverport", UNSET)

        modulesldapidentity = d.pop("modulesldapidentity", UNSET)

        modulesldappassword = d.pop("modulesldappassword", UNSET)

        modulesldapbasedn = d.pop("modulesldapbasedn", UNSET)

        modulesldapfilter = d.pop("modulesldapfilter", UNSET)

        modulesldapbasefilter = d.pop("modulesldapbasefilter", UNSET)

        modulesldapldapconnectionsnumber = d.pop("modulesldapldapconnectionsnumber", UNSET)

        modulesldaptimeout = d.pop("modulesldaptimeout", UNSET)

        modulesldaptimelimit = d.pop("modulesldaptimelimit", UNSET)

        modulesldapnettimeout = d.pop("modulesldapnettimeout", UNSET)

        modulesldapmsadcompatibilityenable = d.pop("modulesldapmsadcompatibilityenable", UNSET)

        modulesldapdmiscenable = d.pop("modulesldapdmiscenable", UNSET)

        modulesldapdefaultprofile = d.pop("modulesldapdefaultprofile", UNSET)

        modulesldapprofileattribute = d.pop("modulesldapprofileattribute", UNSET)

        modulesldapaccessattr = d.pop("modulesldapaccessattr", UNSET)

        modulesldapgroupenable = d.pop("modulesldapgroupenable", UNSET)

        modulesldapgroupnameattribute = d.pop("modulesldapgroupnameattribute", UNSET)

        modulesldapgroupmembershipfilter = d.pop("modulesldapgroupmembershipfilter", UNSET)

        modulesldapgroupmembershipattribute = d.pop("modulesldapgroupmembershipattribute", UNSET)

        modulesldapcomparecheckitems = d.pop("modulesldapcomparecheckitems", UNSET)

        modulesldapdoxlat = d.pop("modulesldapdoxlat", UNSET)

        modulesldapaccessattrusedforallow = d.pop("modulesldapaccessattrusedforallow", UNSET)

        modulesldapkeepaliveidle = d.pop("modulesldapkeepaliveidle", UNSET)

        modulesldapkeepaliveprobes = d.pop("modulesldapkeepaliveprobes", UNSET)

        modulesldapkeepaliveinterval = d.pop("modulesldapkeepaliveinterval", UNSET)

        modulesldapenabletlssupport = d.pop("modulesldapenabletlssupport", UNSET)

        modulesldapenablestarttls = d.pop("modulesldapenablestarttls", UNSET)

        ssl_ca_cert1 = d.pop("ssl_ca_cert1", UNSET)

        ssl_server_cert1 = d.pop("ssl_server_cert1", UNSET)

        modulesldaprequirecert = d.pop("modulesldaprequirecert", UNSET)

        modulesldap2failover = d.pop("modulesldap2failover", UNSET)

        modulesldap2enableauthorize = d.pop("modulesldap2enableauthorize", UNSET)

        modulesldap2enableauthenticate = d.pop("modulesldap2enableauthenticate", UNSET)

        modulesldap2server = d.pop("modulesldap2server", UNSET)

        modulesldap2serverport = d.pop("modulesldap2serverport", UNSET)

        modulesldap2identity = d.pop("modulesldap2identity", UNSET)

        modulesldap2password = d.pop("modulesldap2password", UNSET)

        modulesldap2basedn = d.pop("modulesldap2basedn", UNSET)

        modulesldap2filter = d.pop("modulesldap2filter", UNSET)

        modulesldap2basefilter = d.pop("modulesldap2basefilter", UNSET)

        modulesldap2ldapconnectionsnumber = d.pop("modulesldap2ldapconnectionsnumber", UNSET)

        modulesldap2timeout = d.pop("modulesldap2timeout", UNSET)

        modulesldap2timelimit = d.pop("modulesldap2timelimit", UNSET)

        modulesldap2nettimeout = d.pop("modulesldap2nettimeout", UNSET)

        modulesldap2msadcompatibilityenable = d.pop("modulesldap2msadcompatibilityenable", UNSET)

        modulesldap2dmiscenable = d.pop("modulesldap2dmiscenable", UNSET)

        modulesldap2defaultprofile = d.pop("modulesldap2defaultprofile", UNSET)

        modulesldap2profileattribute = d.pop("modulesldap2profileattribute", UNSET)

        modulesldap2accessattr = d.pop("modulesldap2accessattr", UNSET)

        modulesldap2groupenable = d.pop("modulesldap2groupenable", UNSET)

        modulesldap2groupnameattribute = d.pop("modulesldap2groupnameattribute", UNSET)

        modulesldap2groupmembershipfilter = d.pop("modulesldap2groupmembershipfilter", UNSET)

        modulesldap2groupmembershipattribute = d.pop("modulesldap2groupmembershipattribute", UNSET)

        modulesldap2comparecheckitems = d.pop("modulesldap2comparecheckitems", UNSET)

        modulesldap2doxlat = d.pop("modulesldap2doxlat", UNSET)

        modulesldap2accessattrusedforallow = d.pop("modulesldap2accessattrusedforallow", UNSET)

        modulesldap2keepaliveidle = d.pop("modulesldap2keepaliveidle", UNSET)

        modulesldap2keepaliveprobes = d.pop("modulesldap2keepaliveprobes", UNSET)

        modulesldap2keepaliveinterval = d.pop("modulesldap2keepaliveinterval", UNSET)

        modulesldap2enabletlssupport = d.pop("modulesldap2enabletlssupport", UNSET)

        modulesldap2enablestarttls = d.pop("modulesldap2enablestarttls", UNSET)

        ssl_ca_cert2 = d.pop("ssl_ca_cert2", UNSET)

        ssl_server_cert2 = d.pop("ssl_server_cert2", UNSET)

        modulesldap2requirecert = d.pop("modulesldap2requirecert", UNSET)

        _ssl_ca_cert1_options = d.pop("ssl_ca_cert1_options", UNSET)
        ssl_ca_cert1_options: list[TextValue] | Unset = UNSET
        if _ssl_ca_cert1_options is not UNSET:
            ssl_ca_cert1_options = []
            for ssl_ca_cert1_options_item_data in _ssl_ca_cert1_options:
                ssl_ca_cert1_options_item = TextValue.from_dict(ssl_ca_cert1_options_item_data)

                ssl_ca_cert1_options.append(ssl_ca_cert1_options_item)

        _ssl_server_cert1_options = d.pop("ssl_server_cert1_options", UNSET)
        ssl_server_cert1_options: list[TextValue] | Unset = UNSET
        if _ssl_server_cert1_options is not UNSET:
            ssl_server_cert1_options = []
            for ssl_server_cert1_options_item_data in _ssl_server_cert1_options:
                ssl_server_cert1_options_item = TextValue.from_dict(ssl_server_cert1_options_item_data)

                ssl_server_cert1_options.append(ssl_server_cert1_options_item)

        _ssl_ca_cert2_options = d.pop("ssl_ca_cert2_options", UNSET)
        ssl_ca_cert2_options: list[TextValue] | Unset = UNSET
        if _ssl_ca_cert2_options is not UNSET:
            ssl_ca_cert2_options = []
            for ssl_ca_cert2_options_item_data in _ssl_ca_cert2_options:
                ssl_ca_cert2_options_item = TextValue.from_dict(ssl_ca_cert2_options_item_data)

                ssl_ca_cert2_options.append(ssl_ca_cert2_options_item)

        _ssl_server_cert2_options = d.pop("ssl_server_cert2_options", UNSET)
        ssl_server_cert2_options: list[TextValue] | Unset = UNSET
        if _ssl_server_cert2_options is not UNSET:
            ssl_server_cert2_options = []
            for ssl_server_cert2_options_item_data in _ssl_server_cert2_options:
                ssl_server_cert2_options_item = TextValue.from_dict(ssl_server_cert2_options_item_data)

                ssl_server_cert2_options.append(ssl_server_cert2_options_item)

        freeradiusmodulesldap = cls(
            modulesldapenableauthorize=modulesldapenableauthorize,
            modulesldapenableauthenticate=modulesldapenableauthenticate,
            modulesldapserver=modulesldapserver,
            modulesldapserverport=modulesldapserverport,
            modulesldapidentity=modulesldapidentity,
            modulesldappassword=modulesldappassword,
            modulesldapbasedn=modulesldapbasedn,
            modulesldapfilter=modulesldapfilter,
            modulesldapbasefilter=modulesldapbasefilter,
            modulesldapldapconnectionsnumber=modulesldapldapconnectionsnumber,
            modulesldaptimeout=modulesldaptimeout,
            modulesldaptimelimit=modulesldaptimelimit,
            modulesldapnettimeout=modulesldapnettimeout,
            modulesldapmsadcompatibilityenable=modulesldapmsadcompatibilityenable,
            modulesldapdmiscenable=modulesldapdmiscenable,
            modulesldapdefaultprofile=modulesldapdefaultprofile,
            modulesldapprofileattribute=modulesldapprofileattribute,
            modulesldapaccessattr=modulesldapaccessattr,
            modulesldapgroupenable=modulesldapgroupenable,
            modulesldapgroupnameattribute=modulesldapgroupnameattribute,
            modulesldapgroupmembershipfilter=modulesldapgroupmembershipfilter,
            modulesldapgroupmembershipattribute=modulesldapgroupmembershipattribute,
            modulesldapcomparecheckitems=modulesldapcomparecheckitems,
            modulesldapdoxlat=modulesldapdoxlat,
            modulesldapaccessattrusedforallow=modulesldapaccessattrusedforallow,
            modulesldapkeepaliveidle=modulesldapkeepaliveidle,
            modulesldapkeepaliveprobes=modulesldapkeepaliveprobes,
            modulesldapkeepaliveinterval=modulesldapkeepaliveinterval,
            modulesldapenabletlssupport=modulesldapenabletlssupport,
            modulesldapenablestarttls=modulesldapenablestarttls,
            ssl_ca_cert1=ssl_ca_cert1,
            ssl_server_cert1=ssl_server_cert1,
            modulesldaprequirecert=modulesldaprequirecert,
            modulesldap2failover=modulesldap2failover,
            modulesldap2enableauthorize=modulesldap2enableauthorize,
            modulesldap2enableauthenticate=modulesldap2enableauthenticate,
            modulesldap2server=modulesldap2server,
            modulesldap2serverport=modulesldap2serverport,
            modulesldap2identity=modulesldap2identity,
            modulesldap2password=modulesldap2password,
            modulesldap2basedn=modulesldap2basedn,
            modulesldap2filter=modulesldap2filter,
            modulesldap2basefilter=modulesldap2basefilter,
            modulesldap2ldapconnectionsnumber=modulesldap2ldapconnectionsnumber,
            modulesldap2timeout=modulesldap2timeout,
            modulesldap2timelimit=modulesldap2timelimit,
            modulesldap2nettimeout=modulesldap2nettimeout,
            modulesldap2msadcompatibilityenable=modulesldap2msadcompatibilityenable,
            modulesldap2dmiscenable=modulesldap2dmiscenable,
            modulesldap2defaultprofile=modulesldap2defaultprofile,
            modulesldap2profileattribute=modulesldap2profileattribute,
            modulesldap2accessattr=modulesldap2accessattr,
            modulesldap2groupenable=modulesldap2groupenable,
            modulesldap2groupnameattribute=modulesldap2groupnameattribute,
            modulesldap2groupmembershipfilter=modulesldap2groupmembershipfilter,
            modulesldap2groupmembershipattribute=modulesldap2groupmembershipattribute,
            modulesldap2comparecheckitems=modulesldap2comparecheckitems,
            modulesldap2doxlat=modulesldap2doxlat,
            modulesldap2accessattrusedforallow=modulesldap2accessattrusedforallow,
            modulesldap2keepaliveidle=modulesldap2keepaliveidle,
            modulesldap2keepaliveprobes=modulesldap2keepaliveprobes,
            modulesldap2keepaliveinterval=modulesldap2keepaliveinterval,
            modulesldap2enabletlssupport=modulesldap2enabletlssupport,
            modulesldap2enablestarttls=modulesldap2enablestarttls,
            ssl_ca_cert2=ssl_ca_cert2,
            ssl_server_cert2=ssl_server_cert2,
            modulesldap2requirecert=modulesldap2requirecert,
            ssl_ca_cert1_options=ssl_ca_cert1_options,
            ssl_server_cert1_options=ssl_server_cert1_options,
            ssl_ca_cert2_options=ssl_ca_cert2_options,
            ssl_server_cert2_options=ssl_server_cert2_options,
        )

        freeradiusmodulesldap.additional_properties = d
        return freeradiusmodulesldap

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
