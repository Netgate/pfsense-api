from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpn_conn import OpenVPNConn
    from ..models.open_vpn_route import OpenVPNRoute


T = TypeVar("T", bound="OpenVPNActiveConn")


@_attrs_define
class OpenVPNActiveConn:
    """
    Attributes:
        vpnid (Union[Unset, str]):
        port (Union[Unset, str]):
        mode (Union[Unset, str]):
        name (Union[Unset, str]):
        mgmt (Union[Unset, str]):
        conns (Union[Unset, List['OpenVPNConn']]):
        routes (Union[Unset, List['OpenVPNRoute']]):
        connect_time (Union[Unset, str]):
        state (Union[Unset, str]):
        state_detail (Union[Unset, str]):
        virtual_addr (Union[Unset, str]):
        remote_host (Union[Unset, str]):
        remote_port (Union[Unset, str]):
        local_host (Union[Unset, str]):
        local_port (Union[Unset, str]):
        virtual_addr6 (Union[Unset, str]):
        status (Union[Unset, str]):
        bytes_recv (Union[Unset, str]):
        bytes_sent (Union[Unset, str]):
    """

    vpnid: Union[Unset, str] = UNSET
    port: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    mgmt: Union[Unset, str] = UNSET
    conns: Union[Unset, List["OpenVPNConn"]] = UNSET
    routes: Union[Unset, List["OpenVPNRoute"]] = UNSET
    connect_time: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    state_detail: Union[Unset, str] = UNSET
    virtual_addr: Union[Unset, str] = UNSET
    remote_host: Union[Unset, str] = UNSET
    remote_port: Union[Unset, str] = UNSET
    local_host: Union[Unset, str] = UNSET
    local_port: Union[Unset, str] = UNSET
    virtual_addr6: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    bytes_recv: Union[Unset, str] = UNSET
    bytes_sent: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vpnid = self.vpnid

        port = self.port

        mode = self.mode

        name = self.name

        mgmt = self.mgmt

        conns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conns, Unset):
            conns = []
            for conns_item_data in self.conns:
                conns_item = conns_item_data.to_dict()
                conns.append(conns_item)

        routes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.routes, Unset):
            routes = []
            for routes_item_data in self.routes:
                routes_item = routes_item_data.to_dict()
                routes.append(routes_item)

        connect_time = self.connect_time

        state = self.state

        state_detail = self.state_detail

        virtual_addr = self.virtual_addr

        remote_host = self.remote_host

        remote_port = self.remote_port

        local_host = self.local_host

        local_port = self.local_port

        virtual_addr6 = self.virtual_addr6

        status = self.status

        bytes_recv = self.bytes_recv

        bytes_sent = self.bytes_sent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpnid is not UNSET:
            field_dict["vpnid"] = vpnid
        if port is not UNSET:
            field_dict["port"] = port
        if mode is not UNSET:
            field_dict["mode"] = mode
        if name is not UNSET:
            field_dict["name"] = name
        if mgmt is not UNSET:
            field_dict["mgmt"] = mgmt
        if conns is not UNSET:
            field_dict["conns"] = conns
        if routes is not UNSET:
            field_dict["routes"] = routes
        if connect_time is not UNSET:
            field_dict["connect_time"] = connect_time
        if state is not UNSET:
            field_dict["state"] = state
        if state_detail is not UNSET:
            field_dict["state_detail"] = state_detail
        if virtual_addr is not UNSET:
            field_dict["virtual_addr"] = virtual_addr
        if remote_host is not UNSET:
            field_dict["remote_host"] = remote_host
        if remote_port is not UNSET:
            field_dict["remote_port"] = remote_port
        if local_host is not UNSET:
            field_dict["local_host"] = local_host
        if local_port is not UNSET:
            field_dict["local_port"] = local_port
        if virtual_addr6 is not UNSET:
            field_dict["virtual_addr6"] = virtual_addr6
        if status is not UNSET:
            field_dict["status"] = status
        if bytes_recv is not UNSET:
            field_dict["bytes_recv"] = bytes_recv
        if bytes_sent is not UNSET:
            field_dict["bytes_sent"] = bytes_sent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_vpn_conn import OpenVPNConn
        from ..models.open_vpn_route import OpenVPNRoute

        d = src_dict.copy()
        vpnid = d.pop("vpnid", UNSET)

        port = d.pop("port", UNSET)

        mode = d.pop("mode", UNSET)

        name = d.pop("name", UNSET)

        mgmt = d.pop("mgmt", UNSET)

        conns = []
        _conns = d.pop("conns", UNSET)
        for conns_item_data in _conns or []:
            conns_item = OpenVPNConn.from_dict(conns_item_data)

            conns.append(conns_item)

        routes = []
        _routes = d.pop("routes", UNSET)
        for routes_item_data in _routes or []:
            routes_item = OpenVPNRoute.from_dict(routes_item_data)

            routes.append(routes_item)

        connect_time = d.pop("connect_time", UNSET)

        state = d.pop("state", UNSET)

        state_detail = d.pop("state_detail", UNSET)

        virtual_addr = d.pop("virtual_addr", UNSET)

        remote_host = d.pop("remote_host", UNSET)

        remote_port = d.pop("remote_port", UNSET)

        local_host = d.pop("local_host", UNSET)

        local_port = d.pop("local_port", UNSET)

        virtual_addr6 = d.pop("virtual_addr6", UNSET)

        status = d.pop("status", UNSET)

        bytes_recv = d.pop("bytes_recv", UNSET)

        bytes_sent = d.pop("bytes_sent", UNSET)

        open_vpn_active_conn = cls(
            vpnid=vpnid,
            port=port,
            mode=mode,
            name=name,
            mgmt=mgmt,
            conns=conns,
            routes=routes,
            connect_time=connect_time,
            state=state,
            state_detail=state_detail,
            virtual_addr=virtual_addr,
            remote_host=remote_host,
            remote_port=remote_port,
            local_host=local_host,
            local_port=local_port,
            virtual_addr6=virtual_addr6,
            status=status,
            bytes_recv=bytes_recv,
            bytes_sent=bytes_sent,
        )

        open_vpn_active_conn.additional_properties = d
        return open_vpn_active_conn

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
