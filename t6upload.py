#!/usr/bin/python
import uploadlib

uploadlib.HandleRequest(
    uploadWhat   = "T6 Flight Data",
    uploadPath   = "/home/vhosts/isis-pmr/profile/dropbox/t6upload",
    formInfoHtml = """

<p> Select file to upload<br>
Limit to file extention type listed above </p>
<br>

""")
