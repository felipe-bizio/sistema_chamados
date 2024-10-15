import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard
import win32com.client as win32
import pythoncom

# Configuração da página para modo wide
st.set_page_config(
    page_title="Chamado",
    page_icon="📝",
    layout="wide"
)
st.logo('images/logo_siemens.png')
#st.sidebar.caption('Powerd by: Streamlit  \n Created by: Felipe Bízio')

# Função para enviar e-mail via Outlook
def enviar_email(destinatario, assunto, corpo):
    pythoncom.CoInitialize()  # Inicializa o componente COM
    outlook = win32.Dispatch('outlook.application')
    email = outlook.CreateItem(0)
    
    # Configurar e-mail
    email.To = destinatario
    email.Subject = assunto
    email.Body = corpo
    
    # Enviar e-mail
    email.Send()

def limpar_dados():
    campos_padrao = {
        "problema_reportado": "",
        "problema_encontrado": "",
        "causa_raiz": "",
        "procedimentos": "",
        "status_equipamento": "Funcionando adequadamente",
        "validacao": "",
        "status_chamado": "Finalizado",
        "observacoes": "",
        "pecas_consumidas": "Não",
        "pecas": [],
        "classificacao_chamado": "C1 - Problema Técnico",
        "classificacao_sc": "SC01 - Problema já resolvido",
        "as_info": "NNN",
        "icd_pm": "Não",
        "observacao_assinatura": "N/A",
        "email": "",
        "numero_chamado": "",
        "observacoes":""
    }
    for campo, valor in campos_padrao.items():
        st.session_state[campo] = valor

# Função para limpar os campos do formulário
def limpar_dados_aba2():
    campos_padrao_aba2 = {
        "plano_de_acao": "",
        "pecas_prox_atendimento": "Não",
        "pecas_em_teste": "Não",
        "informar_pecas": "",
        "local_pecas": "",
        "new_pecas": [],
        "prox_visita": "",
        "reenvio_chamado": "",
        "complexidade_atendimento": "",
        "ferramentas_especiais": "Não",
        "ferramenta": "",
        "left_on_notification": "N/A",
        "infos_add": "",
        "problema_e":""
    }
    for campo, valor in campos_padrao_aba2.items():
        st.session_state[campo] = valor

# Inicializando a página
st.title("Sistema de Preenchimento de Relatórios de Serviços")

# Inicializa o session_state se não existir
for campo, valor_padrao in {
    "nome_cse": "",
    "problema_reportado": "",
    "problema_encontrado": "",
    "causa_raiz": "",
    "procedimentos": "",
    "status_equipamento": "Funcionando adequadamente",
    "validacao": "",
    "status_chamado": "Finalizado",
    "observacoes": "",
    "pecas_consumidas": "Não",
    "pecas": [],
    "new_pecas": [],
    "classificacao_chamado": "C1 - Problema Técnico",
    "classificacao_sc": "SC01 - Problema já resolvido",
    "as_info": "NNN",
    "icd_pm": "Não",
    "observacao_assinatura": "N/A",
    "email": "",
    "numero_chamado": "",
    "plano_de_acao": "",
    "pecas_prox_atendimento": "Não",
    "pecas_em_teste": "Não",
    "informar_pecas": "",
    "local_pecas": "",
    "prox_visita": "",
    "reenvio_chamado": "",
    "complexidade_atendimento": "Baixa",
    "ferramentas_especiais": "Não",
    "ferramenta":"",
    "left_on_notification": "N/A",
    "infos_add":""   
}.items():
    if campo not in st.session_state:
        st.session_state[campo] = valor_padrao

# Layout do formulário
col1, col2, col3 = st.columns(3)
st.session_state.nome_cse = col1.text_input("Nome do CSE que realizou o atendimento", value=st.session_state.nome_cse)

tab1, tab2, tab3 = st.tabs(["Chamado MA/MS", "Chamado Follow Up","Chamado MP"])

