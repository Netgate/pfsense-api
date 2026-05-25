from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.haproxy_acl import HaproxyAcl
    from ..models.haproxy_action import HaproxyAction
    from ..models.haproxy_error_file import HaproxyErrorFile
    from ..models.haproxy_server import HaproxyServer


T = TypeVar("T", bound="HaproxyPool")


@_attrs_define
class HaproxyPool:
    """
    Attributes:
        name (str | Unset): Name

            Unique name for this backend pool. Referenced by frontends and actions.
        balance (str | Unset): Balance Algorithm (roundrobin, static-rr, leastconn, source, uri, url_param, hdr, random,
            rdp-cookie)

            Load balancing algorithm used to select a server for each connection.
            - roundrobin: Weighted round-robin, servers are used in turns
            - static-rr: Static round-robin, does not support weight changes at runtime
            - leastconn: Route to the server with the fewest connections
            - source: Hash the source IP for consistent server mapping
            - uri: Hash the URI for consistent routing of same URLs
            - url_param: Hash a URL parameter value
            - hdr: Hash an HTTP header value
            - random: Random server selection
            - rdp-cookie: Hash the RDP cookie for RDP session persistence
        balance_urilen (str | Unset): URI Balance Length

            Maximum URI length to consider for URI-based hashing.
        balance_uridepth (str | Unset): URI Balance Depth

            Maximum directory depth to consider for URI-based hashing.
        balance_uriwhole (bool | Unset): Whole URI

            Hash the entire URI including query string instead of path only.
        transparent_clientip (bool | Unset): Transparent Client IP

            Enable transparent proxy mode using the client's source IP.
        transparent_interface (str | Unset): Transparent Interface

            Interface to use for transparent proxy mode.
        check_type (str | Unset): Health Check Type (none, Basic, HTTP, LDAP, MySQL, PostgreSQL, Redis, SMTP, ESMTP,
            SSL, Agent)

            Type of health check to perform on backend servers.
            - none: No health checks
            - Basic: TCP connection check
            - HTTP: HTTP request check
            - LDAP/MySQL/PostgreSQL/Redis: Protocol-specific check
            - SMTP/ESMTP: Mail server check
            - SSL: SSL connection check
            - Agent: External agent check
        checkinter (str | Unset): Check Interval

            Interval between health checks in milliseconds.
            (Default: 1000)
        log_health_checks (bool | Unset): Log Health Checks

            Log health check status changes to syslog.
        httpcheck_method (str | Unset): HTTP Check Method (OPTIONS, HEAD, GET, POST, PUT, DELETE, TRACE)

            HTTP method to use for HTTP health checks.
            (Default: OPTIONS)
        monitor_uri (str | Unset): Monitor URI

            URI path to request for HTTP health checks.
            (Default: /)
        monitor_httpversion (str | Unset): Monitor HTTP Version

            HTTP version string to use in health check requests.
            (Default: HTTP/1.0)
        monitor_username (str | Unset): Monitor Username

            Username for MySQL/PostgreSQL health check authentication.
        monitor_domain (str | Unset): Monitor Domain

            Domain name for SMTP/ESMTP health check HELO command.
        monitor_agentport (str | Unset): Agent Check Port

            Port to use for agent health checks.
        agent_check (bool | Unset): Enable Agent Check

            Enable an auxiliary agent-based health check in addition to the primary check.
        agent_port (str | Unset): Agent Port

            Port for the auxiliary agent check.
        agent_inter (str | Unset): Agent Check Interval

            Interval between agent checks in milliseconds.
        connection_timeout (str | Unset): Connection Timeout

            Maximum time to wait for a connection to a backend server, in milliseconds.
        server_timeout (str | Unset): Server Timeout

            Maximum time to wait for a response from a backend server, in milliseconds.
        retries (str | Unset): Retries

            Number of connection retry attempts after a failure.
            (Default: 3)
        persist_cookie_enabled (bool | Unset): Cookie Persistence

            Enable cookie-based session persistence.
        persist_cookie_name (str | Unset): Cookie Name

            Name of the persistence cookie.
        persist_cookie_mode (str | Unset): Cookie Mode (passive, passive-silent, reset, set, set-silent, insert-only,
            insert-only-silent, session-prefix, passive-session-prefix)

            How the persistence cookie is managed.
            - passive: Read existing cookies, do not set new ones
            - insert-only: Insert a cookie if none exists
            - set: Always set the cookie
        persist_cookie_cachable (bool | Unset): Cookie Cacheable

            Allow caching of responses with persistence cookies.
        persist_cookie_postonly (bool | Unset): Cookie POST Only

            Only set the persistence cookie on POST responses.
        persist_cookie_httponly (bool | Unset): Cookie HttpOnly

            Set the HttpOnly flag on the persistence cookie.
        persist_cookie_secure (bool | Unset): Cookie Secure

            Set the Secure flag on the persistence cookie.
        haproxy_cookie_maxidle (str | Unset): Cookie Max Idle

            Maximum idle time for the persistence cookie.
        haproxy_cookie_maxlife (str | Unset): Cookie Max Life

            Maximum lifetime for the persistence cookie.
        haproxy_cookie_domains (str | Unset): Cookie Domains

            Domain(s) to set on the persistence cookie.
        haproxy_cookie_dynamic_cookie_key (str | Unset): Dynamic Cookie Key

            Secret key for dynamic cookie value generation.
        persist_sticky_type (str | Unset): Sticky Table Type (none, stick_sslsessionid, stick_sourceipv4,
            stick_sourceipv6, stick_cookie_value, stick_rdp_cookie)

            Type of stick-table persistence to use.
            - none: No stick-table persistence
            - stick_sslsessionid: Persist by SSL session ID
            - stick_sourceipv4: Persist by client IPv4 address
            - stick_sourceipv6: Persist by client IPv6 address
            - stick_cookie_value: Persist by cookie value
            - stick_rdp_cookie: Persist by RDP cookie
        persist_stick_expire (str | Unset): Stick Table Expiration

            Time after which idle entries are removed from the stick table.
        persist_stick_tablesize (str | Unset): Stick Table Size

            Maximum number of entries in the stick table (e.g. 50k, 10m).
        persist_stick_length (str | Unset): Stick Pattern Length

            Maximum length of the stick pattern.
        persist_stick_cookiename (str | Unset): Stick Cookie Name

            Cookie name for cookie-value based stick-table persistence.
        stats_enabled (bool | Unset): Enable Statistics

            Enable the HAProxy statistics page for this backend.
        stats_username (str | Unset): Stats Username

            Username for HTTP basic authentication on the statistics page.
        stats_password (str | Unset): Stats Password

            Password for HTTP basic authentication on the statistics page.
        stats_uri (str | Unset): Stats URI

            URI path for the statistics page.
            (Default: /)
        stats_scope (str | Unset): Stats Scope

            Restrict the stats page to specific backends (comma-separated names).
        stats_realm (str | Unset): Stats Realm

            HTTP authentication realm for the statistics page.
        stats_admin (str | Unset): Stats Admin

            ACL expression to enable admin mode on the statistics page.
        stats_node (str | Unset): Stats Node

            Node name displayed on the statistics page.
        stats_desc (str | Unset): Stats Description

            Description shown on the statistics page.
        stats_refresh (str | Unset): Stats Refresh

            Auto-refresh interval for the statistics page in seconds.
        strict_transport_security (str | Unset): HSTS Header

            Strict-Transport-Security header value (e.g. max-age=31536000).
        cookie_attribute_secure (bool | Unset): Cookie Protection

            Set "secure" attribute on cookies (only used on "http" frontends).
        email_level (str | Unset): Email Alert Level (emerg, alert, crit, err, warning, notice, info, debug)

            Minimum severity level for email notifications for this backend.
        email_to (str | Unset): Email To

            Recipient email address for alerts from this backend.
        ha_servers (list[HaproxyServer] | Unset):
        a_acl (list[HaproxyAcl] | Unset):
        a_actionitems (list[HaproxyAction] | Unset):
        errorfiles (list[HaproxyErrorFile] | Unset):
        advanced (str | Unset): Advanced Frontend Pass Thru

            Base64-encoded raw configuration for the frontend-like section of this backend.
        advanced_backend (str | Unset): Advanced Backend Pass Thru

            Base64-encoded raw configuration appended to this backend section.
        id (str | Unset): (readonly) ID assigned to this entry
    """

    name: str | Unset = UNSET
    balance: str | Unset = UNSET
    balance_urilen: str | Unset = UNSET
    balance_uridepth: str | Unset = UNSET
    balance_uriwhole: bool | Unset = UNSET
    transparent_clientip: bool | Unset = UNSET
    transparent_interface: str | Unset = UNSET
    check_type: str | Unset = UNSET
    checkinter: str | Unset = UNSET
    log_health_checks: bool | Unset = UNSET
    httpcheck_method: str | Unset = UNSET
    monitor_uri: str | Unset = UNSET
    monitor_httpversion: str | Unset = UNSET
    monitor_username: str | Unset = UNSET
    monitor_domain: str | Unset = UNSET
    monitor_agentport: str | Unset = UNSET
    agent_check: bool | Unset = UNSET
    agent_port: str | Unset = UNSET
    agent_inter: str | Unset = UNSET
    connection_timeout: str | Unset = UNSET
    server_timeout: str | Unset = UNSET
    retries: str | Unset = UNSET
    persist_cookie_enabled: bool | Unset = UNSET
    persist_cookie_name: str | Unset = UNSET
    persist_cookie_mode: str | Unset = UNSET
    persist_cookie_cachable: bool | Unset = UNSET
    persist_cookie_postonly: bool | Unset = UNSET
    persist_cookie_httponly: bool | Unset = UNSET
    persist_cookie_secure: bool | Unset = UNSET
    haproxy_cookie_maxidle: str | Unset = UNSET
    haproxy_cookie_maxlife: str | Unset = UNSET
    haproxy_cookie_domains: str | Unset = UNSET
    haproxy_cookie_dynamic_cookie_key: str | Unset = UNSET
    persist_sticky_type: str | Unset = UNSET
    persist_stick_expire: str | Unset = UNSET
    persist_stick_tablesize: str | Unset = UNSET
    persist_stick_length: str | Unset = UNSET
    persist_stick_cookiename: str | Unset = UNSET
    stats_enabled: bool | Unset = UNSET
    stats_username: str | Unset = UNSET
    stats_password: str | Unset = UNSET
    stats_uri: str | Unset = UNSET
    stats_scope: str | Unset = UNSET
    stats_realm: str | Unset = UNSET
    stats_admin: str | Unset = UNSET
    stats_node: str | Unset = UNSET
    stats_desc: str | Unset = UNSET
    stats_refresh: str | Unset = UNSET
    strict_transport_security: str | Unset = UNSET
    cookie_attribute_secure: bool | Unset = UNSET
    email_level: str | Unset = UNSET
    email_to: str | Unset = UNSET
    ha_servers: list[HaproxyServer] | Unset = UNSET
    a_acl: list[HaproxyAcl] | Unset = UNSET
    a_actionitems: list[HaproxyAction] | Unset = UNSET
    errorfiles: list[HaproxyErrorFile] | Unset = UNSET
    advanced: str | Unset = UNSET
    advanced_backend: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        balance = self.balance

        balance_urilen = self.balance_urilen

        balance_uridepth = self.balance_uridepth

        balance_uriwhole = self.balance_uriwhole

        transparent_clientip = self.transparent_clientip

        transparent_interface = self.transparent_interface

        check_type = self.check_type

        checkinter = self.checkinter

        log_health_checks = self.log_health_checks

        httpcheck_method = self.httpcheck_method

        monitor_uri = self.monitor_uri

        monitor_httpversion = self.monitor_httpversion

        monitor_username = self.monitor_username

        monitor_domain = self.monitor_domain

        monitor_agentport = self.monitor_agentport

        agent_check = self.agent_check

        agent_port = self.agent_port

        agent_inter = self.agent_inter

        connection_timeout = self.connection_timeout

        server_timeout = self.server_timeout

        retries = self.retries

        persist_cookie_enabled = self.persist_cookie_enabled

        persist_cookie_name = self.persist_cookie_name

        persist_cookie_mode = self.persist_cookie_mode

        persist_cookie_cachable = self.persist_cookie_cachable

        persist_cookie_postonly = self.persist_cookie_postonly

        persist_cookie_httponly = self.persist_cookie_httponly

        persist_cookie_secure = self.persist_cookie_secure

        haproxy_cookie_maxidle = self.haproxy_cookie_maxidle

        haproxy_cookie_maxlife = self.haproxy_cookie_maxlife

        haproxy_cookie_domains = self.haproxy_cookie_domains

        haproxy_cookie_dynamic_cookie_key = self.haproxy_cookie_dynamic_cookie_key

        persist_sticky_type = self.persist_sticky_type

        persist_stick_expire = self.persist_stick_expire

        persist_stick_tablesize = self.persist_stick_tablesize

        persist_stick_length = self.persist_stick_length

        persist_stick_cookiename = self.persist_stick_cookiename

        stats_enabled = self.stats_enabled

        stats_username = self.stats_username

        stats_password = self.stats_password

        stats_uri = self.stats_uri

        stats_scope = self.stats_scope

        stats_realm = self.stats_realm

        stats_admin = self.stats_admin

        stats_node = self.stats_node

        stats_desc = self.stats_desc

        stats_refresh = self.stats_refresh

        strict_transport_security = self.strict_transport_security

        cookie_attribute_secure = self.cookie_attribute_secure

        email_level = self.email_level

        email_to = self.email_to

        ha_servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ha_servers, Unset):
            ha_servers = []
            for ha_servers_item_data in self.ha_servers:
                ha_servers_item = ha_servers_item_data.to_dict()
                ha_servers.append(ha_servers_item)

        a_acl: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.a_acl, Unset):
            a_acl = []
            for a_acl_item_data in self.a_acl:
                a_acl_item = a_acl_item_data.to_dict()
                a_acl.append(a_acl_item)

        a_actionitems: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.a_actionitems, Unset):
            a_actionitems = []
            for a_actionitems_item_data in self.a_actionitems:
                a_actionitems_item = a_actionitems_item_data.to_dict()
                a_actionitems.append(a_actionitems_item)

        errorfiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errorfiles, Unset):
            errorfiles = []
            for errorfiles_item_data in self.errorfiles:
                errorfiles_item = errorfiles_item_data.to_dict()
                errorfiles.append(errorfiles_item)

        advanced = self.advanced

        advanced_backend = self.advanced_backend

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if balance is not UNSET:
            field_dict["balance"] = balance
        if balance_urilen is not UNSET:
            field_dict["balance_urilen"] = balance_urilen
        if balance_uridepth is not UNSET:
            field_dict["balance_uridepth"] = balance_uridepth
        if balance_uriwhole is not UNSET:
            field_dict["balance_uriwhole"] = balance_uriwhole
        if transparent_clientip is not UNSET:
            field_dict["transparent_clientip"] = transparent_clientip
        if transparent_interface is not UNSET:
            field_dict["transparent_interface"] = transparent_interface
        if check_type is not UNSET:
            field_dict["check_type"] = check_type
        if checkinter is not UNSET:
            field_dict["checkinter"] = checkinter
        if log_health_checks is not UNSET:
            field_dict["log_health_checks"] = log_health_checks
        if httpcheck_method is not UNSET:
            field_dict["httpcheck_method"] = httpcheck_method
        if monitor_uri is not UNSET:
            field_dict["monitor_uri"] = monitor_uri
        if monitor_httpversion is not UNSET:
            field_dict["monitor_httpversion"] = monitor_httpversion
        if monitor_username is not UNSET:
            field_dict["monitor_username"] = monitor_username
        if monitor_domain is not UNSET:
            field_dict["monitor_domain"] = monitor_domain
        if monitor_agentport is not UNSET:
            field_dict["monitor_agentport"] = monitor_agentport
        if agent_check is not UNSET:
            field_dict["agent_check"] = agent_check
        if agent_port is not UNSET:
            field_dict["agent_port"] = agent_port
        if agent_inter is not UNSET:
            field_dict["agent_inter"] = agent_inter
        if connection_timeout is not UNSET:
            field_dict["connection_timeout"] = connection_timeout
        if server_timeout is not UNSET:
            field_dict["server_timeout"] = server_timeout
        if retries is not UNSET:
            field_dict["retries"] = retries
        if persist_cookie_enabled is not UNSET:
            field_dict["persist_cookie_enabled"] = persist_cookie_enabled
        if persist_cookie_name is not UNSET:
            field_dict["persist_cookie_name"] = persist_cookie_name
        if persist_cookie_mode is not UNSET:
            field_dict["persist_cookie_mode"] = persist_cookie_mode
        if persist_cookie_cachable is not UNSET:
            field_dict["persist_cookie_cachable"] = persist_cookie_cachable
        if persist_cookie_postonly is not UNSET:
            field_dict["persist_cookie_postonly"] = persist_cookie_postonly
        if persist_cookie_httponly is not UNSET:
            field_dict["persist_cookie_httponly"] = persist_cookie_httponly
        if persist_cookie_secure is not UNSET:
            field_dict["persist_cookie_secure"] = persist_cookie_secure
        if haproxy_cookie_maxidle is not UNSET:
            field_dict["haproxy_cookie_maxidle"] = haproxy_cookie_maxidle
        if haproxy_cookie_maxlife is not UNSET:
            field_dict["haproxy_cookie_maxlife"] = haproxy_cookie_maxlife
        if haproxy_cookie_domains is not UNSET:
            field_dict["haproxy_cookie_domains"] = haproxy_cookie_domains
        if haproxy_cookie_dynamic_cookie_key is not UNSET:
            field_dict["haproxy_cookie_dynamic_cookie_key"] = haproxy_cookie_dynamic_cookie_key
        if persist_sticky_type is not UNSET:
            field_dict["persist_sticky_type"] = persist_sticky_type
        if persist_stick_expire is not UNSET:
            field_dict["persist_stick_expire"] = persist_stick_expire
        if persist_stick_tablesize is not UNSET:
            field_dict["persist_stick_tablesize"] = persist_stick_tablesize
        if persist_stick_length is not UNSET:
            field_dict["persist_stick_length"] = persist_stick_length
        if persist_stick_cookiename is not UNSET:
            field_dict["persist_stick_cookiename"] = persist_stick_cookiename
        if stats_enabled is not UNSET:
            field_dict["stats_enabled"] = stats_enabled
        if stats_username is not UNSET:
            field_dict["stats_username"] = stats_username
        if stats_password is not UNSET:
            field_dict["stats_password"] = stats_password
        if stats_uri is not UNSET:
            field_dict["stats_uri"] = stats_uri
        if stats_scope is not UNSET:
            field_dict["stats_scope"] = stats_scope
        if stats_realm is not UNSET:
            field_dict["stats_realm"] = stats_realm
        if stats_admin is not UNSET:
            field_dict["stats_admin"] = stats_admin
        if stats_node is not UNSET:
            field_dict["stats_node"] = stats_node
        if stats_desc is not UNSET:
            field_dict["stats_desc"] = stats_desc
        if stats_refresh is not UNSET:
            field_dict["stats_refresh"] = stats_refresh
        if strict_transport_security is not UNSET:
            field_dict["strict_transport_security"] = strict_transport_security
        if cookie_attribute_secure is not UNSET:
            field_dict["cookie_attribute_secure"] = cookie_attribute_secure
        if email_level is not UNSET:
            field_dict["email_level"] = email_level
        if email_to is not UNSET:
            field_dict["email_to"] = email_to
        if ha_servers is not UNSET:
            field_dict["ha_servers"] = ha_servers
        if a_acl is not UNSET:
            field_dict["a_acl"] = a_acl
        if a_actionitems is not UNSET:
            field_dict["a_actionitems"] = a_actionitems
        if errorfiles is not UNSET:
            field_dict["errorfiles"] = errorfiles
        if advanced is not UNSET:
            field_dict["advanced"] = advanced
        if advanced_backend is not UNSET:
            field_dict["advanced_backend"] = advanced_backend
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.haproxy_acl import HaproxyAcl
        from ..models.haproxy_action import HaproxyAction
        from ..models.haproxy_error_file import HaproxyErrorFile
        from ..models.haproxy_server import HaproxyServer

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        balance = d.pop("balance", UNSET)

        balance_urilen = d.pop("balance_urilen", UNSET)

        balance_uridepth = d.pop("balance_uridepth", UNSET)

        balance_uriwhole = d.pop("balance_uriwhole", UNSET)

        transparent_clientip = d.pop("transparent_clientip", UNSET)

        transparent_interface = d.pop("transparent_interface", UNSET)

        check_type = d.pop("check_type", UNSET)

        checkinter = d.pop("checkinter", UNSET)

        log_health_checks = d.pop("log_health_checks", UNSET)

        httpcheck_method = d.pop("httpcheck_method", UNSET)

        monitor_uri = d.pop("monitor_uri", UNSET)

        monitor_httpversion = d.pop("monitor_httpversion", UNSET)

        monitor_username = d.pop("monitor_username", UNSET)

        monitor_domain = d.pop("monitor_domain", UNSET)

        monitor_agentport = d.pop("monitor_agentport", UNSET)

        agent_check = d.pop("agent_check", UNSET)

        agent_port = d.pop("agent_port", UNSET)

        agent_inter = d.pop("agent_inter", UNSET)

        connection_timeout = d.pop("connection_timeout", UNSET)

        server_timeout = d.pop("server_timeout", UNSET)

        retries = d.pop("retries", UNSET)

        persist_cookie_enabled = d.pop("persist_cookie_enabled", UNSET)

        persist_cookie_name = d.pop("persist_cookie_name", UNSET)

        persist_cookie_mode = d.pop("persist_cookie_mode", UNSET)

        persist_cookie_cachable = d.pop("persist_cookie_cachable", UNSET)

        persist_cookie_postonly = d.pop("persist_cookie_postonly", UNSET)

        persist_cookie_httponly = d.pop("persist_cookie_httponly", UNSET)

        persist_cookie_secure = d.pop("persist_cookie_secure", UNSET)

        haproxy_cookie_maxidle = d.pop("haproxy_cookie_maxidle", UNSET)

        haproxy_cookie_maxlife = d.pop("haproxy_cookie_maxlife", UNSET)

        haproxy_cookie_domains = d.pop("haproxy_cookie_domains", UNSET)

        haproxy_cookie_dynamic_cookie_key = d.pop("haproxy_cookie_dynamic_cookie_key", UNSET)

        persist_sticky_type = d.pop("persist_sticky_type", UNSET)

        persist_stick_expire = d.pop("persist_stick_expire", UNSET)

        persist_stick_tablesize = d.pop("persist_stick_tablesize", UNSET)

        persist_stick_length = d.pop("persist_stick_length", UNSET)

        persist_stick_cookiename = d.pop("persist_stick_cookiename", UNSET)

        stats_enabled = d.pop("stats_enabled", UNSET)

        stats_username = d.pop("stats_username", UNSET)

        stats_password = d.pop("stats_password", UNSET)

        stats_uri = d.pop("stats_uri", UNSET)

        stats_scope = d.pop("stats_scope", UNSET)

        stats_realm = d.pop("stats_realm", UNSET)

        stats_admin = d.pop("stats_admin", UNSET)

        stats_node = d.pop("stats_node", UNSET)

        stats_desc = d.pop("stats_desc", UNSET)

        stats_refresh = d.pop("stats_refresh", UNSET)

        strict_transport_security = d.pop("strict_transport_security", UNSET)

        cookie_attribute_secure = d.pop("cookie_attribute_secure", UNSET)

        email_level = d.pop("email_level", UNSET)

        email_to = d.pop("email_to", UNSET)

        _ha_servers = d.pop("ha_servers", UNSET)
        ha_servers: list[HaproxyServer] | Unset = UNSET
        if _ha_servers is not UNSET:
            ha_servers = []
            for ha_servers_item_data in _ha_servers:
                ha_servers_item = HaproxyServer.from_dict(ha_servers_item_data)

                ha_servers.append(ha_servers_item)

        _a_acl = d.pop("a_acl", UNSET)
        a_acl: list[HaproxyAcl] | Unset = UNSET
        if _a_acl is not UNSET:
            a_acl = []
            for a_acl_item_data in _a_acl:
                a_acl_item = HaproxyAcl.from_dict(a_acl_item_data)

                a_acl.append(a_acl_item)

        _a_actionitems = d.pop("a_actionitems", UNSET)
        a_actionitems: list[HaproxyAction] | Unset = UNSET
        if _a_actionitems is not UNSET:
            a_actionitems = []
            for a_actionitems_item_data in _a_actionitems:
                a_actionitems_item = HaproxyAction.from_dict(a_actionitems_item_data)

                a_actionitems.append(a_actionitems_item)

        _errorfiles = d.pop("errorfiles", UNSET)
        errorfiles: list[HaproxyErrorFile] | Unset = UNSET
        if _errorfiles is not UNSET:
            errorfiles = []
            for errorfiles_item_data in _errorfiles:
                errorfiles_item = HaproxyErrorFile.from_dict(errorfiles_item_data)

                errorfiles.append(errorfiles_item)

        advanced = d.pop("advanced", UNSET)

        advanced_backend = d.pop("advanced_backend", UNSET)

        id = d.pop("id", UNSET)

        haproxy_pool = cls(
            name=name,
            balance=balance,
            balance_urilen=balance_urilen,
            balance_uridepth=balance_uridepth,
            balance_uriwhole=balance_uriwhole,
            transparent_clientip=transparent_clientip,
            transparent_interface=transparent_interface,
            check_type=check_type,
            checkinter=checkinter,
            log_health_checks=log_health_checks,
            httpcheck_method=httpcheck_method,
            monitor_uri=monitor_uri,
            monitor_httpversion=monitor_httpversion,
            monitor_username=monitor_username,
            monitor_domain=monitor_domain,
            monitor_agentport=monitor_agentport,
            agent_check=agent_check,
            agent_port=agent_port,
            agent_inter=agent_inter,
            connection_timeout=connection_timeout,
            server_timeout=server_timeout,
            retries=retries,
            persist_cookie_enabled=persist_cookie_enabled,
            persist_cookie_name=persist_cookie_name,
            persist_cookie_mode=persist_cookie_mode,
            persist_cookie_cachable=persist_cookie_cachable,
            persist_cookie_postonly=persist_cookie_postonly,
            persist_cookie_httponly=persist_cookie_httponly,
            persist_cookie_secure=persist_cookie_secure,
            haproxy_cookie_maxidle=haproxy_cookie_maxidle,
            haproxy_cookie_maxlife=haproxy_cookie_maxlife,
            haproxy_cookie_domains=haproxy_cookie_domains,
            haproxy_cookie_dynamic_cookie_key=haproxy_cookie_dynamic_cookie_key,
            persist_sticky_type=persist_sticky_type,
            persist_stick_expire=persist_stick_expire,
            persist_stick_tablesize=persist_stick_tablesize,
            persist_stick_length=persist_stick_length,
            persist_stick_cookiename=persist_stick_cookiename,
            stats_enabled=stats_enabled,
            stats_username=stats_username,
            stats_password=stats_password,
            stats_uri=stats_uri,
            stats_scope=stats_scope,
            stats_realm=stats_realm,
            stats_admin=stats_admin,
            stats_node=stats_node,
            stats_desc=stats_desc,
            stats_refresh=stats_refresh,
            strict_transport_security=strict_transport_security,
            cookie_attribute_secure=cookie_attribute_secure,
            email_level=email_level,
            email_to=email_to,
            ha_servers=ha_servers,
            a_acl=a_acl,
            a_actionitems=a_actionitems,
            errorfiles=errorfiles,
            advanced=advanced,
            advanced_backend=advanced_backend,
            id=id,
        )

        haproxy_pool.additional_properties = d
        return haproxy_pool

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
