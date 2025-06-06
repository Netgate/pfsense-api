from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.altq_root_queue_bandwidthtype import ALTQRootQueueBandwidthtype
from ..models.altq_root_queue_scheduler import ALTQRootQueueScheduler
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.altq_child_queue import ALTQChildQueue


T = TypeVar("T", bound="ALTQRootQueue")


@_attrs_define
class ALTQRootQueue:
    """
    Attributes:
        if_ident (str): identity of the interface for this traffic shaper (root queue)
        scheduler (ALTQRootQueueScheduler): scheduler type
            valid values = HFSC, CBQ, FAIRQ, CODELQ, PRIQ
        bandwidth (int): the amount of bandwidth available on this interface in the outbound direction
        bandwidthtype (ALTQRootQueueBandwidthtype): units for the bandwidth
            valid value = Kb, Mb, Gb, b, %
        enabled (Union[Unset, bool]):
        name (Union[Unset, str]): generated by system when create altq root queue
        qlimit (Union[Unset, int]): the number of packets that can be held in a queue waiting to be transmitted by the
            shaper, default size is 50
        tbrsize (Union[Unset, int]): adjusts the size, in bytes, of the token bucket regulator
        queue (Union[Unset, List['ALTQChildQueue']]):
    """

    if_ident: str
    scheduler: ALTQRootQueueScheduler
    bandwidth: int
    bandwidthtype: ALTQRootQueueBandwidthtype
    enabled: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    qlimit: Union[Unset, int] = UNSET
    tbrsize: Union[Unset, int] = UNSET
    queue: Union[Unset, List["ALTQChildQueue"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if_ident = self.if_ident

        scheduler = self.scheduler.value

        bandwidth = self.bandwidth

        bandwidthtype = self.bandwidthtype.value

        enabled = self.enabled

        name = self.name

        qlimit = self.qlimit

        tbrsize = self.tbrsize

        queue: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.queue, Unset):
            queue = []
            for queue_item_data in self.queue:
                queue_item = queue_item_data.to_dict()
                queue.append(queue_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "if_ident": if_ident,
                "scheduler": scheduler,
                "bandwidth": bandwidth,
                "bandwidthtype": bandwidthtype,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name
        if qlimit is not UNSET:
            field_dict["qlimit"] = qlimit
        if tbrsize is not UNSET:
            field_dict["tbrsize"] = tbrsize
        if queue is not UNSET:
            field_dict["queue"] = queue

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.altq_child_queue import ALTQChildQueue

        d = src_dict.copy()
        if_ident = d.pop("if_ident")

        scheduler = ALTQRootQueueScheduler(d.pop("scheduler"))

        bandwidth = d.pop("bandwidth")

        bandwidthtype = ALTQRootQueueBandwidthtype(d.pop("bandwidthtype"))

        enabled = d.pop("enabled", UNSET)

        name = d.pop("name", UNSET)

        qlimit = d.pop("qlimit", UNSET)

        tbrsize = d.pop("tbrsize", UNSET)

        queue = []
        _queue = d.pop("queue", UNSET)
        for queue_item_data in _queue or []:
            queue_item = ALTQChildQueue.from_dict(queue_item_data)

            queue.append(queue_item)

        altq_root_queue = cls(
            if_ident=if_ident,
            scheduler=scheduler,
            bandwidth=bandwidth,
            bandwidthtype=bandwidthtype,
            enabled=enabled,
            name=name,
            qlimit=qlimit,
            tbrsize=tbrsize,
            queue=queue,
        )

        altq_root_queue.additional_properties = d
        return altq_root_queue

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
