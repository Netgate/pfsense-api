"""Contains all the data models used in inputs/outputs"""

from .acb_backup import ACBBackup
from .acb_config import ACBConfig
from .acb_config_info import ACBConfigInfo
from .acb_list import ACBList
from .acb_manual_backup_request import ACBManualBackupRequest
from .acb_restore_request import ACBRestoreRequest
from .activate_bootenv import ActivateBootenv
from .adv_firewall import AdvFirewall
from .adv_firewall_setting import AdvFirewallSetting
from .adv_misc import AdvMisc
from .adv_misc_setting import AdvMiscSetting
from .adv_network_setting import AdvNetworkSetting
from .adv_networking import AdvNetworking
from .adv_notification_setting import AdvNotificationSetting
from .adv_notifications import AdvNotifications
from .all_software_packages import AllSoftwarePackages
from .all_software_packages_software_packages import AllSoftwarePackagesSoftwarePackages
from .altq_capable_interface import ALTQCapableInterface
from .altq_child_queue import ALTQChildQueue
from .altq_root_queue import ALTQRootQueue
from .altq_root_queue_bandwidthtype import ALTQRootQueueBandwidthtype
from .altq_root_queue_scheduler import ALTQRootQueueScheduler
from .altq_root_queues import ALTQRootQueues
from .apply_dirty_config_request import ApplyDirtyConfigRequest
from .arp_table_entry import ArpTableEntry
from .auth_server import AuthServer
from .auth_servers import AuthServers
from .auth_servers_list import AuthServersList
from .auth_test_credentials import AuthTestCredentials
from .auth_test_result import AuthTestResult
from .boot_envs import BootEnvs
from .boot_envs_envs import BootEnvsEnvs
from .bootenv import Bootenv
from .bridge_capable_interface import BridgeCapableInterface
from .bridge_interface import BridgeInterface
from .bridge_interface_ifpathcost import BridgeInterfaceIfpathcost
from .bridge_interface_ifpriority import BridgeInterfaceIfpriority
from .bridge_interfaces import BridgeInterfaces
from .ca_cert_method_existing import CaCertMethodExisting
from .ca_cert_method_new import CaCertMethodNew
from .captive_allowed_host import CaptiveAllowedHost
from .captive_allowed_ip import CaptiveAllowedIP
from .captive_element import CaptiveElement
from .captive_passthru_mac import CaptivePassthruMac
from .captive_portal_config import CaptivePortalConfig
from .captive_portal_disconnect_request import CaptivePortalDisconnectRequest
from .captive_portal_info import CaptivePortalInfo
from .captive_portal_name import CaptivePortalName
from .captive_portal_status import CaptivePortalStatus
from .captive_portal_user_info import CaptivePortalUserInfo
from .captive_portals import CaptivePortals
from .carp_reset_demotion_result import CARPResetDemotionResult
from .carp_status import CARPStatus
from .carpvip_status import CARPVIPStatus
from .cert_alt_name import CertAltName
from .cert_authorities import CertAuthorities
from .cert_authority import CertAuthority
from .cert_config import CertConfig
from .cert_info import CertInfo
from .cert_key_export_opts import CertKeyExportOpts
from .cert_method_existing_pem import CertMethodExistingPEM
from .cert_method_existing_pkcs_12 import CertMethodExistingPkcs12
from .cert_method_new import CertMethodNew
from .cert_method_sign_csr import CertMethodSignCSR
from .cert_method_signing_request import CertMethodSigningRequest
from .cert_opts import CertOpts
from .cert_pkcs_12_export_opts import CertPkcs12ExportOpts
from .cert_pkcs_12_export_opts_encryption import CertPkcs12ExportOptsEncryption
from .certificate_detailed import CertificateDetailed
from .certs_config import CertsConfig
from .check_ip_service import CheckIPService
from .check_ip_services_list import CheckIPServicesList
from .config_event import ConfigEvent
from .console_client import ConsoleClient
from .console_clients import ConsoleClients
from .controlled_device import ControlledDevice
from .controlled_device_auth import ControlledDeviceAuth
from .controlled_device_cert import ControlledDeviceCert
from .controlled_device_cert_options import ControlledDeviceCertOptions
from .controlled_device_certs import ControlledDeviceCerts
from .controlled_device_detailed import ControlledDeviceDetailed
from .controlled_device_info import ControlledDeviceInfo
from .controlled_devices import ControlledDevices
from .controller_alarm import ControllerAlarm
from .controller_alarms import ControllerAlarms
from .controller_alarms_alarms import ControllerAlarmsAlarms
from .controller_backup import ControllerBackup
from .controller_backup_request import ControllerBackupRequest
from .controller_backup_restore_request import ControllerBackupRestoreRequest
from .controller_backup_restore_result import ControllerBackupRestoreResult
from .controller_backup_result import ControllerBackupResult
from .controller_backups import ControllerBackups
from .controller_descrip import ControllerDescrip
from .controller_descrip_host_os import ControllerDescripHostOs
from .controller_identity import ControllerIdentity
from .controller_info import ControllerInfo
from .controller_service_action import ControllerServiceAction
from .controller_service_action_action import ControllerServiceActionAction
from .controller_stats import ControllerStats
from .controller_summary import ControllerSummary
from .controller_upgrade_info import ControllerUpgradeInfo
from .controller_upgrade_request import ControllerUpgradeRequest
from .controller_upgrade_result import ControllerUpgradeResult
from .controllers_list import ControllersList
from .create_bootenv import CreateBootenv
from .create_controlled_device_cert import CreateControlledDeviceCert
from .create_u_pn_pacl import CreateUPnPACL
from .crl_cert import CRLCert
from .crl_config import CRLConfig
from .crl_config_pkgs import CRLConfigPkgs
from .crl_entries import CRLEntries
from .crl_method_internal_update import CRLMethodInternalUpdate
from .crl_method_internal_update_revoke_reason import CRLMethodInternalUpdateRevokeReason
from .crl_method_new import CRLMethodNew
from .crl_method_x509 import CRLMethodX509
from .crl_package_info import CRLPackageInfo
from .delete_bootenvs import DeleteBootenvs
from .delete_controlled_device_cert_request import DeleteControlledDeviceCertRequest
from .delete_firewall_rule import DeleteFirewallRule
from .device_basic_info import DeviceBasicInfo
from .device_controller_info import DeviceControllerInfo
from .device_identity import DeviceIdentity
from .device_network_port import DeviceNetworkPort
from .device_pkg_install_request import DevicePkgInstallRequest
from .device_pkg_install_result import DevicePkgInstallResult
from .device_pkg_install_results import DevicePkgInstallResults
from .device_pkg_install_results_devices import DevicePkgInstallResultsDevices
from .device_pkg_uninstall_result import DevicePkgUninstallResult
from .device_pkg_uninstall_results import DevicePkgUninstallResults
from .device_pkg_uninstall_results_devices import DevicePkgUninstallResultsDevices
from .device_public_key_option import DevicePublicKeyOption
from .device_service_basic import DeviceServiceBasic
from .device_tag_option import DeviceTagOption
from .device_vpn import DeviceVpn
from .dhcp_6_advanced_options import Dhcp6AdvancedOptions
from .dhcp_address_pool import DhcpAddressPool
from .dhcp_address_pools import DhcpAddressPools
from .dhcp_advanced_options import DhcpAdvancedOptions
from .dhcp_global_settings import DhcpGlobalSettings
from .dhcp_global_settings_ipv_6_duid_type import DhcpGlobalSettingsIpv6DuidType
from .dhcp_high_availability_advance_config import DhcpHighAvailabilityAdvanceConfig
from .dhcp_high_availability_config import DhcpHighAvailabilityConfig
from .dhcp_interface_config import DhcpInterfaceConfig
from .dhcp_interfaces import DhcpInterfaces
from .dhcp_lease import DHCPLease
from .dhcp_lease_ip import DhcpLeaseIp
from .dhcp_leases import DHCPLeases
from .dhcp_network_booting import DhcpNetworkBooting
from .dhcp_range import DhcpRange
from .dhcp_relay_config import DhcpRelayConfig
from .dhcp_relay_toggle import DhcpRelayToggle
from .dhcp_service_config import DhcpServiceConfig
from .dhcp_service_config_interfaces import DhcpServiceConfigInterfaces
from .dhcp_static_mapping import DhcpStaticMapping
from .dhcp_static_mappings import DhcpStaticMappings
from .dhcpd import Dhcpd
from .dhcpd_config import DhcpdConfig
from .dhcpd_lan import DhcpdLan
from .dhcpv_6_static_mapping import Dhcpv6StaticMapping
from .diag_activity import DiagActivity
from .diag_arp_table import DiagArpTable
from .diag_auth_server_list import DiagAuthServerList
from .diag_auth_test_request import DiagAuthTestRequest
from .diag_auth_test_result import DiagAuthTestResult
from .diag_backup_diff import DiagBackupDiff
from .diag_backup_info import DiagBackupInfo
from .diag_backup_request import DiagBackupRequest
from .diag_command_result import DiagCommandResult
from .diag_dns_lookup_result import DiagDnsLookupResult
from .diag_dns_record import DiagDnsRecord
from .diag_dns_server_timing import DiagDnsServerTiming
from .diag_limiters import DiagLimiters
from .diag_php_command import DiagPhpCommand
from .diag_ping_request import DiagPingRequest
from .diag_ping_response import DiagPingResponse
from .diag_prior_backup_info import DiagPriorBackupInfo
from .diag_restore_backup_body import DiagRestoreBackupBody
from .diag_restore_prior_backup_requst import DiagRestorePriorBackupRequst
from .diag_routes import DiagRoutes
from .diag_shell_command import DiagShellCommand
from .diag_socket_stats import DiagSocketStats
from .diag_state import DiagState
from .diag_states import DiagStates
from .diag_table import DiagTable
from .diag_table_action import DiagTableAction
from .diag_table_detailed import DiagTableDetailed
from .diag_tables import DiagTables
from .diag_upload_request import DiagUploadRequest
from .diag_upload_result import DiagUploadResult
from .dimm import Dimm
from .dirty_subsystem import DirtySubsystem
from .dirty_subsystems import DirtySubsystems
from .dirty_subsystems_all_subsystems import DirtySubsystemsAllSubsystems
from .dirty_subsystems_dirty_subsystems import DirtySubsystemsDirtySubsystems
from .disks import Disks
from .dns_alias_request import DnsAliasRequest
from .dns_forwarder_alias import DNSForwarderAlias
from .dns_forwarder_config import DNSForwarderConfig
from .dns_forwarder_config_info import DNSForwarderConfigInfo
from .dns_forwarder_config_info_interfaces import DNSForwarderConfigInfoInterfaces
from .dns_forwarder_domain import DNSForwarderDomain
from .dns_forwarder_host import DNSForwarderHost
from .dns_forwarder_update_req import DNSForwarderUpdateReq
from .dns_resolver_config import DNSResolverConfig
from .dns_resolver_config_info import DNSResolverConfigInfo
from .dns_resolver_config_info_interfaces import DNSResolverConfigInfoInterfaces
from .dns_resolver_domain import DNSResolverDomain
from .dns_resolver_status import DNSResolverStatus
from .dns_resolver_status_speed import DNSResolverStatusSpeed
from .dns_resolver_status_stats import DNSResolverStatusStats
from .dns_resolver_update_req import DNSResolverUpdateReq
from .dnsacl import DNSACL
from .dnsacl_network import DNSACLNetwork
from .dyn_dns_config import DynDNSConfig
from .dyn_dns_list import DynDnsList
from .edit_file_data import EditFileData
from .edit_file_req import EditFileReq
from .encryption_algorithm import EncryptionAlgorithm
from .error import Error
from .event import Event
from .events import Events
from .filter_log import FilterLog
from .filter_log_carp_info import FilterLogCARPInfo
from .filter_log_icmp_info import FilterLogICMPInfo
from .filter_log_summary import FilterLogSummary
from .filter_log_summary_actions import FilterLogSummaryActions
from .filter_log_summary_dest_ips import FilterLogSummaryDestIps
from .filter_log_summary_dest_ports import FilterLogSummaryDestPorts
from .filter_log_summary_interfaces import FilterLogSummaryInterfaces
from .filter_log_summary_protocols import FilterLogSummaryProtocols
from .filter_log_summary_src_ips import FilterLogSummarySrcIps
from .filter_log_summary_src_ports import FilterLogSummarySrcPorts
from .filter_log_summary_tracker_hits import FilterLogSummaryTrackerHits
from .filter_log_tcp_info import FilterLogTCPInfo
from .filter_log_version_4_info import FilterLogVersion4Info
from .filter_log_version_6_info import FilterLogVersion6Info
from .filter_reload_status import FilterReloadStatus
from .filter_separator import FilterSeparator
from .firewall_event import FirewallEvent
from .fw_addr_alias import FWAddrAlias
from .fw_addr_port import FWAddrPort
from .fw_alias import FWAlias
from .fw_alias_req import FWAliasReq
from .fw_alias_type import FWAliasType
from .fw_aliases import FWAliases
from .fw_bogon_rule import FWBogonRule
from .fw_bogon_state import FWBogonState
from .fw_bulk_copy import FwBulkCopy
from .fw_bulk_delete import FwBulkDelete
from .fw_bulk_toggle import FwBulkToggle
from .fw_filter_rule import FWFilterRule
from .fw_filter_rule_nat import FWFilterRuleNAT
from .fw_firewall_interfaces import FWFirewallInterfaces
from .fw_rule_item_order import FWRuleItemOrder
from .fw_rule_list import FWRuleList
from .fw_rule_state import FWRuleState
from .fw_rule_states import FWRuleStates
from .fw_rule_toggle import FwRuleToggle
from .fw_rules import FWRules
from .fw_rules_aliases import FWRulesAliases
from .fw_rules_entry import FwRulesEntry
from .fw_rules_order import FWRulesOrder
from .fw_schedule import FWSchedule
from .fw_schedule_range import FWScheduleRange
from .fw_schedules import FWSchedules
from .fw_single_filter_rule import FWSingleFilterRule
from .fw_single_rule_states import FWSingleRuleStates
from .fw_system_alias import FWSystemAlias
from .fw_target import FWTarget
from .fw_toggle_result import FWToggleResult
from .fw_update_aliasreq import FWUpdateAliasreq
from .fw_user_timestamp import FWUserTimestamp
from .gateway import Gateway
from .gateway_defaults import GatewayDefaults
from .gateway_group import GatewayGroup
from .gateway_group_priority import GatewayGroupPriority
from .gateway_groups import GatewayGroups
from .gateway_p_info import GatewayPInfo
from .gateway_priorities import GatewayPriorities
from .gateway_priority import GatewayPriority
from .gateway_status import GatewayStatus
from .gateway_v_address import GatewayVAddress
from .gateways import Gateways
from .gateways_status import GatewaysStatus
from .gif_capable_interface import GIFCapableInterface
from .gif_interface import GIFInterface
from .gif_interfaces import GIFInterfaces
from .gre_capable_interface import GRECapableInterface
from .gre_interface import GREInterface
from .gre_interfaces import GREInterfaces
from .group_add_req import GroupAddReq
from .group_status import GroupStatus
from .group_update_req import GroupUpdateReq
from .ha_pfsync import HAPfsync
from .ha_sync_opts import HASyncOpts
from .haxmlrpc_sync import HAXMLRPCSync
from .hw_device import HWDevice
from .hw_devices import HWDevices
from .if_stats import IfStats
from .if_stats_bandwidth import IfStatsBandwidth
from .if_stats_summary import IfStatsSummary
from .igmp_proxies import IGMPProxies
from .igmp_proxy import IGMPProxy
from .igmp_proxy_settings import IGMPProxySettings
from .import_pkcs_12_certificate_body import ImportPkcs12CertificateBody
from .initial_setup import InitialSetup
from .insert_filter_rule import InsertFilterRule
from .insert_filter_separator import InsertFilterSeparator
from .install_package_opt import InstallPackageOpt
from .install_packages_opt import InstallPackagesOpt
from .install_packages_response import InstallPackagesResponse
from .install_software_package_info import InstallSoftwarePackageInfo
from .interface import Interface
from .interface_assigned_name import InterfaceAssignedName
from .interface_assignments import InterfaceAssignments
from .interface_descriptors import InterfaceDescriptors
from .interface_descriptors_info import InterfaceDescriptorsInfo
from .interface_descriptors_info_bridges import InterfaceDescriptorsInfoBridges
from .interface_descriptors_info_gif import InterfaceDescriptorsInfoGif
from .interface_descriptors_info_gre import InterfaceDescriptorsInfoGre
from .interface_descriptors_info_lagg import InterfaceDescriptorsInfoLagg
from .interface_descriptors_info_physical import InterfaceDescriptorsInfoPhysical
from .interface_descriptors_info_ppp import InterfaceDescriptorsInfoPpp
from .interface_descriptors_info_qinq import InterfaceDescriptorsInfoQinq
from .interface_descriptors_info_vlan import InterfaceDescriptorsInfoVlan
from .interface_event import InterfaceEvent
from .interface_gateway_update import InterfaceGatewayUpdate
from .interface_group import InterfaceGroup
from .interface_groups import InterfaceGroups
from .interface_info import InterfaceInfo
from .interface_info_list import InterfaceInfoList
from .interface_label_to_name import InterfaceLabelToName
from .interface_ports import InterfacePorts
from .interface_ports_lists import InterfacePortsLists
from .interface_simple import InterfaceSimple
from .interface_statistics_widget import InterfaceStatisticsWidget
from .interface_statistics_widget_result import InterfaceStatisticsWidgetResult
from .interface_statistics_widget_result_interfaces import InterfaceStatisticsWidgetResultInterfaces
from .interface_widgets import InterfaceWidgets
from .interfaces import Interfaces
from .interfaces_simple import InterfacesSimple
from .interfaces_widget import InterfacesWidget
from .intf_router_adv_setting import IntfRouterAdvSetting
from .intf_router_adv_setting_mode import IntfRouterAdvSettingMode
from .ip_sec_bypass_rule import IPSecBypassRule
from .ip_sec_bypass_rules import IPSecBypassRules
from .ip_sec_capable_interface import IPSecCapableInterface
from .ip_sec_child_sas import IPSecChildSAS
from .ip_sec_client import IPSecClient
from .ip_sec_client_config import IPSecClientConfig
from .ip_sec_client_group import IPSecClientGroup
from .ip_sec_client_groups import IPSecClientGroups
from .ip_sec_config import IPSecConfig
from .ip_sec_connect_req import IPSecConnectReq
from .ip_sec_disconnect_req import IPSecDisconnectReq
from .ip_sec_disconnect_req_phase import IPSecDisconnectReqPhase
from .ip_sec_ikesa import IPSecIKESA
from .ip_sec_logging import IPSecLogging
from .ip_sec_mobile_key import IPSecMobileKey
from .ip_sec_mobile_keys import IPSecMobileKeys
from .ip_sec_phase_list import IPSecPhaseList
from .ip_sec_pool import IPSecPool
from .ip_sec_pool_lease import IPSecPoolLease
from .ip_sec_psk import IPSecPSK
from .ip_sec_sad import IPSecSAD
from .ip_sec_spd import IPSecSPD
from .ip_sec_status import IPSecStatus
from .ip_sec_status_overview import IPSecStatusOverview
from .ip_sec_widget import IPSecWidget
from .ip_sec_widget_mobile import IPSecWidgetMobile
from .ip_sec_widget_tunnel import IPSecWidgetTunnel
from .l2tp_config import L2TPConfig
from .l2tp_radius import L2TPRadius
from .l2tp_settings import L2TPSettings
from .l2tp_user import L2TPUser
from .lagg_capable_interface import LAGGCapableInterface
from .lagg_capable_interfaces import LAGGCapableInterfaces
from .lagg_interface import LAGGInterface
from .lagg_interface_lacptimeout import LAGGInterfaceLacptimeout
from .lagg_interface_proto import LAGGInterfaceProto
from .lagg_interfaces import LAGGInterfaces
from .ldap_auth_server import LdapAuthServer
from .lease_interface import LeaseInterface
from .limiter import Limiter
from .limiter_aqm import LimiterAqm
from .limiter_bandwidth import LimiterBandwidth
from .limiter_info import LimiterInfo
from .limiter_mask import LimiterMask
from .limiter_queue import LimiterQueue
from .limiter_queue_aqm import LimiterQueueAqm
from .limiter_queue_mask import LimiterQueueMask
from .limiter_sched import LimiterSched
from .limiters import Limiters
from .load_avg import LoadAvg
from .local_server import LocalServer
from .log_entries import LogEntries
from .log_entry import LogEntry
from .log_stats import LogStats
from .login_credentials import LoginCredentials
from .login_response import LoginResponse
from .memory import Memory
from .memory_map import MemoryMap
from .memory_stat import MemoryStat
from .mesh_stats import MeshStats
from .mesh_vpn_conns import MeshVpnConns
from .monitoring_data_request import MonitoringDataRequest
from .monitoring_data_result import MonitoringDataResult
from .monitoring_dataset_info import MonitoringDatasetInfo
from .monitoring_datasets import MonitoringDatasets
from .name_descr import NameDescr
from .nat1_to_1_rule import NAT1To1Rule
from .nat1_to_1_rules import NAT1To1Rules
from .nat1_to_1_update_result import NAT1To1UpdateResult
from .nat_addr_port import NATAddrPort
from .nat_auto_addr import NATAutoAddr
from .nat_auto_rule import NATAutoRule
from .nat_npt_addr import NATNptAddr
from .nat_npt_rule import NATNptRule
from .nat_npt_rules import NATNptRules
from .nat_npt_update_result import NATNptUpdateResult
from .nat_out_mode_update_response import NATOutModeUpdateResponse
from .nat_out_update_response import NATOutUpdateResponse
from .nat_outbound_mode import NATOutboundMode
from .nat_outbound_rule import NATOutboundRule
from .nat_outbound_rules import NATOutboundRules
from .nat_rule import NATRule
from .nat_rule_order import NATRuleOrder
from .nat_rules import NATRules
from .nat_rules_entry import NATRulesEntry
from .nat_update_result import NATUpdateResult
from .ndp_entry import NDPEntry
from .ndp_table import NDPTable
from .net_if import NetIf
from .net_if_addr import NetIfAddr
from .net_if_assign_owner_req import NetIfAssignOwnerReq
from .net_if_assign_owner_req_owner_type import NetIfAssignOwnerReqOwnerType
from .net_if_dev_config import NetIfDevConfig
from .net_if_dhcp import NetIfDhcp
from .net_if_info import NetIfInfo
from .net_if_ipv_6rd import NetIfIpv6RD
from .net_if_options import NetIfOptions
from .net_if_owner import NetIfOwner
from .net_if_owner_container import NetIfOwnerContainer
from .net_if_owner_host import NetIfOwnerHost
from .net_if_owner_vm import NetIfOwnerVM
from .net_if_owner_vpp import NetIfOwnerVPP
from .net_ifs import NetIfs
from .new_ca_cert_req import NewCaCertReq
from .new_cert_req import NewCertReq
from .new_crl_req import NewCRLReq
from .new_interface_result import NewInterfaceResult
from .nexus_controller_info import NexusControllerInfo
from .ntp_access_restrictions import NtpAccessRestrictions
from .ntp_acls import NtpAcls
from .ntp_gps_flags import NtpGpsFlags
from .ntp_network_access_restriction import NtpNetworkAccessRestriction
from .ntp_pps import NtpPps
from .ntp_pps_flags import NtpPpsFlags
from .ntp_serial_gps import NtpSerialGps
from .ntp_server import NtpServer
from .ntp_server_info import NtpServerInfo
from .ntp_settings import NtpSettings
from .ntp_status import NtpStatus
from .open_vpn_active_conn import OpenVPNActiveConn
from .open_vpn_capable_interface import OpenVPNCapableInterface
from .open_vpn_client import OpenVPNClient
from .open_vpn_client_config import OpenVPNClientConfig
from .open_vpn_clients import OpenVPNClients
from .open_vpn_conn import OpenVPNConn
from .open_vpn_next_port import OpenVPNNextPort
from .open_vpn_route import OpenVPNRoute
from .open_vpn_server import OpenVPNServer
from .open_vpn_server_config import OpenVPNServerConfig
from .open_vpn_servers import OpenVPNServers
from .open_vpn_status import OpenVPNStatus
from .open_vpncs_os import OpenVPNCSOs
from .open_vpncso import OpenVPNCSO
from .open_vpncso_config import OpenVPNCSOConfig
from .os_socket import OsSocket
from .os_socket_list import OsSocketList
from .os_software_packages import OSSoftwarePackages
from .p_flow_exporter import PFlowExporter
from .p_flow_global_options import PFlowGlobalOptions
from .p_flow_global_options_src_ip_address import PFlowGlobalOptionsSrcIpAddress
from .p_flow_options import PFlowOptions
from .package import Package
from .package_install_progress import PackageInstallProgress
from .package_status import PackageStatus
from .packages import Packages
from .packet_capture import PacketCapture
from .packet_capture_filter import PacketCaptureFilter
from .packet_capture_request import PacketCaptureRequest
from .patch_system_certificates_refid_body import PatchSystemCertificatesRefidBody
from .pcap_interface import PcapInterface
from .pf_info import PfInfo
from .pf_info_response import PfInfoResponse
from .pfsense_result import PfsenseResult
from .pftop_response import PftopResponse
from .phase_1 import Phase1
from .phase_1_alg import Phase1Alg
from .phase_1_encryption import Phase1Encryption
from .phase_2 import Phase2
from .phase_2_local_id import Phase2LocalId
from .phase_2_remote_id import Phase2RemoteId
from .physical_interface import PhysicalInterface
from .pp_po_e_config import PPPoEConfig
from .pp_po_e_config_req import PPPoEConfigReq
from .pp_po_e_server import PPPoEServer
from .ppp_capable_interface import PPPCapableInterface
from .ppp_capable_interfaces import PPPCapableInterfaces
from .ppp_interface import PPPInterface
from .ppp_interface_pppoe_pr_preset_val import PPPInterfacePppoePrPresetVal
from .ppp_interface_pppoe_reset_type import PPPInterfacePppoeResetType
from .ppp_interface_type import PPPInterfaceType
from .ppp_interfaces import PPPInterfaces
from .ppp_link_interface import PPPLinkInterface
from .provider_country import ProviderCountry
from .provider_country_setting import ProviderCountrySetting
from .provider_plan_setting import ProviderPlanSetting
from .qin_q_interface import QinQInterface
from .qin_q_interfaces import QinQInterfaces
from .query_interface_rules import QueryInterfaceRules
from .queue_stats import QueueStats
from .quick_result import QuickResult
from .radius import Radius
from .radius_auth_server import RadiusAuthServer
from .radius_server import RadiusServer
from .refresh_token_param import RefreshTokenParam
from .renew_cert_options import RenewCertOptions
from .result import Result
from .retrieved_backup import RetrievedBackup
from .rfc_item import RFCItem
from .rfc_item_list import RFCItemList
from .route_record import RouteRecord
from .router_adv_settings import RouterAdvSettings
from .routes_apply_request import RoutesApplyRequest
from .routes_dirty_state import RoutesDirtyState
from .separator import Separator
from .service_certificate import ServiceCertificate
from .service_provider import ServiceProvider
from .service_provider_setting import ServiceProviderSetting
from .service_providers import ServiceProviders
from .services_action_params import ServicesActionParams
from .services_action_req import ServicesActionReq
from .services_ntp_config import ServicesNtpConfig
from .services_snmp_config import ServicesSNMPConfig
from .services_snmp_config_req import ServicesSNMPConfigReq
from .services_status import ServicesStatus
from .services_status_list import ServicesStatusList
from .services_u_pn_p_config import ServicesUPnPConfig
from .services_u_pn_p_config_req import ServicesUPnPConfigReq
from .set_adv_networking_response import SetAdvNetworkingResponse
from .set_open_vpn_client_response import SetOpenVPNClientResponse
from .set_open_vpn_server_response import SetOpenVPNServerResponse
from .set_open_vpncso_response import SetOpenVPNCSOResponse
from .setup_dns_setting import SetupDNSSetting
from .setup_pp_po_e_cfg import SetupPPPoECfg
from .setup_settings import SetupSettings
from .setup_wizard import SetupWizard
from .setup_wizard_options import SetupWizardOptions
from .simple_interface import SimpleInterface
from .smart_devices import SMARTDevices
from .smart_result import SMARTResult
from .snmp_config import SNMPConfig
from .snmp_interface import SNMPInterface
from .snmp_modules import SNMPModules
from .software_package import SoftwarePackage
from .software_package_list import SoftwarePackageList
from .static_route import StaticRoute
from .static_routes import StaticRoutes
from .status_summary import StatusSummary
from .status_summary_ui_features import StatusSummaryUiFeatures
from .std_log import StdLog
from .std_logs import StdLogs
from .storage_stats import StorageStats
from .sys_firmware_info import SysFirmwareInfo
from .sys_firmware_upgrade_opt import SysFirmwareUpgradeOpt
from .sys_net_if import SysNetIf
from .sysinfo import Sysinfo
from .sysinfo_fs import SysinfoFs
from .sysinfo_update import SysinfoUpdate
from .syslog_config_override import SyslogConfigOverride
from .syslog_configuration import SyslogConfiguration
from .system_adv_admin import SystemAdvAdmin
from .system_adv_admin_setting import SystemAdvAdminSetting
from .system_cert import SystemCert
from .system_control import SystemControl
from .system_event import SystemEvent
from .system_git_sync_settings import SystemGitSyncSettings
from .system_status import SystemStatus
from .system_summary import SystemSummary
from .system_update_boot_envs_settings import SystemUpdateBootEnvsSettings
from .system_update_firmware_branch import SystemUpdateFirmwareBranch
from .system_update_info import SystemUpdateInfo
from .system_update_options import SystemUpdateOptions
from .system_update_progress import SystemUpdateProgress
from .system_update_settings import SystemUpdateSettings
from .system_update_settings_set import SystemUpdateSettingsSet
from .tcp_flags import TCPFlags
from .test_port_request import TestPortRequest
from .test_port_response import TestPortResponse
from .test_port_sources import TestPortSources
from .text_value import TextValue
from .tier import Tier
from .tls_cert_path import TLSCertPath
from .toggle_resp_status import ToggleRespStatus
from .toggle_upnp import ToggleUPNP
from .traceroute_request import TracerouteRequest
from .traceroute_response import TracerouteResponse
from .traffic_queue_stats import TrafficQueueStats
from .traffic_shapers import TrafficShapers
from .tunable import Tunable
from .tunable_request import TunableRequest
from .tunables import Tunables
from .u_pn_p_config import UPnPConfig
from .u_pn_p_mapping import UPnPMapping
from .u_pn_p_mappings import UPnPMappings
from .u_pn_p_perm_user import UPnPPermUser
from .ui_states import UIStates
from .update_bootenv import UpdateBootenv
from .update_ca_cert_req import UpdateCaCertReq
from .update_cert_req import UpdateCertReq
from .update_crl_req import UpdateCRLReq
from .update_pkcs12_cert_req import UpdatePKCS12CertReq
from .user import User
from .user_add_req import UserAddReq
from .user_auth_settings import UserAuthSettings
from .user_auth_settings_req import UserAuthSettingsReq
from .user_generic import UserGeneric
from .user_group import UserGroup
from .user_groups import UserGroups
from .user_privilege import UserPrivilege
from .user_privileges import UserPrivileges
from .user_update_req import UserUpdateReq
from .users import Users
from .users_config import UsersConfig
from .users_config_generic import UsersConfigGeneric
from .users_generic import UsersGeneric
from .virtual_i_ps import VirtualIPs
from .virtual_ip import VirtualIP
from .virtual_ip_result import VirtualIPResult
from .vlan_capable_interface import VLANCapableInterface
from .vlan_interface import VLANInterface
from .vlan_interfaces import VLANInterfaces
from .voucher import Voucher
from .voucher_roll import VoucherRoll
from .wg_config import WGConfig
from .wg_peer import WGPeer
from .wg_peers import WGPeers
from .wg_tunnel import WGTunnel
from .wg_tunnel_conf import WGTunnelConf
from .wg_tunnels import WGTunnels
from .wgip_address import WGIPAddress
from .wgip_addresses import WGIPAddresses
from .wire_guard_keys import WireGuardKeys
from .wire_guard_peer_status import WireGuardPeerStatus
from .wire_guard_settings import WireGuardSettings
from .wire_guard_status import WireGuardStatus
from .wire_guard_tunnel_status import WireGuardTunnelStatus
from .wireless_addl import WirelessAddl
from .wireless_addl_clone import WirelessAddlClone
from .wireless_interface import WirelessInterface
from .wireless_interfaces import WirelessInterfaces
from .wme_setting import WMESetting
from .wpa_setting import WPASetting

