

Documentacion
import pdfquery
import io
pdf = pdfquery.PDFQuery(io.BytesIO(response.body))
pdf.load()