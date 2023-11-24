from createDocs import *
import subprocess

ALL_DOCS_MD_TO_PDF_FLAG=True

createReadme()

removeFile(getPathAllDocs("EN"))
removeFile(getPathAllDocs("JP"))

for di in CONFIG_DATA["docs_config"]:
    py_path=THIS_BASE+di["py_filename"]

    subprocess.run(["python3",py_path],encoding="utf-8")

if(ALL_DOCS_MD_TO_PDF_FLAG):
    def readMd2pdf(md_path:str,pdf_path:str):
        subprocess.run(["pandoc","--pdf-engine=lualatex",md_path,"-s","-o",pdf_path,"-V","documentclass=bxjsarticle","-V","classoption=pandoc"],encoding="utf-8")

    #readMd2pdf(getPathAllDocs("EN",".md"),getPathAllDocs("EN",".pdf"))
    #readMd2pdf(getPathAllDocs("JP",".md"),getPathAllDocs("JP",".pdf"))
