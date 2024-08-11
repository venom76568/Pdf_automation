import json
import fitz  # PyMuPDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def read_pdf_template(template_path):
    """Reads a PDF template and extracts text boxes."""
    pdf_document = fitz.open(template_path)
    text_boxes = []

    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text_boxes.append({
            "page_num": page_num,
            "boxes": []
        })
        for bbox in page.get_text("dict")["blocks"]:
            if bbox["type"] == 0:  # Text block
                for line in bbox["lines"]:
                    for span in line["spans"]:
                        text_boxes[-1]["boxes"].append({
                            "bbox": span["bbox"],  # Coordinates of the text box
                            "text": span["text"]  # Text content
                        })

    pdf_document.close()
    return text_boxes


def create_filled_pdf(output_path, text_boxes, data):
    """Creates a filled PDF from a template and data."""
    try:
        c = canvas.Canvas(output_path, pagesize=letter)

        # Check documentation for `fitz.get_text` to understand coordinate origin
        # Adjust y-axis inversion based on the origin point
        page_height = letter[1]  # Store page height for easier calculations

        for page in text_boxes:
            page_num = page["page_num"]
            for box in page["boxes"]:
                x0, y0, x1, y1 = box["bbox"]
                text = data.get(str(page_num), "")  # Adjust key based on your JSON structure

                # Adjust y-coordinates based on origin point and page height
                y0 = page_height - y0
                y1 = page_height - y1

                c.drawString(x0, y0, text)

        c.save()
        print(f"PDF created successfully: {output_path}")
    except Exception as e:
        print(f"Error creating PDF: {e}")


def fill_pdfs_from_json(json_path, template_path, output_path):
    """Fills PDFs from a JSON file and template."""
    try:
        with open(json_path, 'r') as file:
            data_list = json.load(file)

        text_boxes = read_pdf_template(template_path)
        print(text_boxes)
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        for i, data in enumerate(data_list):
            output_file = f"{output_path}/filled_form_{i + 1}.pdf"
            create_filled_pdf(output_file, text_boxes, data)
    except Exception as e:
        print(f"Error processing JSON or generating PDFs: {e}")


if __name__ == "__main__":
    json_path = 'data.json'  # Path to your JSON data file
    template_path = 'form2.pdf'  # Path to your
    output_path = 'filled_forms'  # Output directory for filled PDFs
    fill_pdfs_from_json(json_path, template_path, output_path)
