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

# --- ADICIONE O ITEM 7 NO MENU LATERAL ---
# options=[..., "5. Arquitetura (R2)", "6. Escopo e Pacotes (R2)", "7. Registro da R2"]

elif passo == "5. Arquitetura (R2)":
    st.markdown('<p class="titulo-sessao">Reunião 2: Arquitetura e Raio-X</p>', unsafe_allow_html=True)
    
    # Conferência de Materiais
    st.markdown('<p class="secao-header">✅ Conferência de Materiais</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.checkbox("Plano de Contas", key="chk_plano_r2")
        st.checkbox("Centros de Custos", key="chk_cc_r2")
    with c2:
        st.checkbox("Faturamento 12 meses", key="chk_fat_r2")
        st.checkbox("Lista de Time", key="chk_time_r2")

    st.divider()

    # DETALHAMENTO MÁXIMO DO DIAGNÓSTICO (R1)
    st.markdown('<p class="secao-header">📊 Diagnóstico Detalhado (Baseado na R1)</p>', unsafe_allow_html=True)
    try:
        df_hist = conn.read(worksheet="Página1")
        u = df_hist.iloc[-1] # Último registro
        
        # Cards de Destaque
        col_d1, col_d2, col_d3 = st.columns(3)
        col_d1.metric("Nível de Estresse", f"{u['Nivel_Estresse']}/10", delta="Crítico" if int(u['Nivel_Estresse']) > 7 else None)
        col_d2.metric("Gargalo Principal", u['Gargalo_Quebra'])
        col_d3.metric("Clareza de Preço", u['Precificacao'])

        st.markdown('<div class="destaque-box">', unsafe_allow_html=True)
        st.write(f"🎯 **Prioridade Estratégica:** {u['Prioridade_30_Dias']}")
        st.write(f"💸 **Vazamentos Identificados:** {u['Vazamentos']}")
        st.write(f"🚧 **Barreiras Mapeadas:** {u['Barreiras']}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Análise Consultiva (Afirmações Labor Business)
        st.write("### 🧠 Análise Labor Business")
        st.info(f"O setor de **{u['Gargalo_Quebra']}** está operando no limite. A rentabilidade está sendo drenada por **{u['Vazamentos']}**. "
                f"Para atingir o objetivo de **{u['Prioridade_30_Dias']}**, a padronização do escopo no Passo 6 é mandatória.")
    except:
        st.warning("Dados da Reunião 1 não encontrados na planilha.")

elif passo == "6. Escopo e Pacotes (R2)":
    # ... (Mantenha o código do Passo 6 anterior, ele já está funcional para a aba Planejamento_Pacotes)
    st.markdown('<p class="titulo-sessao">Reunião 2: Definição de Escopo e Pacotes</p>', unsafe_allow_html=True)
    # [Código de input de pacotes aqui]

elif passo == "7. Registro da R2":
    st.markdown('<p class="titulo-sessao">📝 Ata e Registro Detalhado (R2)</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="secao-header">Pontos Relevantes da Reunião</p>', unsafe_allow_html=True)
    
    topicos = st.multiselect("Tópicos Discutidos Hoje:", 
                             ["Alinhamento de Expectativas", "Definição de Pacotes", "Revisão de Vazamentos", 
                              "Capacidade Operacional", "Critérios de Reprecificação", "Ajuste de Plano de Contas"])
    
    registro_detalhado = st.text_area("Registro Detalhado da Discussão:", 
                                     placeholder="Descreva as decisões tomadas, falas importantes dos sócios e consensos atingidos...",
                                     height=250)
    
    prox_passos = st.text_area("Próximos Passos (Tarefas):", 
                               placeholder="Ex: Labor vai simular preços; Escrita vai validar lista de clientes no setor Contábil.")

    if st.button("💾 SALVAR ATA DA REUNIÃO 2"):
        try:
            registro_ata = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Cliente": "Escrita Contabilidade",
                "Reuniao_Ref": "R2 - Arquitetura de Pacotes",
                "Topicos_Discutidos": ", ".join(topicos),
                "Registro_Detalhado": registro_detalhado,
                "Proximos_Passos": prox_passos
            }
            df_atas = conn.read(worksheet="Atas_Reuniao")
            df_final_ata = pd.concat([df_atas, pd.DataFrame([registro_ata])], ignore_index=True)
            conn.update(worksheet="Atas_Reuniao", data=df_final_ata)
            st.balloons()
            st.success("Ata da R2 registrada com sucesso!")
        except Exception as e:
            st.error(f"Erro ao salvar: {e}. Verifique se a aba 'Atas_Reuniao' existe.")
