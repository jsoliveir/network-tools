# What's in this repository

This repository contains just experiments and examples around tooling and little hacks

Dependencies:
* https://www.docker.com/products/docker-desktop

## Tunneling

* [chisel: ssh tunneling over http (proxy and gateways)](chisel/)
* [socat: tcp/ip p2p vpn tunnel over ssl](socat/vpn-ssl)
* [socat: tcp/ip p2p vpn tunnel](socat/vpn-simple)

## TCP/IP forwarding

* [socat: tcp/ip forwarding thru a proxy server](socat/forward-over-proxy)

## Reverse proxys and gateways

* [mitmproxy: http Request/Response interception and manipulation](mitmproxy/)
* [mitmproxy: kubernetes requests interception; centralizing access tokens](kubernetes/mitm-proxy/)
* [socat: reverse proxing thru another http proxy](socat/)
* [nginx: http/https reverse proxing](nginx/reverse-proxy)
* [nginx: injecting enviornment varialbes](nginx/env-variables)
