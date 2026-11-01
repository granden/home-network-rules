"""Convert the router's maintained DustinWin domain list, without adding domains."""
from pathlib import Path
from urllib.request import urlopen
import re

URL = 'https://raw.githubusercontent.com/DustinWin/ruleset_geodata/mihomo-ruleset/cn.list'

def convert(text):
    result = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        suffix = line.startswith('+.')
        domain = line[2:] if suffix else line
        if not re.fullmatch(r'[A-Za-z0-9_.-]+', domain) or domain.startswith('.'):
            raise ValueError('Unexpected upstream domain syntax; leaving prior file intact')
        result.append(('DOMAIN-SUFFIX,' if suffix else 'DOMAIN,') + domain)
    if len(result) < 10000:
        raise ValueError('Upstream unexpectedly small; leaving prior file intact')
    return '# Source: ' + URL + '\n# Format conversion only; upstream domain membership is preserved.\n' + '\n'.join(result) + '\n'

if __name__ == '__main__':
    with urlopen(URL, timeout=60) as response:
        result = convert(response.read().decode('utf-8'))
    output = Path(__file__).with_name('cn.list')
    tmp = output.with_suffix('.list.tmp')
    tmp.write_text(result, encoding='utf-8')
    tmp.replace(output)
    print('Converted', len(result.splitlines()) - 2, 'domains')
