import gradio as gr
from modules.parse_pdf import process_pdf


# Define Gradio interface
input_file = gr.File(label="Upload PDF")
output_text = gr.Textbox(label="Parsed Text")

gr.Interface(fn=process_pdf, inputs=input_file,
             outputs=output_text, title="PDF Text Parser").launch()
