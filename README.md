# codex-oss-trial

[中文](#中文) | [English](#english)

## 中文

### 简介
这是一个由初学者开发者创建的学习练习项目（learning playground），用来练习 Python、命令行工具、测试和 GitHub 开源协作流程。代码都很简单，欢迎指正。

### 功能
- `hello.py`：打印问候语和日期。
- `todo_cli.py`：一个简单的命令行待办清单，数据保存在 `todo.json`。

### 使用示例
```bash
python hello.py
python todo_cli.py add "buy milk"
python todo_cli.py list
python todo_cli.py done 1
python todo_cli.py remove 1
```

### 运行测试
```bash
pip install pytest && pytest
```

### 路线图
- 增加更多测试
- 添加类型注解（type hints）
- 打包发布（packaging）

### 许可证
MIT，详见 [LICENSE](LICENSE)。欢迎阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 参与贡献。

## English

### Introduction
A learning playground by a beginner developer, used to practice Python, command-line tools, testing, and the GitHub open-source workflow. The code is intentionally simple; feedback is welcome.

### Features
- `hello.py`: prints a greeting and the date.
- `todo_cli.py`: a small command-line todo list, saved in `todo.json`.

### Usage
```bash
python hello.py
python todo_cli.py add "buy milk"
python todo_cli.py list
python todo_cli.py done 1
python todo_cli.py remove 1
```

### Running tests
```bash
pip install pytest && pytest
```

### Roadmap
- More tests
- Type hints
- Packaging

### License
MIT, see [LICENSE](LICENSE). See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute.
