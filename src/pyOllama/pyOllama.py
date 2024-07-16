import ollama
from IPython.display import display, Markdown

# console = Console()


def question_ollama(
    question="",
    model="deepseek-coder-v2",
    tokens=-1,
    context=7168,
    stream=True,
    md=True,
    repeat_last=64,
    temperature=0.8,
):
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": question}],
        stream=stream,
        options={
            "num_predict": tokens,
            "num_ctx": context,
            "repeat_last_n": repeat_last,
            "temperature": temperature,
        },
    )
    if stream:
        for chunk in response:
            print(chunk["message"]["content"], end="", flush=True)
    else:
        if md:
            display(Markdown(response["message"]["content"]))
        else:
            print(response["message"]["content"])