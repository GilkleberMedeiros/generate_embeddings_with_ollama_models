from langchain_community.embeddings import OllamaEmbeddings


ollama_model = "snowflake-arctic-embed2:568m"

text = input(f"Digite um texto para ver o seu embedding feito com Ollama - {ollama_model}: ")
embedding_model = OllamaEmbeddings(model=ollama_model)
embedding_text = embedding_model.embed_documents([text])

embedding_text_len = len(embedding_text[0])
embedding_text_first_fifteen_elems = embedding_text[0][:15]

print(f"texto usado no embedding: {text}")
print(f"O tamanho do embedding gerado é {embedding_text_len}")
print(f"Os quinze primeiros elementos do embedding são: \n{embedding_text_first_fifteen_elems}")