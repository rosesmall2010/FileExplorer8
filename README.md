<p align="center">
  <img src="images/icon-1024.png" width="128" alt="文件8">
</p>

<h1 align="center">文件8</h1>

<p align="center"><strong>macOS 原生文件管理器 · 文件管理器 / 双栏 / 四栏三种形态同窗切换</strong></p>

<p align="center">一套文件操作内核，三种交互范式 · 写操作先预检 · 三级撤销 · 万项目录也不卡</p>

<p align="center">
  <a href="https://rosesmall2010.github.io/FileExplorer8/"><img src="https://img.shields.io/badge/%E6%94%AF%E6%8C%81%E9%A1%B5-blue" alt="Site"></a>
  <a href="privacy.html"><img src="https://img.shields.io/badge/%E9%9A%90%E7%A7%81%E6%94%BF%E7%AD%96-green" alt="Privacy"></a>
  <img src="https://img.shields.io/badge/version-1.1.6-lightgrey" alt="Version">
</p>

<p align="center"><strong>简体中文</strong> · <a href="README.zh-Hant.md" hreflang="zh-Hant" lang="zh-Hant">繁體中文</a> · <a href="README.en.md" hreflang="en" lang="en">English</a> · <a href="README.ja.md" hreflang="ja" lang="ja">日本語</a> · <a href="README.ko.md" hreflang="ko" lang="ko">한국어</a> · <a href="README.de.md" hreflang="de" lang="de">Deutsch</a> · <a href="README.fr.md" hreflang="fr" lang="fr">Français</a> · <a href="README.es.md" hreflang="es" lang="es">Español</a> · <a href="README.pt-BR.md" hreflang="pt-BR" lang="pt-BR">Português (Brasil)</a> · <a href="README.ru.md" hreflang="ru" lang="ru">Русский</a> · <a href="README.vi.md" hreflang="vi" lang="vi">Tiếng Việt</a> · <a href="README.id.md" hreflang="id" lang="id">Bahasa Indonesia</a> · <a href="README.ms.md" hreflang="ms" lang="ms">Bahasa Melayu</a> · <a href="README.th.md" hreflang="th" lang="th">ไทย</a></p>

---

## 这是什么

文件8 是一个在 macOS 上独立运行的**文件管理器**，把「文件管理器」「双栏管理器」「四栏管理器」三种交互范式装进同一个窗口，按 `⇧⌘D` 一步循环切换。三种形态各自保存现场——路径、标签、排序方式、列宽、选中项，来回切都不丢。

它不是 Finder 的替代品，也不是另一个 Finder 皮肤。它补的是 Finder 缺的那一块：**双手在键盘上的批量搬运**。

参照系是经典的双栏文件管理器范式：不设默认打开程序、不做 Finder 扩展、不读写 Finder 偏好。唯一共享的东西是文件系统本身。所以它可以和 Finder 长期并存，不会互相打架。

---

## 界面

### 文件管理器：网格视图与详情面板

![文件管理器：网格视图与详情面板](images/readme/01-explorer.png)

### 双栏管理器：源与目标两栏

![双栏管理器：源与目标两栏](images/readme/02-dual-pane.png)

### 四栏管理器：田字 2×2 布局

![四栏管理器：田字 2×2 布局](images/readme/03-quad-pane.png)

---

## 特性

### 写操作先预检，绝不瞎写

复制、移动、覆盖之前先做一次 dry-run：目标是否可写、磁盘空间够不够、有哪些文件名冲突，全部先摆给你看。**这一步不写任何字节。**

四种冲突策略任选：替换（先备份，支持撤销）、两者都保留、跳过、逐条询问。冲突不超过 5 条时可以逐条决定。

进度有实时速度、已传 / 总量 / 剩余；结束后给一份完整的账——成功几项、跳过几项、失败几项，失败清单逐个列出文件名与原因。

### 三级撤销

同卷移动、重命名、删除到废纸篓、打包与解压 ZIP **保证 100% 可撤销**。复制与跨卷移动尽力而为。不可撤销的操作执行前二次确认。

### 六种视图与专业预览

超大 / 大 / 中 / 小图标、列表、详细信息。图标按真实像素分档（256 / 128 / 64 / 32），高分屏上不糊边。

按 `Space` 快速预览，`←` / `→` 与 `PgUp` / `PgDn` 连续翻：

- 文本与源码走只读等宽视图，带 50 多种语言的语法着色与行号
- PDF 走 PDFKit
- 图片等比缩放整张装进面板
- 富格式交给系统 Quick Look
- 预览不了的，直接给简介

