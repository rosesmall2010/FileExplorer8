<p align="center">
  <img src="images/icon-1024.png" width="128" alt="FileExplorer8">
</p>

<h1 align="center">FileExplorer8</h1>

<p align="center"><strong>Nativer Dateimanager für macOS · Dateimanager / Zwei Bereiche / Vier Bereiche in einem Fenster</strong></p>

<p align="center">Ein Datei-Kern, drei Bedienmodelle · Probelauf vor jedem Schreiben · Dreistufiges Rückgängig · Auch bei zehntausenden Einträgen flüssig</p>

<p align="center">
  <a href="https://rosesmall2010.github.io/FileExplorer8/"><img src="https://img.shields.io/badge/Support-blue" alt="Site"></a>
  <a href="privacy.de.html"><img src="https://img.shields.io/badge/Datenschutz-green" alt="Privacy"></a>
  <img src="https://img.shields.io/badge/version-1.1.6-lightgrey" alt="Version">
</p>

<p align="center"><a href="README.md" hreflang="zh-Hans" lang="zh-Hans">简体中文</a> · <a href="README.zh-Hant.md" hreflang="zh-Hant" lang="zh-Hant">繁體中文</a> · <a href="README.en.md" hreflang="en" lang="en">English</a> · <a href="README.ja.md" hreflang="ja" lang="ja">日本語</a> · <a href="README.ko.md" hreflang="ko" lang="ko">한국어</a> · <strong>Deutsch</strong> · <a href="README.fr.md" hreflang="fr" lang="fr">Français</a> · <a href="README.es.md" hreflang="es" lang="es">Español</a> · <a href="README.pt-BR.md" hreflang="pt-BR" lang="pt-BR">Português (Brasil)</a> · <a href="README.ru.md" hreflang="ru" lang="ru">Русский</a> · <a href="README.vi.md" hreflang="vi" lang="vi">Tiếng Việt</a> · <a href="README.id.md" hreflang="id" lang="id">Bahasa Indonesia</a> · <a href="README.ms.md" hreflang="ms" lang="ms">Bahasa Melayu</a> · <a href="README.th.md" hreflang="th" lang="th">ไทย</a></p>

---

## Was ist das

FileExplorer8 ist ein **Dateimanager**, der nativ unter macOS läuft. Er bringt drei Bedienmodelle – Dateimanager, Zwei Bereiche und Vier Bereiche – in ein einziges Fenster, zyklisch umschaltbar mit `⇧⌘D`. Jeder Modus behält seinen Zustand: Pfad, Tabs, Sortierung, Spaltenbreiten, Auswahl. Hin und her wechseln verliert nichts.

Er ist kein Finder-Ersatz und kein weiterer Finder-Anstrich. Er füllt die Lücke, die der Finder lässt: **Massenverschiebungen mit beiden Händen auf der Tastatur**.

Vorbild ist der klassische Dateimanager mit zwei Bereichen: kein Standardprogramm wird gesetzt, keine Finder-Erweiterung installiert, keine Finder-Einstellungen gelesen oder geschrieben. Geteilt wird nur das Dateisystem selbst – deshalb kann er dauerhaft neben dem Finder bestehen, ohne dass sich beide in die Quere kommen.

---

## Ansichten

### Dateimanager: Rasteransicht mit Detailbereich

![Dateimanager: Rasteransicht mit Detailbereich](images/readme/01-explorer.png)

### Zwei Bereiche: Quelle und Ziel

![Zwei Bereiche: Quelle und Ziel](images/readme/02-dual-pane.png)

### Vier Bereiche: 2×2-Raster

![Vier Bereiche: 2×2-Raster](images/readme/03-quad-pane.png)

---

## Funktionen

### Probelauf vor jedem Schreiben

Vor Kopieren, Verschieben oder Überschreiben läuft ein Probelauf: Ist das Ziel beschreibbar, reicht der Platz, welche Namen kollidieren – alles vorab sichtbar. **Dieser Schritt schreibt kein einziges Byte.**

