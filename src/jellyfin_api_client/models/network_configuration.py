from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkConfiguration")


@_attrs_define
class NetworkConfiguration:
    """Defines the Jellyfin.Networking.Configuration.NetworkConfiguration.

    Attributes:
        require_https (Union[Unset, bool]): Gets or sets a value indicating whether the server should force connections
            over HTTPS.
        certificate_path (Union[Unset, str]): Gets or sets the filesystem path of an X.509 certificate to use for SSL.
        certificate_password (Union[Unset, str]): Gets or sets the password required to access the X.509 certificate
            data in the file specified by Jellyfin.Networking.Configuration.NetworkConfiguration.CertificatePath.
        base_url (Union[Unset, str]): Gets or sets a value used to specify the URL prefix that your Jellyfin instance
            can be accessed at.
        public_https_port (Union[Unset, int]): Gets or sets the public HTTPS port.
        http_server_port_number (Union[Unset, int]): Gets or sets the HTTP server port number.
        https_port_number (Union[Unset, int]): Gets or sets the HTTPS server port number.
        enable_https (Union[Unset, bool]): Gets or sets a value indicating whether to use HTTPS.
        public_port (Union[Unset, int]): Gets or sets the public mapped port.
        u_pn_p_create_http_port_map (Union[Unset, bool]): Gets or sets a value indicating whether the http port should
            be mapped as part of UPnP automatic port forwarding.
        udp_port_range (Union[Unset, str]): Gets or sets the UDPPortRange.
        enable_ipv6 (Union[Unset, bool]): Gets or sets a value indicating whether gets or sets IPV6 capability.
        enable_ipv4 (Union[Unset, bool]): Gets or sets a value indicating whether gets or sets IPV4 capability.
        enable_ssdp_tracing (Union[Unset, bool]): Gets or sets a value indicating whether detailed SSDP logs are sent to
            the console/log.
            "Emby.Dlna": "Debug" must be set in logging.default.json for this property to have any effect.
        ssdp_tracing_filter (Union[Unset, str]): Gets or sets the SSDPTracingFilter
            Gets or sets a value indicating whether an IP address is to be used to filter the detailed ssdp logs that are
            being sent to the console/log.
            If the setting "Emby.Dlna": "Debug" msut be set in logging.default.json for this property to work.
        udp_send_count (Union[Unset, int]): Gets or sets the number of times SSDP UDP messages are sent.
        udp_send_delay (Union[Unset, int]): Gets or sets the delay between each groups of SSDP messages (in ms).
        ignore_virtual_interfaces (Union[Unset, bool]): Gets or sets a value indicating whether address names that match
            Jellyfin.Networking.Configuration.NetworkConfiguration.VirtualInterfaceNames should be Ignore for the purposes
            of binding.
        virtual_interface_names (Union[Unset, str]): Gets or sets a value indicating the interfaces that should be
            ignored. The list can be comma separated. <seealso
            cref="P:Jellyfin.Networking.Configuration.NetworkConfiguration.IgnoreVirtualInterfaces" />.
        gateway_monitor_period (Union[Unset, int]): Gets or sets the time (in seconds) between the pings of SSDP gateway
            monitor.
        enable_multi_socket_binding (Union[Unset, bool]): Gets a value indicating whether multi-socket binding is
            available.
        trust_all_ip6_interfaces (Union[Unset, bool]): Gets or sets a value indicating whether all IPv6 interfaces
            should be treated as on the internal network.
            Depending on the address range implemented ULA ranges might not be used.
        hd_homerun_port_range (Union[Unset, str]): Gets or sets the ports that HDHomerun uses.
        published_server_uri_by_subnet (Union[Unset, List[str]]): Gets or sets the PublishedServerUriBySubnet
            Gets or sets PublishedServerUri to advertise for specific subnets.
        auto_discovery_tracing (Union[Unset, bool]): Gets or sets a value indicating whether Autodiscovery tracing is
            enabled.
        auto_discovery (Union[Unset, bool]): Gets or sets a value indicating whether Autodiscovery is enabled.
        remote_ip_filter (Union[Unset, List[str]]): Gets or sets the filter for remote IP connectivity. Used in
            conjuntion with <seealso
            cref="P:Jellyfin.Networking.Configuration.NetworkConfiguration.IsRemoteIPFilterBlacklist" />.
        is_remote_ip_filter_blacklist (Union[Unset, bool]): Gets or sets a value indicating whether <seealso
            cref="P:Jellyfin.Networking.Configuration.NetworkConfiguration.RemoteIPFilter" /> contains a blacklist or a
            whitelist. Default is a whitelist.
        enable_u_pn_p (Union[Unset, bool]): Gets or sets a value indicating whether to enable automatic port forwarding.
        enable_remote_access (Union[Unset, bool]): Gets or sets a value indicating whether access outside of the LAN is
            permitted.
        local_network_subnets (Union[Unset, List[str]]): Gets or sets the subnets that are deemed to make up the LAN.
        local_network_addresses (Union[Unset, List[str]]): Gets or sets the interface addresses which Jellyfin will bind
            to. If empty, all interfaces will be used.
        known_proxies (Union[Unset, List[str]]): Gets or sets the known proxies. If the proxy is a network, it's added
            to the KnownNetworks.
        enable_published_server_uri_by_request (Union[Unset, bool]): Gets or sets a value indicating whether the
            published server uri is based on information in HTTP requests.
    """

    require_https: Union[Unset, bool] = UNSET
    certificate_path: Union[Unset, str] = UNSET
    certificate_password: Union[Unset, str] = UNSET
    base_url: Union[Unset, str] = UNSET
    public_https_port: Union[Unset, int] = UNSET
    http_server_port_number: Union[Unset, int] = UNSET
    https_port_number: Union[Unset, int] = UNSET
    enable_https: Union[Unset, bool] = UNSET
    public_port: Union[Unset, int] = UNSET
    u_pn_p_create_http_port_map: Union[Unset, bool] = UNSET
    udp_port_range: Union[Unset, str] = UNSET
    enable_ipv6: Union[Unset, bool] = UNSET
    enable_ipv4: Union[Unset, bool] = UNSET
    enable_ssdp_tracing: Union[Unset, bool] = UNSET
    ssdp_tracing_filter: Union[Unset, str] = UNSET
    udp_send_count: Union[Unset, int] = UNSET
    udp_send_delay: Union[Unset, int] = UNSET
    ignore_virtual_interfaces: Union[Unset, bool] = UNSET
    virtual_interface_names: Union[Unset, str] = UNSET
    gateway_monitor_period: Union[Unset, int] = UNSET
    enable_multi_socket_binding: Union[Unset, bool] = UNSET
    trust_all_ip6_interfaces: Union[Unset, bool] = UNSET
    hd_homerun_port_range: Union[Unset, str] = UNSET
    published_server_uri_by_subnet: Union[Unset, List[str]] = UNSET
    auto_discovery_tracing: Union[Unset, bool] = UNSET
    auto_discovery: Union[Unset, bool] = UNSET
    remote_ip_filter: Union[Unset, List[str]] = UNSET
    is_remote_ip_filter_blacklist: Union[Unset, bool] = UNSET
    enable_u_pn_p: Union[Unset, bool] = UNSET
    enable_remote_access: Union[Unset, bool] = UNSET
    local_network_subnets: Union[Unset, List[str]] = UNSET
    local_network_addresses: Union[Unset, List[str]] = UNSET
    known_proxies: Union[Unset, List[str]] = UNSET
    enable_published_server_uri_by_request: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        require_https = self.require_https
        certificate_path = self.certificate_path
        certificate_password = self.certificate_password
        base_url = self.base_url
        public_https_port = self.public_https_port
        http_server_port_number = self.http_server_port_number
        https_port_number = self.https_port_number
        enable_https = self.enable_https
        public_port = self.public_port
        u_pn_p_create_http_port_map = self.u_pn_p_create_http_port_map
        udp_port_range = self.udp_port_range
        enable_ipv6 = self.enable_ipv6
        enable_ipv4 = self.enable_ipv4
        enable_ssdp_tracing = self.enable_ssdp_tracing
        ssdp_tracing_filter = self.ssdp_tracing_filter
        udp_send_count = self.udp_send_count
        udp_send_delay = self.udp_send_delay
        ignore_virtual_interfaces = self.ignore_virtual_interfaces
        virtual_interface_names = self.virtual_interface_names
        gateway_monitor_period = self.gateway_monitor_period
        enable_multi_socket_binding = self.enable_multi_socket_binding
        trust_all_ip6_interfaces = self.trust_all_ip6_interfaces
        hd_homerun_port_range = self.hd_homerun_port_range
        published_server_uri_by_subnet: Union[Unset, List[str]] = UNSET
        if not isinstance(self.published_server_uri_by_subnet, Unset):
            published_server_uri_by_subnet = self.published_server_uri_by_subnet

        auto_discovery_tracing = self.auto_discovery_tracing
        auto_discovery = self.auto_discovery
        remote_ip_filter: Union[Unset, List[str]] = UNSET
        if not isinstance(self.remote_ip_filter, Unset):
            remote_ip_filter = self.remote_ip_filter

        is_remote_ip_filter_blacklist = self.is_remote_ip_filter_blacklist
        enable_u_pn_p = self.enable_u_pn_p
        enable_remote_access = self.enable_remote_access
        local_network_subnets: Union[Unset, List[str]] = UNSET
        if not isinstance(self.local_network_subnets, Unset):
            local_network_subnets = self.local_network_subnets

        local_network_addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.local_network_addresses, Unset):
            local_network_addresses = self.local_network_addresses

        known_proxies: Union[Unset, List[str]] = UNSET
        if not isinstance(self.known_proxies, Unset):
            known_proxies = self.known_proxies

        enable_published_server_uri_by_request = self.enable_published_server_uri_by_request

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if require_https is not UNSET:
            field_dict["RequireHttps"] = require_https
        if certificate_path is not UNSET:
            field_dict["CertificatePath"] = certificate_path
        if certificate_password is not UNSET:
            field_dict["CertificatePassword"] = certificate_password
        if base_url is not UNSET:
            field_dict["BaseUrl"] = base_url
        if public_https_port is not UNSET:
            field_dict["PublicHttpsPort"] = public_https_port
        if http_server_port_number is not UNSET:
            field_dict["HttpServerPortNumber"] = http_server_port_number
        if https_port_number is not UNSET:
            field_dict["HttpsPortNumber"] = https_port_number
        if enable_https is not UNSET:
            field_dict["EnableHttps"] = enable_https
        if public_port is not UNSET:
            field_dict["PublicPort"] = public_port
        if u_pn_p_create_http_port_map is not UNSET:
            field_dict["UPnPCreateHttpPortMap"] = u_pn_p_create_http_port_map
        if udp_port_range is not UNSET:
            field_dict["UDPPortRange"] = udp_port_range
        if enable_ipv6 is not UNSET:
            field_dict["EnableIPV6"] = enable_ipv6
        if enable_ipv4 is not UNSET:
            field_dict["EnableIPV4"] = enable_ipv4
        if enable_ssdp_tracing is not UNSET:
            field_dict["EnableSSDPTracing"] = enable_ssdp_tracing
        if ssdp_tracing_filter is not UNSET:
            field_dict["SSDPTracingFilter"] = ssdp_tracing_filter
        if udp_send_count is not UNSET:
            field_dict["UDPSendCount"] = udp_send_count
        if udp_send_delay is not UNSET:
            field_dict["UDPSendDelay"] = udp_send_delay
        if ignore_virtual_interfaces is not UNSET:
            field_dict["IgnoreVirtualInterfaces"] = ignore_virtual_interfaces
        if virtual_interface_names is not UNSET:
            field_dict["VirtualInterfaceNames"] = virtual_interface_names
        if gateway_monitor_period is not UNSET:
            field_dict["GatewayMonitorPeriod"] = gateway_monitor_period
        if enable_multi_socket_binding is not UNSET:
            field_dict["EnableMultiSocketBinding"] = enable_multi_socket_binding
        if trust_all_ip6_interfaces is not UNSET:
            field_dict["TrustAllIP6Interfaces"] = trust_all_ip6_interfaces
        if hd_homerun_port_range is not UNSET:
            field_dict["HDHomerunPortRange"] = hd_homerun_port_range
        if published_server_uri_by_subnet is not UNSET:
            field_dict["PublishedServerUriBySubnet"] = published_server_uri_by_subnet
        if auto_discovery_tracing is not UNSET:
            field_dict["AutoDiscoveryTracing"] = auto_discovery_tracing
        if auto_discovery is not UNSET:
            field_dict["AutoDiscovery"] = auto_discovery
        if remote_ip_filter is not UNSET:
            field_dict["RemoteIPFilter"] = remote_ip_filter
        if is_remote_ip_filter_blacklist is not UNSET:
            field_dict["IsRemoteIPFilterBlacklist"] = is_remote_ip_filter_blacklist
        if enable_u_pn_p is not UNSET:
            field_dict["EnableUPnP"] = enable_u_pn_p
        if enable_remote_access is not UNSET:
            field_dict["EnableRemoteAccess"] = enable_remote_access
        if local_network_subnets is not UNSET:
            field_dict["LocalNetworkSubnets"] = local_network_subnets
        if local_network_addresses is not UNSET:
            field_dict["LocalNetworkAddresses"] = local_network_addresses
        if known_proxies is not UNSET:
            field_dict["KnownProxies"] = known_proxies
        if enable_published_server_uri_by_request is not UNSET:
            field_dict["EnablePublishedServerUriByRequest"] = enable_published_server_uri_by_request

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        require_https = d.pop("RequireHttps", UNSET)

        certificate_path = d.pop("CertificatePath", UNSET)

        certificate_password = d.pop("CertificatePassword", UNSET)

        base_url = d.pop("BaseUrl", UNSET)

        public_https_port = d.pop("PublicHttpsPort", UNSET)

        http_server_port_number = d.pop("HttpServerPortNumber", UNSET)

        https_port_number = d.pop("HttpsPortNumber", UNSET)

        enable_https = d.pop("EnableHttps", UNSET)

        public_port = d.pop("PublicPort", UNSET)

        u_pn_p_create_http_port_map = d.pop("UPnPCreateHttpPortMap", UNSET)

        udp_port_range = d.pop("UDPPortRange", UNSET)

        enable_ipv6 = d.pop("EnableIPV6", UNSET)

        enable_ipv4 = d.pop("EnableIPV4", UNSET)

        enable_ssdp_tracing = d.pop("EnableSSDPTracing", UNSET)

        ssdp_tracing_filter = d.pop("SSDPTracingFilter", UNSET)

        udp_send_count = d.pop("UDPSendCount", UNSET)

        udp_send_delay = d.pop("UDPSendDelay", UNSET)

        ignore_virtual_interfaces = d.pop("IgnoreVirtualInterfaces", UNSET)

        virtual_interface_names = d.pop("VirtualInterfaceNames", UNSET)

        gateway_monitor_period = d.pop("GatewayMonitorPeriod", UNSET)

        enable_multi_socket_binding = d.pop("EnableMultiSocketBinding", UNSET)

        trust_all_ip6_interfaces = d.pop("TrustAllIP6Interfaces", UNSET)

        hd_homerun_port_range = d.pop("HDHomerunPortRange", UNSET)

        published_server_uri_by_subnet = cast(List[str], d.pop("PublishedServerUriBySubnet", UNSET))

        auto_discovery_tracing = d.pop("AutoDiscoveryTracing", UNSET)

        auto_discovery = d.pop("AutoDiscovery", UNSET)

        remote_ip_filter = cast(List[str], d.pop("RemoteIPFilter", UNSET))

        is_remote_ip_filter_blacklist = d.pop("IsRemoteIPFilterBlacklist", UNSET)

        enable_u_pn_p = d.pop("EnableUPnP", UNSET)

        enable_remote_access = d.pop("EnableRemoteAccess", UNSET)

        local_network_subnets = cast(List[str], d.pop("LocalNetworkSubnets", UNSET))

        local_network_addresses = cast(List[str], d.pop("LocalNetworkAddresses", UNSET))

        known_proxies = cast(List[str], d.pop("KnownProxies", UNSET))

        enable_published_server_uri_by_request = d.pop("EnablePublishedServerUriByRequest", UNSET)

        network_configuration = cls(
            require_https=require_https,
            certificate_path=certificate_path,
            certificate_password=certificate_password,
            base_url=base_url,
            public_https_port=public_https_port,
            http_server_port_number=http_server_port_number,
            https_port_number=https_port_number,
            enable_https=enable_https,
            public_port=public_port,
            u_pn_p_create_http_port_map=u_pn_p_create_http_port_map,
            udp_port_range=udp_port_range,
            enable_ipv6=enable_ipv6,
            enable_ipv4=enable_ipv4,
            enable_ssdp_tracing=enable_ssdp_tracing,
            ssdp_tracing_filter=ssdp_tracing_filter,
            udp_send_count=udp_send_count,
            udp_send_delay=udp_send_delay,
            ignore_virtual_interfaces=ignore_virtual_interfaces,
            virtual_interface_names=virtual_interface_names,
            gateway_monitor_period=gateway_monitor_period,
            enable_multi_socket_binding=enable_multi_socket_binding,
            trust_all_ip6_interfaces=trust_all_ip6_interfaces,
            hd_homerun_port_range=hd_homerun_port_range,
            published_server_uri_by_subnet=published_server_uri_by_subnet,
            auto_discovery_tracing=auto_discovery_tracing,
            auto_discovery=auto_discovery,
            remote_ip_filter=remote_ip_filter,
            is_remote_ip_filter_blacklist=is_remote_ip_filter_blacklist,
            enable_u_pn_p=enable_u_pn_p,
            enable_remote_access=enable_remote_access,
            local_network_subnets=local_network_subnets,
            local_network_addresses=local_network_addresses,
            known_proxies=known_proxies,
            enable_published_server_uri_by_request=enable_published_server_uri_by_request,
        )

        return network_configuration
