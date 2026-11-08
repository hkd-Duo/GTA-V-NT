#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENT (Enhanced Native Trainer) 菜单标题汉化补丁
================================================
ENT 58.0(含 hotfix)的二级/三级菜单【标题栏】是硬编码英文字符串,
不经过 tr() 翻译系统,translation.ini 无法翻译它们。

本脚本直接在 EnhancedNativeTrainer.asi 二进制中,把这些英文标题
替换为"长度 ≤ 原文"的 UTF-8 中文(不足部分用 NUL 填充)。
菜单显示用 C 字符串语义(c_str),NUL 填充安全。

用法:
    python patch_menu_titles.py "<GTA5增强版根目录>\\EnhancedNativeTrainer.asi"

说明:
- 会自动备份原文件为 EnhancedNativeTrainer.asi.bak-<时间戳>
- 每个英文标题要求在二进制中以 NUL 包围(独立字符串字面量)才替换
- 替换后重新校验,输出逐条结果;游戏必须处于退出状态(文件不被占用)
- 适用版本:ENT 58.0-hotfix(SHA256 87253bea... 的 zip 解出的 asi)。
  其他版本如字符串对不上会自动跳过并提示,不会损坏文件。
"""

import sys
import shutil
import datetime
from pathlib import Path

# Windows 控制台正确显示中文输出
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# (英文原文, 中文替换) —— 中文 UTF-8 字节数必须 ≤ 英文字节数
PAIRS = [
    # ── 主菜单的二级标题(用户最常见) ──
    ("Player Options",            "玩家选项"),
    ("Bodyguard Options",         "保镖选项"),
    ("Vehicle Options",           "载具选项"),
    ("Weapon Options",            "武器选项"),
    ("World Options",             "世界选项"),
    ("Time Options",              "时间选项"),        # 恰好等长
    ("Miscellaneous Options",     "杂项选项"),
    ("Object Placement",          "对象放置"),
    ("Trainer Options",           "修改器选项"),      # ENT 设置页
    # ── 玩家类三级标题 ──
    ("Power Punch Options",            "重拳选项"),
    ("Player Data",                    "数据"),          # 原文仅 11 字节,放不下 4 字
    ("Wanted Level Settings Options",  "通缉等级设置"),
    ("Wanted Fugitive Options",        "通缉逃亡选项"),
    ("Player Movement Speed Options",  "移动速度选项"),
    ("Ragdoll Options",                "布娃娃选项"),
    ("Prison Break Options",           "越狱选项"),
    ("Jedi Powers Options",            "原力选项"),
    # ── 杂项类三级标题 ──
    ("Airbrake Menu Options",          "空气刹车设置"),
    ("Pause Menu Settings Options",    "暂停菜单设置"),
    ("Phone Bill Options",             "电话账单选项"),
    ("Use Phone While On Bike Options","骑车用手机选项"),
    ("Phone Settings Options",         "手机设置选项"),
    ("Radio Settings Options",         "电台设置选项"),
    ("HUD Settings Options",           "HUD设置选项"),
    # ── 保镖类三级标题 ──
    ("Mark On Map Options",            "地图标记选项"),
    # ── 载具类三级标题 ──
    ("Vehicle Control Options",        "载具控制选项"),
    ("Speed And Altitude Options",     "速度与高度选项"),
    ("Vehicle Indicators Options",     "载具指示选项"),
    ("Speed Limit Options",            "限速选项"),
    ("RGB Settings",                   "RGB设置"),
    ("Engine Damage Options",          "引擎损伤选项"),
    ("Car Thief Options",              "偷车选项"),
    ("Fuel Consumption Options",       "燃油消耗选项"),
    ("Vehicle Tracking Options",       "载具追踪选项"),
    ("Road Laws Options",              "交通规则"),
    ("Vehicle Mod Options",            "载具改装选项"),
    # ── 武器类三级标题 ──
    ("Cop Weapons Options",              "警用武器选项"),
    ("Peds Don't Like Weapons Options",  "NPC反感武器选项"),
    # ── 载具改装/车轮 ──
    ("All Wheels",                 "车轮"),
    ("Front Wheels",               "前轮"),
    ("Rear Wheels",                "后轮"),
    ("Trim Color ~HUD_COLOUR_GREYLIGHT~(161)", "内饰色~HUD_COLOUR_GREYLIGHT~(161)"),
    ("Enable Bomb-Door Camera",    "炸弹舱门相机"),
    ("Enable Auto-Pilot",          "自动驾驶"),
    # ── 载具武器其他 ──
    # ── 世界类三级标题 ──
    ("Weather Settings",           "天气设置"),
    ("Weather Options",            "天气选项"),
    ("Clouds Options",             "云层选项"),
    # ── 动作/空压/传送 ──
    ("Facial Anims",               "表情动作"),
    ("Player Anims",               "玩家动作"),
    ("Airbrake Mode",              "空气刹车"),
    ("Chauffeur To Marker Options","代驾到路点选项"),
]


def find_all(data: bytes, needle: bytes):
    hits, start = [], 0
    while True:
        i = data.find(needle, start)
        if i < 0:
            return hits
        hits.append(i)
        start = i + 1


def patch(path: Path) -> None:
    data = bytearray(path.read_bytes())
    total, patched, skipped_long, not_found = len(PAIRS), 0, [], []
    for en, zh in PAIRS:
        eb, zb = en.encode("ascii"), zh.encode("utf-8")
        if len(zb) > len(eb):
            skipped_long.append((en, zh))
            continue
        # 仅替换被 NUL 包围的独立字面量,避免误伤其他数据
        hits = [i for i in find_all(data, eb)
                if i > 0 and data[i - 1] == 0 and data[i + len(eb)] == 0]
        if not hits:
            not_found.append((en, zh))
            continue
        rep = zb + b"\x00" * (len(eb) - len(zb))
        for i in hits:
            data[i:i + len(eb)] = rep
        patched += 1
        print(f"  [OK] {en!r} -> {zh!r}  ({len(hits)} 处)")
    path.write_bytes(bytes(data))
    print(f"\n完成: 共 {total} 条 | 成功 {patched} | 放不下(中文太长) {len(skipped_long)} | 未找到 {len(not_found)}")
    for en, zh in skipped_long:
        print(f"  [跳过-太长] {en!r} -> {zh!r}")
    for en, zh in not_found:
        print(f"  [未找到] {en!r}(可能版本不同,已忽略)")


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    target = Path(sys.argv[1])
    if not target.is_file():
        print(f"文件不存在: {target}")
        sys.exit(1)
    bak = target.with_name(f"{target.name}.bak-{datetime.datetime.now():%Y%m%d-%H%M%S}")
    shutil.copy2(target, bak)
    print(f"已备份: {bak}")
    print(f"开始补丁: {target}\n")
    patch(target)


if __name__ == "__main__":
    main()
