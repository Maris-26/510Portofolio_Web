# Haichao Xing Photography Portfolio

这是一个极简风格的摄影作品集网站，适合展示个人摄影主题和作品。左侧为主题导航，右侧为大图展示，点击图片可切换同主题下的照片。

## 目录结构

```
510Portofolio_Web/
├── app.py
├── README.md
└── static/
    └── photos/
        ├── Sakura-1.jpg
        ├── Sakura-2.jpg
        ├── Muse-1.jpg
        ├── Muse-2.jpg
        ├── Botanica-1.jpg
        ├── Botanica-2.jpg
        ├── Pier-1.jpg
        └── Pier-2.jpg
```

## 如何添加/替换图片
1. 将你的图片放入 `static/photos/` 文件夹。
2. 命名方式需与 `app.py` 中一致，例如：`Sakura-1.jpg`、`Muse-2.jpg` 等。
3. 每个主题下两张图片，按需替换即可。

## 运行方法
1. 安装依赖（建议使用虚拟环境）：
   ```bash
   pip install flask
   ```
2. 启动网站：
   ```bash
   python app.py
   ```
3. 在浏览器访问：
   ```
   http://127.0.0.1:5001/
   ```

## 自定义主题和图片
- 在 `app.py` 的 `portfolio_groups` 列表中修改主题名称、图片路径即可。
- 支持本地图片（推荐 jpg/png），也可用网络图片链接。

## 特色说明
- 极简白色背景，左侧导航不换行，图片自适应居中展示。
- 点击图片可切换同主题下的下一张。
- 支持自定义主题数量和图片数量。

---
如有更多美化或功能需求，欢迎随时联系作者或继续优化！ 