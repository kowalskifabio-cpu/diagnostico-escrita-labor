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
    st.markdown("### 🕒 Roteiro da Reunião")
    passo = option_menu(
        menu_title=None,
        options=["1. Abertura", "2. Os 6 Pilares", "3. Diagnóstico e Registro", "4. Dados e Documentos"],
        icons=["play-fill", "diagram-3", "save", "file-earmark-arrow-up"],
        menu_icon="cast", default_index=0,
        styles={"nav-link-selected": {"background-color": "#ff9900"}}
    )
    st.divider()
    st.caption("Plano Light - 12 Meses")

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
        with st.expander("🛒 1. Estratégia de Precificação", expanded=True): st.write("Playbook de Precificação. Resultado: Margem garantida.")
        with st.expander("📊 2. Custeio e Plano de Contas", expanded=True): st.write("Leitura gerencial e centros de custo. Resultado: Clareza financeira.")
        with st.expander("💰 3. Rentabilidade por Cliente", expanded=True): st.write("Identificar quem dá lucro. Resultado: Matriz de decisões.")
    with col2:
        with st.expander("📜 4. Gestão de Contratos e SLAs", expanded=True): st.write("Gatilhos de reajuste. Resultado: Fim da informalidade.")
        with st.expander("🚀 5. Comercial Enxuto e Capacidade", expanded=True): st.write("Slots de Capacidade mensais. Resultado: Crescimento saudável.")
        with st.expander("📈 6. Indicadores e Rotina", expanded=True): st.write("Painel semanal acionável. Resultado: Governança ativa.")

elif passo == "3. Diagnóstico e Registro":
    st.markdown('<p class="titulo-sessao">Mapeamento Estratégico</p>', unsafe_allow_html=True)
    st.write("Preencha todos os campos abaixo e utilize o botão ao final da página para salvar.")

    # --- SEÇÃO FINANCEIRA ---
    st.markdown('<p class="secao-header">💰 Saúde Financeira</p>', unsafe_allow_html=True)
    q1 = st.select_slider("1. Percepção de lucro por contrato:", options=["Déficit", "Subestimado", "Equilibrado", "Lucrativo"], value="Equilibrado")
    q_revisao = st.radio("2. Frequência de revisão de contratos:", ["Nunca", "Só sob pedido", "Anual", "Por demanda"], horizontal=True)
    q_vazamento = st.multiselect("3. Onde perdem dinheiro sem cobrar?", ["Reuniões extras", "Urgências", "Retrabalho", "Consultoria"])

    # --- SEÇÃO OPERACIONAL ---
    st.markdown('<p class="secao-header">⚙️ Eficiência Operacional</p>', unsafe_allow_html=True)
    q2 = st.multiselect("4. Segmentos críticos (Drenos de energia):", ["Simples", "Presumido", "MEI", "Rural"])
    q3 = st.slider("5. Nível de estresse/sobrecarga do time (0-10):", 0, 10, 7)
    q_quebra = st.selectbox("6. Se dobrar o volume hoje, onde quebra primeiro?", ["Atendimento", "Fiscal", "Contábil", "DP"])

    # --- SEÇÃO COMERCIAL ---
    st.markdown('<p class="secao-header">🚀 Comercial e Vendas</p>', unsafe_allow_html=True)
    q_filtro = st.radio("7. Critério de aceite de clientes:", ["Tudo", "Básico", "Por Segmento", "Rigoroso"], horizontal=True)
    q7 = st.number_input("8. Novos contratos/mês com qualidade (Slots):", min_value=0, value=5)

    # --- SEÇÃO FUTURO ---
    st.markdown('<p class="secao-header">🔮 Visão de Futuro</p>', unsafe_allow_html=True)
    q_barreiras = st.text_area("9. O que pode impedir o sucesso do projeto?")
    q4 = st.text_area("10. Prioridade máxima para os próximos 30 dias?")

    st.divider()

    # --- BOTÃO DE SALVAR NA MESMA PÁGINA ---
    if st.button("🚀 FINALIZAR E SALVAR DIAGNÓSTICO"):
        try:
            # Processamento de dados
            vazamentos = ", ".join(q_vazamento) if q_vazamento else "Nenhum"
            segmentos = ", ".join(q2) if q2 else "Nenhum"
            
            registro = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Cliente": "Escrita Contabilidade",
                "Precificacao": q1,
                "Revisao_Contratos": q_revisao,
                "Vazamentos": vazamentos,
                "Segmentos_Criticos": segmentos,
                "Nivel_Estresse": q3,
                "Gargalo_Quebra": q_quebra,
                "Filtro_Comercial": q_filtro,
                "Slots": q7,
                "Barreiras": q_barreiras if q_barreiras else "Nenhuma",
                "Prioridade_30_Dias": q4 if q4 else "Nenhuma"
            }
            
            df_atual = conn.read(worksheet="Página1")
            df_novo = pd.DataFrame([registro])
            df_novo = df_novo.reindex(columns=df_atual.columns)
            df_final = pd.concat([df_atual, df_novo], ignore_index=True)
            
            conn.update(worksheet="Página1", data=df_final)
            st.balloons()
            st.success("✅ Diagnóstico salvo com sucesso na Planilha!")
        except Exception as e:
            st.error(f"Erro ao salvar: {e}")

elif passo == "4. Dados e Documentos":
    st.markdown('<p class="titulo-sessao">Solicitação de Dados - Mês 1</p>', unsafe_allow_html=True)
    st.write("Para iniciarmos a arquitetura da precificação e a nova leitura gerencial, precisamos dos seguintes itens:")
    
    with st.container():
        st.markdown("""
            <div class="doc-check">
                📁 <strong>Dados Financeiros e Estruturais:</strong><br>
                - Relatório de faturamento dos últimos 12 meses por cliente.<br>
                - <b>Plano de Contas atual</b> (mesmo que esteja em rascunho ou incompleto).<br>
                - <b>Estrutura de Centros de Custos</b> utilizada hoje (ou como você separa as despesas).<br>
                - Lista de custos fixos mensais (Aluguel, Softwares, Folha de Pagamento).
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="doc-check">
                📄 <strong>Dados Comerciais:</strong><br>
                - Modelo de contrato atual utilizado com os clientes.<br>
                - Modelo de proposta comercial enviada para novos leads.<br>
                - Tabela de preços vigente (se houver uma padronizada).
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="doc-check">
                ⚙️ <strong>Dados Operacionais:</strong><br>
                - Lista de colaboradores dividida por setor (Fiscal, Contábil, DP, Atendimento).<br>
                - Estimativa de volume de lançamentos ou notas por segmento (amostragem para cálculo de capacidade).
            </div>
        """, unsafe_allow_html=True)

    st.warning("⚠️ **Próximo Passo:** Organize esses arquivos em uma pasta no Drive ou envie por e-mail em até 48h após esta reunião.")

st.divider()
st.caption("Labor Business - Inteligência em Gestão")
