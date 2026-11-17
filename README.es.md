<p align="center">
  <img src="images/icon-1024.png" width="128" alt="FileExplorer8">
</p>

<h1 align="center">FileExplorer8</h1>

<p align="center"><strong>Gestor de archivos nativo de macOS · Gestor / dos paneles / cuatro paneles en una sola ventana</strong></p>

<p align="center">Un núcleo de operaciones, tres modelos de interacción · Simulación antes de escribir · Deshacer en tres niveles · Sin tirones con decenas de miles de entradas</p>

<p align="center">
  <a href="https://rosesmall2010.github.io/FileExplorer8/"><img src="https://img.shields.io/badge/Soporte-blue" alt="Site"></a>
  <a href="privacy.es.html"><img src="https://img.shields.io/badge/Privacidad-green" alt="Privacy"></a>
  <img src="https://img.shields.io/badge/version-1.1.6-lightgrey" alt="Version">
</p>

<p align="center"><a href="README.md" hreflang="zh-Hans" lang="zh-Hans">简体中文</a> · <a href="README.zh-Hant.md" hreflang="zh-Hant" lang="zh-Hant">繁體中文</a> · <a href="README.en.md" hreflang="en" lang="en">English</a> · <a href="README.ja.md" hreflang="ja" lang="ja">日本語</a> · <a href="README.ko.md" hreflang="ko" lang="ko">한국어</a> · <a href="README.de.md" hreflang="de" lang="de">Deutsch</a> · <a href="README.fr.md" hreflang="fr" lang="fr">Français</a> · <strong>Español</strong> · <a href="README.pt-BR.md" hreflang="pt-BR" lang="pt-BR">Português (Brasil)</a> · <a href="README.ru.md" hreflang="ru" lang="ru">Русский</a> · <a href="README.vi.md" hreflang="vi" lang="vi">Tiếng Việt</a> · <a href="README.id.md" hreflang="id" lang="id">Bahasa Indonesia</a> · <a href="README.ms.md" hreflang="ms" lang="ms">Bahasa Melayu</a> · <a href="README.th.md" hreflang="th" lang="th">ไทย</a></p>

---

## Qué es esto

FileExplorer8 es un **gestor de archivos** que se ejecuta de forma nativa en macOS. Reúne tres modelos de interacción —gestor de archivos, dos paneles y cuatro paneles— en una sola ventana, que se alternan con `⇧⌘D`. Cada modo guarda su propio estado: ruta, pestañas, orden, anchos de columna y selección. Se puede ir y volver sin perder nada.

No es un sustituto del Finder ni otra piel del Finder. Cubre el hueco que deja el Finder: **el traslado masivo con las dos manos en el teclado**.

La referencia es el gestor de archivos clásico de dos paneles: no fija ninguna aplicación predeterminada, no instala ninguna extensión del Finder y no lee ni escribe las preferencias del Finder. Lo único compartido es el sistema de archivos. Por eso puede convivir con el Finder indefinidamente sin que los dos se estorben.

---

## Capturas

### Gestor de archivos: vista de cuadrícula con panel de detalles

![Gestor de archivos: vista de cuadrícula con panel de detalles](images/readme/01-explorer.png)

### Dos paneles: origen y destino

![Dos paneles: origen y destino](images/readme/02-dual-pane.png)

### Cuatro paneles: diseño 2×2

![Cuatro paneles: diseño 2×2](images/readme/03-quad-pane.png)

---

## Funciones

### Simulación antes de cada escritura

Antes de copiar, mover o sobrescribir, la app hace una simulación: ¿se puede escribir en el destino?, ¿hay espacio suficiente?, ¿qué nombres colisionan? Todo se muestra de antemano. **Ese paso no escribe ni un byte.**

Cuatro estrategias de conflicto: reemplazar (con copia de seguridad previa y deshacer), conservar ambos, omitir, preguntar uno a uno. Con cinco conflictos o menos puede decidir caso por caso.

El progreso muestra velocidad en vivo, transferido / total / restante y termina con un balance completo: cuántos correctos, omitidos y fallidos, con cada fallo nombrado y su motivo.

### Deshacer en tres niveles

Mover en el mismo volumen, renombrar, borrar a la papelera y comprimir o extraer ZIP están **garantizados como 100 % reversibles**. Copiar y mover entre volúmenes es de mejor esfuerzo. Lo que no se puede deshacer pide confirmación antes de ejecutarse.

### Seis vistas y vistas previas de verdad

Iconos muy grandes / grandes / medianos / pequeños, lista y detalles. Los iconos se eligen en su tamaño real en píxeles (256 / 128 / 64 / 32) para que no se emborronen en pantallas Retina.

Pulse `Espacio` para previsualizar y luego `←` / `→` o `PgUp` / `PgDn` para recorrer:

- El texto y el código fuente tienen una vista monoespaciada de solo lectura, con resaltado de sintaxis para más de 50 lenguajes y números de línea
- Los PDF pasan por PDFKit
- Las imágenes se escalan al panel conservando la proporción
- Los formatos enriquecidos van a Vista Rápida del sistema
- Lo que no se puede representar recibe una ficha informativa

### Comprimir y extraer

**Crear ZIP**: ZIP64, nivel de compresión ajustable, formatos ya comprimidos omitidos automáticamente, opción de seguir enlaces simbólicos y resultado reversible.

