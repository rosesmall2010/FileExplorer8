<p align="center">
  <img src="images/icon-1024.png" width="128" alt="FileExplorer8">
</p>

<h1 align="center">FileExplorer8</h1>

<p align="center"><strong>Native macOS file manager · File manager / dual-pane / quad-pane, one window</strong></p>

<p align="center">One file-operation core, three interaction models · Dry-run before every write · Three-tier undo · No lag on huge folders</p>

<p align="center">
  <a href="https://rosesmall2010.github.io/FileExplorer8/"><img src="https://img.shields.io/badge/Support-blue" alt="Site"></a>
  <a href="https://rosesmall2010.github.io/FileExplorer8/privacy.en.html"><img src="https://img.shields.io/badge/Privacy-green" alt="Privacy"></a>
  <img src="https://img.shields.io/badge/version-1.1.6-lightgrey" alt="Version">
</p>

<p align="center"><a href="README.md" hreflang="zh-Hans" lang="zh-Hans">简体中文</a> · <a href="README.zh-Hant.md" hreflang="zh-Hant" lang="zh-Hant">繁體中文</a> · <strong>English</strong> · <a href="README.ja.md" hreflang="ja" lang="ja">日本語</a> · <a href="README.ko.md" hreflang="ko" lang="ko">한국어</a> · <a href="README.de.md" hreflang="de" lang="de">Deutsch</a> · <a href="README.fr.md" hreflang="fr" lang="fr">Français</a> · <a href="README.es.md" hreflang="es" lang="es">Español</a> · <a href="README.pt-BR.md" hreflang="pt-BR" lang="pt-BR">Português (Brasil)</a> · <a href="README.ru.md" hreflang="ru" lang="ru">Русский</a> · <a href="README.vi.md" hreflang="vi" lang="vi">Tiếng Việt</a> · <a href="README.id.md" hreflang="id" lang="id">Bahasa Indonesia</a> · <a href="README.ms.md" hreflang="ms" lang="ms">Bahasa Melayu</a> · <a href="README.th.md" hreflang="th" lang="th">ไทย</a></p>

---

## What it is

FileExplorer8 is a **file manager** that runs natively on macOS. It puts three interaction models — file manager, dual-pane and quad-pane — into a single window, cycled with `⇧⌘D`. Each mode keeps its own state: path, tabs, sort order, column widths, selection. Switch back and forth and nothing is lost.

It is not a Finder replacement, and not another Finder skin. It fills the gap Finder leaves: **bulk moving with both hands on the keyboard**.

The reference point is the classic dual-pane file manager: it sets no default handler, ships no Finder extension, and never reads or writes Finder preferences. The only thing shared is the file system itself — which is why it can live alongside Finder indefinitely without the two fighting.

---

## Screenshots

### File manager: grid view with the details pane

![File manager: grid view with the details pane](images/readme/01-explorer.png)

### Dual-pane: source and destination

![Dual-pane: source and destination](images/readme/02-dual-pane.png)

### Quad-pane: 2×2 layout

![Quad-pane: 2×2 layout](images/readme/03-quad-pane.png)

---

## Features

### Dry-run before every write

Before copying, moving or overwriting, the app runs a dry-run: is the target writable, is there enough space, which names collide — all shown up front. **This step writes zero bytes.**

Four conflict strategies: replace (back up first, undo supported), keep both, skip, ask per item. With five or fewer conflicts you can decide one by one.

Progress shows live speed, transferred / total / remaining, and ends with a full ledger: how many succeeded, skipped, failed — with each failure named along with its reason.

### Three-tier undo

Same-volume moves, renames, deletes to the Trash, and ZIP pack/unpack are **guaranteed 100% undoable**. Copy and cross-volume moves are best-effort. Anything not undoable asks for confirmation first.

### Six view layouts and real previews

Extra-large / large / medium / small icons, list, and detail views. Icons are picked at true pixel sizes (256 / 128 / 64 / 32) so they stay sharp on Retina displays.

Press `Space` to preview, then `←` / `→` or `PgUp` / `PgDn` to move through files:

- Text and source code get a read-only monospaced view with syntax highlighting for 50+ languages and line numbers
- PDFs render through PDFKit
- Images scale to fit the whole panel, preserving aspect ratio
- Rich formats go to the system Quick Look
- Anything unrenderable falls back to a plain info card

