from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HaproxyAction")


@_attrs_define
class HaproxyAction:
    """
    Attributes:
        action (str | Unset): Action Type

            The action to perform when conditions are met. Valid values include:
            use_backend, use_server, custom,
            http-request_allow, http-request_deny, http-request_tarpit, http-request_auth,
            http-request_redirect, http-request_lua, http-request_set-header,
            http-request_add-header, http-request_set-var, http-request_del-header,
            http-request_replace-header, http-request_replace-value,
            http-request_set-path, http-request_set-uri,
            http-request_track-sc0, http-request_cache-use,
            http-request_set-map, http-request_del-map,
            http-response_set-header, http-response_add-header, http-response_del-header,
            http-response_replace-header, http-response_replace-value,
            http-response_lua, http-response_set-status,
            http-response_set-map, http-response_del-map,
            tcp-request_content_accept, tcp-request_content_reject,
            tcp-request_content_lua, tcp-request_content_set-var,
            tcp-response_content_accept, tcp-response_content_reject,
            tcp-response_content_lua, tcp-response_content_close,
            tcp-response_content_set-var
        acl (str | Unset): ACL Condition

            Space-separated list of ACL names. The action triggers when all named ACLs match.
            Use "!" prefix to negate. Multiple ACLs are ANDed together.
        use_backendbackend (str | Unset): Backend

            Target backend pool name for use_backend actions.
        use_backendserver (str | Unset): Server

            Target server name for use_server actions.
        map_use_backendbackend (str | Unset): Map Backend

            Backend name for map-based use_backend actions.
        http_request_auth_realm (str | Unset): Auth Realm

            HTTP authentication realm string for http-request auth actions.
        http_request_redirect (str | Unset): Redirect Rule

            Full redirect rule for http-request redirect actions.
        customaction (str | Unset): Custom Action

            Raw HAProxy action line for custom action types.
        lua_function (str | Unset): Lua Function

            Name of the Lua function to call for lua action types.
        header_name (str | Unset): Header Name

            HTTP header name for set-header, add-header, del-header, replace-header,
            and replace-value actions.
        header_value (str | Unset): Header Value

            HTTP header value or pattern for header manipulation actions.
        header_replace (str | Unset): Header Replace Pattern

            Replacement pattern for replace-header and replace-value actions.
        set_var_name (str | Unset): Variable Name

            Variable name for set-var actions. Format: scope.name (e.g. req.my_var).
        set_var_expr (str | Unset): Variable Expression

            Expression to evaluate for set-var actions.
        http_response_code (str | Unset): Response Status Code

            HTTP status code for set-status actions.
        http_response_reason (str | Unset): Response Reason

            HTTP status reason phrase for set-status actions.
        set_path (str | Unset): Path

            New path value for set-path actions.
        set_uri (str | Unset): URI

            New URI value for set-uri actions.
        track_sc0_table (str | Unset): Track Table

            Stick-table name for track-sc0 actions.
        track_sc0_key (str | Unset): Track Key

            Key expression for track-sc0 actions.
        cache_name (str | Unset): Cache Name

            Cache name for cache-use actions.
        map_file (str | Unset): Map File

            Map file path for set-map and del-map actions.
        map_keyfmt (str | Unset): Map Key Format

            Key format expression for set-map and del-map actions.
        map_valuefmt (str | Unset): Map Value Format

            Value format expression for set-map actions.
    """

    action: str | Unset = UNSET
    acl: str | Unset = UNSET
    use_backendbackend: str | Unset = UNSET
    use_backendserver: str | Unset = UNSET
    map_use_backendbackend: str | Unset = UNSET
    http_request_auth_realm: str | Unset = UNSET
    http_request_redirect: str | Unset = UNSET
    customaction: str | Unset = UNSET
    lua_function: str | Unset = UNSET
    header_name: str | Unset = UNSET
    header_value: str | Unset = UNSET
    header_replace: str | Unset = UNSET
    set_var_name: str | Unset = UNSET
    set_var_expr: str | Unset = UNSET
    http_response_code: str | Unset = UNSET
    http_response_reason: str | Unset = UNSET
    set_path: str | Unset = UNSET
    set_uri: str | Unset = UNSET
    track_sc0_table: str | Unset = UNSET
    track_sc0_key: str | Unset = UNSET
    cache_name: str | Unset = UNSET
    map_file: str | Unset = UNSET
    map_keyfmt: str | Unset = UNSET
    map_valuefmt: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        acl = self.acl

        use_backendbackend = self.use_backendbackend

        use_backendserver = self.use_backendserver

        map_use_backendbackend = self.map_use_backendbackend

        http_request_auth_realm = self.http_request_auth_realm

        http_request_redirect = self.http_request_redirect

        customaction = self.customaction

        lua_function = self.lua_function

        header_name = self.header_name

        header_value = self.header_value

        header_replace = self.header_replace

        set_var_name = self.set_var_name

        set_var_expr = self.set_var_expr

        http_response_code = self.http_response_code

        http_response_reason = self.http_response_reason

        set_path = self.set_path

        set_uri = self.set_uri

        track_sc0_table = self.track_sc0_table

        track_sc0_key = self.track_sc0_key

        cache_name = self.cache_name

        map_file = self.map_file

        map_keyfmt = self.map_keyfmt

        map_valuefmt = self.map_valuefmt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if acl is not UNSET:
            field_dict["acl"] = acl
        if use_backendbackend is not UNSET:
            field_dict["use_backendbackend"] = use_backendbackend
        if use_backendserver is not UNSET:
            field_dict["use_backendserver"] = use_backendserver
        if map_use_backendbackend is not UNSET:
            field_dict["map_use_backendbackend"] = map_use_backendbackend
        if http_request_auth_realm is not UNSET:
            field_dict["http_request_auth_realm"] = http_request_auth_realm
        if http_request_redirect is not UNSET:
            field_dict["http_request_redirect"] = http_request_redirect
        if customaction is not UNSET:
            field_dict["customaction"] = customaction
        if lua_function is not UNSET:
            field_dict["lua_function"] = lua_function
        if header_name is not UNSET:
            field_dict["header_name"] = header_name
        if header_value is not UNSET:
            field_dict["header_value"] = header_value
        if header_replace is not UNSET:
            field_dict["header_replace"] = header_replace
        if set_var_name is not UNSET:
            field_dict["set_var_name"] = set_var_name
        if set_var_expr is not UNSET:
            field_dict["set_var_expr"] = set_var_expr
        if http_response_code is not UNSET:
            field_dict["http_response_code"] = http_response_code
        if http_response_reason is not UNSET:
            field_dict["http_response_reason"] = http_response_reason
        if set_path is not UNSET:
            field_dict["set_path"] = set_path
        if set_uri is not UNSET:
            field_dict["set_uri"] = set_uri
        if track_sc0_table is not UNSET:
            field_dict["track_sc0_table"] = track_sc0_table
        if track_sc0_key is not UNSET:
            field_dict["track_sc0_key"] = track_sc0_key
        if cache_name is not UNSET:
            field_dict["cache_name"] = cache_name
        if map_file is not UNSET:
            field_dict["map_file"] = map_file
        if map_keyfmt is not UNSET:
            field_dict["map_keyfmt"] = map_keyfmt
        if map_valuefmt is not UNSET:
            field_dict["map_valuefmt"] = map_valuefmt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        acl = d.pop("acl", UNSET)

        use_backendbackend = d.pop("use_backendbackend", UNSET)

        use_backendserver = d.pop("use_backendserver", UNSET)

        map_use_backendbackend = d.pop("map_use_backendbackend", UNSET)

        http_request_auth_realm = d.pop("http_request_auth_realm", UNSET)

        http_request_redirect = d.pop("http_request_redirect", UNSET)

        customaction = d.pop("customaction", UNSET)

        lua_function = d.pop("lua_function", UNSET)

        header_name = d.pop("header_name", UNSET)

        header_value = d.pop("header_value", UNSET)

        header_replace = d.pop("header_replace", UNSET)

        set_var_name = d.pop("set_var_name", UNSET)

        set_var_expr = d.pop("set_var_expr", UNSET)

        http_response_code = d.pop("http_response_code", UNSET)

        http_response_reason = d.pop("http_response_reason", UNSET)

        set_path = d.pop("set_path", UNSET)

        set_uri = d.pop("set_uri", UNSET)

        track_sc0_table = d.pop("track_sc0_table", UNSET)

        track_sc0_key = d.pop("track_sc0_key", UNSET)

        cache_name = d.pop("cache_name", UNSET)

        map_file = d.pop("map_file", UNSET)

        map_keyfmt = d.pop("map_keyfmt", UNSET)

        map_valuefmt = d.pop("map_valuefmt", UNSET)

        haproxy_action = cls(
            action=action,
            acl=acl,
            use_backendbackend=use_backendbackend,
            use_backendserver=use_backendserver,
            map_use_backendbackend=map_use_backendbackend,
            http_request_auth_realm=http_request_auth_realm,
            http_request_redirect=http_request_redirect,
            customaction=customaction,
            lua_function=lua_function,
            header_name=header_name,
            header_value=header_value,
            header_replace=header_replace,
            set_var_name=set_var_name,
            set_var_expr=set_var_expr,
            http_response_code=http_response_code,
            http_response_reason=http_response_reason,
            set_path=set_path,
            set_uri=set_uri,
            track_sc0_table=track_sc0_table,
            track_sc0_key=track_sc0_key,
            cache_name=cache_name,
            map_file=map_file,
            map_keyfmt=map_keyfmt,
            map_valuefmt=map_valuefmt,
        )

        haproxy_action.additional_properties = d
        return haproxy_action

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