**Doble clic para extraer**, con el mismo comportamiento que el Finder: una única carpeta de primer nivel no se anida, al colisionar se renombra el paquete entero, solo se limpia `__MACOSX` y se restauran los bits de permisos Unix.

### Carpetas remotas SSH

SSH / SFTP integrado: conéctese con contraseña o con una clave privada de cualquier ruta y luego explore, copie, elimine, renombre y deshaga en remoto igual que en local, por la misma ruta de escritura.

La barra de pestañas marca las conexiones con un icono de disco de red y un estado rojo o verde, y reconecta con un clic tras una caída. **La contraseña puede quedar sin guardar**, sustituida por una solicitud de inicio de sesión única por conexión. Los archivos remotos de hasta 10 MB se previsualizan al instante.

### Los detalles

- Las siete etiquetas de color del Finder, apilables; al quitarlas todas se conserva una etiqueta de texto propia
- Paleta de comandos `⌘K`, ordenada por coincidencia → uso reciente → alfabético
- Trío de rutas: copiar ruta, copiar ruta del contenedor, copiar nombre de archivo, más «Abrir en Terminal»
- Sumas de comprobación: SHA-256 / SHA-512 / SHA-1 / MD5 / BLAKE3 / CRC32 / CRC64
- Volúmenes detectados automáticamente: memorias USB, discos externos, imágenes de disco montadas; expulsión con un clic
- Restauración de sesión: posición de ventana, pestañas, anchos de columna, orden y proporción de los paneles se recuerdan; las escrituras en cola continúan tras un fallo
- Copiar y pegar bidireccional con el Finder, con arrastrar y soltar en las tres direcciones
- El cambio de idioma está en el menú Idioma de primer nivel: un paso y efecto inmediato

### 14 idiomas

Chino simplificado y tradicional, inglés, japonés, coreano, alemán, francés, español, portugués de Brasil, ruso, vietnamita, indonesio, malayo, tailandés.

El tailandés tiene su propia regla de ordenación: las vocales antepuestas, los signos de tono y el orden de las escrituras no siguen el orden de puntos de código, así que ordenar por punto de código saldría desordenado.

---

## Privacidad

**No se recopila ningún dato.** Sin cuentas, sin analítica, sin SDK de publicidad, sin informes de fallos.

Aparte de las conexiones SSH que usted inicia, la app no envía ni un byte a ningún servidor. Sus archivos, su historial y sus credenciales de servidor se quedan en su Mac: contraseñas y frases en el llavero del sistema, archivos de clave privada donde usted los ponga.

La app se ejecuta en el App Sandbox y solo lee o escribe en las carpetas que usted concede. No solicita contactos, cámara, micrófono, grabación de pantalla ni acceso completo al disco.

[Leer la política de privacidad completa](privacy.es.html)

---

## Soporte

¿Se ha atascado, tiene una idea o ha encontrado un error?

- Consulte la [página de soporte](https://rosesmall2010.github.io/FileExplorer8/) para las preguntas frecuentes
- O abra un [issue](https://github.com/rosesmall2010/FileExplorer8/issues) con su versión de macOS, la de FileExplorer8 y los pasos de reproducción

La versión se ve en «FileExplorer8 › Acerca de FileExplorer8».

### Preguntas frecuentes

**¿Por qué pide permiso al abrir algunas carpetas?**
La app se ejecuta en el App Sandbox. El Escritorio, Descargas, Documentos y los discos externos están fuera del sandbox, así que macOS pregunta la primera vez que entra en una de esas carpetas. Es el diseño de seguridad del sistema, no un fallo. Elija «Permitir acceso a esta carpeta» y la carpeta queda recordada: solo se pregunta una vez por ruta y ejecución.

**¿Lee mis contactos, la cámara o la pantalla?**
No. FileExplorer8 solo solicita acceso a los archivos que usted selecciona, a las carpetas estándar (Descargas / Documentos / Música / Imágenes / Películas) y acceso de red saliente. No tiene acceso a contactos, cámara, micrófono, grabación de pantalla ni al disco completo.

**¿Dónde se guardan las contraseñas SSH?**
En el llavero de macOS. Los puntos de conexión de los servidores están en el contenedor local del sandbox, cifrados con AES-256-GCM. También puede no guardar la contraseña y recibir una solicitud de inicio de sesión única en cada conexión. Vea la <a href="privacy.html">política de privacidad</a>.

**¿Funciona en Apple Silicon e Intel?**
En ambos. El instalador es un binario universal. Se requiere macOS 15.0 o posterior.

**¿Cómo limpio los restos tras desinstalar?**
Elimine la app y luego elimine <code>~/Library/Containers/com.donghuazhu.FileExplorer8/</code> para borrar preferencias, estado de sesión y puntos de conexión (las apps en sandbox guardan sus datos en ese contenedor, no en ubicaciones compartidas del sistema). Las contraseñas SSH están en el llavero y se eliminan junto con su conexión.

---

## Requisitos

- macOS 15.0 o posterior
- Apple Silicon o Intel (binario universal)

---

<p align="center"><sub>macOS es una marca de Apple Inc. Esta app no está afiliada a Apple Inc.</sub></p>
