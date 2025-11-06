# StealthIM Python SDK

StealthIM 的官方 Python SDK，一个安全私密的即时消息平台。

## 概述

StealthIM Python SDK 提供了与 StealthIM 服务器交互的综合接口。它允许您创建能够安全地注册用户、管理群组、发送消息和处理各种通信功能的应用程序。

## 安装

使用 pip 安装 SDK：

```bash
pip install stealthimpysdk
```

## 先决条件

- Python 3.9 或更高版本
- aiohttp >= 3.12.15
- blake3 == 1.0.6

## 快速开始

以下是如何使用 SDK 的简单示例：

```python
import asyncio
from StealthIM import Server, User

async def main():
    # 初始化服务器连接
    server = Server("https://your-stealthim-server.com")
    
    # 检查服务器是否可访问
    if await server.ping():
        print("服务器可访问")
    else:
        print("服务器无法访问")
        return
    
    # 注册新用户
    register_result = await server.register(
        username="testuser",
        password="securepassword",
        nickname="Test User",
        email="test@example.com"
    )
    
    # 登录到服务器
    user = await server.login("testuser", "securepassword")
    
    if user:
        print(f"以 {user.session} 身份登录")
        
        # 获取用户自己的信息
        user_info = await user.get_self_info()
        print(f"用户信息: {user_info}")
        
        # 更新用户信息
        await user.update_info(nickname="更新的名称")
        
        # 获取用户所属的群组
        groups = await user.get_groups()
        print(f"群组: {groups}")
    else:
        print("登录失败")

# 运行异步函数
asyncio.run(main())
```

## API 参考

### Server 类

`Server` 类是连接到 StealthIM 服务器的入口点。

#### 方法

- `__init__(url: str)`: 使用给定的 URL 初始化 Server 实例。
- `ping()`: 检查服务器是否可访问。
- `register(username: str, password: str, nickname: str, email: str = None, phone_number: str = None)`: 注册新用户。
- `login(username: str, password: str)`: 登录到服务器。

### User 类

`User` 类表示一个已登录的用户，并提供用户相关操作的方法。

#### 方法

- `get_self_info()`: 获取当前用户的信息。
- `get_user_info(username: str)`: 获取另一个用户的公开信息。
- `change_password(new_password: str)`: 更改用户密码。
- `change_email(new_email: str)`: 更改用户邮箱。
- `change_nickname(new_nickname: str)`: 更改用户昵称。
- `change_phone_number(new_phone_number: str)`: 更改用户电话号码。
- `update_info(password: str = None, email: str = None, nickname: str = None, phone_number: str = None)`: 一次性更新多个用户信息字段。
- `delete()`: 删除用户账户。
- `get_groups()`: 获取用户所属的所有群组。

### Group 类

`Group` 类提供群组相关操作的方法。

#### 方法

- `create(user: User, group_name: str)`: 创建新群组。
- `join(password: str)`: 使用密码加入群组。
- `get_members()`: 获取群组成员列表。
- `get_info()`: 获取群组的公开信息。
- `invite(username: str)`: 邀请用户加入群组。
- `set_member_role(username: str, role: GroupMemberType)`: 设置群组成员的角色。
- `kick(username: str)`: 从群组中移除成员。
- `change_name(new_name: str)`: 更改群组名称。
- `change_password(new_password: str)`: 更改群组密码。
- `send_text(message: str)`: 向群组发送文本消息。
- `receive_text(from_id: int = 0, sync: bool = True, limit: int = 128)`: 从群组接收文本消息。
- `receive_latest_text(limit: int = 128)`: 接收群组的最新文本消息。
- `receive_new_text(limit: int = 128)`: 接收群组的新文本消息。
- `recall_message(message_id: int)`: 从群组撤回消息。
- `get_file_info(file_hash: str)`: 获取文件信息。
- `send_file(filename: str, file_path: str)`: 向群组上传文件。
- `download_file(file_hash: str, output_path: str, threads: int = 1)`: 从群组下载文件。
- `download_files(file_hash_list, filename_list, output_dir, max_concurrent=1, threads_per_file=1)`: 批量下载多个文件。

## 功能特性

- 用户注册和身份验证
- 群组管理（创建、加入、邀请、管理成员）
- 安全消息传递（文本和文件）
- 文件上传和下载（支持多线程下载）
- 用户信息管理
- 消息撤回功能

## 许可证

本项目根据 [LICENSE](./LICENSE) 文件中指定的条款进行许可。

## 贡献

我们欢迎对 StealthIM Python SDK 的贡献。请按以下步骤操作：

1. Fork 仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

## 支持

如果您遇到任何问题或有疑问，请在 [GitHub 仓库](https://github.com/StealthIM/StealthIMPythonSDK) 上提交 issue。