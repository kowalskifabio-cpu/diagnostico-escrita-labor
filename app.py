elif passo == "4. Registro Final":
    st.markdown('<p class="titulo-sessao">Consolidação de Dados</p>', unsafe_allow_html=True)
    st.write("Clique abaixo para salvar o diagnóstico oficial na planilha do Google.")

    if st.button("🚀 Salvar Diagnóstico"):
        try:
            # Capturando e limpando os dados das multiselects
            vazamentos_lista = st.session_state.get('q_vazamento', [])
            segmentos_lista = st.session_state.get('q2', [])
            
            # Criando o dicionário EXATAMENTE com os nomes da sua planilha
            novo_registro = {
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Cliente": "Escrita Contabilidade",
                "Precificacao": str(st.session_state.get('q1', '')),
                "Revisao_Contratos": str(st.session_state.get('q_revisao', '')),
                "Vazamentos": ", ".join(vazamentos_lista) if vazamentos_lista else "",
                "Segmentos_Criticos": ", ".join(segmentos_lista) if segmentos_lista else "",
                "Nivel_Estresse": int(st.session_state.get('q3', 0)),
                "Gargalo_Quebra": str(st.session_state.get('q_quebra', '')),
                "Filtro_Comercial": str(st.session_state.get('q_filtro', '')),
                "Slots": int(st.session_state.get('q7', 0)),
                "Barreiras": str(st.session_state.get('q_barreiras', '')),
                "Prioridade_30_Dias": str(st.session_state.get('q4', ''))
            }
            
            # Lógica de atualização direta
            df_atual = conn.read(worksheet="Página1")
            df_novo = pd.DataFrame([novo_registro])
            
            # Forçamos o DataFrame novo a ter as mesmas colunas do atual para evitar erro de concatenação
            df_novo = df_novo.reindex(columns=df_atual.columns)
            
            df_final = pd.concat([df_atual, df_novo], ignore_index=True)
            conn.update(worksheet="Página1", data=df_final)
            
            st.balloons()
            st.success("Dados registrados com sucesso na planilha!")
        except Exception as e:
            st.error(f"Erro técnico: {e}")
            st.info("Dica: Verifique se a Coluna F na planilha termina com 's' (Segmentos_Criticos).")
