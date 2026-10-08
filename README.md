# UI Design Skill

用于维护我们自己的 UI Design Skill，以及它引用的第三方设计工程 Skills。

## 使用

自有入口为 [ui-design/SKILL.md](ui-design/SKILL.md)。它结合完整中文版设计规范与内置 Jakub Skills，按请求进行设计、实现、改进、审查或参考网页解析。

它采用按需加载：小任务只读相关领域，完整审查才覆盖全部领域。审查和解析保持只读，实施遵循用户指定范围。

Codex 安装（使用内置 Skill Installer）：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Michel-Johnson/ui-design-skill --path ui-design
```

安装后下一轮可使用：

```text
$ui-design 改进当前页面，沿用现有 Token 和组件，并验证相关状态。
$ui-design 分析 https://example.com 的渐变是如何实现的。
$ui-design 审查当前未提交变更中的界面问题。
```

安装整个 `ui-design/` 目录即可包含上游参考和许可证，无需单独安装 13 个上游 Skills。该安装命令不会覆盖同名已安装目录。

## 结构

```text
ui-design/
  SKILL.md                    自有入口与领域路由
  agents/openai.yaml          Codex 展示信息
  references/
    design-standards.md        完整中文版设计规范
    workflow.md                自有工作流与冲突处理
    upstream.json              上游版本与完整性摘要
  scripts/verify_bundle.py     离线验证上游文件与相对引用
  vendor/jakub/
    LICENSE                   上游 MIT 许可证
    skills/                   13 个原样 Skills 及参考文件
```

## 来源与版权

`ui-design/vendor/jakub/skills/` 中全部文件来自 [jakubkrehel/skills](https://github.com/jakubkrehel/skills)，作者为 Jakub Krehel。介绍页面：[jakub.kr/skills](https://jakub.kr/skills)。这些文件是第三方原作，不属于本仓库原创内容。

- 上游分支：`main`
- 上游 commit：`d574cc8a576dc24256ad38268b8d03d86724a1b3`
- 快照日期：2026-10-08（Asia/Shanghai）
- 许可证：MIT；原版权及许可全文保留在 [ui-design/vendor/jakub/LICENSE](ui-design/vendor/jakub/LICENSE)。
- 本次未修改导入文件。

自有入口、路由与工作流由本仓库维护；[完整设计规范](ui-design/references/design-standards.md)源自此前整理的 Design UI SP，并在末尾保留 Jakub 博客的参考链接。其用途与上游快照分开标注。

## 导入内容

- better-interface
- better-ui
- better-typography
- better-colors
- better-accessibility
- better-layout
- better-writing
- interface-review
- explain-interface
- break
- build-design
- state-machine
- variant

导入目录保留了各 Skill 的参考文件及 `agents/openai.yaml`，并保留它们之间的相对路径关系。

## 验证与更新

```bash
python3 ui-design/scripts/verify_bundle.py
```

该检查验证 13 个上游 Skills、65 个上游文件、固定 SHA-256 摘要和本地 Markdown 引用；它不证明所有运行环境上的实际 UI 行为。

更新上游时，从指定 commit 原样导入 `skills/` 与 `LICENSE`，核对差异后更新 `references/upstream.json` 中的版本与摘要及本 README。自有入口与上游规则有变化时重新检查路由和冲突处理。正常调用不自动联网更新上游快照。
