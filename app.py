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

# --- NAVEGAÇÃO LATERAL (ROTEIRO 90 MIN) ---
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

# --- CONTEÚDO DAS ETAPAS ---

if passo == "1. Abertura":
    st.markdown('<p class="titulo-sessao">Kick-off: Plano Labor OS</p>', unsafe_allow_html=True)
    st.image("tela inicial.png", use_container_width=True)
    
    st.markdown('<div class="destaque-box"><strong>Visão de Futuro:</strong><br>Imagine a Escrita Contabilidade daqui a 12 meses. O crescimento é previsível, a precificação é automática e você sente total alívio ao olhar os indicadores de lucro real. Como é essa sensação?</div>', unsafe_allow_html=True)
    
    st.write("### 🎯 Objetivo do Dia")
    st.write("Estabelecer a governança inicial, diagnosticar gargalos e arquitetar as prioridades do Mês 1.")

elif passo == "2. Os 6 Pilares":
    st.markdown('<p class="titulo-sessao">Estrutura de Governança (12 Meses)</p>', unsafe_allow_html=True)
    st.write("Abaixo, detalhamos a fundação do projeto **Labor OS**. Cada pilar é essencial para que a Escrita cresça sem perder a rentabilidade.")
    
    # Organizador em colunas com expansores para detalhamento
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("🛒 1. Estratégia de Precificação", expanded=True):
            st.write("""
            **O Problema:** Preço baseado em 'feeling' ou mercado, sem olhar o custo interno.
            **A Solução:** Criar um Playbook de Precificação com base no *Preço Mínimo Sustentável*.
            **Resultado:** Garantia de margem de lucro em cada novo contrato assinado.
            """)
        
        with st.expander("📊 2. Custeio e Plano de Contas", expanded=True):
            st.write("""
            **O Problema:** Plano de contas contábil que não serve para tomada de decisão.
            **A Solução:** Adequação para leitura gerencial e separação por centros de custo.
            **Resultado:** Clareza sobre onde o escritório gasta e onde ele ganha dinheiro.
            """)
            
        with st.expander("💰 3. Rentabilidade por Cliente", expanded=True):
            st.write("""
            **O Problema:** Não saber quais dos 800 clientes são rentáveis ou deficitários.
            **A Solução:** Implementar a lógica de 'Cliente como Centro de Resultado'.
            **Resultado:** Matriz de rentabilidade para decidir quem manter e quem reprecificar.
            """)

    with col2:
        with st.expander("📜 4. Gestão de Contratos e SLAs", expanded=True):
            st.write("""
            **O Problema:** Clientes que demandam além do contratado sem pagar a mais.
            **A Solução:** Padronização de contratos com limites de escopo e gatilhos de reajuste.
            **Resultado:** Fim da informalidade e proteção da margem operacional.
            """)

        with st.expander("🚀 5. Comercial Enxuto e Capacidade", expanded=True):
            st.write("""
            **O Problema:** Vender sem saber se o time consegue entregar com qualidade.
            **A Solução:** Funil de vendas controlado por 'Slots de Capacidade' mensais.
            **Resultado:** Crescimento sustentável: entra o cliente certo no momento certo.
            """)

        with st.expander("📈 6. Indicadores e Rotina de Gestão", expanded=True):
            st.write("""
            **O Problema:** Dashboard 'enfeite' ou excesso de reuniões sem ação.
            **A Solução:** Painel semanal com indicadores acionáveis (Ticket Médio, Churn, Margem).
            **Resultado:** Governança ativa onde os sócios gerem o negócio, não o operacional.
            """)
elif passo == "3. Diagnóstico Estratégico":
    st.markdown('<p class="titulo-sessao">Mapeamento de Percepções e Gargalos</p>', unsafe_allow_html=True)
    
    # DIVISÃO POR ÁREAS DE INVESTIGAÇÃO
    aba_preço, aba_operacao, aba_capacidade = st.tabs(["💰 Precificação", "⚙️ Operação", "🚀 Capacidade"])

    with aba_preço:
        st.markdown('<p class="pergunta-texto">Como você vê a clareza da precificação atual?</p>', unsafe_allow_html=True)
        st.select_slider("Nível de clareza:", options=["Caos", "Intuitivo", "Razoável", "Sólido"], key="q1")
        
        st.markdown('<p class="pergunta-texto">Qual o critério atual para dar desconto em novas propostas?</p>', unsafe_allow_html=True)
        st.text_area("Notas sobre política de descontos:", key="q5", placeholder="Ex: Intuição do sócio, pressão do cliente...")

    with aba_operacao:
        st.markdown('<p class="pergunta-texto">Quais segmentos drenam mais energia do time hoje?</p>', unsafe_allow_html=True)
        st.multiselect("Selecione os drenos de energia:", ["Simples", "Presumido", "MEI", "Avulsos", "Rural", "Terceiro Setor"], key="q2")
        
        st.markdown('<p class="pergunta-texto">Qual o nível de ruído/estresse operacional (0-10)?</p>', unsafe_allow_html=True)
        st.slider("Intensidade:", 0, 10, 5, key="q3")
        
        st.markdown('<p class="pergunta-texto">Onde acontece o maior volume de retrabalho?</p>', unsafe_allow_html=True)
        st.radio("Principal causa:", ["Falta de documento do cliente", "Erro de digitação interno", "Mudança na legislação", "Falta de integração"], key="q6")

    with aba_capacidade:
        st.markdown('<p class="pergunta-texto">Slots de Capacidade: Quantos novos clientes cabem hoje?</p>', unsafe_allow_html=True)
        st.number_input("Número de novos contratos/mês sem perda de qualidade:", min_value=0, max_value=50, value=5, key="q7")
        
        st.markdown('<p class="pergunta-texto">Visão de Futuro: Qual processo, se resolvido hoje, traria o maior alívio?</p>', unsafe_allow_html=True)
        st.text_area("Notas e Observações Estratégicas:", key="q4", height=150)

elif passo == "4. Registro Final":
    st.markdown('<p class="titulo-sessao">Consolidação de Dados</p>', unsafe_allow_html=True)
    st.write("Revise os pontos e clique no botão abaixo para registrar na planilha oficial.")

    if st.button("🚀 Salvar Diagnóstico na Planilha"):
        try:
            novo_registro = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Cliente": "Escrita Contabilidade",
                "Precificacao": st.session_state.q1,
                "Segmentos_Criticos": ", ".join(st.session_state.q2),
                "Peso_Incerteza": st.session_state.q3,
                "Observacoes": st.session_state.q4
            }
            
            df_atual = conn.read(worksheet="Página1")
            df_novo = pd.DataFrame([novo_registro])
            df_final = pd.concat([df_atual, df_novo], ignore_index=True)
            
            conn.update(worksheet="Página1", data=df_final)
            
            st.balloons()
            st.success("Dados registrados com sucesso!")
        except Exception as e:
            st.error(f"Erro ao salvar: {e}. Verifique as Secrets.")

# --- RODAPÉ ---
st.divider()
st.caption("Labor Business - Governança & Resultados")
