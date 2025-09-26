A simply tool to rename arxiv paper file name to its title offline

## Install

Clone this repository, then build and install this tool with uv

```
uv build
uv tool install dist/arxiv2title-0.1.0-py3-none-any.whl
#
# Options, only if you hasn't add ~/.local/bin to your PATH environment
#
# uv tool update-shell
```

Then you can tab-complete the command 'arxiv2title' in the shell

## Uninstall

```
uv tool uninstall arxiv2title
```

## Usage

```
arxiv2title <path/to/pdf or path/to/pdf_directory> 
```

# Sample

before:

```bash
[code-server@suzakuwcx-server arxiv-rename2title]$ ls pdf/
1409.3215.pdf  2206.08317.pdf  2302.08917.pdf  2305.07243v2.pdf  2305.11013.pdf  2310.11010.pdf  2407.10446v1.pdf

[code-server@suzakuwcx-server arxiv-rename2title]$ arxiv2title ./pdf
```

after:

```
[code-server@suzakuwcx-server arxiv-rename2title]$ ls pdf/
Better-speech-synthesis-through-scaling.pdf
DDFAD--Dataset-Distillation-Framework-for-Audio-Data.pdf
FunASR--A-Fundamental-End-to-End-Speech-Recognition-Toolkit.pdf
ITERATIVE-SHALLOW-FUSION-OF-BACKWARD-LANGUAGE-MODEL-FOR-END-TO-END-SPEECH-RECOGNITION.pdf
MASSIVELY-MULTILINGUAL-SHALLOW-FUSION-WITH-LARGE-LANGUAGE-MODELS.pdf
Paraformer--Fast-and-Accurate-Parallel-Transformer-for-Non-autoregressive-End-to-End-Speech-Recognition.pdf
Sequence-to-Sequence-Learning-with-Neural-Networks.pdf
```
