import ipaddress
import argparse
import logging

# Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_reverse_dns_entries(cidr, host_template, make_a_records, make_ptr_records):
    ptr_records = []
    a_records = []

    try:
        network = ipaddress.IPv4Network(cidr, strict=False)
    except ipaddress.AddressValueError:
        logging.error("Invalid CIDR format")
        return ptr_records, a_records

    for ip in network.hosts():
        reversed_ip = "-".join(reversed(ip.exploded.split('.')))
        host = host_template.format(reverse=reversed_ip, host=ip.exploded.replace('.', '-'))

        if make_ptr_records:
            ptr_record = f"{ '.'.join(reversed(ip.exploded.split('.')))}.in-addr.arpa. IN PTR {host}"
            # logging.info(f"PTR Record: {ptr_record}")
            ptr_records.append(ptr_record)

        if make_a_records:
            a_record = f"{host}. IN A {ip.exploded}"
            # logging.info(f"A Record: {a_record}")
            a_records.append(a_record)

    return ptr_records, a_records

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate reverse DNS entries")
    parser.add_argument("-cidr", required=True, help="CIDR notation for the IP range")
    parser.add_argument("-host", required=True, help="Hostname template (e.g., ecc-{host}.finnacloud.io})")
    parser.add_argument("-F", action="store_true", help="Create A records")
    parser.add_argument("-R", action="store_true", help="Create PTR records")

    args = parser.parse_args()

    ptr_records, a_records = generate_reverse_dns_entries(args.cidr, args.host, args.F, args.R)
    print("PTR Records:", ptr_records)
    print("A Records:", a_records)

# Example:
# python3 rdns-cidr.py -cidr 194.87.64.0/24 -host ecc-{host}.finnacloud.io -FR
