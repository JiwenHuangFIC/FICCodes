# BoA-SQL (2026)

**BoA-SQL: Executable Blueprint-of-Action for Text-to-SQL with reinforcement learning**

- 作者：Yang Wang; Zhilong Xie; Lin Zhang; Lingyun Gu; Qing Li
- 期刊：Engineering Applications of Artificial Intelligence, 166, 113454 (2026)
- 代码提交与维护：[wangy5027](https://github.com/wangy5027)

本目录提供 BoA-SQL 的 Agent 推理与 Spider 实验部分，通过数据库结构筛选、任务规划、逐步 SQL 生成及执行反馈完成 Text-to-SQL。**强化学习训练代码不包含在本次提交中。**

## 开始使用

- [项目说明、环境配置、运行与评测](Spider_Experiment/README.md)
- [Spider 和 test-suite 数据下载及放置说明](Spider_Experiment/DATA_SETUP.md)
- [Agent 运行入口](Spider_Experiment/Run.py)

外层文件夹按团队规范命名为 `BoA-SQL_2026`。内部以 `Spider_Experiment` 存放 Agent 项目。资源路径根据源码位置定位，该子目录可重命名；请保持其内部相对层级。本文链接使用仓库当前目录名称。

默认模型接口使用 `OPENAI_API_KEY`、`OPENAI_BASE_URL` 和 `OPENAI_MODEL` 环境变量，不包含真实 API 密钥。

本次保留 Agent 源码、test-suite 工具、三份历史预测及配套 gold，以及修正版评测所需的 70 个参考文件。原始数据、模型权重、运行缓存、旧 Git 历史和中间实验结果不随代码上传。

当前版本已完成静态检查、模拟入口检查和路径迁移回归检查，尚未重新执行完整实验；依赖版本、最终预测版本及已知运行限制见项目说明。

## 通过命令行提交更新

以下示例使用 PowerShell、Git 和 GitHub CLI（`gh`）。Git 负责克隆与提交，`gh` 负责创建 Fork 和 Pull Request。首次使用需执行 `gh auth login` 完成本人账号授权，并通过 `gh api user --jq .login` 核对账号。

首次创建工作副本时执行（已有 Fork 可直接复用；已有本地副本则跳过克隆）：

```powershell
gh repo fork wangy5027/FICCodes --clone=false
$account = gh api user --jq .login
git clone "https://github.com/$account/FICCodes.git"
Set-Location FICCodes
git remote add upstream https://github.com/wangy5027/FICCodes.git
git fetch upstream
git switch -c docs/boa-sql-update upstream/main
```

按本人信息设置当前仓库的提交署名，并确认 Git 的推送凭据对应自己的 Fork 账号。提交署名与 GitHub 登录账号是两项独立设置。只修改本论文目录中的相关文件，保持外层目录名称 `BoA-SQL_2026`。

完成修改后，在仓库根目录执行：

```powershell
git diff --check
git diff -- BoA-SQL_2026
git add -- BoA-SQL_2026
git diff --cached --stat
git diff --cached -- BoA-SQL_2026
git commit -m "docs: update BoA-SQL contribution instructions"
git push -u origin docs/boa-sql-update
$account = gh api user --jq .login
gh pr create --repo wangy5027/FICCodes --base main --head "${account}:docs/boa-sql-update" --title "提交：BoA-SQL_2026" --body-file pr-description.md
```

创建 PR 前，按[仓库提交要求](../README.md)准备根目录下的 `pr-description.md`，写明论文全名、文件夹、负责人及账号、本次修改、数据链接所在位置、实际完成的检查和未解决问题。该文件仅作为命令输入，无须提交。上述 `git add` 会暂存论文目录内所有改动，请核对完整差异，避免混入数据、密钥或无关文件。

若分支名已存在，应改用新的分支名，后续推送及 PR 命令保持一致。发起 PR 后，将链接交给维护者审核；后续修改继续提交并推送到同一分支，PR 会自动更新。由维护者决定是否合并。
