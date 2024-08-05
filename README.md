A simply tool to rename arxiv paper file name to its title

## Install

clone this repository, then installing the dependency (remember to create a python virtual environment like venv or conda)

```
pip install -r requirement.txt
```

## Usage

```
./arxiv-rename2title.py <path/to/pdf or path/to/pdf_directory> 
```

# Sample

before:

```bash
(default) [code-server@suzakuwcx-server arxiv-rename2title]$ ls pdf/
1409.3215.pdf  2206.08317.pdf  2302.08917.pdf  2305.07243v2.pdf  2305.11013.pdf  2310.11010.pdf  2407.10446v1.pdf

(default) [code-server@suzakuwcx-server arxiv-rename2title]$ ./arxiv-rename2title.py ./pdf
```

after:

```
(default) [code-server@suzakuwcx-server arxiv-rename2title]$ ls pdf/
Better-speech-synthesis-through-scaling.pdf
DDFAD--Dataset-Distillation-Framework-for-Audio-Data.pdf
FunASR--A-Fundamental-End-to-End-Speech-Recognition-Toolkit.pdf
ITERATIVE-SHALLOW-FUSION-OF-BACKWARD-LANGUAGE-MODEL-FOR-END-TO-END-SPEECH-RECOGNITION-Atsunori-Ogawa,-Takafumi-Moriya,-Naoyuki-Kamo,-Naohiro-Tawara,-and-Marc-Delcroix-NTT-Corporation,-Japan.pdf
MASSIVELY-MULTILINGUAL-SHALLOW-FUSION-WITH-LARGE-LANGUAGE-MODELS-Ke-Hu,-Tara-N.-Sainath,-Bo-Li,-Nan-Du,-Yanping-Huang,-Andrew-M.-Dai,-Yu-Zhang,-Rodrigo-Cabrera,-Zhifeng-Chen,-Trevor-Strohman-Google-LLC,-USA.pdf
Paraformer--Fast-and-Accurate-Parallel-Transformer-for-Non-autoregressive-End-to-End-Speech-Recognition.pdf
Sequence-to-Sequence-Learning-with-Neural-Networks.pdf
```
