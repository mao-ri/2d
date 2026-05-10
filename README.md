# 2D Geometry Editor（工业设计软件与计算几何基础大作业）

## 项目简介
本项目是一个基于 Python + PyQt5 的二维几何编辑器，实现了基础的CAD风格绘图功能，包括点、线、曲线的创建、编辑与删除。

---

## 功能说明

### ✔ 已实现功能

- 点的创建（左键点击空白区域）
- 线段绘制（点击两个点自动连接）
- 曲线绘制（点击3个点生成贝塞尔曲线）
- 点拖拽移动
- 线段删除（右键点击线段）
- 网格背景辅助绘图
- 清空画布
- JSON保存（points + lines）

---

## 技术实现

### 几何逻辑层
- Point（点）
- Line（线）
- Curve（曲线）
- 选点逻辑
- 拖拽逻辑
- 距离计算（点到线）

### GUI层（PyQt5）
- QWidget画布
- QPainter绘图
- 鼠标事件处理
- 实时刷新

---

## 运行方式

```bash
python main.py
```

## 项目结构

```text
2d/
│── main.py
│── main_window.py
│── canvas.py
│── point.py
│── line.py
│── curve.py
│── scene.json
```
## GitHub 仓库

https://github.com/mao-ri/2d