#TAB1
with tab1:
    st.markdown("### Script Chamado MA/MS")
    col1, col3 = st.columns(2)
    # Descrição do Problema
    with col1:
        st.markdown("#### Descrição do Problema")
        st.session_state.problema_reportado = st.text_area("Problema reportado pelo cliente",value=st.session_state.problema_reportado)
        st.session_state.problema_encontrado = st.text_area("Problema encontrado pelo CSE", value=st.session_state.problema_encontrado)
        st.session_state.causa_raiz = st.text_area("Causa Raiz", value=st.session_state.causa_raiz)

        # Procedimentos Realizados
        st.markdown("#### Procedimentos Realizados")
        st.session_state.procedimentos = st.text_area("Verificações e procedimentos realizados",height=250, value=st.session_state.procedimentos)
        # Status do Equipamento e Validação
        st.markdown("#### Status do Equipamento e Validação")
        
        col1,col2 = st.columns(2)
        with col1:
            st.session_state.status_equipamento = st.selectbox(
            "Status do Equipamento", 
            ["Funcionando adequadamente", "Parado", "Parcialmente em funcionamento"],
            index=["Funcionando adequadamente", "Parado", "Parcialmente em funcionamento"].index(st.session_state.status_equipamento)
            )
            st.session_state.validacao = st.text_area("Validação realizada após intervenção técnica", value=st.session_state.validacao)
        with col2:
            st.session_state.status_chamado = st.selectbox("Status do Chamado", ["Finalizado", "Permanecerá aberto para acompanhamento", "Permanecerá aberto aguardando peça"], index=0)
            st.session_state.observacoes = st.text_area("Observações adicionais (caso necessário)", value=st.session_state.observacoes)


        st.markdown("#### Pecas Consumidas")
        st.session_state.pecas_consumidas = st.radio("Peças Consumidas", ["Não", "Sim"], index=["Não", "Sim"].index(st.session_state.pecas_consumidas),horizontal=True)

        if st.session_state.pecas_consumidas == "Sim":
            if st.button("Nova Peça"):
                st.session_state.pecas.append({"nome_peca": "", "smn": "", "batch_id": ""})

            col1, col2, col4 = st.columns(3)
            for i, peca in enumerate(st.session_state.pecas):
                with col1:
                    peca["nome_peca"] = st.text_input(f"Nome da peça {i + 1}", value=peca["nome_peca"], key=f"nome_peca_{i}")
                with col2:
                    peca["smn"] = st.text_input(f"SMN {i + 1}", value=peca["smn"], key=f"smn_{i}")
                with col4:
                    peca["batch_id"] = st.text_input(f"Batch ID {i + 1}", value=peca["batch_id"], key=f"batch_id_{i}")
        st.divider()
