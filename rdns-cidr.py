import ipaddress

def generate_reverse_dns_entries(cidr, host_template, make_a_records, make_ptr_records):
    try:
        network = ipaddress.IPv4Network(cidr, strict=False)
    except ipaddress.AddressValueError:
        print("Invalid CIDR format")
        return

    for ip in network.hosts():
        reversed_ip = ".".join(reversed(ip.exploded.split('.'))

        if make_ptr_records:
            ptr_record = f"{reversed_ip}.in-addr.arpa. IN PTR {host_template.format(reverseIP=reversed_ip)}."
            print(ptr_record)

        if make_a_records:
            host = host_template.format(reverseIP=reversed_ip)
            a_record = f"{host}. IN A {ip.exploded}"
            print(a_record)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate reverse DNS entries")
    parser.add_argument("-cidr", required=True, help="CIDR notation for the IP range")
    parser.add_argument("-host", required=True, help="Hostname template (e.g., ec2-{reverseIP}.{host})")
    parser.add_argument("-F", action="store_true", help="Create A records")
    parser.add_argument("-R", action="store_true", help="Create PTR records")

    args = parser.parse_args()

    generate_reverse_dns_entries(args.cidr, args.host, args.F, args.R)
