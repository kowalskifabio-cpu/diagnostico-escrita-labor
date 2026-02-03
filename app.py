import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Labor OS | Diagnóstico Escrita Contabilidade", layout="wide")

# --- CONEXÃO COM GOOGLE SHEETS ---
# Certifique-se de ter configurado as Secrets no Streamlit Cloud
conn = st.connection("gsheets", type=GSheetsConnection)

# --- ESTILO VISUAL LABOR BUSINESS ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .titulo-sessao { color: #2c3e50; font-size: 32px; font-weight: bold; }
    .sub-sessao { color: #ff9900; font-size: 18px; font-weight: 500; }
    .pnl-box { 
        background-color: #f1f3f6; padding: 20px; border-radius: 15px; 
        border-left: 8px solid #ff9900; margin-bottom: 20px; 
    }
    .pergunta-texto { color: #2c3e50; font-weight: bold; font-size: 18px; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL (ROTEIRO 90 MIN) ---
with st.sidebar:
    st.image("tela inicial.png", use_container_width=True)
    st.markdown("### 🕒 Roteiro da Reunião")
    passo = option_menu(
        menu_title=None,
        options=["1. Abertura", "2. Os 6 Pilares", "3. Diagnóstico PNL", "4. Registro Final"],
        icons=["play-fill", "diagram-3", "brain", "save"],
        menu_icon="cast", default_index=0,
        styles={"nav-link-selected": {"background-color": "#ff9900"}}
    )
    st.divider()
    st.caption("Plano Light - 12 Meses")

# --- CONTEÚDO DAS ETAPAS ---

if passo == "1. Abertura":
    st.markdown('<p class="titulo-sessao">Kick-off: Plano Labor OS</p>', unsafe_allow_html=True)
    st.image("tela inicial.png", use_container_width=True)
    
    st.markdown('<div class="pnl-box"><strong>Ponte ao Futuro (PNL):</strong><br>Imagine a Escrita Contabilidade daqui a 12 meses. O crescimento é previsível, a precificação é automática e você sente total alívio ao olhar os indicadores de lucro real. Como é essa sensação?</div>', unsafe_allow_html=True)
    
    st.write("### 🎯 Objetivo do Dia")
    st.write("Estabelecer a governança inicial, diagnosticar gargalos e arquitetar o Mês 1.")

elif passo == "2. Os 6 Pilares":
    st.markdown('<p class="titulo-sessao">Estrutura de Governança (12 Meses)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🛒 Precificação\n*Método alinhado ao custo real e segmentação.*")
        st.markdown("### 📊 Custeio Gerencial\n*Plano de contas e Centros de Custo.*")
        st.markdown("### 💰 Rentabilidade\n*Cliente como Centro de Resultado.*")
    with col2:
        st.markdown("### 📜 Gestão de Contratos\n*SLAs e limites de escopo padronizados.*")
        st.markdown("### 🚀 Comercial Enxuto\n*Crescimento por slots de capacidade.*")
        st.markdown("### 📈 Indicadores\n*Gestão semanal auditável e acionável.*")

elif passo == "3. Diagnóstico PNL":
    st.markdown('<p class="titulo-sessao">Mapeamento Estratégico</p>', unsafe_allow_html=True)
    st.write("Preencha as percepções dos sócios em tempo real durante a discussão:")

    # Armazenando respostas em variáveis para salvar depois
    st.markdown('<p class="pergunta-texto">1. Como você vê a clareza da precificação atual?</p>', unsafe_allow_html=True)
    percepcao_preço = st.select_slider("Nível de clareza:", options=["Caos", "Intuitivo", "Razoável", "Sólido"], key="q1")

    st.markdown('<p class="pergunta-texto">2. Quais segmentos drenam mais energia do time hoje?</p>', unsafe_allow_html=True)
    segmentos = st.multiselect("Selecione:", ["Simples", "Presumido", "MEI", "Avulsos", "Rural"], key="q2")

    st.markdown('<p class="pergunta-texto">3. Qual o peso da incerteza ao fechar um contrato novo?</p>', unsafe_allow_html=True)
    peso_incerteza = st.slider("Escala 0-10:", 0, 10, 5, key="q3")

    st.markdown('<p class="pergunta-texto">4. Notas e Observações Adicionais:</p>', unsafe_allow_html=True)
    notas = st.text_area("Registre pontos críticos discutidos:", key="q4")

elif passo == "4. Registro Final":
    st.markdown('<p class="titulo-sessao">Consolidação de Dados</p>', unsafe_allow_html=True)
    st.write("Revise os pontos e clique no botão abaixo para enviar os dados para a planilha oficial.")

    if st.button("🚀 Salvar Diagnóstico na Planilha"):
        try:
            # Organizando os dados para a planilha
            novo_registro = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Cliente": "Escrita Contabilidade",
                "Precificacao": st.session_state.q1,
                "Segmentos_Criticos": ", ".join(st.session_state.q2),
                "Peso_Incerteza": st.session_state.q3,
                "Observacoes": st.session_state.q4
            }
            
            # Lógica de salvar no Google Sheets
            df_atual = conn.read(worksheet="Página1")
            df_novo = pd.DataFrame([novo_registro])
            df_final = pd.concat([df_atual, df_novo], ignore_index=True)
            
            conn.update(worksheet="Página1", data=df_final)
            
            st.balloons()
            st.success("Dados registrados com sucesso! A Labor Business já pode iniciar a análise.")
        except Exception as e:
            st.error(f"Erro ao salvar: {e}. Verifique as Secrets do Streamlit.")

# --- RODAPÉ ---
st.divider()
st.caption("Apresentação Gerada pela Labor Business - Governança & Resultados")
