include ../../build_system/make/make.mk

# suppress warning caused by lwip
CFLAGS_GCC += \
  -Wno-error=null-dereference \
  -Wno-error=unused-parameter \
  -Wno-error=unused-variable

INC += \
  src \
  $(TOP)/hw \
  $(TOP)/lib/lwip/src/include \
  $(TOP)/lib/lwip/src/include/ipv4 \
  $(TOP)/lib/lwip/src/include/lwip/apps \
  $(TOP)/lib/networking

# Example source
EXAMPLE_SOURCE += $(wildcard src/*.c)
SRC_C += $(addprefix $(CURRENT_PATH)/, $(EXAMPLE_SOURCE))

# lwip sources
SRC_C += \
  lib/lwip/src/core/altcp.c \
  lib/lwip/src/core/altcp_alloc.c \
  lib/lwip/src/core/altcp_tcp.c \
  lib/lwip/src/core/def.c \
  lib/lwip/src/core/dns.c \
  lib/lwip/src/core/inet_chksum.c \
  lib/lwip/src/core/init.c \
  lib/lwip/src/core/ip.c \
  lib/lwip/src/core/mem.c \
  lib/lwip/src/core/memp.c \
  lib/lwip/src/core/netif.c \
  lib/lwip/src/core/pbuf.c \
  lib/lwip/src/core/raw.c \
  lib/lwip/src/core/stats.c \
  lib/lwip/src/core/sys.c \
  lib/lwip/src/core/tcp.c \
  lib/lwip/src/core/tcp_in.c \
  lib/lwip/src/core/tcp_out.c \
  lib/lwip/src/core/timeouts.c \
  lib/lwip/src/core/udp.c \
  lib/lwip/src/core/ipv4/autoip.c \
  lib/lwip/src/core/ipv4/dhcp.c \
  lib/lwip/src/core/ipv4/etharp.c \
  lib/lwip/src/core/ipv4/icmp.c \
  lib/lwip/src/core/ipv4/igmp.c \
  lib/lwip/src/core/ipv4/ip4.c \
  lib/lwip/src/core/ipv4/ip4_addr.c \
  lib/lwip/src/core/ipv4/ip4_frag.c \
  lib/lwip/src/core/ipv6/dhcp6.c \
  lib/lwip/src/core/ipv6/ethip6.c \
  lib/lwip/src/core/ipv6/icmp6.c \
  lib/lwip/src/core/ipv6/inet6.c \
  lib/lwip/src/core/ipv6/ip6.c \
  lib/lwip/src/core/ipv6/ip6_addr.c \
  lib/lwip/src/core/ipv6/ip6_frag.c \
  lib/lwip/src/core/ipv6/mld6.c \
  lib/lwip/src/core/ipv6/nd6.c \
  lib/lwip/src/netif/ethernet.c \
  lib/lwip/src/netif/slipif.c \
  lib/lwip/src/apps/http/httpd.c \
  lib/lwip/src/apps/http/fs.c \
  lib/lwip/src/apps/lwiperf/lwiperf.c \
  lib/networking/dhserver.c \
  lib/networking/dnserver.c \
  lib/networking/rndis_reports.c

include ../../build_system/make/rules.mk