__all__ = (
    "ACBBackup",
    "ACBConfig",
    "ACBConfigInfo",
    "ACBList",
    "ACBManualBackupRequest",
    "ACBRestoreRequest",
    "ActivateBootenv",
    "AdvFirewall",
    "AdvFirewallSetting",
    "AdvMisc",
    "AdvMiscSetting",
    "AdvNetworking",
    "AdvNetworkSetting",
    "AdvNotifications",
    "AdvNotificationSetting",
    "AllSoftwarePackages",
    "AllSoftwarePackagesSoftwarePackages",
    "ALTQCapableInterface",
    "ALTQChildQueue",
    "ALTQRootQueue",
    "ALTQRootQueueBandwidthtype",
    "ALTQRootQueues",
    "ALTQRootQueueScheduler",
    "ApplyDirtyConfigRequest",
    "ArpTableEntry",
    "AuthServer",
    "AuthServers",
    "AuthServersList",
    "AuthTestCredentials",
    "AuthTestResult",
    "Bootenv",
    "BootEnvs",
    "BootEnvsEnvs",
    "BridgeCapableInterface",
    "BridgeInterface",
    "BridgeInterfaceIfpathcost",
    "BridgeInterfaceIfpriority",
    "BridgeInterfaces",
    "CaCertMethodExisting",
    "CaCertMethodNew",
    "CaptiveAllowedHost",
    "CaptiveAllowedIP",
    "CaptiveElement",
    "CaptivePassthruMac",
    "CaptivePortalConfig",
    "CaptivePortalDisconnectRequest",
    "CaptivePortalInfo",
    "CaptivePortalName",
    "CaptivePortals",
    "CaptivePortalStatus",
    "CaptivePortalUserInfo",
    "CARPResetDemotionResult",
    "CARPStatus",
    "CARPVIPStatus",
    "CertAltName",
    "CertAuthorities",
    "CertAuthority",
    "CertConfig",
    "CertificateDetailed",
    "CertInfo",
    "CertKeyExportOpts",
    "CertMethodExistingPEM",
    "CertMethodExistingPkcs12",
    "CertMethodNew",
    "CertMethodSignCSR",
    "CertMethodSigningRequest",
    "CertOpts",
    "CertPkcs12ExportOpts",
    "CertPkcs12ExportOptsEncryption",
    "CertsConfig",
    "CheckIPService",
    "CheckIPServicesList",
    "ConfigEvent",
    "ConsoleClient",
    "ConsoleClients",
    "ControlledDevice",
    "ControlledDeviceAuth",
    "ControlledDeviceCert",
    "ControlledDeviceCertOptions",
    "ControlledDeviceCerts",
    "ControlledDeviceDetailed",
    "ControlledDeviceInfo",
    "ControlledDevices",
    "ControllerAlarm",
    "ControllerAlarms",
    "ControllerAlarmsAlarms",
    "ControllerBackup",
    "ControllerBackupRequest",
    "ControllerBackupRestoreRequest",
    "ControllerBackupRestoreResult",
    "ControllerBackupResult",
    "ControllerBackups",
    "ControllerDescrip",
    "ControllerDescripHostOs",
    "ControllerIdentity",
    "ControllerInfo",
    "ControllerServiceAction",
    "ControllerServiceActionAction",
    "ControllersList",
    "ControllerStats",
    "ControllerSummary",
    "ControllerUpgradeInfo",
    "ControllerUpgradeRequest",
    "ControllerUpgradeResult",
    "CreateBootenv",
    "CreateControlledDeviceCert",
    "CreateUPnPACL",
    "CRLCert",
    "CRLConfig",
    "CRLConfigPkgs",
    "CRLEntries",
    "CRLMethodInternalUpdate",
    "CRLMethodInternalUpdateRevokeReason",
    "CRLMethodNew",
    "CRLMethodX509",
    "CRLPackageInfo",
    "DeleteBootenvs",
    "DeleteControlledDeviceCertRequest",
    "DeleteFirewallRule",
    "DeviceBasicInfo",
    "DeviceControllerInfo",
    "DeviceIdentity",
    "DeviceNetworkPort",
    "DevicePkgInstallRequest",
    "DevicePkgInstallResult",
    "DevicePkgInstallResults",
    "DevicePkgInstallResultsDevices",
    "DevicePkgUninstallResult",
    "DevicePkgUninstallResults",
    "DevicePkgUninstallResultsDevices",
    "DevicePublicKeyOption",
    "DeviceServiceBasic",
    "DeviceTagOption",
    "DeviceVpn",
    "Dhcp6AdvancedOptions",
    "DhcpAddressPool",
    "DhcpAddressPools",
    "DhcpAdvancedOptions",
    "Dhcpd",
    "DhcpdConfig",
    "DhcpdLan",
    "DhcpGlobalSettings",
    "DhcpGlobalSettingsIpv6DuidType",
    "DhcpHighAvailabilityAdvanceConfig",
    "DhcpHighAvailabilityConfig",
    "DhcpInterfaceConfig",
    "DhcpInterfaces",
    "DHCPLease",
    "DhcpLeaseIp",
    "DHCPLeases",
    "DhcpNetworkBooting",
    "DhcpRange",
    "DhcpRelayConfig",
    "DhcpRelayToggle",
    "DhcpServiceConfig",
    "DhcpServiceConfigInterfaces",
    "DhcpStaticMapping",
    "DhcpStaticMappings",
    "Dhcpv6StaticMapping",
    "DiagActivity",
    "DiagArpTable",
    "DiagAuthServerList",
    "DiagAuthTestRequest",
    "DiagAuthTestResult",
    "DiagBackupDiff",
    "DiagBackupInfo",
    "DiagBackupRequest",
    "DiagCommandResult",
    "DiagDnsLookupResult",
    "DiagDnsRecord",
    "DiagDnsServerTiming",
    "DiagLimiters",
    "DiagPhpCommand",
    "DiagPingRequest",
    "DiagPingResponse",
    "DiagPriorBackupInfo",
    "DiagRestoreBackupBody",
    "DiagRestorePriorBackupRequst",
    "DiagRoutes",
    "DiagShellCommand",
    "DiagSocketStats",
    "DiagState",
    "DiagStates",
    "DiagTable",
    "DiagTableAction",
    "DiagTableDetailed",
    "DiagTables",
    "DiagUploadRequest",
    "DiagUploadResult",
    "Dimm",
    "DirtySubsystem",
    "DirtySubsystems",
    "DirtySubsystemsAllSubsystems",
    "DirtySubsystemsDirtySubsystems",
    "Disks",
    "DNSACL",
    "DNSACLNetwork",
    "DnsAliasRequest",
    "DNSForwarderAlias",
    "DNSForwarderConfig",
    "DNSForwarderConfigInfo",
    "DNSForwarderConfigInfoInterfaces",
    "DNSForwarderDomain",
    "DNSForwarderHost",
    "DNSForwarderUpdateReq",
    "DNSResolverConfig",
    "DNSResolverConfigInfo",
    "DNSResolverConfigInfoInterfaces",
    "DNSResolverDomain",
    "DNSResolverStatus",
    "DNSResolverStatusSpeed",
    "DNSResolverStatusStats",
    "DNSResolverUpdateReq",
    "DynDNSConfig",
    "DynDnsList",
    "EditFileData",
    "EditFileReq",
    "EncryptionAlgorithm",
    "Error",
    "Event",
    "Events",
    "FilterLog",
    "FilterLogCARPInfo",
    "FilterLogICMPInfo",
    "FilterLogSummary",
    "FilterLogSummaryActions",
    "FilterLogSummaryDestIps",
    "FilterLogSummaryDestPorts",
    "FilterLogSummaryInterfaces",
    "FilterLogSummaryProtocols",
    "FilterLogSummarySrcIps",
    "FilterLogSummarySrcPorts",
    "FilterLogSummaryTrackerHits",
    "FilterLogTCPInfo",
    "FilterLogVersion4Info",
    "FilterLogVersion6Info",
    "FilterReloadStatus",
    "FilterSeparator",
    "FirewallEvent",
    "FWAddrAlias",
    "FWAddrPort",
    "FWAlias",
    "FWAliases",
    "FWAliasReq",
    "FWAliasType",
    "FWBogonRule",
    "FWBogonState",
    "FwBulkCopy",
    "FwBulkDelete",
    "FwBulkToggle",
    "FWFilterRule",
    "FWFilterRuleNAT",
    "FWFirewallInterfaces",
    "FWRuleItemOrder",
    "FWRuleList",
    "FWRules",
    "FWRulesAliases",
    "FwRulesEntry",
    "FWRulesOrder",
    "FWRuleState",
    "FWRuleStates",
    "FwRuleToggle",
    "FWSchedule",
    "FWScheduleRange",
    "FWSchedules",
    "FWSingleFilterRule",
    "FWSingleRuleStates",
    "FWSystemAlias",
    "FWTarget",
    "FWToggleResult",
    "FWUpdateAliasreq",
    "FWUserTimestamp",
    "Gateway",
    "GatewayDefaults",
    "GatewayGroup",
    "GatewayGroupPriority",
    "GatewayGroups",
    "GatewayPInfo",
    "GatewayPriorities",
    "GatewayPriority",
    "Gateways",
    "GatewaysStatus",
    "GatewayStatus",
    "GatewayVAddress",
    "GIFCapableInterface",
    "GIFInterface",
    "GIFInterfaces",
    "GRECapableInterface",
    "GREInterface",
    "GREInterfaces",
    "GroupAddReq",
    "GroupStatus",
    "GroupUpdateReq",
    "HAPfsync",
    "HASyncOpts",
    "HAXMLRPCSync",
    "HWDevice",
    "HWDevices",
    "IfStats",
    "IfStatsBandwidth",
    "IfStatsSummary",
    "IGMPProxies",
    "IGMPProxy",
    "IGMPProxySettings",
    "ImportPkcs12CertificateBody",
    "InitialSetup",
    "InsertFilterRule",
    "InsertFilterSeparator",
    "InstallPackageOpt",
    "InstallPackagesOpt",
    "InstallPackagesResponse",
    "InstallSoftwarePackageInfo",
    "Interface",
    "InterfaceAssignedName",
    "InterfaceAssignments",
    "InterfaceDescriptors",
    "InterfaceDescriptorsInfo",
    "InterfaceDescriptorsInfoBridges",
    "InterfaceDescriptorsInfoGif",
    "InterfaceDescriptorsInfoGre",
    "InterfaceDescriptorsInfoLagg",
    "InterfaceDescriptorsInfoPhysical",
    "InterfaceDescriptorsInfoPpp",
    "InterfaceDescriptorsInfoQinq",
    "InterfaceDescriptorsInfoVlan",
    "InterfaceEvent",
    "InterfaceGatewayUpdate",
    "InterfaceGroup",
    "InterfaceGroups",
    "InterfaceInfo",
    "InterfaceInfoList",
    "InterfaceLabelToName",
    "InterfacePorts",
    "InterfacePortsLists",
    "Interfaces",
    "InterfaceSimple",
    "InterfacesSimple",
    "InterfaceStatisticsWidget",
    "InterfaceStatisticsWidgetResult",
    "InterfaceStatisticsWidgetResultInterfaces",
    "InterfacesWidget",
    "InterfaceWidgets",
    "IntfRouterAdvSetting",
    "IntfRouterAdvSettingMode",
    "IPSecBypassRule",
    "IPSecBypassRules",
    "IPSecCapableInterface",
    "IPSecChildSAS",
    "IPSecClient",
    "IPSecClientConfig",
    "IPSecClientGroup",
    "IPSecClientGroups",
    "IPSecConfig",
    "IPSecConnectReq",
    "IPSecDisconnectReq",
    "IPSecDisconnectReqPhase",
    "IPSecIKESA",
    "IPSecLogging",
    "IPSecMobileKey",
    "IPSecMobileKeys",
    "IPSecPhaseList",
    "IPSecPool",
    "IPSecPoolLease",
    "IPSecPSK",
    "IPSecSAD",
    "IPSecSPD",
    "IPSecStatus",
    "IPSecStatusOverview",
    "IPSecWidget",
    "IPSecWidgetMobile",
    "IPSecWidgetTunnel",
    "L2TPConfig",
    "L2TPRadius",
    "L2TPSettings",
    "L2TPUser",
    "LAGGCapableInterface",
    "LAGGCapableInterfaces",
    "LAGGInterface",
    "LAGGInterfaceLacptimeout",
    "LAGGInterfaceProto",
    "LAGGInterfaces",
    "LdapAuthServer",
    "LeaseInterface",
    "Limiter",
    "LimiterAqm",
    "LimiterBandwidth",
    "LimiterInfo",
    "LimiterMask",
    "LimiterQueue",
    "LimiterQueueAqm",
    "LimiterQueueMask",
    "Limiters",
    "LimiterSched",
    "LoadAvg",
    "LocalServer",
    "LogEntries",
    "LogEntry",
    "LoginCredentials",
    "LoginResponse",
    "LogStats",
    "Memory",
    "MemoryMap",
    "MemoryStat",
    "MeshStats",
    "MeshVpnConns",
    "MonitoringDataRequest",
    "MonitoringDataResult",
    "MonitoringDatasetInfo",
    "MonitoringDatasets",
    "NameDescr",
    "NAT1To1Rule",
    "NAT1To1Rules",
    "NAT1To1UpdateResult",
    "NATAddrPort",
    "NATAutoAddr",
    "NATAutoRule",
    "NATNptAddr",
    "NATNptRule",
    "NATNptRules",
    "NATNptUpdateResult",
    "NATOutboundMode",
    "NATOutboundRule",
    "NATOutboundRules",
    "NATOutModeUpdateResponse",
    "NATOutUpdateResponse",
    "NATRule",
    "NATRuleOrder",
    "NATRules",
    "NATRulesEntry",
    "NATUpdateResult",
    "NDPEntry",
    "NDPTable",
    "NetIf",
    "NetIfAddr",
    "NetIfAssignOwnerReq",
    "NetIfAssignOwnerReqOwnerType",
    "NetIfDevConfig",
    "NetIfDhcp",
    "NetIfInfo",
    "NetIfIpv6RD",
    "NetIfOptions",
    "NetIfOwner",
    "NetIfOwnerContainer",
    "NetIfOwnerHost",
    "NetIfOwnerVM",
    "NetIfOwnerVPP",
    "NetIfs",
    "NewCaCertReq",
    "NewCertReq",
    "NewCRLReq",
    "NewInterfaceResult",
    "NexusControllerInfo",
    "NtpAccessRestrictions",
    "NtpAcls",
    "NtpGpsFlags",
    "NtpNetworkAccessRestriction",
    "NtpPps",
    "NtpPpsFlags",
    "NtpSerialGps",
    "NtpServer",
    "NtpServerInfo",
    "NtpSettings",
    "NtpStatus",
    "OpenVPNActiveConn",
    "OpenVPNCapableInterface",
    "OpenVPNClient",
    "OpenVPNClientConfig",
    "OpenVPNClients",
    "OpenVPNConn",
    "OpenVPNCSO",
    "OpenVPNCSOConfig",
    "OpenVPNCSOs",
    "OpenVPNNextPort",
    "OpenVPNRoute",
    "OpenVPNServer",
    "OpenVPNServerConfig",
    "OpenVPNServers",
    "OpenVPNStatus",
    "OsSocket",
    "OsSocketList",
    "OSSoftwarePackages",
    "Package",
    "PackageInstallProgress",
    "Packages",
    "PackageStatus",
    "PacketCapture",
    "PacketCaptureFilter",
    "PacketCaptureRequest",
    "PatchSystemCertificatesRefidBody",
    "PcapInterface",
    "PfInfo",
    "PfInfoResponse",
    "PFlowExporter",
    "PFlowGlobalOptions",
    "PFlowGlobalOptionsSrcIpAddress",
    "PFlowOptions",
    "PfsenseResult",
    "PftopResponse",
    "Phase1",
    "Phase1Alg",
    "Phase1Encryption",
    "Phase2",
    "Phase2LocalId",
    "Phase2RemoteId",
    "PhysicalInterface",
    "PPPCapableInterface",
    "PPPCapableInterfaces",
    "PPPInterface",
    "PPPInterfacePppoePrPresetVal",
    "PPPInterfacePppoeResetType",
    "PPPInterfaces",
    "PPPInterfaceType",
    "PPPLinkInterface",
    "PPPoEConfig",
    "PPPoEConfigReq",
    "PPPoEServer",
    "ProviderCountry",
    "ProviderCountrySetting",
    "ProviderPlanSetting",
    "QinQInterface",
    "QinQInterfaces",
    "QueryInterfaceRules",
    "QueueStats",
    "QuickResult",
    "Radius",
    "RadiusAuthServer",
    "RadiusServer",
    "RefreshTokenParam",
    "RenewCertOptions",
    "Result",
    "RetrievedBackup",
    "RFCItem",
    "RFCItemList",
    "RouterAdvSettings",
    "RouteRecord",
    "RoutesApplyRequest",
    "RoutesDirtyState",
    "Separator",
    "ServiceCertificate",
    "ServiceProvider",
    "ServiceProviders",
    "ServiceProviderSetting",
    "ServicesActionParams",
    "ServicesActionReq",
    "ServicesNtpConfig",
    "ServicesSNMPConfig",
    "ServicesSNMPConfigReq",
    "ServicesStatus",
    "ServicesStatusList",
    "ServicesUPnPConfig",
    "ServicesUPnPConfigReq",
    "SetAdvNetworkingResponse",
    "SetOpenVPNClientResponse",
    "SetOpenVPNCSOResponse",
    "SetOpenVPNServerResponse",
    "SetupDNSSetting",
    "SetupPPPoECfg",
    "SetupSettings",
    "SetupWizard",
    "SetupWizardOptions",
    "SimpleInterface",
    "SMARTDevices",
    "SMARTResult",
    "SNMPConfig",
    "SNMPInterface",
    "SNMPModules",
    "SoftwarePackage",
    "SoftwarePackageList",
    "StaticRoute",
    "StaticRoutes",
    "StatusSummary",
    "StatusSummaryUiFeatures",
    "StdLog",
    "StdLogs",
    "StorageStats",
    "SysFirmwareInfo",
    "SysFirmwareUpgradeOpt",
    "Sysinfo",
    "SysinfoFs",
    "SysinfoUpdate",
    "SyslogConfigOverride",
    "SyslogConfiguration",
    "SysNetIf",
    "SystemAdvAdmin",
    "SystemAdvAdminSetting",
    "SystemCert",
    "SystemControl",
    "SystemEvent",
    "SystemGitSyncSettings",
    "SystemStatus",
    "SystemSummary",
    "SystemUpdateBootEnvsSettings",
    "SystemUpdateFirmwareBranch",
    "SystemUpdateInfo",
    "SystemUpdateOptions",
    "SystemUpdateProgress",
    "SystemUpdateSettings",
    "SystemUpdateSettingsSet",
    "TCPFlags",
    "TestPortRequest",
    "TestPortResponse",
    "TestPortSources",
    "TextValue",
    "Tier",
    "TLSCertPath",
    "ToggleRespStatus",
    "ToggleUPNP",
    "TracerouteRequest",
    "TracerouteResponse",
    "TrafficQueueStats",
    "TrafficShapers",
    "Tunable",
    "TunableRequest",
    "Tunables",
    "UIStates",
    "UpdateBootenv",
    "UpdateCaCertReq",
    "UpdateCertReq",
    "UpdateCRLReq",
    "UpdatePKCS12CertReq",
    "UPnPConfig",
    "UPnPMapping",
    "UPnPMappings",
    "UPnPPermUser",
    "User",
    "UserAddReq",
    "UserAuthSettings",
    "UserAuthSettingsReq",
    "UserGeneric",
    "UserGroup",
    "UserGroups",
    "UserPrivilege",
    "UserPrivileges",
    "Users",
    "UsersConfig",
    "UsersConfigGeneric",
    "UsersGeneric",
    "UserUpdateReq",
    "VirtualIP",
    "VirtualIPResult",
    "VirtualIPs",
    "VLANCapableInterface",
    "VLANInterface",
    "VLANInterfaces",
    "Voucher",
    "VoucherRoll",
    "WGConfig",
    "WGIPAddress",
    "WGIPAddresses",
    "WGPeer",
    "WGPeers",
    "WGTunnel",
    "WGTunnelConf",
    "WGTunnels",
    "WireGuardKeys",
    "WireGuardPeerStatus",
    "WireGuardSettings",
    "WireGuardStatus",
    "WireGuardTunnelStatus",
    "WirelessAddl",
    "WirelessAddlClone",
    "WirelessInterface",
    "WirelessInterfaces",
    "WMESetting",
    "WPASetting",
)
