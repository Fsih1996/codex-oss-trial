# codex-oss-trial

A local Python todo list, kept as a learning project for command-line tools, tests, and GitHub. 一个本地 Python 待办清单，用来练习命令行、测试和 GitHub 开源流程。

[中文](#中文) | [English](#english)

## 中文

### 这个仓库做什么

练习把一个很小的命令行工具做完整：任务写在本机 JSON 文件里，命令失败时给出明确错误，并用测试和 CI 把行为固定下来。它是学习示例，不是任务管理产品。

`todo_cli.py` 是待办清单。`hello.py` 是更早的一个问候脚本，打印一句话和当天日期，和待办清单互不依赖。

### 现状

- 一个人维护的学习仓库。
- 命令在本机运行。数据默认写到当前目录的 `todo.json`，也可以用 `--file` 指定路径。
- 没有账号、没有网络请求、没有遥测。
- 运行 CLI 不需要第三方库。测试使用 pytest。
- `pyproject.toml` 里的 `0.1.0` 只是本地版本号，没有发布到 PyPI。
- 不统计、也不声称使用者、star 或下载量。

### 安装与运行

需要 Python 3.11 或更新版本。只运行 CLI 时不必安装依赖：

```bash
git clone https://github.com/Fsih1996/codex-oss-trial.git
cd codex-oss-trial
python3 todo_cli.py --help
python3 hello.py
```

跑测试时再安装开发依赖：

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -m pip install -e ".[dev]"
pytest
```

安装后也可以用入口脚本 `codex-todo`（和 `python todo_cli.py` 是同一个 `main`）。

### 命令

| 命令 | 作用 |
| --- | --- |
| `add TITLE` | 追加一条未完成任务。标题会去掉首尾空白，不能为空，不能换行，最长 200 个字符 |
| `list` | 按文件中的顺序显示。没有任务时打印 `No tasks yet.` |
| `done N` | 把第 N 条标为完成 |
| `remove N` | 删除第 N 条。后面的编号会前移 |
| `--file PATH` | 使用别的 JSON 文件，默认是 `todo.json` |
| `--help` | 显示说明和示例 |

编号从 1 开始，不是稳定 id。删除一条之后，后面的编号都会变。

```bash
python3 todo_cli.py add "buy milk"
python3 todo_cli.py list
python3 todo_cli.py done 1
python3 todo_cli.py remove 1
python3 todo_cli.py --file /tmp/tasks.json list
```

列表看起来像这样：

```text
1. [ ] buy milk
2. [x] walk
```

找不到编号、标题不合法、JSON 损坏时，错误写到 stderr，进程以状态码 1 退出。缺少参数这类 argparse 错误以状态码 2 退出。

### 测试与 CI

```bash
pytest
```

测试在 `tests/`。待办测试使用临时文件，不会改写你自己的 `todo.json`。

GitHub Actions（`.github/workflows/ci.yml`）在推送到 `main` 以及 pull request 上运行，Python 3.11 和 3.12，命令是 `pytest -q`。

### 目录

```text
.
├── todo_cli.py                 # 待办命令和 JSON 读写
├── hello.py                    # 问候脚本
├── tests/                      # pytest
├── docs/APPLICATION_NOTES.md   # 申请表短文草稿
├── .github/workflows/ci.yml    # CI
├── pyproject.toml              # 项目元数据和开发依赖
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE                     # MIT
└── README.md
```

### 这些文件能说明的能力

仓库里看得到的部分：

- 用 argparse 写带子命令的 CLI，`--help` 里带示例
- 把任务存成 JSON，写入时先写临时文件再替换
- 对空标题、过长标题、错误编号、损坏 JSON 给出明确错误
- 用 pytest 和临时目录做命令测试
- 用 GitHub Actions 跑这些测试
- MIT 许可证、贡献说明、以及一份针对本地工具的安全说明
- 中英双语文档

### 申请表可以怎么答

短字段（大约 500 字以内）的英文草稿在 [docs/APPLICATION_NOTES.md](docs/APPLICATION_NOTES.md)。那是草稿，提交前改成你自己的说法。

- **项目是什么：** 一个本地 Python 待办 CLI，用来练习开源仓库怎么组织。没有部署，也没有可引用的使用数据。
- **为什么公开：** 让别人能克隆、跑测试、看提交记录，并对照 README 检查行为。
- **做这个仓库时练习了什么：** argparse、JSON 文件、pytest、GitHub Actions，以及把项目状态写清楚。
- **有没有生产用户：** 没有声称任何生产使用。
- **别人能贡献什么：** 看 [CONTRIBUTING.md](CONTRIBUTING.md)。小的修复、测试和文档更合适。

### 还没做的事

- 删除后编号会变，没有稳定 id
- 不能按“只看未完成”过滤
- 不计划加账号、同步或网络服务，除非真的需要

### 许可证

MIT，见 [LICENSE](LICENSE)。贡献方式见 [CONTRIBUTING.md](CONTRIBUTING.md)，安全说明见 [SECURITY.md](SECURITY.md)。

## English

### What this repo is for

A small exercise in finishing a command-line tool: tasks live in a JSON file on the machine where you run it, bad input fails with a clear error, and tests plus CI lock the behavior down. It is a learning demo, not a task-management product.

`todo_cli.py` is the todo list. `hello.py` is an earlier greeting script that prints one line and today's date. The two programs do not depend on each other.

### Status

- A learning repo with one maintainer.
- Commands run locally. The default data file is `todo.json` in the working directory. `--file` selects another path.
- No accounts, no network calls, and no telemetry.
- The CLI has no third-party runtime dependencies. Tests use pytest.
- `0.1.0` in `pyproject.toml` is a local version label. The project is not published to PyPI.
- Users, stars, and downloads are not tracked and are not claimed.

### Install and run

Python 3.11 or newer. You can run the CLI without installing anything else:

```bash
git clone https://github.com/Fsih1996/codex-oss-trial.git
cd codex-oss-trial
python3 todo_cli.py --help
python3 hello.py
```

Install the dev extra when you want the tests:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -m pip install -e ".[dev]"
pytest
```

The install also adds a `codex-todo` command. It calls the same `main` as `python todo_cli.py`.

### Commands

| Command | What it does |
| --- | --- |
| `add TITLE` | Append an open task. The title is stripped, must be non-empty, must be a single line, and must be at most 200 characters |
| `list` | Print tasks in file order. Prints `No tasks yet.` when the file is missing or empty |
| `done N` | Mark task N done |
| `remove N` | Delete task N. Later numbers shift down by one |
| `--file PATH` | Store tasks in another JSON file. The default is `todo.json` |
| `--help` | Show the description and examples |

Numbers start at 1. They are positions in the file, not stable ids. Removing a task renumbers the ones after it.

```bash
python3 todo_cli.py add "buy milk"
python3 todo_cli.py list
python3 todo_cli.py done 1
python3 todo_cli.py remove 1
python3 todo_cli.py --file /tmp/tasks.json list
```

List output looks like this:

```text
1. [ ] buy milk
2. [x] walk
```

An unknown number, a rejected title, or corrupt JSON is written to stderr and the process exits with code 1. Missing arguments and other argparse usage errors exit with code 2.

### Tests and CI

```bash
pytest
```

Tests live in `tests/`. The todo tests pass a temporary file, so they do not write your real `todo.json`.

GitHub Actions (`.github/workflows/ci.yml`) runs on pushes to `main` and on pull requests, on Python 3.11 and 3.12, with `pytest -q`.

### Layout

```text
.
├── todo_cli.py                 # todo commands and JSON storage
├── hello.py                    # greeting script
├── tests/                      # pytest
├── docs/APPLICATION_NOTES.md   # short draft answers for application forms
├── .github/workflows/ci.yml    # CI
├── pyproject.toml              # project metadata and the dev extra
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE                     # MIT
└── README.md
```

### What the repo demonstrates

Visible in the tree:

- An argparse CLI with subcommands and examples in `--help`
- JSON storage that writes a temp file and then replaces the destination
- Clear failures for an empty title, a too-long title, a bad number, and corrupt JSON
- pytest, using a temporary directory for command tests
- GitHub Actions running those tests
- An MIT license, a contributing guide, and a security note for a local tool
- Bilingual docs

### Short answers for an application form

Paste-ready English drafts, each under 500 characters, are in [docs/APPLICATION_NOTES.md](docs/APPLICATION_NOTES.md). They are drafts. Edit them into your own words before you submit. The notes file records the character count of each paragraph.

- **What is the project?** A local Python todo CLI, used to practice how a small open-source repo is put together. It is not deployed, and it has no usage figures to cite.
- **Why open source it?** So a reviewer can clone it, run the tests, and check the behavior against the README and the commit history.
- **What did the work practice?** argparse, a JSON file, pytest, GitHub Actions, and writing the project status in plain language.
- **Is it in production?** No production use is claimed.
- **How can other people contribute?** See [CONTRIBUTING.md](CONTRIBUTING.md). Small fixes, tests, and doc corrections fit this repo.

### Still open

- Task numbers change after a removal. There are no stable ids.
- There is no "open tasks only" filter.
- Accounts, sync, and a network service are out of scope unless a real need shows up.

### License

MIT. See [LICENSE](LICENSE). Contributing: [CONTRIBUTING.md](CONTRIBUTING.md). Security notes: [SECURITY.md](SECURITY.md).
