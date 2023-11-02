from spider2local import send_request, resp_filter, Request, Filter, FilterRule

if __name__ == '__main__':
    req = Request('https://gitee.com/')
    resp = send_request(req)
    rules = [FilterRule('title', {})]
    entity = resp_filter(Filter(resp, rules))
    print(entity.text())
