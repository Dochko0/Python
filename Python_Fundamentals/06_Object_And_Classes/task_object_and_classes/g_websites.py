class Website:
    def __init__(self, host, domain, queries):
        self.host = host
        self.domain = domain
        self.queries = list(queries)


websites = []

while True:
    line = input()
    if line == 'end':
        break
    queries = []
    spl_line = line.split(' | ')
    host = spl_line[0]
    domain = spl_line[1]
    try:
        queries = spl_line[2].split(',')
    except:
        pass

    websites.append(Website(host,domain,queries))


for web in websites:
    print(f'https://www.{web.host}.{web.domain}', end='')
    if len(web.queries) != 0:
        print(f'/query?=' + '[' + ']&['.join(x for x in web.queries) + ']')


