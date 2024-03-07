import ipaddress
import requests

def find_all_subnets(cidr, new_prefix):
    # 解析原始CIDR
    network = ipaddress.ip_network(cidr, strict=False)

    # 计算新CIDR中每个子网的大小
    new_network_size = 2 ** (32 - new_prefix)

    # 计算原始CIDR中可以容纳多少个新CIDR
    num_subnets = network.num_addresses // new_network_size

    # 计算原始网络的网络地址和广播地址
    network_address = network.network_address
    broadcast_address = network.broadcast_address

    # 计算并打印所有新CIDR
    for i in range(num_subnets):
        # 计算新子网的起始地址
        new_network_address = network_address + (i * new_network_size)
        # 计算新子网的结束地址（广播地址前一个）
        new_broadcast_address = new_network_address + new_network_size - 1
        # 创建新的子网对象
        new_subnet = ipaddress.ip_network(f"{new_network_address}/{new_prefix}", strict=False)
        # 打印新的/24子网
        print(f"{new_subnet.network_address}/24")

    # 使用CIDR和新的前缀长度

response=requests.get('https://www.cloudflare.com/ips-v4').text
# print(response)
for cidr in response.split('\n'):
    new_prefix = 24
    find_all_subnets(cidr, new_prefix)