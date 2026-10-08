---
name: ui-design
description: 设计、实现、改进或审查产品 UI；结合项目约束、自有设计规范与内置 Jakub Skills，按需处理布局、排版、颜色、无障碍和动效。也支持用户明确要求的参考网页解析、设计稿还原、组件方案探索及状态验证。
---

# UI Design

把用户的产品目标转成可实现、可验证的界面。先理解主要任务、使用频率、真实内容与现有系统，再决定该增加、复用或删除什么。

## 先确定任务

读取与当前界面有关的项目约定、组件、Token、数据边界、预览和验证命令。根据用户请求区分设计、实现、改进、审查或解析；审查和解析默认只读，实施只修改用户要求的范围。

如果用户给出设计稿，明确是否要求忠实还原；如果用户给出喜欢的网站，明确是在解释实现还是迁移设计机制。只解释一个效果时，不扩展成整个网站的审计。

## 按需引用 Jakub Skills

下表路径相对于本文件。先读取选中的完整 `SKILL.md`，然后根据它的路由读取相关参考。不要默认加载全部 13 个 Skills。

| 任务 | 入口 |
| --- | --- |
| 布局、分组、响应式、RTL | [better-layout](vendor/jakub/skills/better-layout/SKILL.md) |
| 字体、字号体系、换行、数字 | [better-typography](vendor/jakub/skills/better-typography/SKILL.md) |
| 色板、语义 Token、渐变、对比度测量 | [better-colors](vendor/jakub/skills/better-colors/SKILL.md) |
| 键盘、Focus、ARIA、表单、Reduced Motion | [better-accessibility](vendor/jakub/skills/better-accessibility/SKILL.md) |
| 圆角、表面、图标、交互动效 | [better-ui](vendor/jakub/skills/better-ui/SKILL.md) |
| 按钮、错误、空状态及产品文案 | [better-writing](vendor/jakub/skills/better-writing/SKILL.md) |
| 整体界面审查 | [better-interface](vendor/jakub/skills/better-interface/SKILL.md) |
| 用户要求审查分支、PR、范围或未提交变更 | [interface-review](vendor/jakub/skills/interface-review/SKILL.md) |
| 用户要求解释网站或视觉效果如何实现 | [explain-interface](vendor/jakub/skills/explain-interface/SKILL.md) |
| 根据设计稿实现 UI | [build-design](vendor/jakub/skills/build-design/SKILL.md) |
| 用户要求探索组件的多种方案 | [variant](vendor/jakub/skills/variant/SKILL.md) |
| 用户要求搭建组件状态工作台 | [state-machine](vendor/jakub/skills/state-machine/SKILL.md) |
| 用户要求压力验证组件 | [break](vendor/jakub/skills/break/SKILL.md) |

这些入口是随本 Skill 安装的本地参考。上游提到另一 Skill 的名称时，在 `vendor/jakub/skills/<name>/SKILL.md` 解析它；其余相对链接仍相对于那个文件。无需用户另行安装或输入同名命令。

上游标记为 user-invoked 的工作流，只有用户明确要求对应任务时才选择。用户通过 `$ui-design 审查当前 diff`、`$ui-design 分析这个网页` 等表达任务时，直接读取对应入口执行；普通设计任务不自动开展这些工作流。变更审查先读取 `interface-review`，由它解析范围，再读取 `better-interface` 汇总。

## 自有规范如何补充

[设计规范](references/design-standards.md)保留原有完整 SP，作为领域索引和补充依据。只读当前任务涉及的章节：

- 设计决策与复用：1；AI 辅助实现：17。
- 布局、响应式、排版、色彩和表面：2–9、16；领域细则以对应 Jakub Skill 为准。
- 手势与 Shared Layout：11–12；结合 `better-ui` 的动效规则。
- 性能、Locale 和交付验证：14–15、18；结合项目实际约束。

[工作流与冲突处理](references/workflow.md)用于从零设计、参考迁移、实现及规范之间的取舍。

用户的明确要求决定任务和授权；现有设计系统决定品牌、密度与实现方式。旧 SP 中的数值是没有项目规范时的起点，不是硬性判分标准。Jakub 最新领域细则补充旧 SP 的细节；发现会影响任务完成或可访问性的冲突，给出证据及最小修正方案。忠实还原设计稿时，遵循 `build-design` 报告冲突，不自行重新设计。

## 验证与交付

按任务风险验证有关状态、视口、输入方式和内容变化。记录实际运行的命令或检查，以及无法检查的内容。代码阅读不能证明视觉效果，截图不能证明键盘与屏幕阅读器行为。

- 设计：交付信息层级、关键状态、Token/组件映射和需要取舍的决策。
- 实现或改进：交付改动、预览或产物、验证结果及剩余差异。
- 审查或解析：使用所选 Jakub 入口的证据与输出格式；只对实际检查过的范围下结论。
- 方案或状态工作台：交付可访问的预览、方案/状态及操作方式，按上游规则保留临时页面供用户使用。

## 来源与维护

内置参考来自 Jakub Krehel 的 [jakubkrehel/skills](https://github.com/jakubkrehel/skills)，原样保留，许可证见 [MIT License](vendor/jakub/LICENSE)，快照版本见 [upstream.json](references/upstream.json)。此入口及工作流是本仓库维护的补充。

维护或安装后可运行 `python3 scripts/verify_bundle.py`（相对于本 Skill 目录），检查上游副本完整性与本地引用。
