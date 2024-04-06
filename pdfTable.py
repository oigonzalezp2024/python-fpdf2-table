
from fpdf import FPDF

class PdfTable(FPDF):

    def createTable(self, data):
        self.tableConfig(data)
        self.tableSetFont()
        self.tableSetDrawColor()
        self.tableSetLineWidth()
        self.tableDeployment()

    def tableConfig(self, data):
        self.setFont = data['set_font']
        self.setDrawColor = data['set_draw_color']
        self.setLineWidth = data['set_line_width']
        self.borders_layout = data['borders_layout']
        self.width = data['width']
        self.titles = data['titles']
        rows = [self.titles[0]]
        self.rows = rows + data['rows']

    def tableSetFont(self):
        self.set_font(
            family = self.setFont['family'],
            style = self.setFont['style'],
            size = self.setFont['size']
        )

    def tableSetDrawColor(self):
        self.set_draw_color(
            r = self.setDrawColor['r'],
            g = self.setDrawColor['g'],
            b = self.setDrawColor['b']
        )

    def tableSetLineWidth(self):
        self.set_line_width(float(self.setLineWidth))

    def tableDeployment(self):
        with self.table(
            text_align = self.titles[1],
            col_widths = self.titles[2],
            borders_layout = self.borders_layout,
            width = self.width
        ) as table:
            for data_row in self.rows:
                row = table.row()
                for datum in data_row:
                    row.cell(datum)
