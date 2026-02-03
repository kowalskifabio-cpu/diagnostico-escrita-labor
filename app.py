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
    st.markdown('<p class="sub-sessao">Fase de Investigação Profunda (40-50 min)</p>', unsafe_allow_html=True)

    # Organização por Abas para dar densidade ao conteúdo
    tab_financeiro, tab_operacional, tab_comercial, tab_futuro = st.tabs([
        "💰 Saúde Financeira", "⚙️ Eficiência Operacional", "🚀 Comercial e Vendas", "🔮 Visão de Futuro"
    ])

    with tab_financeiro:
        st.markdown('<p class="pergunta-texto">1. Maturidade da Precificação</p>', unsafe_allow_html=True)
        st.select_slider(
            "Como os sócios enxergam a precisão do preço cobrado hoje vs. o trabalho entregue?",
            options=["Déficit (Pagamos para trabalhar)", "Subestimado", "Equilibrado", "Lucrativo"],
            key="q1"
        )
        
        st.markdown('<p class="pergunta-texto">2. Recuperação de Margem</p>', unsafe_allow_html=True)
        st.radio(
            "Qual a frequência de revisão de contratos antigos na base de 800 clientes?",
            ["Nunca revisamos", "Apenas quando o cliente pede", "Anualmente (IPCA/IGPM)", "Baseado no aumento de demanda do cliente"],
            key="q_revisao"
        )
        
        st.markdown('<p class="pergunta-texto">3. Vazamentos de Receita</p>', unsafe_allow_html=True)
        st.multiselect(
            "Onde vocês sentem que 'perdem' dinheiro sem cobrar?",
            ["Reuniões extras", "Pedidos de urgência", "Consultoria pontual", "Retrabalho por erro do cliente", "Parcelamentos de impostos"],
            key="q_vazamento"
        )

    with tab_operacao:
        st.markdown('<p class="pergunta-texto">4. Drenos de Energia (Segmentação)</p>', unsafe_allow_html=True)
        st.multiselect(
            "Selecione os perfis de clientes que mais geram ruído ou retrabalho:",
            ["Simples Nacional (Serviços)", "Simples Nacional (Comércio)", "Lucro Presumido", "MEI", "Associações/Terceiro Setor", "Rural"],
            key="q2"
        )

        st.markdown('<p class="pergunta-texto">5. Nível de Estresse da Equipe (0-10)</p>', unsafe_allow_html=True)
        st.slider("Qual a percepção de sobrecarga do time atual?", 0, 10, 7, key="q3")

        st.markdown('<p class="pergunta-texto">6. O Gargalo Real</p>', unsafe_allow_html=True)
        st.selectbox(
            "Se o volume de clientes dobrasse hoje, onde o escritório quebraria primeiro?",
            ["Atendimento/Relacionamento", "Setor Fiscal", "Setor Contábil", "Departamento Pessoal", "Tecnologia/Sistemas"],
            key="q_quebra"
        )

    with tab_comercial:
        st.markdown('<p class="pergunta-texto">7. Filtro de Entrada</p>', unsafe_allow_html=True)
        st.radio(
            "Existe um critério de 'cliente ideal' (ICP) ou aceitam qualquer demanda que chega?",
            ["Aceitamos tudo para crescer", "Temos alguns critérios básicos", "Filtramos por faturamento/segmento", "Filtro rigoroso de rentabilidade"],
            key="q_filtro"
        )

        st.markdown('<p class="pergunta-texto">8. Slots de Capacidade</p>', unsafe_allow_html=True)
        st.number_input(
            "Quantos novos clientes o escritório consegue absorver por mês com excelência?",
            min_value=0, max_value=100, value=5, key="q7"
        )

    with tab_futuro:
        st.markdown('<p class="pergunta-texto">9. Obstáculos ao Projeto</p>', unsafe_allow_html=True)
        st.text_area(
            "O que pode impedir a implantação desse método nos próximos 12 meses?",
            placeholder="Ex: Falta de tempo dos sócios, resistência da equipe, sistemas limitados...",
            key="q_barreiras"
        )

        st.markdown('<p class="pergunta-texto">10. Prioridade Máxima</p>', unsafe_allow_html=True)
        st.text_area(
            "Se tivéssemos que resolver apenas UMA coisa nos próximos 30 dias, o que seria?",
            key="q4",
            height=100
        )

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
