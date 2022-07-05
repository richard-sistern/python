# Adapted from https://medium.com/codex/visualising-the-cloud-diagrams-as-code-62487b3bfa8a

# pip install diagrams
# https://graphviz.gitlab.io/download/

from diagrams import Cluster, Diagram
from diagrams.azure.general import Subscriptions, Usericon
from diagrams.azure.compute import ContainerInstances
from diagrams.azure.identity import ActiveDirectory
from diagrams.azure.database import CacheForRedis, SQLDatabases
from diagrams.azure.network import LoadBalancers, DNSZones

with Diagram("Azure Monitor Distributed Architecture", show=False):
    dns = DNSZones("dns")
    nlb = LoadBalancers("nlb")

    with Cluster("Services"):
        svc_group = [
            ContainerInstances("web1"),
            ContainerInstances("web2"),
            ContainerInstances("web3")
            ]

    with Cluster("DB Cluster"):
        db_master = SQLDatabases("userdb")
        db_master - [SQLDatabases("userdb ro")]

    memcached = CacheForRedis("memcached")

    dns >> nlb >> svc_group
    svc_group >> db_master
    svc_group >> memcached


# https://diagrams.mingrammer.com/docs/nodes/azure