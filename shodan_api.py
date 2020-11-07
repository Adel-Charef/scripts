import shodan
import requests
import os

SHODAN_API_KEY = os.environ.get("API_KEY")
api = shodan.Shodan(SHODAN_API_KEY)

target = "www.packtpub.com"

dnsResolve = f"https://api.shodan.io/dns/resolve?hostnames={target}&key={SHODAN_API_KEY}"

try:
    # first we need to resolve our targets domain to an IP
    resolved = requests.get(dnsResolve)
    hostIP = resolved.json()[target]

    # Then we need to do a Shodan search on that IP
    host = api.host(hostIP)
    print("IP: %s" % (host['ip_str']))
    print("Organization: %s" % host.get('org', 'n/a'))
    print("Operating System: %s" % host.get('os', 'n/a'))

    # print all banners
    for item in host["data"]:
        print("Port: %s" % item['port'])
        print("Banner: %s" % item['data'])

    # Print vuln information
    for v in host['vulns']:
        CVE = v.replace('!', '')
        print('Vulns: %s' % v)
        exploits = api.exploits.search(CVE)
        for item in exploits:
            if item.get('cve')[0] == CVE:
                print(item.get('description'))
except:
    print("An error occured")
