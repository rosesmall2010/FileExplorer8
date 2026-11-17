<p align="center">
  <img src="images/icon-1024.png" width="128" alt="FileExplorer8">
</p>

<h1 align="center">FileExplorer8</h1>

<p align="center"><strong>Gestionnaire de fichiers natif macOS · Gestionnaire / deux volets / quatre volets dans une seule fenêtre</strong></p>

<p align="center">Un noyau de fichiers, trois modèles d'interaction · Essai à blanc avant chaque écriture · Annulation à trois niveaux · Fluide même sur des dizaines de milliers d'entrées</p>

<p align="center">
  <a href="https://rosesmall2010.github.io/FileExplorer8/"><img src="https://img.shields.io/badge/Assistance-blue" alt="Site"></a>
  <a href="privacy.fr.html"><img src="https://img.shields.io/badge/Confidentialit%C3%A9-green" alt="Privacy"></a>
  <img src="https://img.shields.io/badge/version-1.1.6-lightgrey" alt="Version">
</p>

<p align="center"><a href="README.md" hreflang="zh-Hans" lang="zh-Hans">简体中文</a> · <a href="README.zh-Hant.md" hreflang="zh-Hant" lang="zh-Hant">繁體中文</a> · <a href="README.en.md" hreflang="en" lang="en">English</a> · <a href="README.ja.md" hreflang="ja" lang="ja">日本語</a> · <a href="README.ko.md" hreflang="ko" lang="ko">한국어</a> · <a href="README.de.md" hreflang="de" lang="de">Deutsch</a> · <strong>Français</strong> · <a href="README.es.md" hreflang="es" lang="es">Español</a> · <a href="README.pt-BR.md" hreflang="pt-BR" lang="pt-BR">Português (Brasil)</a> · <a href="README.ru.md" hreflang="ru" lang="ru">Русский</a> · <a href="README.vi.md" hreflang="vi" lang="vi">Tiếng Việt</a> · <a href="README.id.md" hreflang="id" lang="id">Bahasa Indonesia</a> · <a href="README.ms.md" hreflang="ms" lang="ms">Bahasa Melayu</a> · <a href="README.th.md" hreflang="th" lang="th">ไทย</a></p>

---

## De quoi s'agit-il

FileExplorer8 est un **gestionnaire de fichiers** qui tourne nativement sous macOS. Il réunit trois modèles d'interaction — gestionnaire de fichiers, deux volets et quatre volets — dans une seule fenêtre, à faire défiler avec `⇧⌘D`. Chaque mode conserve son état : chemin, onglets, tri, largeurs de colonnes, sélection. On passe de l'un à l'autre sans rien perdre.

Ce n'est pas un remplaçant du Finder, ni un nouveau déguisement du Finder. Il comble le manque du Finder : **le déplacement en masse, les deux mains sur le clavier**.

La référence est le gestionnaire de fichiers classique à deux volets : il ne définit aucune application par défaut, n'installe aucune extension Finder et ne lit ni n'écrit les préférences du Finder. La seule chose partagée est le système de fichiers lui-même — c'est pourquoi il peut cohabiter durablement avec le Finder sans que les deux se gênent.

---

## Captures

### Gestionnaire de fichiers : vue grille avec panneau de détails

![Gestionnaire de fichiers : vue grille avec panneau de détails](images/readme/01-explorer.png)

### Deux volets : source et destination

![Deux volets : source et destination](images/readme/02-dual-pane.png)

### Quatre volets : disposition 2×2

![Quatre volets : disposition 2×2](images/readme/03-quad-pane.png)

---

## Fonctions

### Essai à blanc avant chaque écriture

Avant de copier, déplacer ou écraser, l'app fait un essai à blanc : la cible est-elle inscriptible, l'espace est-il suffisant, quels noms entrent en collision — tout est montré d'avance. **Cette étape n'écrit pas un octet.**