### 打包与解压

**打包为 ZIP**：ZIP64、可调压缩级别、已压缩格式自动跳过、可选择是否跟随符号链接，打包结果可撤销。

**双击即解压**，行为与 Finder 一致：单一顶层目录不套壳、冲突整包改名、只清理 `__MACOSX`，还原 Unix 权限位。

### SSH 远端目录

内置 SSH / SFTP：用密码或任意路径的私钥连服务器，远端目录和本地目录一样浏览、复制、删除、改名、撤销，走同一条写管线。

标签栏用网络盘图标加红绿状态表示连接情况，断线可一键重连。**密码可以不保存**，改为每次连接弹一次性登录框。远端文件 10 MB 以内也能快速预览。

### 细节

- Finder 七色标签，支持多标签叠加，取消全部标签时保留自定义文字标签
- 命令面板 `⌘K`，按匹配度 → 最近使用 → 字母序排序
- 路径三件套：复制路径、复制所在目录路径、复制文件名，外加「在终端中打开」
- 计算校验和：SHA-256 / SHA-512 / SHA-1 / MD5 / BLAKE3 / CRC32 / CRC64
- 宗卷自动发现：U 盘、移动硬盘、已挂载的磁盘映像自动出现，可一键弹出
- 会话恢复：窗口位置、标签、列宽、排序、两栏比例都记住；崩溃后能恢复排队中的写任务
- 与 Finder 双向复制粘贴，三个方向拖放打通
- 语言切换在菜单栏一级「语言」菜单，一步可到，切换立即生效

### 14 种语言

简体中文、繁体中文、英文、日文、韩文、德文、法文、西班牙文、巴西葡萄牙文、俄文、越南文、印尼文、马来文、泰文。

泰文单独实现了一套排序规则——前置元音、声调符号、脚本次序都不是码位序，按码位排会乱。

---

## 隐私

**不收集任何数据。** 没有账号，没有统计分析，没有广告 SDK，没有崩溃上报。

除你主动发起的 SSH 连接外，应用不向任何服务器发送任何字节。你的文件、浏览记录、服务器凭据都只留在你自己的 Mac 上：密码与私钥口令存在系统钥匙串，私钥文件始终留在你放它的地方。

应用开启 App Sandbox，只在你授予的目录范围内读写，不申请通讯录、摄像头、麦克风、屏幕录制或完全磁盘访问。

[详见隐私政策](privacy.html)

---

## 支持

遇到问题、想提建议、或者发现 bug？

- 打开[支持页面](https://rosesmall2010.github.io/FileExplorer8/)查看常见问题
- 在 [Issues](https://github.com/rosesmall2010/FileExplorer8/issues) 里提交，附上 macOS 版本、文件8 版本号与复现步骤

版本号在「文件8 › 关于文件8」里可以看到。

### 常见问题

**为什么进入某些目录会弹窗要求授权？**
应用开启了 App Sandbox。桌面、下载、文稿、外接磁盘等位置在沙盒之外，首次进入某个目录时 macOS 会强制弹窗询问，这是系统的安全设计，不是缺陷。选择「授权此文件夹」后，该目录会被记住，同一路径一次运行只问一次。

**会不会读取我的通讯录、摄像头或屏幕？**
不会。文件8 只申请了用户选择的文件访问、标准文件夹（下载 / 文稿 / 音乐 / 图片 / 影片）与出站网络访问，没有通讯录、摄像头、麦克风、屏幕录制或完全磁盘访问权限。

**SSH 密码存在哪里？**
存在 macOS 系统钥匙串里。服务器端点信息存在本机沙盒容器内（AES-256-GCM 加密）。密码可以不保存，改为每次连接时弹一次性登录框。详见<a href="privacy.html">隐私政策</a>。

**支持 Apple Silicon 和 Intel 吗？**
两者都支持，安装包是通用二进制。系统要求 macOS 15.0 或更高版本。

**卸载后残留数据怎么清理？**
删除应用后，再删除 <code>~/Library/Containers/com.donghuazhu.FileExplorer8/</code> 即可清空偏好、会话记录与服务器端点信息（沙盒应用的数据都在你自己的容器里，不在系统共享位置）。SSH 密码存在系统钥匙串，删除对应连接时会一并删除。

---

## 系统要求

- macOS 15.0 或更高版本
- Apple Silicon 或 Intel 芯片（通用二进制）

---

<p align="center"><sub>macOS 是 Apple Inc. 的商标。本应用与 Apple Inc. 无关联。</sub></p>
