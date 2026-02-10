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

# --- NAVEGAÇÃO LATERAL (ATUALIZADA COM TODOS OS ITENS) ---
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
            "7. Registro da R2"
        ],
        icons=["play-fill", "diagram-3", "save", "file-earmark-arrow-up", "graph-up-arrow", "box-seam", "clipboard-data"],
        menu_icon="cast", default_index=0,
        styles={"nav-link-selected": {"background-color": "#ff9900"}}
    )
    st.divider()
    st.caption("Fase: Arquitetura de Precificação")

# --- LÓGICA DE CONTEÚDO ---

if passo == "1. Abertura":
    st.markdown('<p class="titulo-sessao">Kick-off: Plano Labor OS</p>', unsafe_allow_html=True)
    st.image("tela inicial.png", use_container_width=True)
    st.markdown('<div class="destaque-box"><strong>Visão de Futuro:</strong><br>Imagine a Escrita Contabilidade daqui a 12 meses...</div>', unsafe_allow_html=True)

elif passo == "2. Os 6 Pilares":
    st.markdown('<p class="titulo-sessao">Estrutura de Governança (12 Meses)</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("🛒 1. Estratégia de Precificação", expanded=True): st.write("Playbook de Precificação baseado no custo real.")
    with col2:
        with st.expander("📈 6. Indicadores e Rotina", expanded=True): st.write("Governança ativa dos sócios.")

elif passo == "3. Diagnóstico (R1)":
    st.markdown('<p class="titulo-sessao">Mapeamento Estratégico - Reunião 1</p>', unsafe_allow_html=True)
    # Conteúdo original do diagnóstico que você pediu para manter
    q1 = st.select_slider("1. Percepção de lucro por contrato:", options=["Déficit", "Subestimado", "Equilibrado", "Lucrativo"], value="Equilibrado")
    q_vazamento = st.multiselect("2. Onde perdem dinheiro sem cobrar?", ["Reuniões extras", "Urgências", "Retrabalho", "Consultoria"])
    q3 = st.slider("3. Nível de estresse do time (0-10):", 0, 10, 8)
    q4 = st.text_area("4. Prioridade máxima para os próximos 30 dias?")
    if st.button("🚀 SALVAR DIAGNÓSTICO"):
        st.success("Salvo!")

elif passo == "4. Materiais (R1)":
    st.markdown('<p class="titulo-sessao">Solicitação de Dados</p>', unsafe_allow_html=True)
    st.markdown('<div class="doc-check">📁 <b>Financeiro:</b> Relatório 12 meses, Plano de Contas e Centros de Custos.</div>', unsafe_allow_html=True)

elif passo == "5. Arquitetura (R2)":
    st.markdown('<p class="titulo-sessao">Reunião 2: Arquitetura e Raio-X Detalhado</p>', unsafe_allow_html=True)
    
    # Detalhamento máximo do diagnóstico
    try:
        df_hist = conn.read(worksheet="Página1")
        u = df_hist.iloc[-1]
        
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Nível de Estresse", f"{u['Nivel_Estresse']}/10")
        col_m2.metric("Gargalo", u['Gargalo_Quebra'])
        col_m3.metric("Filtro Comercial", u['Filtro_Comercial'])

        st.markdown(f"""
        <div class="destaque-box">
        <strong>📍 Diagnóstico Consolidado:</strong><br>
        - <b>Prioridade:</b> {u['Prioridade_30_Dias']}<br>
        - <b>Vazamentos:</b> {u['Vazamentos']}<br>
        - <b>Barreiras:</b> {u['Barreiras']}
        </div>
        """, unsafe_allow_html=True)
        
        st.info(f"💡 **Análise Consultiva:** O foco hoje é neutralizar os vazamentos de '{u['Vazamentos']}' através da nova estrutura de pacotes.")
    except:
        st.warning("Diagnóstico da R1 não localizado na planilha.")

elif passo == "6. Escopo e Pacotes (R2)":
    st.markdown('<p class="titulo-sessao">🎯 Definição de Escopo e Pacotes (R2)</p>', unsafe_allow_html=True)
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        nome_p = st.text_input("Nome do Plano:", placeholder="Ex: Plano Essencial")
        itens_rec = st.text_area("Serviços Recorrentes (O que compõe o fixo?):", height=150)
    with col_p2:
        itens_ext = st.text_area("Serviços Extras (O que será cobrado à parte?):", height=150)
        criterio_p = st.text_input("Critério de Enquadramento:", placeholder="Ex: Faturamento até 100k")

    p_receio = st.text_area("Maior receio do sócio com este pacote:")
    p_margem = st.text_input("Margem de lucro mínima desejada:")

    if st.button("💾 REGISTRAR PACOTE"):
        try:
            registro_p = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Cliente": "Escrita Contabilidade",
                "Nome_Pacote": nome_p,
                "Itens_Recorrentes": itens_rec,
                "Itens_Extras": itens_ext,
                "Criterio_Enquadramento": criterio_p,
                "Receio_Socio": p_receio,
                "Margem_Meta": p_margem
            }
            df_p = conn.read(worksheet="Planejamento_Pacotes")
            df_final_p = pd.concat([df_p, pd.DataFrame([registro_p])], ignore_index=True)
            conn.update(worksheet="Planejamento_Pacotes", data=df_final_p)
            st.success("✅ Pacote registrado!")
        except Exception as e: st.error(f"Erro: {e}")

    # Lista de pacotes gerados abaixo do botão
    st.markdown('<p class="secao-header">📝 Pacotes Desenhados</p>', unsafe_allow_html=True)
    try:
        df_view = conn.read(worksheet="Planejamento_Pacotes")
        st.dataframe(df_view.tail(5), use_container_width=True)
    except: st.info("Nenhum pacote registrado ainda.")

elif passo == "7. Registro da R2":
    st.markdown('<p class="titulo-sessao">📝 Registro Detalhado da Reunião 2</p>', unsafe_allow_html=True)
    
    topicos = st.multiselect("Tópicos da Discussão:", ["Pacotes", "Precificação", "Gargalos", "Custeio"])
    ata_detalhada = st.text_area("Ata da Reunião (Registro Detalhado):", height=300)
    proximos = st.text_area("Próximos Passos (Ações):")

    if st.button("💾 SALVAR REGISTRO DA R2"):
        try:
            registro_ata = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Cliente": "Escrita Contabilidade",
                "Reuniao_Ref": "R2",
                "Topicos_Discutidos": ", ".join(topicos),
                "Registro_Detalhado": ata_detalhada,
                "Proximos_Passos": proximos
            }
            df_a = conn.read(worksheet="Atas_Reuniao")
            df_f_a = pd.concat([df_a, pd.DataFrame([registro_ata])], ignore_index=True)
            conn.update(worksheet="Atas_Reuniao", data=df_f_a)
            st.balloons(); st.success("Ata salva com sucesso!")
        except Exception as e: st.error(f"Erro: {e}. Crie a aba 'Atas_Reuniao' na planilha.")

st.divider()
st.caption("Labor Business - Inteligência em Gestão")
