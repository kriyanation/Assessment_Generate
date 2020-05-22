import logging
import traceback

from reportlab.pdfgen import canvas
import data_capture_assessment
from reportlab.pdfgen import canvas
from textwrap import wrap

import data_capture_assessment

logger = logging.getLogger("MagicLogger")
def generate_ip_paper(lesson_id,filename,db):
    try:
        data_capture_assessment.TEST_ROW = lesson_id
        text_id = data_capture_assessment.get_ip_data(db)
        text = text_id[1]
        text = text.replace('\n\n\n','\n')
        id = text_id[2]
        title = text_id[0]
        cc = canvas.Canvas(filename)
        cc.setTitle("Learning Assessment")
        cc.setFont("Helvetica", 16)
        cc.drawCentredString(300,820,"A Learning Assessment for "+title)
        cc.setFont("Helvetica", 10)
        wraped_text = "\n".join(wrap(text, 90,replace_whitespace=False))
        textobject = cc.beginText()
        textobject.setTextOrigin(50, 800)
        textobject.textLines(wraped_text)
        cc.drawText(textobject)
        cc.showPage()
        cc.save()
    except:
        print("Assessment paper generation failed")
        logger.error(traceback.print_exc())
