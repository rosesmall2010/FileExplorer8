# 文件8 / FileExplorer8 — 支持与隐私

这个仓库只放 **App Store 审核与用户支持**所需的公开文件，不含应用源码。

- 源码仓库：<https://github.com/rosesmall2010/xmfinder8>

## 内容

| 路径 | 说明 |
| --- | --- |
| `index.html` | 支持页面：常见问题、功能概览、应用截图 |
| `privacy.html` | 隐私政策（中文正文 + 英文摘要） |
| `images/` | 应用截图，2560×1600 |

## 用途

Mac App Store 上架时，App Store Connect 要求填两个**可公开访问**的网址：

| 字段 | 值 |
| --- | --- |
| 支持 URL | `https://rosesmall2010.github.io/FileExplorer8/` |
| 隐私政策 URL | `https://rosesmall2010.github.io/FileExplorer8/privacy.html` |

两个页面都是纯静态 HTML，无外部依赖、无脚本、无跟踪代码，改完直接提交即可生效。

## 更新方式

页面内容与源码仓库里的 `docs/PRIVACY.md` 保持一致。修改隐私政策时两处都要同步：
源码仓库那份供开发查阅，本仓库这份对外公开并作为审核链接。

本地预览：

```bash
python3 -m http.server 8000
# 打开 http://localhost:8000/
```
