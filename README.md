Exercício da disciplina de Tópicos Avançados em Tecnologia em Sistemas para internet I

main.py cria e mostra o embedding de um texto passado.

# Instruções
## Configuração do ambiente necessário para rodar o script
Baixe o ollama em sua máquina, seguindo o tutorial [tutorial](https://www.youtube.com/watch?v=8KFE_4fvXG4) se desejar.

Inicie o serviço do ollama na sua máquina com `ollama serve` e baixe o modelo usado no script com `ollama pull snowflake-arctic-embed2:568m` ou use outro modelo de sua preferência, mas saiba que terá que mudar a variável `ollama_model` em main.py

O modelo `snowflake-arctic-embed2:568m` requer 1.3GB de memória ram livre.

Com o serviço do ollama iniciado e o modelo baixado, você deve:
OU inicializar o venv com `.\venv\Scripts\activate` caso seu SO seja windows, caso seu SO seja outro busque como incializar o venv no seu SO.
OU baixar a biblioteca `langchain_community` no seu ambiente python global.

## Execução do script
execute o script com `python main.py` no terminal, espere a pergunta aparecer e passe seu texto para ele.

