from createDocs import *
import subprocess

createReadme()

removeFile(getPathAllDocs("EN"))
removeFile(getPathAllDocs("JP"))

writeAllDocsOfMetaData("EN","a")
writeAllDocsOfMetaData("JP","a")

for di in CONFIG_DATA["docs_config"]:
    py_path=THIS_BASE+di["py_filename"]

    subprocess.run(["python3",py_path],encoding="utf-8")