Vier Konfliktstrategien: ersetzen (vorher sichern, rückgängig möglich), beide behalten, überspringen, einzeln fragen. Bei höchstens fünf Konflikten entscheiden Sie Stück für Stück.

Der Fortschritt zeigt Live-Geschwindigkeit, übertragen / gesamt / verbleibend und endet mit einer vollständigen Bilanz: wie viele erfolgreich, übersprungen, fehlgeschlagen – jeder Fehlschlag mit Dateiname und Grund.

### Dreistufiges Rückgängig

Verschieben im selben Volume, Umbenennen, Löschen in den Papierkorb sowie ZIP-Packen und -Entpacken sind **zu 100 % rückgängig zu machen**. Kopieren und volumeübergreifendes Verschieben sind Best-Effort. Was sich nicht rückgängig machen lässt, verlangt vorher eine Bestätigung.

### Sechs Ansichten und echte Vorschauen

Sehr große / große / mittlere / kleine Symbole, Liste und Details. Symbole werden in echten Pixelgrößen (256 / 128 / 64 / 32) gewählt und bleiben so auf Retina-Displays scharf.

`Space` öffnet die Vorschau, `←` / `→` oder `PgUp` / `PgDn` blättern weiter:

- Text und Quelltext erhalten eine schreibgeschützte Monospace-Ansicht mit Syntaxhervorhebung für über 50 Sprachen und Zeilennummern
- PDFs rendert PDFKit
- Bilder werden seitenverhältnistreu so skaliert, dass sie ganz in den Bereich passen
- Reichhaltige Formate übernimmt Quick Look des Systems
- Was sich nicht darstellen lässt, bekommt eine schlichte Info-Karte

### Packen und Entpacken

**ZIP erstellen**: ZIP64, einstellbare Kompressionsstufe, bereits komprimierte Formate werden übersprungen, optional Symbolischen Links folgen – das Ergebnis ist rückgängig zu machen.

**Doppelklick zum Entpacken**, im Verhalten wie der Finder: ein einzelner oberster Ordner wird nicht verschachtelt, bei Kollision wird das ganze Archiv umbenannt, nur `__MACOSX` wird entfernt, Unix-Rechtebits werden wiederhergestellt.

### Entfernte SSH-Ordner

SSH/SFTP eingebaut: Verbindung per Passwort oder privatem Schlüssel von beliebigem Pfad aus. Entfernte Ordner lassen sich durchsuchen, kopieren, löschen, umbenennen und rückgängig machen wie lokale – über dieselbe Schreibpipeline.

Die Tabelleiste kennzeichnet Verbindungen mit einem Netzlaufwerk-Symbol und rotem bzw. grünem Status und verbindet nach einem Abbruch mit einem Klick neu. **Das Passwort kann ungespeichert bleiben**, dann fragt jede Verbindung einmalig nach der Anmeldung. Entfernte Dateien bis 10 MB lassen sich sofort ansehen.

### Die Details

- Die sieben Farbmarkierungen des Finders, stapelbar; werden alle entfernt, bleibt eine eigene Textmarkierung
- Befehlspalette `⌘K`, sortiert nach Trefferqualität → letzte Verwendung → alphabetisch
- Pfad-Trio: Pfad kopieren, Pfad des übergeordneten Ordners kopieren, Dateinamen kopieren – plus „Im Terminal öffnen“
- Prüfsummen: SHA-256 / SHA-512 / SHA-1 / MD5 / BLAKE3 / CRC32 / CRC64
- Volumes erscheinen automatisch: USB-Sticks, externe Laufwerke, eingebundene Disk-Images – mit einem Klick auswerfen
- Sitzungswiederherstellung: Fensterposition, Tabs, Spaltenbreiten, Sortierung und Bereichsverhältnis werden gemerkt; anstehende Schreibvorgänge laufen nach einem Absturz weiter
- Kopieren und Einsetzen in beide Richtungen mit dem Finder, Ziehen und Ablegen in alle drei Richtungen
- Sprachwechsel liegt im Sprachmenü oberster Ebene – ein Schritt, sofort wirksam

### 14 Sprachen

