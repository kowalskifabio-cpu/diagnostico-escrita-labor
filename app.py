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

# --- NAVEGAÇÃO LATERAL ---
with st.sidebar:
    st.image("tela inicial.png", use_container_width=True)
    st.markdown("### 🕒 Roteiro de Implementação")
    passo = option_menu(
        menu_title=None,
        options=["1. Abertura", "2. Os 6 Pilares", "3. Diagnóstico e Registro", "4. Dados e Documentos", "5. Mês 1: Arquitetura"],
        icons=["play-fill", "diagram-3", "save", "file-earmark-arrow-up", "gear-fill"],
        menu_icon="cast", default_index=0,
        styles={"nav-link-selected": {"background-color": "#ff9900"}}
    )
    st.divider()
    st.caption("Plano Light - Escrita Contabilidade")

# --- LÓGICA DE CONTEÚDO ---

if passo == "1. Abertura":
    st.markdown('<p class="titulo-sessao">Kick-off: Plano Labor OS</p>', unsafe_allow_html=True)
    st.image("tela inicial.png", use_container_width=True)
    st.markdown('<div class="destaque-box"><strong>Visão de Futuro:</strong><br>Crescimento previsível e alívio operacional em 12 meses.</div>', unsafe_allow_html=True)

elif passo == "2. Os 6 Pilares":
    st.markdown('<p class="titulo-sessao">Estrutura de Governança (12 Meses)</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("🛒 1. Estratégia de Precificação", expanded=True): st.write("Playbook de Precificação e Margem.")
        with st.expander("📊 2. Custeio e Plano de Contas", expanded=True): st.write("Leitura gerencial e centros de custo.")
        with st.expander("💰 3. Rentabilidade por Cliente", expanded=True): st.write("Matriz de decisões sobre a carteira.")
    with col2:
        with st.expander("📜 4. Gestão de Contratos e SLAs", expanded=True): st.write("Padronização e gatilhos de reajuste.")
        with st.expander("🚀 5. Comercial Enxuto", expanded=True): st.write("Slots de Capacidade mensais.")
        with st.expander("📈 6. Indicadores e Rotina", expanded=True): st.write("Governança ativa dos sócios.")

elif passo == "3. Diagnóstico e Registro":
    st.markdown('<p class="titulo-sessao">Mapeamento Estratégico</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="secao-header">💰 Saúde Financeira</p>', unsafe_allow_html=True)
    q1 = st.select_slider("1. Percepção de lucro por contrato:", options=["Déficit", "Subestimado", "Equilibrado", "Lucrativo"], key="diag_q1")
    q_vazamento = st.multiselect("2. Vazamentos de receita:", ["Reuniões extras", "Urgências", "Retrabalho", "Consultoria"])

    st.markdown('<p class="secao-header">⚙️ Eficiência Operacional</p>', unsafe_allow_html=True)
    q2 = st.multiselect("3. Segmentos críticos:", ["Simples", "Presumido", "MEI", "Rural"])
    q3 = st.slider("4. Nível de estresse do time (0-10):", 0, 10, 8)

    st.markdown('<p class="secao-header">🔮 Visão de Futuro</p>', unsafe_allow_html=True)
    q4 = st.text_area("5. Prioridade máxima para os próximos 30 dias?")

    if st.button("🚀 SALVAR DIAGNÓSTICO"):
        try:
            registro = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Cliente": "Escrita Contabilidade",
                "Precificacao": q1,
                "Vazamentos": ", ".join(q_vazamento),
                "Segmentos_Criticos": ", ".join(q2),
                "Nivel_Estresse": q3,
                "Prioridade_30_Dias": q4
            }
            df_atual = conn.read(worksheet="Página1")
            df_novo = pd.DataFrame([registro])
            df_novo = df_novo.reindex(columns=df_atual.columns)
            df_final = pd.concat([df_atual, df_novo], ignore_index=True)
            conn.update(worksheet="Página1", data=df_final)
            st.success("✅ Diagnóstico salvo!")
        except Exception as e: st.error(f"Erro: {e}")

elif passo == "4. Dados e Documentos":
    st.markdown('<p class="titulo-sessao">Solicitação de Materiais</p>', unsafe_allow_html=True)
    st.markdown('<div class="doc-check">📁 <b>Financeiro:</b> Faturamento 12 meses, Plano de Contas e Centros de Custos.</div>', unsafe_allow_html=True)
    st.markdown('<div class="doc-check">📄 <b>Comercial:</b> Modelos de Contrato, Propostas e Tabela atual.</div>', unsafe_allow_html=True)
    st.markdown('<div class="doc-check">⚙️ <b>Operacional:</b> Lista de time e volume de notas.</div>', unsafe_allow_html=True)

