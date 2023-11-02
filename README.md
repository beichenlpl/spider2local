## 轻量级通用爬虫框架spider2local
### 1、框架设计
![spider2local.png](spider2local.png)
### 2、安装
```commandline
pip install spider2local
```
### 3、使用示例
```python
from spider2local import send_request, resp_filter, Request, ResponseType, Filter, FilterRule
from time import sleep

if __name__ == '__main__':
    req = Request(
        host='https://xueqiu.com/',
        uri='statuses/hot/listV2.json',
        params={
            'since_id': -1,
            'max_id': -1,
            'size': 15
        },
        resp_type=ResponseType.JSON
    )
    req.auto_set_cookie()
    resp = send_request(req)

    data = resp.get_content()
    for item in data['items']:
        user_id = item['original_status']['user_id']
        article_id = item['original_status']['id']
        req = Request(
            host='https://xueqiu.com/',
            uri=f'{user_id}/{article_id}'
        )
        req.auto_set_cookie()
        resp = send_request(req)

        filter_rules = [FilterRule('div', {'class': 'article__bd__detail'})]
        entity = resp_filter(Filter(resp, filter_rules))
        print(entity.text())

        sleep(10)

```