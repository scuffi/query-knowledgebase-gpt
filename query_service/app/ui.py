import gradio as gr

from pipeline import upload_context_pipeline, upload_question_pipeline, clear_database_pipeline  # noqa: E501
def start_ui():
    with gr.Blocks() as demo:

        gr.Markdown('<center><h1>Query Knowledgebase</h1></center>')
        gr.Markdown("Give some text input as context, then query away!")

        with gr.Row():
            
            with gr.Group():
                question = gr.Textbox(label='Enter your question here')
                qa_btn = gr.Button(variant="primary", value='Submit')
                qa_btn.style(full_width=True)
                
                context = gr.TextArea(label="Enter any contextual knowledge here")
                context_btn = gr.Button(variant="primary", value="Submit Context")
                context_btn.style(full_width=True)
                
                delete_btn = gr.Button(variant="secondary", value="Clear Database")

            with gr.Group():
                answer = gr.Textbox(label='The answer to your question is :')

            qa_btn.click(upload_question_pipeline, inputs=[question], outputs=[answer])
            context_btn.click(upload_context_pipeline, inputs=[context])
            delete_btn.click(clear_database_pipeline)

    demo.launch(server_name="0.0.0.0", server_port=7860)
    