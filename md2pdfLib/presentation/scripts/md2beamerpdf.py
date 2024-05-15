import os
import subprocess

input_dir = "data/presentation"
output_dir = "data/out"
presentation_name = "beamer_output.pdf"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# List all files in the input directory and sort them numerically based on the prefix
input_files = sorted(
    [
        os.path.join(input_dir, file)
        for file in os.listdir(input_dir)
        if os.path.isfile(os.path.join(input_dir, file))
    ],
    key=lambda x: int(os.path.splitext(os.path.basename(x).split("-")[0])[0]),
)

# # Build the pandoc command
pandoc_cmd = [
    "pandoc",
    *input_files,
    "--resource-path=.",
    "--metadata-file",
    "md2pdfLib/presentation/pandoc/metadata.yml",
    "-t",
    "beamer",
    "--template",
    "md2pdfLib/presentation/pandoc/awesome-beamer-template.tex",
    "--verbose",
    "--pdf-engine",
    "lualatex",
    # "--include-in-header",
    # "latex_template/main.tex",
    # "-V",
    # "theme:awesome",
    "-V",
    "linkcolor:blue",
    "-V",
    "themeoptions:english",
    "-V",
    "themeoptions:secslide",
    "-V",
    "themeoptions:color",
    "-V",
    "themeoptions:listings",
    "-V",
    "themeoptions:footnote",
    "-V",
    "titlegraphic:data/presentation/images/The World's First AI.jpg",
    "-V",
    "institute:Institute of Software Engineering and Programming Languages",
    "-V",
    "themeoptions:coloraccent=white",
    "-V",
    "mainfont=Roboto",
    # "-V", "monofont=SauceCodePro Nerd Font",
    "-o",
    os.path.join(output_dir, presentation_name),
]

# Run the pandoc command
subprocess.run(pandoc_cmd)
