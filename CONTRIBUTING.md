# Contributing / 参与贡献

## 中文

感谢你对这个项目感兴趣。这是一个初学者的学习仓库，用来练习 Python 命令行、测试和 GitHub 协作。改动不需要很大，提问也欢迎。

1. Fork 本仓库并克隆到本地。
2. 确认本机是 Python 3.11 或更新版本。
3. 新建分支：`git checkout -b my-change`
4. 需要跑测试时安装开发依赖：`python -m pip install -e ".[dev]"`
5. 修改代码。行为变化请在 `tests/` 里补测试。
6. 运行 `pytest`。
7. 提交并发起 Pull Request，用几句话说明改了什么、怎么验证的。

请保持改动集中。文档修正、失败信息、测试覆盖都是有用的贡献。不要在 README 或申请材料里加入无法核对的使用者、star 或下载量。

遇到问题或有想法，可以直接开一个 Issue。请保持友善和耐心。

## English

Thanks for your interest. This is a beginner's learning repo for a Python CLI, tests, and the GitHub workflow. Small changes are useful, and questions are welcome.

1. Fork this repo and clone it.
2. Use Python 3.11 or newer.
3. Create a branch: `git checkout -b my-change`
4. Install test tools when you need them: `python -m pip install -e ".[dev]"`
5. Make the change. If behavior changes, add a test under `tests/`.
6. Run `pytest`.
7. Open a pull request that says what changed and how you checked it.

Keep the diff focused. Doc fixes, clearer errors, and tests are all useful. Do not add user, star, or download claims that nobody can check.

Have a question or idea? Open an issue. Please be kind and patient.

The CLI itself has no third-party runtime dependencies. `pytest` is only for tests. `hello.py` is a separate greeting script; `todo_cli.py` is the todo list.
