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
    .titulo-sessao { color: #2c3e50; font-size: 32px; font-weight: bold; }
    .secao-header { color: #ff9900; font-size: 22px; font-weight: bold; margin-top: 30px; border-bottom: 2px solid #eee; }
    .destaque-box { background-color: #f1f3f6; padding: 20px; border-radius: 15px; border-left: 8px solid #ff9900; margin-bottom: 20px; }
    .pergunta-texto { color: #2c3e50; font-weight: bold; font-size: 18px; margin-top: 20px; }
    .doc-check { background-color: #fff4e5; padding: 15px; border-radius: 10px; border: 1px solid #ff9900; margin-bottom: 10px; }
    .tabela-historico { font-size: 14px; }
    </style>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL ORGANIZADA POR REUNIÕES ---
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
            "6. Escopo e Pacotes (R2)"
        ],
        icons=["play-fill", "diagram-3", "save", "file-earmark-arrow-up", "gear-fill", "box-seam"],
        menu_icon="cast", default_index=0,
        styles={"nav-link-selected": {"background-color": "#ff9900"}}
    )
    st.divider()
    st.caption("Fase: Diagnóstico e Arquitetura")

# --- LÓGICA DE CONTEÚDO ---

# --- REUNIÃO 1: BLOCOS 1 A 4 ---
if passo == "1. Abertura":
    st.markdown('<p class="titulo-sessao">Kick-off: Plano Labor OS</p>', unsafe_allow_html=True)
    st.image("tela inicial.png", use_container_width=True)
    st.markdown('<div class="destaque-box"><strong>Visão de Futuro:</strong><br>Imagine a Escrita Contabilidade daqui a 12 meses. O crescimento é previsível e você sente total alívio ao olhar os indicadores de lucro real. Como é essa sensação?</div>', unsafe_allow_html=True)

elif passo == "2. Os 6 Pilares":
    st.markdown('<p class="titulo-sessao">Estrutura de Governança (12 Meses)</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("🛒 1. Estratégia de Precificação", expanded=True): st.write("Playbook de Precificação baseado no custo real.")
        with st.expander("📊 2. Custeio e Plano de Contas", expanded=True): st.write("Leitura gerencial e centros de custo.")
    with col2:
        with st.expander("📜 4. Gestão de Contratos e SLAs", expanded=True): st.write("Gatilhos de reajuste.")
        with st.expander("📈 6. Indicadores e Rotina", expanded=True): st.write("Governança ativa dos sócios.")

elif passo == "3. Diagnóstico (R1)":
    st.markdown('<p class="titulo-sessao">Mapeamento Estratégico - Reunião 1</p>', unsafe_allow_html=True)
    q1 = st.select_slider("1. Percepção de lucro por contrato:", options=["Déficit", "Subestimado", "Equilibrado", "Lucrativo"], value="Equilibrado")
    q_revisao = st.radio("2. Frequência de revisão de contratos:", ["Nunca", "Só sob pedido", "Anual", "Por demanda"], horizontal=True)
    q_vazamento = st.multiselect("3. Onde perdem dinheiro sem cobrar?", ["Reuniões extras", "Urgências", "Retrabalho", "Consultoria"])
    q3 = st.slider("4. Nível de estresse do time (0-10):", 0, 10, 8)
    q_quebra = st.selectbox("5. Se dobrar o volume hoje, onde quebra primeiro?", ["Atendimento", "Fiscal", "Contábil", "DP"])
    q4 = st.text_area("6. Prioridade máxima para os próximos 30 dias?")

    if st.button("🚀 SALVAR DIAGNÓSTICO R1"):
        try:
            registro = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"), "Cliente": "Escrita Contabilidade",
                "Precificacao": q1, "Revisao_Contratos": q_revisao, "Vazamentos": ", ".join(q_vazamento),
                "Nivel_Estresse": q3, "Gargalo_Quebra": q_quebra, "Prioridade_30_Dias": q4
            }
            df_atual = conn.read(worksheet="Página1")
            df_novo = pd.DataFrame([registro]).reindex(columns=df_atual.columns)
            df_final = pd.concat([df_atual, df_novo], ignore_index=True)
            conn.update(worksheet="Página1", data=df_final)
            st.balloons(); st.success("✅ Diagnóstico da R1 salvo!")
        except Exception as e: st.error(f"Erro ao salvar: {e}")

elif passo == "4. Materiais (R1)":
    st.markdown('<p class="titulo-sessao">Solicitação de Dados - Reunião 1</p>', unsafe_allow_html=True)
    st.markdown('<div class="doc-check">📁 <b>Financeiro:</b> Relatório 12 meses, Plano de Contas e Centros de Custos.</div>', unsafe_allow_html=True)
    st.markdown('<div class="doc-check">📄 <b>Comercial:</b> Contratos, Propostas e Tabela de Preços.</div>', unsafe_allow_html=True)
    st.warning("⚠️ Solicitar envio em até 48h.")

# --- REUNIÃO 2: BLOCOS 5 E 6 ---
elif passo == "5. Arquitetura (R2)":
    st.markdown('<p class="titulo-sessao">Reunião 2: Arquitetura do Método</p>', unsafe_allow_html=True)
    st.markdown('<p class="secao-header">✅ Conferência de Materiais Enviados</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.checkbox("Plano de Contas", key="chk_plano_r2")
        st.checkbox("Centros de Custos", key="chk_cc_r2")
    with c2:
        st.checkbox("Faturamento 12 meses", key="chk_fat_r2")
        st.checkbox("Lista de Time", key="chk_time_r2")
    
    st.divider()
    st.markdown('<p class="secao-header">📊 Resumo do Diagnóstico (R1)</p>', unsafe_allow_html=True)
    try:
        df_hist = conn.read(worksheet="Página1")
        ult = df_hist.iloc[-1]
        st.info(f"**Prioridade definida na R1:** {ult['Prioridade_30_Dias']}")
    except: st.write("Dados da R1 não encontrados.")

elif passo == "6. Escopo e Pacotes (R2)":
    st.markdown('<p class="titulo-sessao">Reunião 2: Definição de Escopo e Pacotes</p>', unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        nome_plano = st.text_input("Nome do Plano:", placeholder="Ex: Plano Essencial")
        itens_recorrentes = st.text_area("Serviços Recorrentes:", height=100)
    with col_b:
        itens_extras = st.text_area("Serviços Extras (Cobrancas à parte):", height=100)
        criterio_enquadra = st.text_input("Critério de Enquadramento:", placeholder="Ex: Faturamento até 100k")

    p_receio = st.text_area("Maior receio do sócio com este pacote:")
    p_margem = st.text_input("Margem de lucro desejada:")

    if st.button("💾 REGISTRAR PACOTE"):
        try:
            registro_p = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"), "Cliente": "Escrita Contabilidade",
                "Nome_Pacote": nome_plano, "Itens_Recorrentes": itens_recorrentes,
                "Itens_Extras": itens_extras, "Criterio_Enquadramento": criterio_enquadra,
                "Receio_Socio": p_receio, "Margem_Meta": p_margem
            }
            df_p = conn.read(worksheet="Planejamento_Pacotes")
            df_novo_p = pd.DataFrame([registro_p]).reindex(columns=df_p.columns)
            df_final_p = pd.concat([df_p, df_novo_p], ignore_index=True)
            conn.update(worksheet="Planejamento_Pacotes", data=df_final_p)
            st.success(f"✅ Pacote '{nome_plano}' adicionado!")
        except Exception as e: st.error(f"Erro: {e}")

    # --- HISTÓRICO VISUAL ABAIXO DO BOTÃO ---
    st.markdown('<p class="secao-header">📝 Pacotes Desenhados nesta Reunião</p>', unsafe_allow_html=True)
    try:
        df_visual = conn.read(worksheet="Planejamento_Pacotes")
        # Filtra apenas os registros de hoje para mostrar o progresso da reunião atual
        hoje = datetime.now().strftime("%d/%m/%Y")
        df_hoje = df_visual[df_visual['Data'].str.contains(hoje)]
        
        if not df_hoje.empty:
            st.dataframe(df_hoje[['Nome_Pacote', 'Itens_Recorrentes', 'Itens_Extras', 'Margem_Meta']], use_container_width=True)
        else:
            st.info("Nenhum pacote registrado hoje ainda.")
    except:
        st.write("Aguardando primeiro registro...")

st.divider()
st.caption("Labor Business - Inteligência em Gestão")
