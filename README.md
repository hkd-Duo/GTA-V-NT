# GTA V 增强版 ENT 汉化包(Enhanced Native Trainer 中文翻译)

为 **GTA5 增强版(Enhanced)** 的内置修改器 **ENT(Enhanced Native Trainer)** 提供的完整简体中文翻译,基于 ENT 官方 `translation.ini` 翻译机制制作,**不修改任何游戏文件、不含任何可执行文件**,纯文本翻译,覆盖 ENT 全部 966 个内置翻译键。

> ✅ 已在 GTA5 增强版 `1.0.1158.16` + ENT `58.0-hotfix` + ScriptHookV `3889.0` 上完整验证通过。
> ⚠️ 仅限**单机故事模式**使用!携带修改器进入线上模式(GTA Online)属于作弊行为,有封号风险。

---

## 📋 版本适配表

| 组件 | 版本 | 发布日期 | SHA256 校验 |
|---|---|---|---|
| GTA V 增强版(游戏) | 1.0.1158.16(Steam,appid 3240220) | — | — |
| ENT(修改器) | 58.0 Hotfix 1 | 2026-08-07 | `87253bea2c047ba4d89c98ca7599d4573bc4dd71c3e6d265ac984d283cbadbb1`(zip) |
| ENT(修改器) | 58.0 | 2026-07 | `4b4a5733fdf3a81656ba0eeeb20c173957f7bb60fcc9c154ab780ab62d75bc98`(zip) |
| ScriptHookV | v3889.0 / 1158.13 | 2026-07-15 | `b64c97c3353906f14621e7e9511e4aec2a7d436ecc21ed124d3816585e2e6188`(zip) |
| ScriptHookV.dll(装后) | — | — | `126be57ca9dca00e471f9de611766009c900aad88f89ae6c2926ec62e5aaeb4f` |
| asi loader dinput8.dll | SHV bin 自带 | — | `9fd9e02353b7d39fe07b9667f7ea2697229a7f2d0e7d389eb79eb212b1bb181d` |
| asi loader xinput1_4.dll | SHV bin 自带 | — | `a1a8bde409ed75d94a0439c37cf881bc354b13c2f8cd32e4bef3b10f308f1392` |

**适配说明:**

- 本汉化基于 ENT 58.0-hotfix 的翻译键制作,通过二进制扫描确认**覆盖该版本 .asi 内置的 100% 翻译键**(966/966)。
- ENT 后续版本若新增菜单条目,缺失的键会在游戏内**自动回退英文**(不影响使用),也可自行在 `translation.ini` 补翻译。
- ScriptHookV 必须选择**支持增强版**的版本(文件名带 `1158.xx` 字样);传承版(Legacy)的 SHV 与增强版不通用。

## 📦 目录结构

```
GTA-V-NT/
├── README.md                    ← 本说明书
├── translation/
│   └── translation.ini          ← 简体中文翻译文件(UTF-8)
├── tools/
│   └── gen_translation.py       ← 翻译生成脚本(键值表内嵌,可自定义后重跑)
└── screenshots/                 ← 游戏内汉化效果截图
```

## 🚀 安装步骤

### 第一步:安装 ScriptHookV + ENT(已装过可跳过)