Quatre stratégies de conflit : remplacer (sauvegarde d'abord, annulation prise en charge), conserver les deux, ignorer, demander un par un. Avec cinq conflits ou moins, vous décidez au cas par cas.

La progression affiche la vitesse en direct, le transféré / le total / le restant, et se termine par un bilan complet : combien de réussites, d'ignorés, d'échecs — chaque échec nommé avec sa raison.

### Annulation à trois niveaux

Déplacements sur le même volume, renommages, suppressions vers la corbeille, création et extraction de ZIP sont **garantis annulables à 100 %**. Copie et déplacement entre volumes sont du meilleur effort. Ce qui n'est pas annulable demande une confirmation avant exécution.

### Six dispositions et de vrais aperçus

Icônes très grandes / grandes / moyennes / petites, liste et détails. Les icônes sont choisies à leur taille réelle en pixels (256 / 128 / 64 / 32) pour rester nettes sur écran Retina.

Appuyez sur `Espace` pour prévisualiser, puis `←` / `→` ou `PgUp` / `PgDn` pour parcourir :

- Le texte et le code source obtiennent une vue à chasse fixe en lecture seule, avec coloration syntaxique pour plus de 50 langages et numéros de ligne
- Les PDF passent par PDFKit
- Les images sont mises à l'échelle dans le panneau en conservant leurs proportions
- Les formats riches vont au Coup d'œil du système
- Ce qui ne peut pas être rendu reçoit une simple fiche d'informations

### Compresser et extraire

**Créer un ZIP** : ZIP64, niveau de compression réglable, formats déjà compressés ignorés automatiquement, suivi facultatif des liens symboliques, et le résultat est annulable.

**Double-clic pour extraire**, comme le Finder : un unique dossier de premier niveau n'est pas imbriqué, l'archive entière est renommée en cas de conflit, seul `__MACOSX` est nettoyé et les bits de permission Unix sont restaurés.

### Dossiers distants SSH

SSH / SFTP intégré : connectez-vous par mot de passe ou par une clé privée située n'importe où, puis parcourez, copiez, supprimez, renommez et annulez à distance exactement comme en local, via le même pipeline d'écriture.

La barre d'onglets indique les connexions par une icône de disque réseau et un état rouge ou vert, et reconnecte en un clic après une coupure. **Le mot de passe peut rester non enregistré**, remplacé par une demande de connexion unique à chaque fois. Les fichiers distants jusqu'à 10 Mo s'affichent instantanément.

### Les détails

- Les sept étiquettes couleur du Finder, cumulables ; les retirer toutes conserve une étiquette texte personnalisée
- Palette de commandes `⌘K`, triée par pertinence → usage récent → ordre alphabétique
- Trio de chemins : copier le chemin, copier le chemin du parent, copier le nom — plus « Ouvrir dans le Terminal »
- Sommes de contrôle : SHA-256 / SHA-512 / SHA-1 / MD5 / BLAKE3 / CRC32 / CRC64
- Volumes détectés automatiquement : clés USB, disques externes, images disque montées — éjection en un clic
- Restauration de session : position de fenêtre, onglets, largeurs de colonnes, tri et proportion des volets sont mémorisés ; les écritures en attente reprennent après un plantage
- Copier-coller bidirectionnel avec le Finder, glisser-déposer dans les trois directions
- Le changement de langue est dans le menu Langue au premier niveau — une étape, effet immédiat

### 14 langues

Chinois simplifié et traditionnel, anglais, japonais, coréen, allemand, français, espagnol, portugais du Brésil, russe, vietnamien, indonésien, malais, thaï.

Le thaï a reçu sa propre règle de tri — voyelles antéposées, signes de ton et ordre des écritures ne suivent pas l'ordre des points de code ; trier par point de code donnerait un résultat incohérent.

---

## Confidentialité

**Aucune donnée n'est collectée.** Pas de comptes, pas de statistiques, pas de SDK publicitaire, pas de rapport de plantage.

Hormis les connexions SSH que vous lancez vous-même, l'app n'envoie pas un octet à un serveur. Vos fichiers, votre historique et vos identifiants de serveur restent sur votre Mac : mots de passe et phrases secrètes dans le trousseau du système, fichiers de clé privée là où vous les placez.

L'app tourne dans le bac à sable et ne lit ou n'écrit que dans les dossiers que vous accordez. Elle ne demande ni contacts, ni caméra, ni micro, ni enregistrement d'écran, ni accès complet au disque.

[Lire la politique de confidentialité complète](privacy.fr.html)

---

## Assistance

Un blocage, une idée, un bug ?

- Consultez la [page d'assistance](https://rosesmall2010.github.io/FileExplorer8/) pour les questions fréquentes
- Ou ouvrez un [ticket](https://github.com/rosesmall2010/FileExplorer8/issues) avec votre version de macOS, celle de FileExplorer8 et les étapes de reproduction

La version se lit dans « FileExplorer8 › À propos de FileExplorer8 ».

### Questions fréquentes

**Pourquoi une autorisation est-elle demandée à l'ouverture de certains dossiers ?**
L'app tourne dans le bac à sable (App Sandbox). Le Bureau, Téléchargements, Documents et les disques externes sont hors du bac à sable : macOS demande donc votre accord la première fois que vous entrez dans un tel dossier. C'est un choix de sécurité du système, pas un défaut. Choisissez « Autoriser l'accès à ce dossier » et le dossier est mémorisé — une seule demande par chemin et par session.

**L'app lit-elle mes contacts, ma caméra ou mon écran ?**
Non. FileExplorer8 ne demande que l'accès aux fichiers que vous sélectionnez, aux dossiers standard (Téléchargements / Documents / Musique / Images / Vidéos) et à l'accès réseau sortant. Aucun accès aux contacts, à la caméra, au micro, à l'enregistrement d'écran ni au disque entier.

**Où sont stockés les mots de passe SSH ?**
Dans le trousseau macOS. Les points de connexion des serveurs sont dans le conteneur local du bac à sable, chiffrés en AES-256-GCM. Vous pouvez aussi ne pas enregistrer le mot de passe et obtenir une demande de connexion unique à chaque fois. Voir la <a href="privacy.html">politique de confidentialité</a>.

**L'app fonctionne-t-elle sur Apple Silicon et Intel ?**
Oui, sur les deux. L'installateur est un binaire universel. macOS 15.0 ou ultérieur est requis.

**Comment nettoyer les résidus après désinstallation ?**
Supprimez l'app, puis supprimez <code>~/Library/Containers/com.donghuazhu.FileExplorer8/</code> pour effacer préférences, état de session et points de connexion (les apps en bac à sable stockent leurs données dans ce conteneur, pas dans des emplacements système partagés). Les mots de passe SSH sont dans le trousseau et disparaissent avec la connexion correspondante.

---

## Configuration requise

- macOS 15.0 ou ultérieur
- Apple Silicon ou Intel (binaire universel)

---

<p align="center"><sub>macOS est une marque d'Apple Inc. Cette app n'est pas affiliée à Apple Inc.</sub></p>
