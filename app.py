import streamlit as st

# Configuração visual
st.set_page_config(page_title="Diagnóstico Labor OS", layout="centered")

# Estilização para ficar "bonito"
st.markdown("""
    <style>
    .stProgress > div > div > div > div { background-color: #ff9900; }
    h1 { color: #2c3e50; }
    .pergunta { font-size: 18px; font-weight: bold; color: #ff9900; margin-top: 25px; }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Diagnóstico Estratégico Labor OS")
st.write("Escrita Contabilidade | Plano Light")

# Barra de progresso para dar sensação de avanço (PNL - Realização)
etapa = st.sidebar.select_slider("Etapas do Diagnóstico", options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
st.progress(etapa * 10)

# --- PERGUNTAS ---

if etapa == 1:
    st.markdown('<p class="pergunta">1. Ao olhar para sua carteira de 800 clientes, qual é a imagem que vem à mente sobre o controle dos prazos?</p>', unsafe_allow_html=True)
    st.radio("Escolha a que mais faz sentido:", ["Uma engrenagem lubrificada", "Um incêndio sendo controlado", "Uma névoa onde não vejo o fim"])

elif etapa == 2:
    st.markdown('<p class="pergunta">2. Se você pudesse ouvir o que o seu time diz no final do dia, qual seria o som predominante?</p>', unsafe_allow_html=True)
    st.select_slider("Nível de ruído operacional:", options=["Silêncio Produtivo", "Conversas Ajustadas", "Murmúrios de Cansaço", "Gritos de Urgência"])

elif etapa == 3:
    st.markdown('<p class="pergunta">3. Qual é a sensação cinestésica (o peso) de fechar um novo contrato hoje sem saber a margem exata?</p>', unsafe_allow_html=True)
    st.slider("Peso da incerteza (0 a 10):", 0, 10, 5)

elif etapa == 4:
    st.markdown('<p class="pergunta">4. Imagine que passamos 12 meses. Como você descreveria a cena de olhar um painel e ver o lucro real por cliente?</p>', unsafe_allow_html=True)
    st.text_area("Descreva essa visão brevemente:")

elif etapa == 5:
    st.markdown('<p class="pergunta">5. Qual desses segmentos hoje parece "sugar" mais a energia vital da operação?</p>', unsafe_allow_html=True)
    st.multiselect("Selecione os drenos de energia:", ["Simples Nacional", "Lucro Presumido", "MEI", "Serviços Avulsos/Projetos"])

elif etapa == 6:
    st.markdown('<p class="pergunta">6. Na sua percepção, o time está "correndo para onde" atualmente?</p>', unsafe_allow_html=True)
    st.selectbox("Direção atual:", ["Em direção ao crescimento", "Em círculos para apagar fogo", "Apenas tentando sobreviver ao mês"])

elif etapa == 7:
    st.markdown('<p class="pergunta">7. Quando falamos em "Slots de Capacidade", qual a clareza você tem sobre quantos novos clientes cabem no escritório este mês?</p>', unsafe_allow_html=True)
    st.select_slider("Nível de clareza:", ["Escuridão total", "Luz de vela", "Luz de escritório", "Sol do meio-dia"])

elif etapa == 8:
    st.markdown('<p class="pergunta">8. Se pudéssemos materializar a segurança jurídica dos seus contratos atuais, eles seriam como:</p>', unsafe_allow_html=True)
    st.radio("Resistência dos contratos:", ["Um cofre de banco", "Uma porta de madeira", "Uma cortina de fumaça"])

elif etapa == 9:
    st.markdown('<p class="pergunta">9. Qual é o principal indicador que, ao ser visualizado toda segunda-feira, traria paz de espírito para você?</p>', unsafe_allow_html=True)
    st.text_input("Ex: Margem por segmento, Churn, Ticket médio...")

elif etapa == 10:
    st.markdown('<p class="pergunta">10. Você está pronto para iniciar essa jornada de 12 meses de construção de governança?</p>', unsafe_allow_html=True)
    if st.button("Sim, vamos construir o Labor OS!"):
        st.balloons()
        st.success("Diagnóstico concluído! Estes dados serão a base da nossa primeira reunião.")
