from pypdflite.pdflite import PDFLite
from pypdflite.pdfobjects.pdfcolor import PDFColor
from pypdflite.pdfobjects.pdfcursor import PDFCursor


def BarChartTest():
    """
    Functional test for drawing eclipses
    """
    # Create PDFLite object
    writer = PDFLite("generated/BarChart.pdf")

    # Set compression defaults to False
    writer.set_compression(False)

    # Set document metadata
    writer.set_information(title="Testing Bar Chart")  # set optional information

    # Get document object
    document = writer.get_document()
    cursor = PDFCursor(100, 300)
    data = [("Sunday", 11.5), ("Monday", 13.9), ("Tuesday", 15.1), ("Wednesday", 15.2), ("Thursday", 16.3),
            ("Friday", 18.0), ("Saturday", 12.1)]

    document.add_simple_bar_chart(data, cursor, 400, 300, axis_titles=("day", "percent chance of retweet"), y_axis_limits=(11, 19), y_axis_frequency=1)

    # Close Document
    writer.close()


if __name__ == '__main__':
    BarChartTest()