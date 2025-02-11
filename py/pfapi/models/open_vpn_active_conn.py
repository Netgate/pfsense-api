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
        vpnid (str):
        port (str):
        mode (str):
        name (str):
        mgmt (str):
        connect_time (str):
        state (str):
        state_detail (str):
        virtual_addr (str):
        remote_host (str):
        remote_port (str):
        local_host (str):
        local_port (str):
        virtual_addr6 (str):
        status (str):
        bytes_recv (str):
        bytes_sent (str):
        conns (Union[Unset, List['OpenVPNConn']]):
        routes (Union[Unset, List['OpenVPNRoute']]):
    """

    vpnid: str
    port: str
    mode: str
    name: str
    mgmt: str
    connect_time: str
    state: str
    state_detail: str
    virtual_addr: str
    remote_host: str
    remote_port: str
    local_host: str
    local_port: str
    virtual_addr6: str
    status: str
    bytes_recv: str
    bytes_sent: str
    conns: Union[Unset, List["OpenVPNConn"]] = UNSET
    routes: Union[Unset, List["OpenVPNRoute"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vpnid = self.vpnid

        port = self.port

        mode = self.mode

        name = self.name

        mgmt = self.mgmt

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vpnid": vpnid,
                "port": port,
                "mode": mode,
                "name": name,
                "mgmt": mgmt,
                "connect_time": connect_time,
                "state": state,
                "state_detail": state_detail,
                "virtual_addr": virtual_addr,
                "remote_host": remote_host,
                "remote_port": remote_port,
                "local_host": local_host,
                "local_port": local_port,
                "virtual_addr6": virtual_addr6,
                "status": status,
                "bytes_recv": bytes_recv,
                "bytes_sent": bytes_sent,
            }
        )
        if conns is not UNSET:
            field_dict["conns"] = conns
        if routes is not UNSET:
            field_dict["routes"] = routes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_vpn_conn import OpenVPNConn
        from ..models.open_vpn_route import OpenVPNRoute

        d = src_dict.copy()
        vpnid = d.pop("vpnid")

        port = d.pop("port")

        mode = d.pop("mode")

        name = d.pop("name")

        mgmt = d.pop("mgmt")

        connect_time = d.pop("connect_time")

        state = d.pop("state")

        state_detail = d.pop("state_detail")

        virtual_addr = d.pop("virtual_addr")

        remote_host = d.pop("remote_host")

        remote_port = d.pop("remote_port")

        local_host = d.pop("local_host")

        local_port = d.pop("local_port")

        virtual_addr6 = d.pop("virtual_addr6")

        status = d.pop("status")

        bytes_recv = d.pop("bytes_recv")

        bytes_sent = d.pop("bytes_sent")

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

        open_vpn_active_conn = cls(
            vpnid=vpnid,
            port=port,
            mode=mode,
            name=name,
            mgmt=mgmt,
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
            conns=conns,
            routes=routes,
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
