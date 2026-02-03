import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Labor OS | Diagnóstico Escrita Contabilidade", layout="wide")

# --- CONEXÃO COM GOOGLE SHEETS ---
conn = st.connection("gsheets", type=GSheetsConnection)

# --- ESTILO VISUAL LABOR BUSINESS ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .titulo-sessao { color: #2c3e50; font-size: 32px; font-weight: bold; }
    .sub-sessao { color: #ff9900; font-size: 18px; font-weight: 500; }
    .destaque-box { 
        background-color: #f1f3f6; padding: 20px; border-radius: 15px; 
        border-left: 8px solid #ff9900; margin-bottom: 20px; 
    }
    .pergunta-texto { color: #2c3e50; font-weight: bold; font-size: 18px; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL ---
with st.sidebar:
    st.image("tela inicial.png", use_container_width=True)
    st.markdown("### 🕒 Roteiro da Reunião")
    passo = option_menu(
        menu_title=None,
        options=["1. Abertura", "2. Os 6 Pilares", "3. Diagnóstico Estratégico", "4. Registro Final"],
        icons=["play-fill", "diagram-3", "search", "save"],
        menu_icon="cast", default_index=0,
        styles={"nav-link-selected": {"background-color": "#ff9900"}}
    )
    st.divider()
    st.caption("Plano Light - 12 Meses")

# --- CONTEÚDO ---

if passo == "1. Abertura":
    st.markdown('<p class="titulo-sessao">Kick-off: Plano Labor OS</p>', unsafe_allow_html=True)
    st.image("tela inicial.png", use_container_width=True)
    st.markdown('<div class="destaque-box"><strong>Visão de Futuro:</strong><br>Imagine a Escrita Contabilidade daqui a 12 meses. O crescimento é previsível e você sente total alívio ao olhar os indicadores de lucro real. Como é essa sensação?</div>', unsafe_allow_html=True)
    st.write("### 🎯 Objetivo do Dia")
    st.write("Estabelecer a governança inicial, diagnosticar gargalos e arquitetar as prioridades do Mês 1.")

elif passo == "2. Os 6 Pilares":
    st.markdown('<p class="titulo-sessao">Estrutura de Governança (12 Meses)</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("🛒 1. Estratégia de Precificação", expanded=True):
            st.write("Criar um Playbook de Precificação baseado no custo real. Resultado: Margem garantida.")
        with st.expander("📊 2. Custeio e Plano de Contas", expanded=True):
            st.write("Leitura gerencial e centros de custo. Resultado: Clareza financeira total.")
        with st.expander("💰 3. Rentabilidade por Cliente", expanded=True):
            st.write("Identificar quem dá lucro. Resultado: Matriz para decisões de reprecificação.")
    with col2:
        with st.expander("📜 4. Gestão de Contratos e SLAs", expanded=True):
            st.write("Padronização com gatilhos de reajuste. Resultado: Fim da informalidade.")
        with st.expander("🚀 5. Comercial Enxuto e Capacidade", expanded=True):
            st.write("Slots de Capacidade mensais. Resultado: Crescimento sustentável.")
        with st.expander("📈 6. Indicadores e Rotina", expanded=True):
            st.write("Painel semanal acionável. Resultado: Governança ativa dos sócios.")

elif passo == "3. Diagnóstico Estratégico":
    st.markdown('<p class="titulo-sessao">Mapeamento de Percepções e Gargalos</p>', unsafe_allow_html=True)
    tab_financeiro, tab_operacional, tab_comercial, tab_futuro = st.tabs([
        "💰 Saúde Financeira", "⚙️ Eficiência Operacional", "🚀 Comercial e Vendas", "🔮 Visão de Futuro"
    ])

    with tab_financeiro:
        st.markdown('<p class="pergunta-texto">1. Maturidade da Precificação</p>', unsafe_allow_html=True)
        st.select_slider("Percepção de lucro por contrato:", options=["Déficit", "Subestimado", "Equilibrado", "Lucrativo"], key="q1")
        st.markdown('<p class="pergunta-texto">2. Recuperação de Margem</p>', unsafe_allow_html=True)
        st.radio("Frequência de revisão de contratos:", ["Nunca", "Só sob pedido", "Anual", "Por demanda"], key="q_revisao")
        st.markdown('<p class="pergunta-texto">3. Vazamentos de Receita</p>', unsafe_allow_html=True)
        st.multiselect("Onde perdem dinheiro sem cobrar?", ["Reuniões extras", "Urgências", "Retrabalho", "Consultoria"], key="q_vazamento")

    with tab_operacional:
        st.markdown('<p class="pergunta-texto">4. Drenos de Energia (Segmentação)</p>', unsafe_allow_html=True)
        st.multiselect("Segmentos críticos:", ["Simples", "Presumido", "MEI", "Rural"], key="q2")
        st.markdown('<p class="pergunta-texto">5. Sobrecarga do Time (0-10)</p>', unsafe_allow_html=True)
        st.slider("Nível de estresse:", 0, 10, 7, key="q3")
        st.markdown('<p class="pergunta-texto">6. O Gargalo Real</p>', unsafe_allow_html=True)
        st.selectbox("Onde quebraria primeiro?", ["Atendimento", "Fiscal", "Contábil", "DP"], key="q_quebra")

    with tab_comercial:
        st.markdown('<p class="pergunta-texto">7. Filtro de Entrada</p>', unsafe_allow_html=True)
        st.radio("Critério de aceite:", ["Tudo", "Básico", "Por Segmento", "Rigoroso"], key="q_filtro")
        st.markdown('<p class="pergunta-texto">8. Slots de Capacidade</p>', unsafe_allow_html=True)
        st.number_input("Novos contratos/mês com qualidade:", min_value=0, value=5, key="q7")

    with tab_futuro:
        st.markdown('<p class="pergunta-texto">9. Obstáculos ao Projeto</p>', unsafe_allow_html=True)
        st.text_area("O que pode impedir o sucesso?", key="q_barreiras")
        st.markdown('<p class="pergunta-texto">10. Prioridade Máxima</p>', unsafe_allow_html=True)
        st.text_area("O que resolver nos próximos 30 dias?", key="q4")

elif passo == "4. Registro Final":
    st.markdown('<p class="titulo-sessao">Consolidação de Dados</p>', unsafe_allow_html=True)
    if st.button("🚀 Salvar Diagnóstico na Planilha"):
        try:
            vazamentos = ", ".join(st.session_state.get('q_vazamento', []))
            segmentos = ", ".join(st.session_state.get('q2', []))
            
            novo_registro = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Cliente": "Escrita Contabilidade",
                "Precificacao": st.session_state.get('q1', ''),
                "Revisao_Contratos": st.session_state.get('q_revisao', ''),
                "Vazamentos": vazamentos,
                "Segmentos_Criticos": segmentos,
                "Nivel_Estresse": st.session_state.get('q3', 0),
                "Gargalo_Quebra": st.session_state.get('q_quebra', ''),
                "Filtro_Comercial": st.session_state.get('q_filtro', ''),
                "Slots": st.session_state.get('q7', 0),
                "Barreiras": st.session_state.get('q_barreiras', ''),
                "Prioridade_30_Dias": st.session_state.get('q4', '')
            }
            
            df_atual = conn.read(worksheet="Página1")
            df_novo = pd.DataFrame([novo_registro])
            df_final = pd.concat([df_atual, df_novo], ignore_index=True)
            conn.update(worksheet="Página1", data=df_final)
            st.balloons()
            st.success("Dados registrados com sucesso!")
        except Exception as e:
            st.error(f"Erro: {e}")

st.divider()
st.caption("Labor Business - Inteligência em Gestão")
