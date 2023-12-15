from spider2local import send_request, resp_filter, Request, AttributeFilter, AttributeFilterRule

if __name__ == '__main__':
    req = Request('https://gitee.com/')
    resp = send_request(req)
    rules = [AttributeFilterRule('title', {})]
    entity = resp_filter(AttributeFilter(resp, rules))
    print(entity.text())
