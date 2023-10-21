import ipaddress

def generate_reverse_dns_entries(cidr, host, make_a_records, make_ptr_records):
    try:
        network = ipaddress.IPv4Network(cidr, strict=False)
    except ipaddress.AddressValueError:
        print("Invalid CIDR format")
        return

    if make_ptr_records:
        for ip in network.hosts():
            reversed_ip = ".".join(reversed(ip.exploded.split('.')))
            ptr_record = f"{reversed_ip}.in-addr.arpa. IN PTR {reversed_ip}.{host}."
            print(ptr_record)

    if make_a_records:
        for ip in network.hosts():
            a_record = f"{ip.exploded} IN A {host}."
            print(a_record)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate reverse DNS entries")
    parser.add_argument("-cidr", required=True, help="CIDR notation for the IP range")
    parser.add_argument("-host", required=True, help="Hostname")
    parser.add_argument("-F", action="store_true", help="Create A records")
    parser.add_argument("-R", action="store_true", help="Create PTR records")

    args = parser.parse_args()

    generate_reverse_dns_entries(args.cidr, args.host, args.F, args.R)
