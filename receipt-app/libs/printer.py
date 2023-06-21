from fpdf import FPDF

class Printer():
    # def __init__(self, _data_voucherNo, _data_accHead, _data_paidTo, _data_rupeesNo, _data_rupeesTxt, _data_accountOf, _data_byCCNo, _data_bankAccNo, _data_onTime):
    #     self._voucherNo = _data_voucherNo
    #     self._accHead = _data_accHead
    #     self._paidTo = _data_paidTo
    #     self._rupeesNo = _data_rupeesNo
    #     self._rupeesTxt = _data_rupeesTxt
    #     self._accountOf = _data_accountOf
    #     self._byCCNo = _data_byCCNo
    #     self._bankAccNo = _data_bankAccNo
    #     self._onTime = _data_onTime
    
    def startPrinting(self):
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_margins(0, 0, 0)
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(w = 40, h = 10, txt="Hello World!", border = 0, ln = 1, align = '', fill = False, link = '')
        pdf.set_font('Arial', '', 12)
        pdf.ln(50)
        pdf.cell(85)
        pdf.cell(0, 0, 'We have a new line.', 0)
        pdf.output('sample.pdf', 'F')

        # print(self._voucherNo, self._accHead, self._paidTo, self._rupeesNo, self._rupeesTxt, self._accountOf, self._byCCNo, self._bankAccNo, self._onTime)

Printer().startPrinting()