把以下 5 个文件放进游戏根目录(`...\steamapps\common\Grand Theft Auto V Enhanced\`):

| 文件 | 来源 |
|---|---|
| `dinput8.dll` | ScriptHookV 压缩包 `bin\` 目录 |
| `xinput1_4.dll` | ScriptHookV 压缩包 `bin\` 目录 |
| `ScriptHookV.dll` | ScriptHookV 压缩包 `bin\` 目录 |
| `EnhancedNativeTrainer.asi` | ENT 压缩包根目录 |
| `args.txt`(内容:`-nobattleye -noBE`) | 自建,用于关闭 BattlEye(见 FAQ) |

> ⚠️ **增强版关键区别**:增强版(DX12)**不会加载 `dinput8.dll`**,必须同时放 `xinput1_4.dll` 才能激活 asi loader!只放 dinput8 会出现"游戏能进但修改器无效"的现象。
> 不要安装 SHV 自带的 `NativeTrainer.asi`,它和 ENT 会冲突。
> ENT 压缩包里的 `Enhanced Native Trainer\` 文件夹(载具预览图)也要复制到游戏根目录。

### 第二步:安装汉化(核心)

把 [`translation/translation.ini`](translation/translation.ini) 复制到:

```
...\Grand Theft Auto V Enhanced\Enhanced Native Trainer\translation.ini
```

(即 ENT 的 `Enhanced Native Trainer` 文件夹内,与 `ent-config.xml` 同目录。)

- 必须是 **UTF-8 无 BOM** 编码;
- **游戏运行时该文件被占用无法覆盖**,请先完全退出游戏再复制;
- 启动游戏 → 进故事模式 → 按 **F4**,菜单即为简体中文。

## 🎮 按键操作

| 操作 | 按键 |
|---|---|
| 呼出/关闭菜单 | **F4** |
| 上下选择 | 小键盘 **2 / 8**(或方向键) |
| 确认 | 小键盘 **5**(或回车) |
| 返回上一级 | 小键盘 **0** 或 **退格 Backspace** |
| 输入框确认/取消 | **Enter** 确认,**退格**取消 |

## ❓ 常见问题(FAQ)

**Q:启动游戏十几秒就退出?**
直接双击 `GTA5_Enhanced.exe` 会被 Steam DRM 接管重启,属正常现象。请**通过 Steam 启动**游戏。

**Q:按 F4 没反应 / 修改器无效?**
1. 确认游戏根目录有 `xinput1_4.dll`(增强版必须有,见上文);
2. 查看 `ScriptHookV.log`:出现 `INIT: Success, game version is VER_EN_1_0_1158_13` 且 `Registering script 'EnhancedNativeTrainer.asi'` 才算加载成功;
3. 游戏版本更新后 SHV 报版本不支持 → 去官网等新版 ScriptHookV。

**Q: BattlEye 弹窗拦截?**
在游戏根目录建 `args.txt`,内容一行:`-nobattleye -noBE`(asi loader 会把它注入启动参数)。此法仅适合单机游玩。

**Q:部分菜单条目还是英文?**
`translation.ini` 缺少该键,ENT 会回退英文。若因 ENT 升级新增了条目,可手动在 ini 对应 Section 补一行 `键名=中文`,格式与现有行一致即可。

**Q:想恢复默认/重置 ENT 设置?**
在游戏根目录新建**空文件** `ENT-RESET`,下次启动 ENT 会重置全部配置。

**Q:游戏语言必须是中文吗?**
是。ENT 菜单用游戏自身字体渲染,**游戏语言设为简体中文**(Steam → 右键游戏 → 属性 → 语言)才能显示汉字,否则中文会显示为方块。本汉化包验证时游戏语言为 `schinese`。

## 📸 汉化效果截图

<!-- 在游戏内按 F12 截图,把图片放进 screenshots/ 后取消下面注释
![主菜单](screenshots/main-menu.png)
![玩家菜单](screenshots/player-menu.png)
![杂项菜单](screenshots/misc-menu.png)
![载具菜单](screenshots/vehicle-menu.png)
-->

## 🛠 自定义 / 二次翻译

`tools/gen_translation.py` 内嵌全部 981 条键值映射,修改翻译表后运行即可重新生成 `translation.ini`(生成规则:占位符 `%02d`/`%d` 与颜色标记 `~r~`、`~HUD_COLOUR_~` 必须原样保留)。

## 🙏 致谢

- [ENT - Enhanced Native Trainer](https://www.gta5-mods.com/tools/enhanced-native-trainer) — Zemanez & Others,维护:[FIying-Scotsman](https://github.com/FIying-Scotsman/GTAV-EnhancedNativeTrainer)
- [ScriptHookV](http://www.dev-c.com/gtav/scripthookv/) — Alexander Blade
- 简体中文翻译:基于 ENT 官方 `tr()` 翻译机制逐键人工校对制作

## 📄 许可

本仓库**仅包含翻译文本与文档**,不含 ENT、ScriptHookV 或游戏本体的任何二进制文件;相关权利归原作者所有。请在合法购买的游戏上、仅于单机模式使用。
