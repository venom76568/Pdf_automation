# Pdf_automation
This code automates the filling pdf irrespective of format of blanks in the document as well as it is applicable for tables in the document also, there are two codes in this repository
1) main.py is the main code in which first the pdf gets converted into docx file and then it finds the text in the document and searches for if the text is present as the key in the JSON file and then replaces with key:value. For tables it iterates through table and then each row and then each cell and searches if text is present and follows the same process as above.
   
2) pdf_automate.py also does the same work but the difference is that in this code, there is no conversion of pdf to word, in this text is extracted from the file and then it is searched in JSON file and then if it is found as key, it appends the value in front of key and returns the pdf, but the problem in this code is that
a)Text is extracted successfully from the file but while recreating pdf file with the key and value pair, I dont know why but the output files are corrupted.

 #how to use both the codes : 
Replace your document in the form of pdf with the form2.pdf and also change the template path in the code to your pdf path and run the code you will get your pdfs as a result in the newy created folder output_pdfs.
