import ollama
from tqdm import trange

MD_FILE_PATH = "input.md"
DEST_PATH = "output.txt"
MODEL_NAME = "llama3:latest"

PROMPT_PREFIX = "Generate as many question-answer pairs as possible from the passage. Generate all question-answer pairs possible. Remember that each pair is intended for an entry into an Anki flashcards deck. Include descriptive answers as well as very short answers:"

with open(MD_FILE_PATH, "r") as input_f:
    content = input_f.read()

content_ls = content.split("Component")[:-1]


def write_qas(example=False, verbose=False):
    """
    Generates Q-A pairs, and writes them to DEST_PATH.
    example: Bool -> generates QA pairs using the provided document
    verbose: Bool -> prints the generated QAs to terminal
    """
    if example:
        for i in trange(len(content_ls)):
            if i not in [0, 1, 4, 5]:
                my_prompt = f"{PROMPT_PREFIX} {content_ls[i]}"
                model_response = ollama.generate(model=MODEL_NAME, prompt=my_prompt)
                qa_pairs = model_response["response"]
                if verbose:
                    print(qa_pairs)
    else:
        my_prompt = f"{PROMPT_PREFIX} {content}"
        model_response = ollama.generate(model=MODEL_NAME, prompt=my_prompt)
        qa_pairs = model_response["response"]
        if verbose:
            print(qa_pairs)

    with open(DEST_PATH, "a") as output_f:
        output_f.write(qa_pairs)

    return


if __name__ == "__main__":
    # set example=False to generate QAs on your own document
    write_qas(example=False, verbose=True)
