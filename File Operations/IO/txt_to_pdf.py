#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Create PDF
# =============================================================================
from fpdf import FPDF 

# Initialize class 
pdf = FPDF() 

# Add a page 
pdf.add_page() 

# Set style 
pdf.set_font("Arial", size = 15) 

# open the text file in read mode 
f = open("test.txt", "r") 

# insert the texts in pdf 
for x in f: 
	pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 

# save the pdf with name .pdf 
pdf.output("myPDF.pdf") 