with col3: 
    # Avaliação de Segurança (3 campos)
        st.markdown('#### Avaliação de Segurança')
        causou_contribuiu = st.radio(" 1- O equipamento causou ou contribuiu para a morte ou ferimento grave ao usuário, paciente ou qualquer outra pessoa?", ["S", "N"], index=1,horizontal=True)
        mau_funcionamento = st.radio(" 2- Poderia o mau funcionamento do equipamento causar morte ou ferimento grave ao usuário, paciente ou qualquer outra pessoa caso ocorra novamente?", ["S", "N"], index=1,horizontal=True)
        outro_problema = st.radio(" 3- Existe algum outro Problema Potencial de Segurança (PSI) considerando os requerimentos do GD39?", ["S", "N"], index=1,horizontal=True)

        st.session_state.as_info = causou_contribuiu + mau_funcionamento + outro_problema
        st.text(f"A/S: {st.session_state.as_info}")

    # Classificação do Chamado (original e novo campo SC)
        st.markdown('#### Classificação do Chamado')
        st.session_state.classificacao_chamado = st.selectbox(
            "Classificação do Chamado", 
            ["C1 - Problema Técnico", "C2 - Problema Infraestrutura", "C3 - Problema Operacional", "C4 - Assessoria Científica", "C5 - Atualização de Sistema","C6 - Proativo"],
            index=0
        )
        st.session_state.classificacao_sc = st.selectbox(
            "Classificação SC", 
            ["",
             "SC01 - Problema já resolvido ou não apresentado na visita técnica", 
             "SC02 - Falta de Limpeza | Remoção de lixo", 
             "SC03 - Erro de cubetas | Film", 
             "SC04 - Erro nas probes (danificada | falta troca)", 
             "SC05 - Falta ou falha nos consumíveis (lâmpada, cubetas, soluções, etc.)", 
             "SC06 - Problemas com software (má operação | Falta de treinamento)", 
             "SC07 - Interfaceamento (não há problemas no sistema)", 
             "SC08 - Magline suja | Etiquetas com problema", 
             "SC09 - Outros"],
            index=0
        )
    # Observação da Assinatura
        st.session_state.observacao_assinatura = st.selectbox(
            "Observação da Assinatura", 
            [
                "N/A",
                "Tentei obter a assinatura do cliente, mas não havia um representante disponível no momento do serviço. Colhi a assinatura de _____ como testemunha.",
                "Tentei obter a assinatura do cliente, mas não havia um representante disponível no momento do serviço. Pedi ao _____ que assinasse como testemunha, mas ele(a) se negou.",
                "Tentei obter a assinatura do cliente, mas não havia um representante disponível no momento do serviço, razão pela qual foi impossível colher a assinatura do cliente na Ordem de Serviço.",
                "Tentei obter a assinatura do cliente, mas não foi possível registrá-la por falha técnica no dispositivo móvel / falta de internet. Isto posto, a Ordem de Serviço foi enviada para o e-mail cadastrado tão logo o problema técnico foi resolvido."
            ], 
            index=0
        )
        st.divider()
        # Conteúdo do relatório
        conteudo = (f"""----- DESCRIÇÃO DO PROBLEMA ------
-Problema reportado: {st.session_state.problema_reportado}
-Problema encontrado: {st.session_state.problema_encontrado}
-Causa raiz: {st.session_state.causa_raiz}

----- PROCEDIMENTOS REALIZADOS -----
{st.session_state.procedimentos}
-Status do Equipamento: {st.session_state.status_equipamento}        
-Validação: {st.session_state.validacao}        
-Status do Chamado: {st.session_state.status_chamado}        
-Observações: {st.session_state.observacoes}
-Peças consumidas: {st.session_state.pecas_consumidas}
"""
        )
        # Adiciona as peças consumidas no relatório
        for i, peca in enumerate(st.session_state.pecas):
            conteudo += f"Peça {i + 1}: Nome: {peca['nome_peca']}, SMN: {peca['smn']}, Batch ID: {peca['batch_id']}\n"
        # Continua o conteúdo
        conteudo += f"""
----- OBSERVAÇÕES SOBRE O CHAMADO -----
-Avaliação de Segurança (A/S): {st.session_state.as_info}
-Classificação do Chamado: {st.session_state.classificacao_chamado}
-Classificação SC: {st.session_state.classificacao_sc}
-Assinatura: {st.session_state.observacao_assinatura}

As entregas e serviços discriminados neste documento estarão consideradas devidamente entregues e prestadas, formal e tacitamente, exceto se de outra forma expressado pelo cliente, por escrito e enviado a atendimentoaclientehealthcare.br.team@siemens-healthineers.com, em até 2 dias úteis contados desta data.
        """
        # Exibe o conteúdo do relatório
        st.text_area("Relatório", value=conteudo, height=400) 
        # Botão de copiar para a área de transferência
        if st.button("📝 Copiar Conteúdo",type="secondary"):
            st.caption("Confirmar copia?")
            st_copy_to_clipboard(conteudo, before_copy_label="📝 Deseja copiar conteúdo ? ", after_copy_label="👍 Conteúdo copiado com sucesso",show_text=False)
        # Função para limpar os campos do formulário       
        if st.button("❌ Limpar Dados"):
                limpar_dados()
                st.success("Dados limpos com sucesso!")
       
            
    # Campo de e-mail e número de chamado
        st.divider()
                # Interface Streamlit
        st.title("Envio de E-mail via Outlook")
        st.session_state.email = st.text_input("E-mail de pesquisa de satisfação", value=st.session_state.email)
        st.session_state.numero_chamado = st.text_input("Número do chamado")


        # Campos de input
        destinatario = st.text_input("Destinatário",value = 'fw.bizio@gmail.com')
        assunto = st.text_input("Assunto",value="Pesquisa de Satisfação")
        corpo = st.text_area("Corpo do E-mail", value=f'Chamado: {st.session_state.numero_chamado} \n Contato: {st.session_state.email}')

        # Botão para enviar o e-mail
        if st.button("Enviar E-mail"):
            if destinatario and assunto and corpo:
                try:
                    enviar_email(destinatario, assunto, corpo)
                    st.success(f"E-mail enviado para {destinatario}")
                except Exception as e:
                    st.error(f"Ocorreu um erro ao enviar o e-mail: {str(e)}")
            else:
                st.error("Por favor, preencha todos os campos antes de enviar.")


