
# Sistema de Preenchimento de Relatórios de Serviços

Este é um aplicativo desenvolvido com Streamlit para facilitar o preenchimento de relatórios de atendimento técnico, focado em manutenção de equipamentos da área de saúde. O sistema permite registrar e organizar informações de atendimentos realizados, gerando relatórios detalhados com a possibilidade de copiar o conteúdo para a área de transferência.

### Benefícios do Sistema
- **Padronização dos Relatórios:** Com este sistema, todos os relatórios seguem um formato padronizado, garantindo consistência nas informações registradas em cada atendimento. Isso facilita a análise posterior dos dados, gera mais confiança na comunicação entre equipe técnica e gestores, e evita erros causados pela variação de formatos manuais.

- **Redução de Tempo no Preenchimento Manual:** Engenheiros e técnicos podem preencher os relatórios de forma mais rápida e eficiente. Ao invés de perder tempo inserindo dados manualmente em diferentes sistemas ou planilhas, o usuário simplesmente preenche os campos obrigatórios, e o sistema gera um relatório completo e pronto para uso. O resultado? Uma significativa redução no tempo necessário para documentar cada atendimento, permitindo que o time técnico se concentre no que realmente importa: a solução dos problemas.

- **Facilidade de Uso e Acesso Rápido:** Com uma interface simples e intuitiva, o sistema permite que qualquer pessoa possa usá-lo sem a necessidade de um treinamento extenso. Tudo está acessível em uma única tela, com botões de ação claros e funcionalidades práticas, como a cópia automática do relatório para a área de transferência.

- **Automação do Processo de Relatório:** Automatizar o preenchimento de relatórios técnicos elimina a chance de erro humano, como a omissão de informações importantes ou o preenchimento incorreto de dados. Além disso, o sistema também permite a inserção de peças utilizadas e avaliações de segurança, que são essenciais para relatórios completos e detalhados.

- **Versatilidade para Diferentes Tipos de Chamado:** O sistema está preparado para atender chamados de manutenção corretiva (MA/MS) e também follow-ups, permitindo o acompanhamento preciso de atendimentos que exigem peças sobressalentes ou reavaliações.

## Funcionalidades
- Preenchimento de Relatório: Interface intuitiva para registrar as informações do chamado, como problema reportado, causa raiz, procedimentos realizados, status do equipamento, e outras informações pertinentes ao atendimento técnico.

- Classificação do Chamado: Inclui campos para a classificação do problema, permitindo selecionar entre diversas categorias como problemas técnicos, infraestruturais, operacionais, entre outros.

- Avaliação de Segurança: O sistema permite a inclusão de informações sobre possíveis problemas de segurança relacionados ao equipamento.

- Registro de Peças Consumidas: Opção para adicionar peças consumidas durante o atendimento, registrando o nome da peça, SMN, e Batch ID.

- Copiar Conteúdo do Relatório: Funcionalidade para copiar o conteúdo do relatório gerado para a área de transferência, facilitando o envio de informações via e-mail ou outros meios.

## Como Executar o Projeto
### Requisitos
Para executar o projeto, você precisará ter as seguintes dependências instaladas:

- Python 3.7 ou superior
- Bibliotecas Python necessárias:
- Streamlit
- st_copy_to_clipboard (para a funcionalidade de copiar o relatório gerado)

### Instalação
1- Clone o repositório para o seu ambiente local:
```
git clone https://github.com/felipe-bizio/preenchimento_chamados
```
2- Acesse o diretório do projeto:
```
cd preenchimento_chamados
```
3- Instale as dependências listadas no arquivo requirements.txt:
```
pip install -r requirements.txt
```
4- Executando o Aplicativo
Para iniciar o aplicativo, execute o seguinte comando no terminal:
```
streamlit run Home.py
```

### Estrutura do Código

- Configuração da Página: O aplicativo está configurado em modo 'wide' (largura total), com ícone de página e título personalizados.

- Session State: Utiliza o st.session_state do Streamlit para armazenar e gerenciar os dados inseridos, garantindo que os valores sejam mantidos entre as interações do usuário.

- Layouts e Colunas: O layout do formulário é organizado em colunas para melhor visualização das informações inseridas.

- Abas para Diferentes Tipos de Chamado:

  - Chamado MA/MS: Campos para descrever o problema reportado, encontrado e a causa raiz.
  - Chamado Follow Up: Inclui plano de ação, status das peças para o próximo atendimento, e outros detalhes específicos para acompanhamento.

- Avaliação de Segurança: Campos de rádio para avaliar se o equipamento causou ou poderia causar problemas de segurança.

- Classificação de Chamado: Inclui duas classificações, uma principal e outra SC (chamado específico).

- Funções de Limpeza de Campos: Inclui funções que permitem limpar os campos do formulário com um clique, facilitando o preenchimento de novos chamados.

### Personalização

- Logotipo: O logo exibido na aplicação pode ser personalizado, alterando o caminho da imagem na linha onde é chamada a função st.logo('images/logo_siemens.png').

- Footer Personalizado: No rodapé da barra lateral, é exibida uma legenda informando que o sistema foi criado com Streamlit e desenvolvido por Felipe Bízio.

### Contribuições
Se você deseja contribuir com melhorias ou novas funcionalidades para este projeto, siga os seguintes passos:

1- Faça um fork do repositório.
2- Crie uma nova branch para sua funcionalidade:
```
git checkout -b nova-funcionalidade
```
3- Envie suas modificações:
```
git commit -m "Descrição das alterações"
git push origin nova-funcionalidade
```
4- Abra um pull request no repositório original.

### Como o Sistema Pode Ajudar Sua Empresa
Ao adotar este sistema, sua empresa experimentará um impacto direto na eficiência do time técnico e na qualidade dos relatórios gerados. A padronização do processo de documentação, aliada à diminuição do tempo de preenchimento manual, resulta em economias significativas de tempo e custo. Além disso, com o aumento da precisão e da clareza dos relatórios, o processo de revisão e auditoria também se torna mais ágil.

Imagine o tempo que seus engenheiros ganhariam ao não precisar lidar com relatórios manuais demorados e o valor que essa automação traz à sua empresa em termos de produtividade, confiabilidade e segurança operacional. Ao digitalizar esse processo, sua equipe poderá se concentrar no que realmente importa: a resolução rápida e eficiente dos problemas técnicos, enquanto o sistema cuida da burocracia.

Se você deseja levar a produtividade da sua equipe para o próximo nível e garantir relatórios precisos, completos e consistentes, este sistema é a solução ideal.
 
