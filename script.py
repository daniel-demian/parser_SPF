import dns.resolver

def get_spf_record(domain):
    answers = dns.resolver.resolve(domain, 'TXT')
    for rdata in answers:
        spf_record = rdata.to_text()
        if 'v=spf1' in spf_record:
            return spf_record
    return None

def get_ip_addresses(spf_record):
    ip_addresses = []
    spf_records = spf_record.split(" ")
    for record in spf_records:
        if record.startswith('ip4:'):
            ip_addr = record.split(":")[1]
            ip_addresses.append(ip_addr)
    return ip_addresses

def get_domains(spf_record):
    domains = []
    spf_records = spf_record.split(" ")
    for record in spf_records:
        if record.startswith('include:'):
            domain = record.split(":")[1]
            domains.append(domain)
    return domains

def get_all_ips(domain, visited_domains=set()):
    print(f"Spracovanie domény: {domain}")

    if domain in visited_domains:
        return

    visited_domains.add(domain)
    spf_record = get_spf_record(domain)

    if not spf_record:
        return

    print(f"SPF záznam pre {domain}: {spf_record}")
    ip_addresses = get_ip_addresses(spf_record)
    include_domains = get_domains(spf_record)

    print(f"Najdene IP adresy pre {domain}: {ip_addresses}")
    print(f"Najdene Domeny pre {domain}: {include_domains}\n")

    for include_domain in include_domains:
        ip_addresses.extend(get_all_ips(include_domain, visited_domains))
    return ip_addresses

if __name__ == "__main__":
    domain = "somi.sk"
    ip_addresses = get_all_ips(domain)
    print("\nIP ADRESY:")
    print(*ip_addresses, sep="\n")
