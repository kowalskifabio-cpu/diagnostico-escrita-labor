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
    </style>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL (ATUALIZADA COM O ITEM 6) ---
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

# --- LÓGICA DE CONTEÚDO (PASSOS 1 A 5) ---

if passo == "1. Abertura":
    st.markdown('<p class="titulo-sessao">Kick-off: Plano Labor OS</p>', unsafe_allow_html=True)
    st.image("tela inicial.png", use_container_width=True)
    st.markdown('<div class="destaque-box"><strong>Visão de Futuro:</strong><br>Crescimento previsível e alívio operacional em 12 meses.</div>', unsafe_allow_html=True)

elif passo == "2. Os 6 Pilares":
    st.markdown('<p class="titulo-sessao">Estrutura de Governança (12 Meses)</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("🛒 1. Estratégia de Precificação", expanded=True): st.write("Playbook de Precificação e Margem.")
    with col2:
        with st.expander("📈 6. Indicadores e Rotina", expanded=True): st.write("Governança ativa dos sócios.")

elif passo == "3. Diagnóstico e Registro":
    st.markdown('<p class="titulo-sessao">Mapeamento Estratégico</p>', unsafe_allow_html=True)
    # ... (Seu código anterior do diagnóstico)
    if st.button("🚀 SALVAR DIAGNÓSTICO"):
        st.success("Diagnóstico salvo na Planilha!")

elif passo == "4. Dados e Documentos":
    st.markdown('<p class="titulo-sessao">Solicitação de Materiais</p>', unsafe_allow_html=True)
    st.markdown('<div class="doc-check">📁 <b>Financeiro:</b> Faturamento 12 meses, Plano de Contas e Centros de Custos.</div>', unsafe_allow_html=True)

elif passo == "5. Mês 1: Arquitetura":
    st.markdown('<p class="titulo-sessao">Mês 1: Arquitetura do Método</p>', unsafe_allow_html=True)
    
    # Raio-X Automático baseado no seu diagnóstico real
    st.markdown('<p class="secao-header">📊 Raio-X do Diagnóstico Realizado</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.info("**Prioridade Máxima:** Saber precificar e ver rentabilidade.")
        st.warning("**Gargalo Crítico:** Setor Contábil.")
    with c2:
        st.error("**Sobrecarga Atual:** 8/10.")
        st.markdown("**Vazamentos:** Reuniões extras, Urgências, Consultoria.")

# --- NOVO BLOCO 6: DEFINIÇÃO DE ESCOPO ---

elif passo == "6. Definição de Escopo e Pacotes":
    st.markdown('<p class="titulo-sessao">🎯 Arquitetura de Pacotes e Serviços</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="destaque-box">
    <strong>Estratégia:</strong> Definir pacotes claros para responder se os contratos atuais são rentáveis.
    </div>
    """, unsafe_allow_html=True)

    # Campos abertos para digitação conforme solicitado
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.subheader("📦 Desenho do Pacote")
        nome_p = st.text_input("Nome do Plano:", placeholder="Ex: Plano Essencial")
        itens_rec = st.text_area("Serviços Recorrentes (O que compõe o fixo?):", 
                                 placeholder="Ex: Escrituração Contábil, Apuração de Impostos...",
                                 height=150)
        
    with col_p2:
        st.subheader("⚡ Gestão de Extras")
        itens_ext = st.text_area("Serviços Extras (O que será cobrado à parte?):", 
                                 placeholder="Ex: Reuniões extras, Alterações contratuais...",
                                 height=150)
        criterio_p = st.text_area("Critérios de Enquadramento:", 
                                  placeholder="Ex: Até X lançamentos contábeis/mês...")

    st.markdown('<p class="secao-header">💬 Perguntas de Validação com Sócios</p>', unsafe_allow_html=True)
    p1 = st.text_area("1. Qual o maior receio ao aplicar este novo escopo na base atual?", height=100)
    p2 = st.text_area("2. Qual a margem de lucro mínima aceitável para este modelo?", placeholder="Ex: 30%")

    if st.button("💾 Registrar Estrutura de Pacotes"):
        try:
            # Lógica para salvar na nova aba 'Planejamento_Pacotes'
            novo_p = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Cliente": "Escrita Contabilidade",
                "Nome_Pacote": nome_p,
                "Recorrentes": itens_rec,
                "Extras": itens_ext,
                "Critérios": criterio_p,
                "Margem_Desejada": p2
            }
            # Aqui você deve ter a aba 'Planejamento_Pacotes' criada na sua planilha
            df_p = conn.read(worksheet="Planejamento_Pacotes")
            df_final_p = pd.concat([df_p, pd.DataFrame([novo_p])], ignore_index=True)
            conn.update(worksheet="Planejamento_Pacotes", data=df_final_p)
            st.balloons()
            st.success("Pacote registrado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao salvar na aba 'Planejamento_Pacotes': {e}")

st.divider()
st.caption("Labor Business - Inteligência em Gestão")
