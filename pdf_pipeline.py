import pdfquery
import io
import requests

response = requests.get('http://escolar1.unam.mx/Febrero2020/resultados.pdf')

pdf = pdfquery.PDFQuery(io.BytesIO(response.content))
pdf.load()

links_resultados = pdf.tree.xpath('//a[contains(@title, "resultados")]')

print(links_resultados)