### Pack and unpack

**Create ZIP**: ZIP64, adjustable compression level, already-compressed formats skipped automatically, optional follow-symlinks, and the result is undoable.

**Double-click to extract**, matching Finder's behaviour: a single top-level folder is not nested, whole-archive naming on conflict, only `__MACOSX` is cleaned up, and Unix permission bits are restored.

### Remote SSH folders

Built-in SSH / SFTP: connect with a password or a private key from any path, then browse, copy, delete, rename and undo on the remote side exactly as you would locally — through the same write pipeline.

The tab strip marks connections with a network-drive icon and a red/green status, and reconnects in one click after a drop. **The password can be left unsaved**, replaced by a one-time login prompt per connection. Remote files up to 10 MB preview instantly.

### The details

- Finder's seven colour tags, stackable; clearing all tags keeps a custom text tag
- Command palette `⌘K`, ordered by match quality → recency → alphabetical
- Path trio: copy path, copy parent path, copy filename — plus “Open in Terminal”
- Checksums: SHA-256 / SHA-512 / SHA-1 / MD5 / BLAKE3 / CRC32 / CRC64
- Volumes appear automatically: USB sticks, external drives, mounted disk images — eject in one click
- Session restore: window position, tabs, column widths, sort order and pane ratio are all remembered; queued writes resume after a crash
- Two-way copy/paste with Finder, with drag and drop working in all three directions
- Language switching sits in the top-level Language menu — one step, applied immediately

### 14 languages

Simplified Chinese, Traditional Chinese, English, Japanese, Korean, German, French, Spanish, Brazilian Portuguese, Russian, Vietnamese, Indonesian, Malay, Thai.

Thai got its own collation implementation — leading vowels, tone marks and script order are not code-point order, so sorting by code point would come out scrambled.

---

## Privacy

**No data is collected.** No accounts, no analytics, no ad SDK, no crash reporting.

Apart from SSH connections you start yourself, the app sends no bytes to any server. Your files, browsing history and server credentials stay on your own Mac: passwords and passphrases live in the system Keychain, and private-key files never leave where you put them.

The app runs in the App Sandbox and only reads or writes within folders you grant. It does not request contacts, camera, microphone, screen recording or full disk access.

[Read the full privacy policy](https://rosesmall2010.github.io/FileExplorer8/privacy.en.html)

---

## Support

Stuck, got an idea, or found a bug?

- Check the [support page](https://rosesmall2010.github.io/FileExplorer8/) for frequently asked questions
- Or open an [issue](https://github.com/rosesmall2010/FileExplorer8/issues) with your macOS version, FileExplorer8 version and reproduction steps

The version number is in “FileExplorer8 › About FileExplorer8”.

### Frequently asked

**Why does it ask for permission when I open some folders?**
The app runs in the App Sandbox. Desktop, Downloads, Documents and external disks live outside the sandbox, so macOS prompts you the first time you enter such a folder. That is the system's security design, not a defect. Choose “Grant access to this folder” and the folder is remembered — you are only asked once per path per run.

**Does it read my contacts, camera, or screen?**
No. FileExplorer8 only requests user-selected file access, the standard folders (Downloads / Documents / Music / Pictures / Movies), and outbound network access. It has no contacts, camera, microphone, screen-recording or full-disk access.

**Where are SSH passwords stored?**
In the macOS Keychain. Server endpoints live in the local sandbox container, encrypted with AES-256-GCM. You can also skip saving the password and get a one-time login prompt on every connection. See the <a href="https://rosesmall2010.github.io/FileExplorer8/privacy.en.html">privacy policy</a>.

**Does it support Apple Silicon and Intel?**
Both. The installer is a universal binary. macOS 15.0 or later is required.

**How do I clean up leftovers after uninstalling?**
Delete the app, then delete <code>~/Library/Containers/com.donghuazhu.FileExplorer8/</code> to clear preferences, session state and server endpoints (sandboxed apps keep their data in that container, not in shared system locations). SSH passwords live in the Keychain and are removed along with their connections.

---

## Requirements

- macOS 15.0 or later
- Apple Silicon or Intel (universal binary)

---

<p align="center"><sub>macOS is a trademark of Apple Inc. This app is not affiliated with Apple Inc.</sub></p>