with tab2:
    st.markdown("### Script Follow Up")
    col1, col3 = st.columns(2)
    with col1:
        st.markdown("#### Informações para o próximmo CSE que irá continuar o atendimento")
        st.session_state.problema_e = st.selectbox("O problema é", ["", "Fixo", "Reproduzivel","Intermitente"], index=0)
        st.session_state.plano_de_acao = st.text_area("Plano de Ação para próximo atendimento", value=st.session_state.plano_de_acao)

        #Peças em teste?
        st.session_state.pecas_em_teste = st.radio("Peças em teste", ["Não", "Sim"], index=["Não", "Sim"].index(st.session_state.pecas_em_teste),horizontal=True)
        col1, col2 = st.columns(2)
        if st.session_state.pecas_em_teste == "Sim":
            with col1:
                st.session_state.informar_pecas = st.text_area("Informar Peças que estão montaqdas no equipamento em testes", value=st.session_state.informar_pecas)
            with col2:
                st.session_state.local_pecas = st.text_area("Informar local das peças e/ou caixas das peças em teste no cliente", value=st.session_state.local_pecas)

    with col3:    
        #Informação para coordenadores de atendimento
        st.markdown("#### Informação para coordenadores de atendimento")
        #Tempo previsto para proximo atendimento
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.prox_visita = st.text_input("Tempo previsto para próxima visita (Hr)", value=st.session_state.prox_visita)
        with col2:
            #Tempo previsto para reenvio do chamado
            st.session_state.reenvio_chamado = st.text_input("Tempo previsto para reenvio do chamado (dias)", value=st.session_state.reenvio_chamado)
            #Complexidade do Atendimento
        st.session_state.complexidade_atendimento = st.selectbox("Complexidade do Atendimento", ["","Baixa", "Media", "Alta"], index=["","Baixa", "Media", "Alta"].index(st.session_state.complexidade_atendimento))
        #Ferramentas especiais
        st.session_state.ferramentas_especiais = st.radio("Ferramentas especiais", ["Não", "Sim"], index=["Não", "Sim"].index(st.session_state.ferramentas_especiais),horizontal=True)
        if st.session_state.ferramentas_especiais == "Sim":
            st.session_state.ferramenta = st.text_input("Descreva abaixo os detalhes caso houver necessidade de ferramentas especiais", value=st.session_state.ferramenta)
            


        #peças Solicitadas para proximo atendimento ?
        st.session_state.pecas_prox_atendimento = st.radio("Peças solicitadas para próximo atendimento", ["Não", "Sim"], index=["Não", "Sim"].index(st.session_state.pecas_prox_atendimento),horizontal=True)
        if st.session_state.pecas_prox_atendimento == "Sim":
                if st.button("Solicitar nova peça"):
                    st.session_state.new_pecas.append({"nome_peca2": "", "pn":""})

                col1, col2 = st.columns(2)
                for i, new_peca in enumerate(st.session_state.new_pecas):
                    with col1:
                        new_peca["nome_peca2"] = st.text_input(f"Nome da peça {i + 1}", value=new_peca["nome_peca2"], key=f"nome_peca2_{i}")
                    with col2:
                        new_peca["pn"] = st.text_input(f"PN {i + 1}", value=new_peca["pn"], key=f"pn_{i}")

        #Left on Notification com selectbox
        st.session_state.left_on_notification = st.selectbox("Left on Notification", ["N/A", "1 - Envio de mais peças (agendar ida CSE e Cliente(parada equipamento))", "2 - Peças em teste (sem retorno CSE e sem agendamento cliente)","3 - Peças em teste (somente agendar ida CSE ao cliente)","4 - Peças em teste (agendar ida CSE e cliente (parada equipamento))"], index=["N/A", "1 - Envio de mais peças (agendar ida CSE e Cliente(parada equipamento))", "2 - Peças em teste (sem retorno CSE e sem agendamento cliente)","3 - Peças em teste (somente agendar ida CSE ao cliente)","4 - Peças em teste (agendar ida CSE e cliente (parada equipamento))"].index(st.session_state.left_on_notification))

        #Informação adicional
        st.session_state.infos_add = st.text_area("Informações adicionais", value=st.session_state.infos_add)

        # Botão para copiar conteúdo da aba 2
        conteudo_follow_up = f"""----- INFORMAÇÕES PARA PRÓXIMO CSE -----

- CSE que realizou o atendimento: {st.session_state.nome_cse}
- O problema é: {st.session_state.problema_e}
- Plano de Ação para próximo atendimento: {st.session_state.plano_de_acao}
- Peças em teste: {st.session_state.pecas_em_teste}
- Informar Peças: {st.session_state.informar_pecas}
- Localização das Peças: {st.session_state.local_pecas}

----- INFORMAÇÕES PARA COORDENAÇÃO DE ATENDIMENTO -----

- Tempo previto para próxima visita: {st.session_state.prox_visita} Hr(s)
- Tempo previsto para Reenvio de Chamado: {st.session_state.reenvio_chamado} Dia(s)
- Complexidade do Atendimento: {st.session_state.complexidade_atendimento}
- Ferramentas Especiais Necessárias: {st.session_state.ferramentas_especiais}
- Ferramenta: {st.session_state.ferramenta}
- Peças para o próximo atendimento: {st.session_state.pecas_prox_atendimento}
"""
        for i, new_peca in enumerate(st.session_state.new_pecas):
            conteudo_follow_up += f"Peça {i + 1}: Nome: {new_peca['nome_peca2']}, PN: {new_peca['pn']}\n"

        conteudo_follow_up += f"""- Left on Notification: {st.session_state.left_on_notification}

----- INFORMAÇÕES ADICIONAIS -----
{st.session_state.infos_add}
"""
        if st.button("🧾 Copiar Conteúdo"):
            st.caption("Confirmar copia?")
            st_copy_to_clipboard(conteudo_follow_up, before_copy_label="📝 Deseja copiar conteúdo ?", after_copy_label="👍 Conteúdo copiado com sucesso",show_text=False)            
            # Botão para limpar dados da aba 2
        if st.button("❌ Limpar Dados Follow Up"):
            limpar_dados_aba2()
        st.text_area("Relatório", value=conteudo_follow_up, height=400)


