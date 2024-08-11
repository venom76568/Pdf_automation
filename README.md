# Pdf_automation
This code automates the filling pdf irrespective of format of blanks in the document as well as it is applicable for tables in the document also, there are two codes in this repository
1) main.py is the mai code in which first the pdf gets converted into docx file and then it finds the text in the document and searches for if the text is present as the key in the JSON file and then replaces with key:value
   for tables it iterates through table and then each row and then each cell and searches if text is present and follows the same process as above.
   #steps to use this
   a) replace your document in the form of pdf with the form2
3) pdf_automate.py is also
