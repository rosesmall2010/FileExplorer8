<p align="center">
  <img src="images/icon-1024.png" width="128" alt="FileExplorer8">
</p>

<h1 align="center">FileExplorer8</h1>

<p align="center"><strong>Gerenciador de arquivos nativo do macOS · Gerenciador / dois painéis / quatro painéis numa só janela</strong></p>

<p align="center">Um núcleo de operações, três modelos de interação · Simulação antes de escrever · Desfazer em três níveis · Sem travamentos com dezenas de milhares de itens</p>

<p align="center">
  <a href="https://rosesmall2010.github.io/FileExplorer8/"><img src="https://img.shields.io/badge/Suporte-blue" alt="Site"></a>
  <a href="https://rosesmall2010.github.io/FileExplorer8/privacy.pt-BR.html"><img src="https://img.shields.io/badge/Privacidade-green" alt="Privacy"></a>
  <img src="https://img.shields.io/badge/version-1.1.6-lightgrey" alt="Version">
</p>

<p align="center"><a href="README.md" hreflang="zh-Hans" lang="zh-Hans">简体中文</a> · <a href="README.zh-Hant.md" hreflang="zh-Hant" lang="zh-Hant">繁體中文</a> · <a href="README.en.md" hreflang="en" lang="en">English</a> · <a href="README.ja.md" hreflang="ja" lang="ja">日本語</a> · <a href="README.ko.md" hreflang="ko" lang="ko">한국어</a> · <a href="README.de.md" hreflang="de" lang="de">Deutsch</a> · <a href="README.fr.md" hreflang="fr" lang="fr">Français</a> · <a href="README.es.md" hreflang="es" lang="es">Español</a> · <strong>Português (Brasil)</strong> · <a href="README.ru.md" hreflang="ru" lang="ru">Русский</a> · <a href="README.vi.md" hreflang="vi" lang="vi">Tiếng Việt</a> · <a href="README.id.md" hreflang="id" lang="id">Bahasa Indonesia</a> · <a href="README.ms.md" hreflang="ms" lang="ms">Bahasa Melayu</a> · <a href="README.th.md" hreflang="th" lang="th">ไทย</a></p>

---

## O que é

O FileExplorer8 é um **gerenciador de arquivos** que roda nativamente no macOS. Ele reúne três modelos de interação — gerenciador de arquivos, dois painéis e quatro painéis — numa única janela, alternados com `⇧⌘D`. Cada modo guarda o próprio estado: caminho, abas, ordenação, largura das colunas e seleção. Pode ir e voltar sem perder nada.

Não é um substituto do Finder, nem outra pele do Finder. Ele preenche o que falta no Finder: **a movimentação em massa com as duas mãos no teclado**.

A referência é o gerenciador de arquivos clássico de dois painéis: não define aplicativo padrão, não instala extensão do Finder e não lê nem escreve as preferências do Finder. O único item compartilhado é o sistema de arquivos. Por isso ele convive com o Finder por tempo indeterminado sem que os dois se atrapalhem.

---

## Capturas

### Gerenciador de arquivos: visualização em grade com painel de detalhes

![Gerenciador de arquivos: visualização em grade com painel de detalhes](images/readme/01-explorer.png)

### Dois painéis: origem e destino

![Dois painéis: origem e destino](images/readme/02-dual-pane.png)

### Quatro painéis: layout 2×2

![Quatro painéis: layout 2×2](images/readme/03-quad-pane.png)

---

## Recursos

### Simulação antes de cada escrita

Antes de copiar, mover ou sobrescrever, o app faz uma simulação: dá para gravar no destino, há espaço suficiente, quais nomes colidem — tudo mostrado de antemão. **Essa etapa não escreve um único byte.**

Quatro estratégias de conflito: substituir (com backup antes e desfazer), manter ambos, ignorar, perguntar item a item. Com cinco conflitos ou menos, você decide caso a caso.

O progresso mostra velocidade em tempo real, transferido / total / restante e termina com um balanço completo: quantos deram certo, quantos foram ignorados, quantos falharam — cada falha nomeada com o motivo.

### Desfazer em três níveis

Mover no mesmo volume, renomear, apagar na lixeira e compactar ou extrair ZIP são **garantidamente 100% reversíveis**. Copiar e mover entre volumes é o melhor esforço. O que não pode ser desfeito pede confirmação antes de executar.

### Seis visualizações e prévias de verdade

Ícones extragrandes / grandes / médios / pequenos, lista e detalhes. Os ícones são escolhidos no tamanho real em pixels (256 / 128 / 64 / 32), então não ficam borrados em telas Retina.

Pressione `Espaço` para pré-visualizar e depois `←` / `→` ou `PgUp` / `PgDn` para percorrer:

- Texto e código-fonte ganham uma visualização monoespaçada somente leitura, com realce de sintaxe para mais de 50 linguagens e números de linha
- PDFs passam pelo PDFKit
- Imagens são escaladas para caber no painel mantendo a proporção
- Formatos ricos vão para a Visualização Rápida do sistema
- O que não pode ser renderizado recebe uma ficha informativa

### Compactar e extrair

**Criar ZIP**: ZIP64, nível de compactação ajustável, formatos já compactados ignorados automaticamente, opção de seguir links simbólicos e resultado reversível.

