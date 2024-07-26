import pdfkit

# Especifica la ruta al ejecutable wkhtmltopdf si no está en el PATH
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# Convertir el informe HTML a PDF
pdfkit.from_file('./reports/report.html', './reports/report.pdf', configuration=config)
