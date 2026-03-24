import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Labor OS | Gestão Escrita Contabilidade", layout="wide")

# --- CONEXÃO COM GOOGLE SHEETS ---
conn = st.connection("gsheets", type=GSheetsConnection)

# --- ESTILO VISUAL LABOR BUSINESS ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .titulo-sessao { color: #2c3e50; font-size: 32px; font-weight: bold; }
    .secao-header { color: #ff9900; font-size: 22px; font-weight: bold; margin-top: 30px; border-bottom: 2px solid #eee; }
    .destaque-box { background-color: #f1f3f6; padding: 20px; border-radius: 15px; border-left: 8px solid #ff9900; margin-bottom: 20px; }
    .pergunta-texto { color: #2c3e50; font-weight: bold; font-size: 18px; margin-top: 20px; }
    .doc-check { background-color: #fff4e5; padding: 15px; border-radius: 10px; border: 1px solid #ff9900; margin-bottom: 10px; }
    .texto-fundamento { font-size: 16px; line-height: 1.6; color: #444; }
    </style>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL (ROTEIRO COMPLETO) ---
with st.sidebar:
    st.image("tela inicial.png", use_container_width=True)
    st.markdown("### 🚀 Jornada de Implementação")
    passo = option_menu(
        menu_title=None,
        options=[
            "1. Abertura", 
            "2. Os 6 Pilares", 
            "3. Diagnóstico (R1)", 
            "4. Materiais (R1)", 
            "5. Arquitetura (R2)",
            "6. Escopo e Pacotes (R2)",
            "7. Registro da R2",
            "8. Gestão e NPS (R3)",
            "9. Estratégia Comercial (R4)",
            "10. Fundamentos e DRE"
        ],
        icons=["play-fill", "diagram-3", "save", "file-earmark-arrow-up", "graph-up-arrow", "box-seam", "clipboard-data", "star-fill", "megaphone-fill", "book-half"],
        menu_icon="cast", default_index=0,
        styles={"nav-link-selected": {"background-color": "#ff9900"}}
    )
    st.divider()
    st.caption("Fase: Diagnóstico e Estrutura Econômica")

# --- BLOCO 1: ABERTURA ---
if passo == "1. Abertura":
    st.markdown('<p class="titulo-sessao">Kick-off: Plano Labor OS</p>', unsafe_allow_html=True)
    st.image("tela inicial.png", use_container_width=True)
    st.markdown('<div class="destaque-box"><strong>Visão de Futuro:</strong><br>Imagine a Escrita Contabilidade daqui a 12 meses. O crescimento é previsível e você sente total alívio ao olhar os indicadores de lucro real. Como é essa sensação?</div>', unsafe_allow_html=True)
    st.write("### 🎯 Objetivo do Dia: Estabelecer governança e diagnosticar gargalos.")

# --- BLOCO 2: OS 6 PILARES ---
elif passo == "2. Os 6 Pilares":
    st.markdown('<p class="titulo-sessao">Estrutura de Governança (12 Meses)</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("🛒 1. Estratégia de Precificação", expanded=True): st.write("Playbook de Precificação baseado no custo real. Resultado: Margem garantida.")
        with st.expander("📊 2. Custeio e Plano de Contas", expanded=True): st.write("Leitura gerencial e centros de custo. Resultado: Clareza financeira total.")
        with st.expander("💰 3. Rentabilidade por Cliente", expanded=True): st.write("Identificar quem dá lucro. Resultado: Matriz para decisões de reprecificação.")
    with col2:
        with st.expander("📜 4. Gestão de Contratos e SLAs", expanded=True): st.write("Padronização com gatilhos de reajuste. Resultado: Fim da informalidade.")
        with st.expander("🚀 5. Comercial Enxuto e Capacidade", expanded=True): st.write("Slots de Capacidade mensais. Resultado: Crescimento sustentável.")
        with st.expander("📈 6. Indicadores e Rotina", expanded=True): st.write("Painel semanal acionável. Resultado: Governança ativa dos sócios.")

# --- BLOCO 3: DIAGNÓSTICO (R1) ---
elif passo == "3. Diagnóstico (R1)":
    st.markdown('<p class="titulo-sessao">Mapeamento Estratégico - Reunião 1</p>', unsafe_allow_html=True)
    st.markdown('<p class="secao-header">💰 Saúde Financeira</p>', unsafe_allow_html=True)
    q1 = st.select_slider("1. Percepção de lucro por contrato:", options=["Déficit", "Subestimado", "Equilibrado", "Lucrativo"], value="Equilibrado")
    q_revisao = st.radio("2. Frequência de revisão de contratos:", ["Nunca", "Só sob pedido", "Anual", "Por demanda"], horizontal=True)
    q_vazamento = st.multiselect("3. Onde perdem dinheiro sem cobrar?", ["Reuniões extras", "Urgências", "Retrabalho", "Consultoria"])

    st.markdown('<p class="secao-header">⚙️ Eficiência Operacional</p>', unsafe_allow_html=True)
    q2 = st.multiselect("4. Segmentos críticos:", ["Simples", "Presumido", "MEI", "Rural"])
    q3 = st.slider("5. Nível de estresse do time (0-10):", 0, 10, 8)
    q_quebra = st.selectbox("6. Se dobrar o volume hoje, onde quebra primeiro?", ["Atendimento", "Fiscal", "Contábil", "DP"])

    st.markdown('<p class="secao-header">🚀 Comercial e Vendas</p>', unsafe_allow_html=True)
    q_filtro = st.radio("7. Critério de aceite de clientes:", ["Tudo", "Básico", "Por Segmento", "Rigoroso"], horizontal=True)
    q7 = st.number_input("8. Novos contratos/mês com qualidade (Slots):", min_value=0, value=5)

    st.markdown('<p class="secao-header">🔮 Visão de Futuro</p>', unsafe_allow_html=True)
    q_barreiras = st.text_area("9. O que pode impedir o sucesso do projeto?")
    q4 = st.text_area("10. Prioridade máxima para os próximos 30 dias?")

    if st.button("🚀 FINALIZAR E SALVAR DIAGNÓSTICO"):
        try:
            registro = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"), "Cliente": "Escrita Contabilidade",
                "Precificacao": q1, "Revisao_Contratos": q_revisao, "Vazamentos": ", ".join(q_vazamento),
                "Segmentos_Criticos": ", ".join(q2), "Nivel_Estresse": q3, "Gargalo_Quebra": q_quebra,
                "Filtro_Comercial": q_filtro, "Slots": q7, "Barreiras": q_barreiras, "Prioridade_30_Dias": q4
            }
            df_atual = conn.read(worksheet="Página1")
            df_novo = pd.DataFrame([registro]).reindex(columns=df_atual.columns)
            df_final = pd.concat([df_atual, df_novo], ignore_index=True)
            conn.update(worksheet="Página1", data=df_final)
            st.balloons(); st.success("✅ Diagnóstico salvo!")
        except Exception as e: st.error(f"Erro ao salvar: {e}")

# --- BLOCO 4: MATERIAIS (R1) ---
elif passo == "4. Materiais (R1)":
    st.markdown('<p class="titulo-sessao">Solicitação de Dados - Mês 1</p>', unsafe_allow_html=True)
    st.markdown('<div class="doc-check">📁 <b>Financeiro:</b> Relatório 12 meses, Plano de Contas e Centros de Custos.</div>', unsafe_allow_html=True)
    st.markdown('<div class="doc-check">📄 <b>Comercial:</b> Contratos, Propostas e Tabela de Preços.</div>', unsafe_allow_html=True)
    st.markdown('<div class="doc-check">⚙️ <b>Operacional:</b> Lista de time e volume de lançamentos.</div>', unsafe_allow_html=True)
    st.warning("⚠️ Enviar em até 48h após esta reunião.")

# --- BLOCO 5: ARQUITETURA (R2) ---
elif passo == "5. Arquitetura (R2)":
    st.markdown('<p class="titulo-sessao">Reunião 2: Arquitetura e Raio-X Detalhado</p>', unsafe_allow_html=True)
    st.markdown('<p class="secao-header">✅ Conferência de Materiais</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.checkbox("Plano de Contas", key="chk_plano_r2")
        st.checkbox("Centros de Custos", key="chk_cc_r2")
    with c2:
        st.checkbox("Faturamento 12 meses", key="chk_fat_r2")
        st.checkbox("Lista de Time", key="chk_time_r2")

    st.divider()

    st.markdown('<p class="secao-header">📊 Detalhamento do Diagnóstico (R1)</p>', unsafe_allow_html=True)
    try:
        df_hist = conn.read(worksheet="Página1")
        u = df_hist.iloc[-1]
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Nível de Estresse", f"{u['Nivel_Estresse']}/10", delta="Crítico" if int(u['Nivel_Estresse']) > 7 else None)
        col_m2.metric("Gargalo Principal", u['Gargalo_Quebra'])
        col_m3.metric("Clareza de Preço", u['Precificacao'])

        st.markdown(f"""
        <div class="destaque-box">
        <strong>📍 Diagnóstico Consolidado:</strong><br>
        - <b>Prioridade 30 dias:</b> {u['Prioridade_30_Dias']}<br>
        - <b>Vazamentos de Lucro:</b> {u['Vazamentos']}<br>
        - <b>Principais Barreiras:</b> {u['Barreiras']}
        </div>
        """, unsafe_allow_html=True)
        st.info(f"💡 **Análise Labor:** O foco hoje é neutralizar os vazamentos de '{u['Vazamentos']}' através da nova estrutura de pacotes.")
    except:
        st.warning("Dados da R1 não localizados.")

# --- BLOCO 6: ESCOPO E PACOTES (R2) ---
elif passo == "6. Escopo e Pacotes (R2)":
    st.markdown('<p class="titulo-sessao">🎯 Definição de Escopo e Pacotes (R2)</p>', unsafe_allow_html=True)
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        nome_p = st.text_input("Nome do Plano:", placeholder="Ex: Plano Essencial")
        itens_rec = st.text_area("Serviços Recorrentes (O que compõe o fixo?):", height=150)
    with col_p2:
        itens_ext = st.text_area("Serviços Extras (O que será cobrado à parte?):", height=150)
        criterio_p = st.text_input("Critério de Enquadramento:", placeholder="Ex: Faturamento até 100k")

    st.markdown('<p class="secao-header">💬 Validação com os Sócios</p>', unsafe_allow_html=True)
    p_receio = st.text_area("Maior receio do sócio com este pacote:")
    p_margem = st.text_input("Margem de lucro mínima desejada:")

    if st.button("💾 REGISTRAR PACOTE"):
        try:
            registro_p = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"), "Cliente": "Escrita Contabilidade",
                "Nome_Pacote": nome_p, "Itens_Recorrentes": itens_rec,
                "Itens_Extras": itens_ext, "Criterio_Enquadramento": criterio_p,
                "Receio_Socio": p_receio, "Margem_Meta": p_margem
            }
            df_p = conn.read(worksheet="Planejamento_Pacotes")
            df_final_p = pd.concat([df_p, pd.DataFrame([registro_p])], ignore_index=True)
            conn.update(worksheet="Planejamento_Pacotes", data=df_final_p)
            st.success("✅ Pacote registrado!")
        except Exception as e: st.error(f"Erro: {e}")

    st.markdown('<p class="secao-header">📝 Pacotes Desenhados nesta Reunião</p>', unsafe_allow_html=True)
    try:
        df_visual = conn.read(worksheet="Planejamento_Pacotes")
        st.dataframe(df_visual.tail(5), use_container_width=True)
    except: st.info("Nenhum pacote registrado ainda.")

# --- BLOCO 7: REGISTRO DA R2 (ATA) ---
elif passo == "7. Registro da R2":
    st.markdown('<p class="titulo-sessao">📝 Registro Detalhado e Ata (R2)</p>', unsafe_allow_html=True)
    topicos = st.multiselect("Tópicos Discutidos Hoje:", ["Alinhamento Inicial", "Definição de Pacotes", "Revisão de Vazamentos", "Capacidade Operacional"])
    ata_detalhada = st.text_area("Registro Detalhado da Discussão (Ata):", height=300)
    proximos = st.text_area("Próximos Passos (Ações e Responsáveis):")

    if st.button("💾 SALVAR REGISTRO DA R2"):
        try:
            registro_ata = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"), "Cliente": "Escrita Contabilidade",
                "Reuniao_Ref": "R2 - Arquitetura", "Topicos_Discutidos": ", ".join(topicos),
                "Registro_Detalhado": ata_detalhada, "Proximos_Passos": proximos
            }
            df_a = conn.read(worksheet="Atas_Reuniao")
            df_f_a = pd.concat([df_a, pd.DataFrame([registro_ata])], ignore_index=True)
            conn.update(worksheet="Atas_Reuniao", data=df_f_a)
            st.balloons(); st.success("✅ Ata da R2 registrada com sucesso!")
        except Exception as e: st.error(f"Erro ao salvar: {e}")

# --- BLOCO 8: GESTÃO E NPS (R3) ---
elif passo == "8. Gestão e NPS (R3)":
    st.markdown('<p class="titulo-sessao">Reunião 3: Gestão de Precificação e NPS</p>', unsafe_allow_html=True)
    st.markdown('<p class="secao-header">⭐ Pesquisa NPS (Net Promoter Score)</p>', unsafe_allow_html=True)
    nps_ajustes = st.text_area("Ajustes necessários no esboço do NPS:", height=150)
    nps_canal = st.selectbox("Canal de Envio Definido:", ["WhatsApp", "E-mail", "Forms Automático", "Manual"])
    
    if st.button("💾 REGISTRAR ESTRATÉGIA NPS"):
        try:
            reg_nps = {"Data": datetime.now().strftime("%d/%m/%Y %H:%M"), "Ajustes": nps_ajustes, "Canal": nps_canal}
            df_nps = conn.read(worksheet="Config_NPS")
            df_f_nps = pd.concat([df_nps, pd.DataFrame([reg_nps])], ignore_index=True)
            conn.update(worksheet="Config_NPS", data=df_f_nps)
            st.success("✅ Salvo!")
        except Exception as e: st.error(f"Erro: {e}")

    st.markdown('<p class="secao-header">📊 Indicadores de Gestão</p>', unsafe_allow_html=True)
    col_i1, col_i2 = st.columns(2)
    with col_i1:
        kpi_nome = st.text_input("Nome do Indicador:")
        kpi_def = st.text_area("Definição e Cálculo:")
    with col_i2:
        kpi_meta = st.text_input("Meta Esperada:")
        kpi_frequencia = st.selectbox("Frequência:", ["Mensal", "Trimestral", "Semestral"])

    if st.button("💾 REGISTRAR INDICADORES"):
        try:
            reg_kpi = {"Data": datetime.now().strftime("%d/%m/%Y %H:%M"), "Indicador": kpi_nome, "Definicao": kpi_def, "Meta": kpi_meta, "Frequencia": kpi_frequencia}
            df_kpi = conn.read(worksheet="Indicadores_Gestao")
            df_f_kpi = pd.concat([df_kpi, pd.DataFrame([reg_kpi])], ignore_index=True)
            conn.update(worksheet="Indicadores_Gestao", data=df_f_kpi)
            st.success("✅ Indicadores salvos!")
        except Exception as e: st.error(f"Erro: {e}")

# --- BLOCO 9: ESTRATÉGIA COMERCIAL (R4) ---
elif passo == "9. Estratégia Comercial (R4)":
    st.markdown('<p class="titulo-sessao">Reunião 4: Estratégia Comercial e Expansão</p>', unsafe_allow_html=True)
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.text_area("Ações de Precificação Atual:", placeholder="Ajustes finos nos contratos...")
        st.text_area("Apresentação Comercial:", placeholder="O que mudar na abordagem?")
    with col_e2:
        st.text_area("Treinamento de Atendimento:", placeholder="Instruções para o contato NPS...")
        st.number_input("Meta de Recomendações (PNL):", value=5)

    st.markdown('<p class="secao-header">🧠 Scripts de Contato (PNL e Conversão)</p>', unsafe_allow_html=True)
    aba_script = st.tabs(["Clientes Insatisfeitos", "Clientes Promotores", "Script Recomendados"])
    with aba_script[0]: st.text_area("Script Detratores:", height=200, value="Olá [Nome], entendo sua frustração...")
    with aba_script[1]: st.text_area("Script Promotores:", height=200, value="Fico feliz! Quem você conhece que merece essa tranquilidade?...")
    with aba_script[2]: st.text_area("Script Recomendados:", height=200, value="Olá, [Nome do Amigo] recomendou seu negócio...")

    if st.button("💾 SALVAR ESTRATÉGIA R4"):
        st.balloons(); st.success("Estratégia salva!")

# --- BLOCO 10: FUNDAMENTOS E DRE ---
elif passo == "10. Fundamentos e DRE":
    st.markdown('<p class="titulo-sessao">Fundamentação Econômica e Diagnóstico de DRE</p>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class="texto-fundamento">
        <h3>Introdução</h3>
        Antes de avançar para qualquer desenvolvimento tecnológico, é importante alinhar um ponto essencial: 
        o desafio atual não está na ausência de uma ferramenta, mas sim na <b>ausência de um modelo de precificação estruturado.</b><br><br>
        Criar um sistema sem corrigir a lógica econômica que sustenta a precificação levará, inevitavelmente, a um resultado 
        visualmente bem construído, porém conceitualmente equivocado. O sistema refletirá os mesmos erros que já existem hoje, 
        apenas de forma mais organizada.<br><br>
        Por isso, este trabalho foi estruturado em três pilares fundamentais:
        <ul>
            <li>Diagnóstico real do desempenho econômico (DRE)</li>
            <li>Definição de um modelo correto de precificação</li>
            <li>Estrutura lógica para desenvolvimento do sistema</li>
        </ul>

        <h3 class="secao-header">1. Diagnóstico do DRE: o que os números realmente mostram</h3>
        Com base na Demonstração de Resultado do Exercício de <b>2025</b>, é possível extrair uma leitura mais profunda da operação.

        <b>Principais indicadores:</b>
        <ul>
            <li>Receita total: R$ 11,88 milhões</li>
            <li>Despesa total: R$ 11,24 milhões</li>
            <li>Lucro final: R$ 630 mil</li>
            <li>Margem líquida aproximada: 5,3%</li>
        </ul>
        
        <b>Análise:</b><br>
        Embora a empresa apresente lucro, a margem é baixa para o modelo de serviços contábeis. Isso indica que o crescimento da receita não está sendo acompanhado por um controle proporcional de custos ou por uma precificação adequada.<br><br>

        <b>1.1 Custo de pessoal elevado</b><br>
        As despesas com pessoal somam aproximadamente R$ 6,87 milhões, representando cerca de 58% da receita. Esse percentual está acima do que se considera saudável (ideal entre 35% e 45%).<br><br>

        <b>1.2 Modelo de precificação desconectado da operação</b><br>
        O modelo atual não reflete o custo real. O que realmente gera custo é o Volume de lançamentos, Documentos fiscais, Número de funcionários e Complexidade.<br><br>

        <h3 class="secao-header">2. Estrutura correta de precificação</h3>
        A correção passa pela construção de um modelo que relacione custo operacional com margem desejada.
        
        <b>2.1 Custo hora da operação:</b> Determinar o custo real por hora produtiva.<br>
        <b>2.2 Mapeamento de esforço:</b> Lançamentos, notas, funcionários, regime tributário.<br>
        <b>2.3 Cálculo do custo por cliente:</b> Visibilidade real de consumo da estrutura.<br>
        <b>2.4 Formação do preço:</b> Margem mínima de 20%, ideal entre 30% e 50%.<br><br>

        <h3 class="secao-header">3. Estrutura do sistema de precificação</h3>
        O sistema deve ser composto por módulos:
        <ul>
            <li><b>Módulo 1:</b> Diagnóstico do cliente</li>
            <li><b>Módulo 2:</b> Motor de custo (Horas)</li>
            <li><b>Módulo 3:</b> Motor de precificação (Margens)</li>
            <li><b>Módulo 4:</b> Análise de carteira (Lucrativos/Neutros/Prejuízo)</li>
            <li><b>Módulo 5:</b> Reprecificação contínua</li>
        </ul>
        
        <h3>Conclusão</h3>
        A construção do sistema não deve começar pela tecnologia, mas pela estrutura econômica. Com a base correta, o sistema torna-se um instrumento de gestão capaz de sustentar o crescimento com rentabilidade.
        </div>
        """, unsafe_allow_html=True)

st.divider()
st.caption("Labor Business - Inteligência em Gestão")
