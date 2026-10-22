# Security / 安全说明

## English

This is a local command-line demo. It has no accounts, no API keys, and no network calls. Task text is written as plain JSON to a file you choose (`todo.json` in the working directory, or the path passed with `--file`).

- Do not put secrets, tokens, or passwords in task titles. The file is not encrypted.
- `--file` writes to any path the process is allowed to use. Pass a path you mean to write.
- There is no telemetry.

### Reporting a problem

There is no private security contact and no bug-bounty program. Open a [GitHub issue](https://github.com/Fsih1996/codex-oss-trial/issues) if something looks wrong.

If a later change adds network access or credential handling, update this file in that same change.

## 中文

这是一个本地命令行示例。它没有账号、没有 API 密钥，也不会发起网络请求。任务内容以普通 JSON 写到你指定的文件（默认是当前目录的 `todo.json`，也可以用 `--file` 指定路径）。

- 不要把密钥、令牌或密码写进任务标题。文件没有加密。
- `--file` 会写到进程有权限写入的路径。请只填写你打算使用的路径。
- 没有遥测。

发现问题请开一个 [GitHub issue](https://github.com/Fsih1996/codex-oss-trial/issues)。这里没有单独的安全邮箱，也没有漏洞赏金。如果以后的改动加入网络访问或凭据处理，请在同一次改动里更新本文件。