with tab3:
    # Inicializando session state para armazenar dados das peças
    if 'pecas_mp' not in st.session_state:
        st.session_state['pecas_mp'] = [{'peca': '', 'snm': '', 'batch_id': ''}]

    # Função para adicionar um novo conjunto de campos de peça
    def adicionar_novo_campo_mp():
        st.session_state['pecas_mp'].append({'peca': '', 'snm': '', 'batch_id': ''})

    # Função para remover um campo de peça
    def remover_campo_mp(index):
        st.session_state['pecas_mp'].pop(index)

    # Função para gerar conteúdo do relatório
    def gerar_relatorio():
        relatorio = ""
        
        # 1) Condição do equipamento
        relatorio += f"Condição do equipamento: {st.session_state['equipamento_condicao_mp']}\n"
        
        # 2) Problema identificado
        relatorio += f"Problema identificado durante a preventiva: {st.session_state['problema_identificado_mp']}\n"
        if st.session_state['problema_identificado_mp'] == "Sim":
            relatorio += f"Problemas encontrados: {st.session_state['problemas_mp']}\n"
            relatorio += f"Plano de ação: {st.session_state['plano_acao_mp']}\n"
        
        # 3) Inspeções e testes realizados
        relatorio += "Inspeções e Testes Realizados:\n"
        for teste_mp in testes_mp:
            relatorio += f"{teste_mp}: {st.session_state[teste_mp]}\n"
        
        # 4) Peças consumidas no atendimento
        relatorio += f"Peças consumidas no atendimento: {st.session_state['pecas_consumidas_mp']}\n"
        if st.session_state['pecas_consumidas_mp'] == "Sim":
            relatorio += "Peças consumidas:\n"
            for idx_mp, peca_mp in enumerate(st.session_state['pecas_mp']):
                relatorio += f"Peça {idx_mp + 1}: {peca_mp['peca']}, SNM: {peca_mp['snm']}, Batch ID: {peca_mp['batch_id']}\n"
        
        # 5) Observações
        relatorio += f"Observações / Assinatura: {st.session_state['observacao_assinatura_mp']}\n"
        
        return relatorio

    # Título do formulário
    st.title("Formulário de Inspeção e Preventiva de Equipamento")
    col1, col2 = st.columns([2,1])
    with col1:
        # 1) Condição do equipamento
        equipamento_condicao_mp = st.radio(
            "Condição do equipamento:", 
            ["Funcional", "Parado", "Parcialmente Funcional"],
            key='equipamento_condicao_mp', horizontal=True
        )

        # 2) Identificou problema durante a preventiva?
        problema_identificado_mp = st.radio("Identificou problema durante a preventiva?", ("Não", "Sim"), key='problema_identificado_mp',horizontal=True)

        # 2.1) Se sim, descreva os problemas encontrados
        if problema_identificado_mp == "Sim":
            problemas_mp = st.text_input("Descreva os problemas encontrados:", key='problemas_mp')
            plano_acao_mp = st.text_input("Descreva o plano de ação:", key='plano_acao_mp')
        
           # 4) Peças consumidas no atendimento
        pecas_consumidas_mp = st.radio("Peças consumidas no atendimento?", ("Não", "Sim"), key='pecas_consumidas_mp',horizontal=True)

        if pecas_consumidas_mp == "Sim":
            st.subheader("Adicionar peças consumidas")

            # Exibir campos para cada peça adicionada
            for idx_mp, peca_mp in enumerate(st.session_state['pecas_mp']):
                col1_mp, col2_mp, col3_mp, col4_mp = st.columns([3, 3, 3, 1])
                with col1_mp:
                    st.session_state['pecas_mp'][idx_mp]['peca'] = st.text_input(f"Peça {idx_mp + 1}:", key=f'peca_{idx_mp}')
                with col2_mp:
                    st.session_state['pecas_mp'][idx_mp]['snm'] = st.text_input(f"SNM {idx_mp + 1}:", key=f'snm_{idx_mp}')
                with col3_mp:
                    st.session_state['pecas_mp'][idx_mp]['batch_id'] = st.text_input(f"Batch ID {idx_mp + 1}:", key=f'batch_id_{idx_mp}')
                with col4_mp:
                    if st.button("Remover", key=f'remover_peca_{idx_mp}'):
                        remover_campo_mp(idx_mp)
            
            # Botão para adicionar mais campos de peças
            if st.button("Adicionar nova peça"):
                adicionar_novo_campo_mp()

    with col2:
        # 3) Inspeções e testes realizados (Agora utilizando radio buttons)
        st.subheader("Inspeções e Testes Realizados")

        # Lista de testes e inspeções
        testes_mp = [
            "Limpeza do sistema", 
            "Inspeção hidráulica", 
            "Inspeção de segurança", 
            "Inspeção de segurança mecânica", 
            "Inspeção de segurança elétrica", 
            "Qualidade da imagem", 
            "Qualidade do sistema", 
            "Testes finais de segurança", 
            "Testes finais"
        ]

        # Criação de radios para cada item da lista
        for teste_mp in testes_mp:
            st.radio(f"{teste_mp}:", ["OK", "N OK", "N/A"], key=teste_mp,horizontal=True)

 

    # 5) Observações e assinatura
    observacao_assinatura_mp = st.text_area("Observações / Assinatura:", key='observacao_assinatura_mp')

    # Botão para copiar o conteúdo para a área de transferência
    st_copy_to_clipboard(gerar_relatorio(),before_copy_label="📝 Copiar Conteúdo", after_copy_label="👍 Conteúdo copiado com sucesso")