Chinesisch vereinfacht und traditionell, Englisch, Japanisch, Koreanisch, Deutsch, Französisch, Spanisch, brasilianisches Portugiesisch, Russisch, Vietnamesisch, Indonesisch, Malaiisch, Thailändisch.

Thailändisch hat eine eigene Sortierregel bekommen – vorangestellte Vokale, Tonzeichen und Schriftreihenfolge folgen nicht der Codepoint-Reihenfolge, nach Codepoints sortiert käme es durcheinander.

---

## Datenschutz

**Es werden keine Daten erhoben.** Keine Konten, keine Analyse, kein Werbe-SDK, keine Absturzberichte.

Außer von Ihnen gestarteten SSH-Verbindungen sendet die App kein Byte an einen Server. Ihre Dateien, Ihr Verlauf und Ihre Server-Zugangsdaten bleiben auf Ihrem Mac: Passwörter und Passphrasen liegen im Systemschlüsselbund, Dateien mit privaten Schlüsseln bleiben, wo Sie sie ablegen.

Die App läuft in der App Sandbox und liest oder schreibt nur in Ordnern, die Sie freigeben. Kontakte, Kamera, Mikrofon, Bildschirmaufnahme oder vollständiger Festplattenzugriff werden nicht verlangt.

[Vollständige Datenschutzerklärung lesen](privacy.de.html)

---

## Support

Hängt etwas, haben Sie eine Idee oder einen Fehler gefunden?

- Auf der [Support-Seite](https://rosesmall2010.github.io/FileExplorer8/) finden Sie häufige Fragen
- Oder öffnen Sie ein [Issue](https://github.com/rosesmall2010/FileExplorer8/issues) mit macOS-Version, FileExplorer8-Version und Schritten zum Nachstellen

Die Versionsnummer steht unter „FileExplorer8 › Über FileExplorer8“.

### Häufige Fragen

**Warum fragt die App beim Öffnen mancher Ordner nach einer Freigabe?**
Die App läuft in der App Sandbox. Schreibtisch, Downloads, Dokumente und externe Laufwerke liegen außerhalb der Sandbox, deshalb fragt macOS beim ersten Betreten eines solchen Ordners nach. Das ist so von macOS vorgesehen und kein Fehler. Mit „Zugriff auf diesen Ordner erlauben“ wird der Ordner gemerkt – pro Pfad und Sitzung wird nur einmal gefragt.

**Liest die App meine Kontakte, die Kamera oder den Bildschirm?**
Nein. FileExplorer8 fordert nur Zugriff auf vom Benutzer gewählte Dateien, auf die Standardordner (Downloads / Dokumente / Musik / Bilder / Filme) und auf ausgehende Netzwerkverbindungen an. Es gibt keinen Zugriff auf Kontakte, Kamera, Mikrofon, Bildschirmaufnahme oder das gesamte Laufwerk.

**Wo werden SSH-Passwörter gespeichert?**
Im macOS-Schlüsselbund. Server-Endpunkte liegen im lokalen Sandbox-Container, verschlüsselt mit AES-256-GCM. Sie können das Passwort auch nicht speichern und stattdessen bei jeder Verbindung einmal abfragen lassen. Details in der <a href="privacy.html">Datenschutzerklärung</a>.

**Läuft die App auf Apple Silicon und Intel?**
Auf beiden. Das Installationspaket ist ein Universal Binary. Erforderlich ist macOS 15.0 oder neuer.

**Wie entferne ich Reste nach dem Deinstallieren?**
Löschen Sie die App und danach <code>~/Library/Containers/com.donghuazhu.FileExplorer8/</code>, um Einstellungen, Sitzungsdaten und Server-Endpunkte zu entfernen (Sandbox-Apps speichern ihre Daten in diesem Container, nicht an gemeinsamen Systemorten). SSH-Passwörter liegen im Schlüsselbund und werden mit der jeweiligen Verbindung gelöscht.

---

## Systemanforderungen

- macOS 15.0 oder neuer
- Apple Silicon oder Intel (Universal Binary)

---

<p align="center"><sub>macOS ist eine Marke von Apple Inc. Diese App steht in keiner Verbindung zu Apple Inc.</sub></p>
