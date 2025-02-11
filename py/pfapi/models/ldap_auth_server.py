from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LdapAuthServer")


@_attrs_define
class LdapAuthServer:
    """
    Attributes:
        type (str):
        name (str):
        host (str):
        version (int): protocol version (3 default)
        port (int): 636 assumes "tls" encryption
        transport (str): "starttls", "tls", "none"
        timeout (int): seconds to timeout operation
        search_scope (str): "one", "subtree"
        base_dn (str): root base dn, e.g. dc=domain,dc=com
        auth_containers (str): semicolon separated list of search containers, prepended to base_dn
        extended_query (str): optional extra restriction for filtering username query, e.g.:
            - memberOf=CN=Pfnet,CN=Users,DC=example,DC=com
            - &(objectClass=posixGroup)(cn=Pfnet)(memberUid=*)
        bind_user_dn (str): for authenticated binding, the user-DN
        bind_password (str): for authenticated binding, the password (base64-encoded)
        user_naming_attrib (str): user naming attribute, e.g. "uid"
        group_naming_attrib (str): group naming attribute, e.g. "cn"
        group_member_attrib (str): e.g. "memberOf", "member"
        rfc2307 (bool): use RFC2307 style group membership
        rfc2307_group_class (str): object class for groups in rfc2307 mode, e.g. groupOfNames, posixGroup, group
        rfc2307_use_userdn (bool): use user-DN for querying user record
        shell_group_dn (str): group DN required for shell access
        username_alterations (bool): "true" to keep username verbatim (unstripped user@host)
        utf8_encode (bool): encodings are in utf-8
        unauthenticated_bind (bool): bind without password
        no_strip_at (bool): don't strip @<domain>
        caref (Union[Unset, str]): server's CA, ref
        certref (Union[Unset, str]): client certificate for secure transport
        refid (Union[Unset, str]):
    """

    type: str
    name: str
    host: str
    version: int
    port: int
    transport: str
    timeout: int
    search_scope: str
    base_dn: str
    auth_containers: str
    extended_query: str
    bind_user_dn: str
    bind_password: str
    user_naming_attrib: str
    group_naming_attrib: str
    group_member_attrib: str
    rfc2307: bool
    rfc2307_group_class: str
    rfc2307_use_userdn: bool
    shell_group_dn: str
    username_alterations: bool
    utf8_encode: bool
    unauthenticated_bind: bool
    no_strip_at: bool
    caref: Union[Unset, str] = UNSET
    certref: Union[Unset, str] = UNSET
    refid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        name = self.name

        host = self.host

        version = self.version

        port = self.port

        transport = self.transport

        timeout = self.timeout

        search_scope = self.search_scope

        base_dn = self.base_dn

        auth_containers = self.auth_containers

        extended_query = self.extended_query

        bind_user_dn = self.bind_user_dn

        bind_password = self.bind_password

        user_naming_attrib = self.user_naming_attrib

        group_naming_attrib = self.group_naming_attrib

        group_member_attrib = self.group_member_attrib

        rfc2307 = self.rfc2307

        rfc2307_group_class = self.rfc2307_group_class

        rfc2307_use_userdn = self.rfc2307_use_userdn

        shell_group_dn = self.shell_group_dn

        username_alterations = self.username_alterations

        utf8_encode = self.utf8_encode

        unauthenticated_bind = self.unauthenticated_bind

        no_strip_at = self.no_strip_at

        caref = self.caref

        certref = self.certref

        refid = self.refid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "name": name,
                "host": host,
                "version": version,
                "port": port,
                "transport": transport,
                "timeout": timeout,
                "search_scope": search_scope,
                "base_dn": base_dn,
                "auth_containers": auth_containers,
                "extended_query": extended_query,
                "bind_user_dn": bind_user_dn,
                "bind_password": bind_password,
                "user_naming_attrib": user_naming_attrib,
                "group_naming_attrib": group_naming_attrib,
                "group_member_attrib": group_member_attrib,
                "rfc2307": rfc2307,
                "rfc2307_group_class": rfc2307_group_class,
                "rfc2307_use_userdn": rfc2307_use_userdn,
                "shell_group_dn": shell_group_dn,
                "username_alterations": username_alterations,
                "utf8_encode": utf8_encode,
                "unauthenticated_bind": unauthenticated_bind,
                "no_strip_at": no_strip_at,
            }
        )
        if caref is not UNSET:
            field_dict["caref"] = caref
        if certref is not UNSET:
            field_dict["certref"] = certref
        if refid is not UNSET:
            field_dict["refid"] = refid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        name = d.pop("name")

        host = d.pop("host")

        version = d.pop("version")

        port = d.pop("port")

        transport = d.pop("transport")

        timeout = d.pop("timeout")

        search_scope = d.pop("search_scope")

        base_dn = d.pop("base_dn")

        auth_containers = d.pop("auth_containers")

        extended_query = d.pop("extended_query")

        bind_user_dn = d.pop("bind_user_dn")

        bind_password = d.pop("bind_password")

        user_naming_attrib = d.pop("user_naming_attrib")

        group_naming_attrib = d.pop("group_naming_attrib")

        group_member_attrib = d.pop("group_member_attrib")

        rfc2307 = d.pop("rfc2307")

        rfc2307_group_class = d.pop("rfc2307_group_class")

        rfc2307_use_userdn = d.pop("rfc2307_use_userdn")

        shell_group_dn = d.pop("shell_group_dn")

        username_alterations = d.pop("username_alterations")

        utf8_encode = d.pop("utf8_encode")

        unauthenticated_bind = d.pop("unauthenticated_bind")

        no_strip_at = d.pop("no_strip_at")

        caref = d.pop("caref", UNSET)

        certref = d.pop("certref", UNSET)

        refid = d.pop("refid", UNSET)

        ldap_auth_server = cls(
            type=type,
            name=name,
            host=host,
            version=version,
            port=port,
            transport=transport,
            timeout=timeout,
            search_scope=search_scope,
            base_dn=base_dn,
            auth_containers=auth_containers,
            extended_query=extended_query,
            bind_user_dn=bind_user_dn,
            bind_password=bind_password,
            user_naming_attrib=user_naming_attrib,
            group_naming_attrib=group_naming_attrib,
            group_member_attrib=group_member_attrib,
            rfc2307=rfc2307,
            rfc2307_group_class=rfc2307_group_class,
            rfc2307_use_userdn=rfc2307_use_userdn,
            shell_group_dn=shell_group_dn,
            username_alterations=username_alterations,
            utf8_encode=utf8_encode,
            unauthenticated_bind=unauthenticated_bind,
            no_strip_at=no_strip_at,
            caref=caref,
            certref=certref,
            refid=refid,
        )

        ldap_auth_server.additional_properties = d
        return ldap_auth_server

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
