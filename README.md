# NineSkyLabelImg

## 简介

NineSkyLabelImg 是一款基于 [LabelImg](https://github.com/tzutalin/labelImg) 修改的图像标注工具，专门针对 YOLO 格式进行了优化。

## 主要功能

### 保留功能
- 图像标注（矩形框）
- 支持 YOLO、PascalVOC、CreateML 格式（但默认仅启用 YOLO）
- 快捷键支持（D/A 切换图片，W 创建框等）
- 预定义类别加载

### 新增/修改功能

1. **默认 YOLO 格式**
   - 软件启动默认使用 YOLO 格式
   - 禁用了格式切换按钮（其他格式保留但默认不启用）

2. **自动保存**
   - 默认开启自动保存模式
   - 切换图片时自动保存标注

3. **图片目录保存**
   - 标注文件默认保存到与图片相同的目录
   - 禁用了"更改保存目录"按钮

4. **YAML 配置文件**
   - 设置文件从 `.pkl` 改为 `.yaml` 格式
   - 位置：`~/.NineSkyLabelImgSettings.yaml`
   - 可直接用文本编辑器查看和修改

5. **启动日志**
   - 启动时显示版本号和设置加载信息

6. **优化 UI**
   - 禁用了"打开文件"按钮（仅支持打开目录）
   - 简化了工作流程

## 安装

### 依赖
```bash
pip install pyqt5 lxml pyyaml
```

### 编译资源文件
```bash
pyrcc5 -o libs/resources.py resources.qrc
```

### 运行
```bash
python NineSkyLabelImg.py
```

## 快捷键

| 按键 | 功能 |
|------|------|
| Ctrl+U | 打开图片目录 |
| Ctrl+S | 保存 |
| Ctrl+D | 复制当前标注 |
| W | 创建矩形框 |
| D | 下一张图片 |
| A | 上一张图片 |
| Del | 删除选中框 |
| Space | 标记图片为已验证 |

## 使用方法

1. 运行软件
2. 点击菜单 **File → Open Dir** (Ctrl+U) 选择图片目录
3. 点击 **Create RectBox** 或按 W 开始标注
4. 按 D 切换下一张图片（自动保存）
5. 标注文件 `.txt` 保存在图片同目录下