elif passo == "5. Mês 1: Arquitetura":
    st.markdown('<p class="titulo-sessao">Mês 1: Arquitetura do Método</p>', unsafe_allow_html=True)
    
    # --- 1. CHECKLIST DE MATERIAIS ---
    st.markdown('<p class="secao-header">✅ Conferência de Materiais</p>', unsafe_allow_html=True)
    st.write("Verifique a entrega dos documentos necessários para a análise de rentabilidade:")
    
    c1, c2 = st.columns(2)
    with c1:
        st.checkbox("Plano de Contas Atual", key="chk_plano")
        st.checkbox("Estrutura de Centros de Custos", key="chk_cc")
    with c2:
        st.checkbox("Relatório de Faturamento (12 meses)", key="chk_fat")
        st.checkbox("Lista de Colaboradores/Setores", key="chk_time")

    st.divider()

    # --- 2. DIAGNÓSTICO AUTOMÁTICO (LIDO DA PLANILHA) ---
    st.markdown('<p class="secao-header">📊 Raio-X do Diagnóstico Anterior</p>', unsafe_allow_html=True)
    
    # Buscando o último registro da planilha
    try:
        df_historico = conn.read(worksheet="Página1")
        ultimo_diagnostico = df_historico.iloc[-1] # Pega a última linha preenchida

        col_a, col_b = st.columns(2)
        with col_a:
            st.info(f"**Prioridade Máxima (30 dias):**\n\n{ultimo_diagnostico['Prioridade_30_Dias']}")
            st.warning(f"**Gargalo Identificado:** Setor {ultimo_diagnostico['Gargalo_Quebra']}")
        
        with col_b:
            st.error(f"**Nível de Sobrecarga:** {ultimo_diagnostico['Nivel_Estresse']}/10")
            st.markdown(f"**Vazamentos de Lucro:**\n{ultimo_diagnostico['Vazamentos']}")

        with st.expander("🔍 Ver Riscos e Barreiras Mapeados"):
            st.write(ultimo_diagnostico['Barreiras'])
            
    except Exception as e:
        st.warning("Aguardando carregamento dos dados históricos da planilha.")

    st.divider()

    # --- 3. INÍCIO DA ARQUITETURA DE PRECIFICAÇÃO ---
    st.markdown('<p class="secao-header">🎯 Definição de Escopo e Pacotes</p>', unsafe_allow_html=True)
    st.write(f"Com base na prioridade de **{ultimo_diagnostico['Prioridade_30_Dias']}**, vamos desenhar os pacotes:")
    
    st.markdown('<p class="pergunta-texto">Serviços que compõem o Recorrente:</p>', unsafe_allow_html=True)
    servicos_base = st.multiselect(
        "Selecione os itens do Pacote Base:",
        ["Escrituração Contábil", "Apuração de Impostos", "Folha de Pagamento", "Certidões Negativas", "Atendimento WhatsApp"],
        default=["Escrituração Contábil", "Apuração de Impostos", "Folha de Pagamento"]
    )

    st.info("💡 **Próximo Passo:** Após definir o escopo, aplicaremos o cálculo de custo sobre o Plano de Contas enviado.")

elif passo == "6. Definição de Escopo e Pacotes":
    st.markdown('<p class="titulo-sessao">🎯 Arquitetura de Pacotes e Serviços</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="destaque-box">
    <strong>Diretriz do Dia:</strong> Eliminar a subjetividade. Se não está no pacote, é extra. 
    Se é extra, tem preço.
    </div>
    """, unsafe_allow_html=True)

    # --- DESENHO DOS PACOTES (CAMPOS ABERTOS) ---
    col_e1, col_e2 = st.columns(2)
    
    with col_e1:
        st.subheader("📦 Estrutura do Pacote")
        nome_pacote = st.text_input("Nome Sugerido para o Plano:", placeholder="Ex: Essencial, Business, Premium...")
        recorrencia = st.text_area("O que compõe a Entrega Recorrente?", 
                                   help="Liste o que o cliente recebe todo mês pelo valor fixo.",
                                   placeholder="Ex: Escrituração, Impostos, 01 Reunião trimestral...")
        
    with col_e2:
        st.subheader("⚡ Gatilhos de Extras")
        extras_texto = st.text_area("O que será cobrado à parte (Fim dos Vazamentos)?", 
                                    help="Itens que hoje são 'de graça' e passariam a ser cobrados.",
                                    placeholder="Ex: Parcelamentos, Alterações, IRPF sócios...")
        criterio = st.text_area("Critério de Enquadramento:", 
                                placeholder="Ex: Até 50 lançamentos mês ou faturamento até X...")

    # --- PERGUNTAS E AFIRMAÇÕES ESTRATÉGICAS ---
    st.markdown('<p class="secao-header">💬 Validação com os Sócios</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="pergunta-texto">"Ao apresentar este novo pacote, qual o maior receio em relação aos 800 clientes atuais?"</p>', unsafe_allow_html=True)
    receio_texto = st.text_area("Resposta dos Sócios:", key="p_receio")

    st.markdown('<p class="pergunta-texto">"Qual a meta de margem de lucro desejada para este novo modelo?"</p>', unsafe_allow_html=True)
    margem_meta = st.text_input("Ex: 30%, 40%...", key="p_margem")

    st.divider()

    # --- BOTÃO DE REGISTRO NA NOVA ABA ---
    if st.button("💾 Registrar Definições de Escopo"):
        try:
            # Conexão com a nova aba 'Planejamento_Pacotes'
            registro_plano = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Cliente": "Escrita Contabilidade",
                "Nome_Pacote": nome_pacote,
                "Itens_Recorrentes": recorrencia,
                "Itens_Extras": extras_texto,
                "Criterio_Precificacao": criterio,
                "Observacoes_Estrategicas": f"Receio: {receio_texto} | Margem: {margem_meta}"
            }
            
            # Lógica para salvar na aba específica
            df_pacotes = conn.read(worksheet="Planejamento_Pacotes")
            df_novo_p = pd.DataFrame([registro_plano])
            df_final_p = pd.concat([df_pacotes, df_novo_p], ignore_index=True)
            
            conn.update(worksheet="Planejamento_Pacotes", data=df_final_p)
            st.balloons()
            st.success("Arquitetura de Pacote registrada com sucesso!")
        except Exception as e:
            st.error(f"Erro ao salvar: {e}. Certifique-se de criar a aba 'Planejamento_Pacotes' na planilha.")
