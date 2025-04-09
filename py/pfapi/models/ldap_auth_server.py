from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LdapAuthServer")


@_attrs_define
class LdapAuthServer:
    """
    Attributes:
        name (str):
        host (str):
        base_dn (str): root base dn, e.g. dc=domain,dc=com
        type (Union[Unset, str]):
        version (Union[Unset, int]): protocol version (3 default)
        port (Union[Unset, int]): 636 assumes "tls" encryption
        transport (Union[Unset, str]): "starttls", "tls", "none"
        timeout (Union[Unset, int]): seconds to timeout operation
        search_scope (Union[Unset, str]): "one", "subtree"
        auth_containers (Union[Unset, str]): semicolon separated list of search containers, prepended to base_dn
        extended_query (Union[Unset, str]): optional extra restriction for filtering username query, e.g.:
            - memberOf=CN=Pfnet,CN=Users,DC=example,DC=com
            - &(objectClass=posixGroup)(cn=Pfnet)(memberUid=*)
        bind_user_dn (Union[Unset, str]): for authenticated binding, the user-DN
        bind_password (Union[Unset, str]): for authenticated binding, the password (base64-encoded)
        user_naming_attrib (Union[Unset, str]): user naming attribute, e.g. "uid"
        group_naming_attrib (Union[Unset, str]): group naming attribute, e.g. "cn"
        group_member_attrib (Union[Unset, str]): e.g. "memberOf", "member"
        rfc2307 (Union[Unset, bool]): use RFC2307 style group membership
        rfc2307_group_class (Union[Unset, str]): object class for groups in rfc2307 mode, e.g. groupOfNames, posixGroup,
            group
        rfc2307_use_userdn (Union[Unset, bool]): use user-DN for querying user record
        shell_group_dn (Union[Unset, str]): group DN required for shell access
        username_alterations (Union[Unset, bool]): "true" to keep username verbatim (unstripped user@host)
        utf8_encode (Union[Unset, bool]): encodings are in utf-8
        unauthenticated_bind (Union[Unset, bool]): bind without password
        no_strip_at (Union[Unset, bool]): don't strip @<domain>
        caref (Union[Unset, str]): server's CA, ref
        certref (Union[Unset, str]): client certificate for secure transport
        refid (Union[Unset, str]):
    """

    name: str
    host: str
    base_dn: str
    type: Union[Unset, str] = UNSET
    version: Union[Unset, int] = UNSET
    port: Union[Unset, int] = UNSET
    transport: Union[Unset, str] = UNSET
    timeout: Union[Unset, int] = UNSET
    search_scope: Union[Unset, str] = UNSET
    auth_containers: Union[Unset, str] = UNSET
    extended_query: Union[Unset, str] = UNSET
    bind_user_dn: Union[Unset, str] = UNSET
    bind_password: Union[Unset, str] = UNSET
    user_naming_attrib: Union[Unset, str] = UNSET
    group_naming_attrib: Union[Unset, str] = UNSET
    group_member_attrib: Union[Unset, str] = UNSET
    rfc2307: Union[Unset, bool] = UNSET
    rfc2307_group_class: Union[Unset, str] = UNSET
    rfc2307_use_userdn: Union[Unset, bool] = UNSET
    shell_group_dn: Union[Unset, str] = UNSET
    username_alterations: Union[Unset, bool] = UNSET
    utf8_encode: Union[Unset, bool] = UNSET
    unauthenticated_bind: Union[Unset, bool] = UNSET
    no_strip_at: Union[Unset, bool] = UNSET
    caref: Union[Unset, str] = UNSET
    certref: Union[Unset, str] = UNSET
    refid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        host = self.host

        base_dn = self.base_dn

        type = self.type

        version = self.version

        port = self.port

        transport = self.transport

        timeout = self.timeout

        search_scope = self.search_scope

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
                "name": name,
                "host": host,
                "base_dn": base_dn,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if version is not UNSET:
            field_dict["version"] = version
        if port is not UNSET:
            field_dict["port"] = port
        if transport is not UNSET:
            field_dict["transport"] = transport
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if search_scope is not UNSET:
            field_dict["search_scope"] = search_scope
        if auth_containers is not UNSET:
            field_dict["auth_containers"] = auth_containers
        if extended_query is not UNSET:
            field_dict["extended_query"] = extended_query
        if bind_user_dn is not UNSET:
            field_dict["bind_user_dn"] = bind_user_dn
        if bind_password is not UNSET:
            field_dict["bind_password"] = bind_password
        if user_naming_attrib is not UNSET:
            field_dict["user_naming_attrib"] = user_naming_attrib
        if group_naming_attrib is not UNSET:
            field_dict["group_naming_attrib"] = group_naming_attrib
        if group_member_attrib is not UNSET:
            field_dict["group_member_attrib"] = group_member_attrib
        if rfc2307 is not UNSET:
            field_dict["rfc2307"] = rfc2307
        if rfc2307_group_class is not UNSET:
            field_dict["rfc2307_group_class"] = rfc2307_group_class
        if rfc2307_use_userdn is not UNSET:
            field_dict["rfc2307_use_userdn"] = rfc2307_use_userdn
        if shell_group_dn is not UNSET:
            field_dict["shell_group_dn"] = shell_group_dn
        if username_alterations is not UNSET:
            field_dict["username_alterations"] = username_alterations
        if utf8_encode is not UNSET:
            field_dict["utf8_encode"] = utf8_encode
        if unauthenticated_bind is not UNSET:
            field_dict["unauthenticated_bind"] = unauthenticated_bind
        if no_strip_at is not UNSET:
            field_dict["no_strip_at"] = no_strip_at
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
        name = d.pop("name")

        host = d.pop("host")

        base_dn = d.pop("base_dn")

        type = d.pop("type", UNSET)

        version = d.pop("version", UNSET)

        port = d.pop("port", UNSET)

        transport = d.pop("transport", UNSET)

        timeout = d.pop("timeout", UNSET)

        search_scope = d.pop("search_scope", UNSET)

        auth_containers = d.pop("auth_containers", UNSET)

        extended_query = d.pop("extended_query", UNSET)

        bind_user_dn = d.pop("bind_user_dn", UNSET)

        bind_password = d.pop("bind_password", UNSET)

        user_naming_attrib = d.pop("user_naming_attrib", UNSET)

        group_naming_attrib = d.pop("group_naming_attrib", UNSET)

        group_member_attrib = d.pop("group_member_attrib", UNSET)

        rfc2307 = d.pop("rfc2307", UNSET)

        rfc2307_group_class = d.pop("rfc2307_group_class", UNSET)

        rfc2307_use_userdn = d.pop("rfc2307_use_userdn", UNSET)

        shell_group_dn = d.pop("shell_group_dn", UNSET)

        username_alterations = d.pop("username_alterations", UNSET)

        utf8_encode = d.pop("utf8_encode", UNSET)

        unauthenticated_bind = d.pop("unauthenticated_bind", UNSET)

        no_strip_at = d.pop("no_strip_at", UNSET)

        caref = d.pop("caref", UNSET)

        certref = d.pop("certref", UNSET)

        refid = d.pop("refid", UNSET)

        ldap_auth_server = cls(
            name=name,
            host=host,
            base_dn=base_dn,
            type=type,
            version=version,
            port=port,
            transport=transport,
            timeout=timeout,
            search_scope=search_scope,
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
