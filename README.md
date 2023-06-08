这是一个关于金融业务，构造数据的测试工具练手项目，for 为数不多的测开同学。
### 启动
后端：
```shell
$ pip install -r requirements.txt
```

```shell
$ export FLASK_APP=main.py
```

```shell
$ flask run
```

前端：
```shell
$ cd web
```

```shell
$ npm install
```

```shell
$ npm run dev
```

### 项目结构
整体结构：
```
.
├── README.md
├── app                             # 后端文件目录
├── main.py                         # 后端启动文件
├── requirements.txt                # python依赖
└── web                             # 前端项目
```

后端结构：
```
.
├── app
│   ├── __init__.py      
│   ├── apis.py                     # 路由文件
│   ├── approve                     # 审批类
│   ├── extensions.py               
│   ├── factory.py                  # 工厂类，便于创建app与路由
│   ├── fakes                       # 数据构造类
│   ├── logger                      # 统一日志类
│   ├── params                      # 参数类，定义前后端对接的参数
│   ├── sign                        # 登录类，定义类统一的注册、登录方法
│   ├── submit                      # 提交类，定义了不同地区的提交方法
│   └── utils                       # 工具类
├── main.py
└──requirements.txt
```

### 功能模块
- [x] 注册用户
- [x] 提交开户申请
- [x] 审批开户申请
- [x] 开户信息查询
