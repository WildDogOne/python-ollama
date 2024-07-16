# Ollama Wrapper

## Summary
This operator uses the Ollama library to interact with a specified language model and generate a response to a given question. 

## Inputs
* **question**: (str) The question to be asked to the language model.

## Parameters
* **model**: (str, optional) The name of the language model to use. Defaults to "deepseek-coder-v2".
* **tokens**: (int, optional) The maximum number of tokens to generate in the response. Defaults to -1 (unlimited).
* **context**: (int, optional) The context window size for the model. Defaults to 7168.
* **stream**: (bool, optional) Whether to stream the response as it is generated. Defaults to True.
* **md**: (bool, optional) Whether to display the response as Markdown. Defaults to True.
* **repeat_last**: (int, optional) The number of times to repeat the last token in the response. Defaults to 64.
* **temperature**: (float, optional) The temperature parameter for controlling the randomness of the response. Defaults to 0.8.

## Outputs
* **response**: (str or Markdown object) The generated response from the language model.


## Functionality
The `question_ollama` function uses the Ollama library to interact with a specified language model.

1.  **`run_step`:** This function takes the input question and parameters, constructs a message dictionary for Ollama, and initiates a chat session with the specified model. 
2.  **Helper functions:**
    *   **Streaming (`stream=True`)**: If `stream` is True, the response is generated and printed in chunks as it becomes available. This allows for real-time interaction with the model.

    *   **Markdown output (`md=True`)**: If `md` is True, the final response is rendered as Markdown using IPython's `display(Markdown(...))`. This allows for formatted text and code highlighting within the Jupyter notebook output.

