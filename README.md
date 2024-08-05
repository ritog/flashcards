# PDF2Quiz

### Introduction

- This is a lightweight demo of how LLMs can be used to generate quizzes, i.e. question answer pairs from a PDF file.

- This uses only local LLMs. Only Ollama has been used as model server, and llama3 has been used in this example. You can use other models, too.

- I have tested this on Linux x64 machine running Ubuntu. But, this example is not platform dependent. I tested this on a laptop having NVIDIA RTX 3050 Ti GPU, and the example PDF file takes about 30 seconds to generate answers. Running it on CPU (i5 11th gen) only was tested as well. It takes a slightly longer time, but works.

- Modify the files according to your needs.

#### Steps to Set-Up

1. Install Ollama in your system.
2. Install the model of your choice, here- llama3 (7B)
3. Create a conda environment using the **environment.yaml** file that is provided.

```bash
conda env create -f environment.yml
```

4. Modify the files as you need.
5. First copy the PDF file into the directory and rename it to **source.pdf**.
6. Run the file **pdf_reading_md_gen.py**. It writes **input.md**.
7. Run the **qa_gen.py** file. It writes the file **output.txt**, the final output file.
8. You can reformat it as needed, and import it to Anki.

The file provided here as source is a class material for Buddhist Philosophy taught by Central Institute of Higher Tibetan Studies, Sarnath, via NPTEL, by IIT-Madras.

### Community

Join the [ritoLAB discord] for discussions.
