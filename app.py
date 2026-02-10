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
    </style>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL ---
with st.sidebar:
    st.image("tela inicial.png", use_container_width=True)
    st.markdown("### 🕒 Roteiro de Implementação")
    passo = option_menu(
        menu_title=None,
        options=[
            "1. Abertura", 
            "2. Os 6 Pilares", 
            "3. Diagnóstico e Registro", 
            "4. Dados e Documentos", 
            "5. Mês 1: Arquitetura",
            "6. Definição de Escopo e Pacotes"
        ],
        icons=["play-fill", "diagram-3", "save", "file-earmark-arrow-up", "gear-fill", "box-seam"],
        menu_icon="cast", default_index=0,
        styles={"nav-link-selected": {"background-color": "#ff9900"}}
    )
    st.divider()
    st.caption("Plano Light - Escrita Contabilidade")

# --- LÓGICA DE CONTEÚDO ---

if passo == "1. Abertura":
    st.markdown('<p class="titulo-sessao">Kick-off: Plano Labor OS</p>', unsafe_allow_html=True)
    st.image("tela inicial.png", use_container_width=True)
    st.markdown('<div class="destaque-box"><strong>Visão de Futuro:</strong><br>Imagine a Escrita Contabilidade daqui a 12 meses. O crescimento é previsível e você sente total alívio ao olhar os indicadores de lucro real. Como é essa sensação?</div>', unsafe_allow_html=True)
    st.write("### 🎯 Objetivo do Dia: Estabelecer governança e diagnosticar gargalos.")

elif passo == "2. Os 6 Pilares":
    st.markdown('<p class="titulo-sessao">Estrutura de Governança (12 Meses)</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("🛒 1. Estratégia de Precificação", expanded=True): st.write("Playbook de Precificação baseado no custo real. Resultado: Margem garantida.")
        with st.expander("📊 2. Custeio e Plano de Contas", expanded=True): st.write("Leitura gerencial e centros de custo. Resultado: Clareza financeira.")
        with st.expander("💰 3. Rentabilidade por Cliente", expanded=True): st.write("Identificar quem dá lucro. Resultado: Matriz de decisões.")
    with col2:
        with st.expander("📜 4. Gestão de Contratos e SLAs", expanded=True): st.write("Gatilhos de reajuste. Resultado: Fim da informalidade.")
        with st.expander("🚀 5. Comercial Enxuto e Capacidade", expanded=True): st.write("Slots de Capacidade mensais. Resultado: Crescimento sustentável.")
        with st.expander("📈 6. Indicadores e Rotina", expanded=True): st.write("Painel semanal acionável. Resultado: Governança ativa.")

elif passo == "3. Diagnóstico e Registro":
    st.markdown('<p class="titulo-sessao">Mapeamento Estratégico</p>', unsafe_allow_html=True)
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

elif passo == "4. Dados e Documentos":
    st.markdown('<p class="titulo-sessao">Solicitação de Dados - Mês 1</p>', unsafe_allow_html=True)
    st.markdown('<div class="doc-check">📁 <b>Financeiro:</b> Relatório 12 meses, Plano de Contas e Centros de Custos.</div>', unsafe_allow_html=True)
    st.markdown('<div class="doc-check">📄 <b>Comercial:</b> Contratos, Propostas e Tabela de Preços.</div>', unsafe_allow_html=True)
    st.markdown('<div class="doc-check">⚙️ <b>Operacional:</b> Lista de time e volume de lançamentos.</div>', unsafe_allow_html=True)
    st.warning("⚠️ Enviar em até 48h após esta reunião.")

elif passo == "5. Mês 1: Arquitetura":
    st.markdown('<p class="titulo-sessao">Mês 1: Arquitetura do Método</p>', unsafe_allow_html=True)
    st.markdown('<p class="secao-header">✅ Conferência de Materiais</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.checkbox("Plano de Contas Atual", key="chk_plano")
        st.checkbox("Estrutura de Centros de Custos", key="chk_cc")
    with c2:
        st.checkbox("Relatório de Faturamento (12 meses)", key="chk_fat")
        st.checkbox("Lista de Colaboradores/Setores", key="chk_time")
    
    st.divider()
    st.markdown('<p class="secao-header">📊 Raio-X do Diagnóstico Realizado</p>', unsafe_allow_html=True)
    try:
        df_hist = conn.read(worksheet="Página1")
        ult = df_hist.iloc[-1]
        st.info(f"**Prioridade:** {ult['Prioridade_30_Dias']}")
        st.warning(f"**Gargalo:** {ult['Gargalo_Quebra']} | **Estresse:** {ult['Nivel_Estresse']}/10")
    except: st.write("Realize o diagnóstico no passo 3 primeiro.")

# --- BLOCO 6: DEFINIÇÃO DE ESCOPO E PACOTES ---
elif passo == "6. Definição de Escopo e Pacotes":
    st.markdown('<p class="titulo-sessao">🎯 Definição de Escopo e Pacotes</p>', unsafe_allow_html=True)
    st.markdown('<div class="destaque-box">Com base na prioridade de <b>Saber precificar e ver rentabilidade</b>, vamos desenhar os pacotes.</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("📦 Desenho do Pacote")
        nome_plano = st.text_input("Nome do Plano:", placeholder="Ex: Plano Essencial")
        itens_recorrentes = st.text_area("Serviços Recorrentes (O que compõe o fixo?):", height=150)
    with col_b:
        st.subheader("⚡ Gestão de Extras")
        itens_extras = st.text_area("Serviços Extras (O que será cobrado à parte?):", height=150)
        criterio_enquadra = st.text_area("Critérios de Enquadramento:", placeholder="Ex: Até X lançamentos/mês")

    st.markdown('<p class="secao-header">💬 Perguntas e Afirmações</p>', unsafe_allow_html=True)
    pergunta_1 = st.text_area("1. Qual o maior receio ao aplicar este escopo na base atual?")
    afirmacao_1 = st.text_input("2. Margem de lucro mínima desejada (Afirmação do sócio):")

    if st.button("💾 REGISTRAR DEFINIÇÃO DE PACOTES"):
        try:
            registro_p = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"), "Cliente": "Escrita Contabilidade",
                "Nome_Pacote": nome_plano, "Itens_Recorrentes": itens_recorrentes,
                "Itens_Extras": itens_extras, "Criterio_Enquadramento": criterio_enquadra,
                "Receio_Socio": pergunta_1, "Margem_Meta": afirmacao_1
            }
            df_p = conn.read(worksheet="Planejamento_Pacotes")
            df_novo_p = pd.DataFrame([registro_p]).reindex(columns=df_p.columns)
            df_final_p = pd.concat([df_p, df_novo_p], ignore_index=True)
            conn.update(worksheet="Planejamento_Pacotes", data=df_final_p)
            st.balloons(); st.success("✅ Pacote registrado na aba Planejamento_Pacotes!")
        except Exception as e: st.error(f"Erro: {e}. Certifique-se de criar a aba na planilha.")

st.divider()
st.caption("Labor Business - Inteligência em Gestão")
