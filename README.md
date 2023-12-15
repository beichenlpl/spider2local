## 轻量级爬虫框架spider2local
### 1、框架设计
![spider2local.png](spider2local.png)
### 2、安装
```commandline
pip install spider2local
```
### 3、使用示例
```python
from spider2local import send_request, resp_filter, Request, AttributeFilter, AttributeFilterRule

if __name__ == '__main__':
    req = Request('https://gitee.com/')
    resp = send_request(req)
    rules = [AttributeFilterRule('title', {})]
    entity = resp_filter(AttributeFilter(resp, rules))
    print(entity.text())
```