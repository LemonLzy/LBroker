class Headers(dict):
    """
    统一Headers类，默认属性为host、user_agent、upgrade_insecure_requests
    通过addXXX方法增加content_type等其他自定义属性
    默认返回字典
    """

    def __init__(self, host):
        super().__init__(
            {
                "Host": host,
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; MI 5s Build/MXB48T; wv) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile "
                              "MQQBrowser/6.2 TBS/043124 Safari/537.36 CliLang/zh-cn",
            }
        )

    def __getattr__(self, name):
        return self.get(name, None)

    def __setattr__(self, name, value):
        self[name] = value

    def add_content_type(self, value):
        self.__setattr__("Content-Type", value)
        return self

    def add_referer(self, value):
        self.__setattr__("Referer", value)
        return self

    def add_origin(self, value):
        self.__setattr__("Origin", value)
        return self

    def add_x_forwarded_for(self, value):
        self.__setattr__("X-Forwarded-For", value)
        return self

    def add_x_csrf_token(self, value):
        self.__setattr__("X-Csrf-Token", value)
        return self

    def add_cookie(self, value):
        self.__setattr__("Cookie", value)
        return self


if __name__ == '__main__':
    ch = Headers("baidu.com").add_origin("https://google.com"). \
        add_content_type("application/json").add_referer("https://tencent.com")
    print(ch)