**Duplo clique para extrair**, com o mesmo comportamento do Finder: uma única pasta de primeiro nível não é aninhada, em caso de colisão o pacote inteiro é renomeado, só `__MACOSX` é limpo e os bits de permissão Unix são restaurados.

### Pastas remotas SSH

SSH / SFTP integrado: conecte por senha ou por uma chave privada em qualquer caminho e depois navegue, copie, apague, renomeie e desfaça no remoto exatamente como no local, pelo mesmo caminho de escrita.

A barra de abas marca as conexões com um ícone de disco de rede e estado vermelho ou verde, e reconecta num clique após queda. **A senha pode ficar sem salvar**, substituída por um pedido de login único por conexão. Arquivos remotos de até 10 MB são pré-visualizados na hora.

### Os detalhes

- As sete etiquetas coloridas do Finder, empilháveis; ao remover todas, uma etiqueta de texto própria é mantida
- Paleta de comandos `⌘K`, ordenada por correspondência → uso recente → alfabética
- Trio de caminhos: copiar caminho, copiar caminho da pasta acima, copiar nome do arquivo, mais “Abrir no Terminal”
- Somas de verificação: SHA-256 / SHA-512 / SHA-1 / MD5 / BLAKE3 / CRC32 / CRC64
- Volumes detectados automaticamente: pendrives, discos externos, imagens de disco montadas; ejetar com um clique
- Restauração de sessão: posição da janela, abas, larguras de coluna, ordenação e proporção dos painéis são lembradas; gravações na fila continuam após uma queda
- Copiar e colar bidirecional com o Finder, com arrastar e soltar nas três direções
- A troca de idioma fica no menu Idioma de primeiro nível: um passo e efeito imediato

### 14 idiomas

Chinês simplificado e tradicional, inglês, japonês, coreano, alemão, francês, espanhol, português do Brasil, russo, vietnamita, indonésio, malaio, tailandês.

O tailandês ganhou uma regra de ordenação própria: vogais anteriores, sinais de tom e ordem das escritas não seguem a ordem dos pontos de código, então ordenar por ponto de código sairia embaralhado.

---

## Privacidade

**Nenhum dado é coletado.** Sem contas, sem análise, sem SDK de anúncios, sem relatório de falhas.

Fora as conexões SSH que você mesmo inicia, o app não envia um único byte a servidor algum. Seus arquivos, histórico e credenciais de servidor ficam no seu Mac: senhas e frases no Keychain do sistema, arquivos de chave privada onde você os colocou.

O app roda no App Sandbox e só lê ou grava nas pastas que você concede. Não solicita contatos, câmera, microfone, gravação de tela nem acesso total ao disco.

[Ler a política de privacidade completa](https://rosesmall2010.github.io/FileExplorer8/privacy.pt-BR.html)

---

## Suporte

Travou, tem uma ideia ou achou um bug?

- Consulte a [página de suporte](https://rosesmall2010.github.io/FileExplorer8/) para as perguntas frequentes
- Ou abra uma [issue](https://github.com/rosesmall2010/FileExplorer8/issues) com a sua versão do macOS, a do FileExplorer8 e os passos de reprodução

A versão aparece em “FileExplorer8 › Sobre o FileExplorer8”.

### Perguntas frequentes

**Por que ele pede permissão ao abrir algumas pastas?**
O app roda no App Sandbox. Mesa, Downloads, Documentos e discos externos ficam fora do sandbox, então o macOS pergunta na primeira vez que você entra numa dessas pastas. É o desenho de segurança do sistema, não um defeito. Escolha “Permitir acesso a esta pasta” e a pasta fica lembrada: só se pergunta uma vez por caminho e por execução.

**Ele lê meus contatos, a câmera ou a tela?**
Não. O FileExplorer8 pede apenas acesso aos arquivos que você seleciona, às pastas padrão (Downloads / Documentos / Música / Imagens / Filmes) e acesso de rede de saída. Não tem acesso a contatos, câmera, microfone, gravação de tela nem ao disco inteiro.

**Onde ficam as senhas SSH?**
No Keychain do macOS. Os endpoints dos servidores ficam no contêiner local do sandbox, cifrados com AES-256-GCM. Você também pode não salvar a senha e receber um pedido de login único a cada conexão. Veja a <a href="https://rosesmall2010.github.io/FileExplorer8/privacy.pt-BR.html">política de privacidade</a>.

**Funciona em Apple Silicon e Intel?**
Nos dois. O instalador é um binário universal. É necessário macOS 15.0 ou superior.

**Como limpo os restos depois de desinstalar?**
Apague o app e depois apague <code>~/Library/Containers/com.donghuazhu.FileExplorer8/</code> para apagar preferências, estado de sessão e endpoints (apps em sandbox guardam os dados nesse contêiner, não em locais compartilhados do sistema). As senhas SSH ficam no Keychain e são removidas junto com a conexão.

---

## Requisitos

- macOS 15.0 ou superior
- Apple Silicon ou Intel (binário universal)

---

<p align="center"><sub>macOS é uma marca da Apple Inc. Este app não é afiliado à Apple Inc.</sub></p>
