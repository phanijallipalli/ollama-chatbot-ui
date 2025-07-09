import ollama
import gradio as gr

# Default system message
default_system_message = "You are a helpful assistant"

def get_available_models():
    """Get list of available models from Ollama"""
    try:
        response = ollama.list()
        model_names = []
        
        if hasattr(response, 'models'):
            for model in response.models:
                if hasattr(model, 'model'):
                    model_names.append(model.model)
        elif 'models' in response:
            for model in response['models']:
                if hasattr(model, 'model'):
                    model_names.append(model.model)
                elif 'model' in model:
                    model_names.append(model['model'])
        
        return model_names if model_names else ["llama3.2"]
    except Exception as e:
        print(f"Error fetching models: {e}")
        return ["llama3.2"]

def chat(message, history, model_name, system_message):
    if not model_name:
        model_name = "llama3.2"
    
    if not system_message.strip():
        system_message = default_system_message

    messages = [{"role": "system", "content": system_message}]
    
    for msg in history:
        if isinstance(msg, dict):
            messages.append(msg)
        elif isinstance(msg, (list, tuple)) and len(msg) == 2:
            messages.append({"role": "user", "content": msg[0]})
            messages.append({"role": "assistant", "content": msg[1]})
    
    messages.append({"role": "user", "content": message})
    
    try:
        stream = ollama.chat(model=model_name, messages=messages, stream=True)
        
        data = ""
        for chunk in stream:
            if chunk.message.content:
                data += chunk.message.content
                yield data
    except Exception as e:
        yield f"Error: {str(e)}"

available_models = get_available_models()

with gr.Blocks(title="Ollama Chat Interface", theme=gr.themes.Soft(), css="""
    .gradio-container {
        max-height: 100vh;
        overflow: hidden;
    }
    .sidebar {
        background: #f8f9fa;
        padding: 20px;
        border-right: 1px solid #e0e0e0;
        min-height: 80vh;
    }
    .chat-area {
        padding: 20px;
        display: flex;
        flex-direction: column;
        height: 85vh;
    }
    .chatbot-container {
        flex: 1;
        overflow-y: auto;
        margin-bottom: 10px;
    }
    .input-container {
        position: sticky;
        bottom: 0;
        background: white;
        padding-top: 10px;
        z-index: 10;
    }
    .system-message-area {
        background: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        margin-top: 20px;
        border: 1px solid #e0e0e0;
    }
""") as demo:
    
    gr.Markdown("# 🦙 Ollama Chat Interface")
    
    with gr.Row():
        # Sidebar
        with gr.Column(scale=1, elem_classes="sidebar"):
            gr.Markdown("### Settings")
            
            model_dropdown = gr.Dropdown(
                choices=available_models,
                value=available_models[0] if available_models else "llama3.2",
                label="Select Model",
                interactive=True
            )

            with gr.Group(elem_classes="system-message-area"):
                gr.Markdown("**System Message:**")
                system_msg_input = gr.Textbox(
                    value=default_system_message,
                    label="",
                    placeholder="Define AI behavior...",
                    lines=3,
                    max_lines=4,
                    show_label=False
                )
            
            with gr.Row():
                refresh_btn = gr.Button("🔄 Refresh Models", size="sm")
                clear_btn = gr.Button("🗑️ Clear Chat", size="sm")
        
        # Main chat interface
        with gr.Column(scale=3, elem_classes="chat-area"):
            with gr.Column(elem_classes="chatbot-container"):
                chatbot = gr.Chatbot(
                    label="Conversation",
                    type="messages",
                    show_label=True
                )
            
            with gr.Row(elem_classes="input-container"):
                with gr.Column(scale=4):
                    msg_input = gr.Textbox(
                        placeholder="Type your message and press Enter or click Send...",
                        label="",
                        lines=1,
                        max_lines=3,
                        show_label=False
                    )
                with gr.Column(scale=1, min_width=100):
                    send_btn = gr.Button("Send", variant="primary", size="lg")

    def refresh_models():
        new_models = get_available_models()
        return gr.Dropdown(choices=new_models, value=new_models[0] if new_models else "llama3.2")

    def clear_chat():
        return [], ""

    def send_message(message, history, model, system_msg):
        if not message.strip():
            return history, ""
        
        new_history = history + [{"role": "user", "content": message}]
        new_history.append({"role": "assistant", "content": ""})
        
        try:
            ai_response = ""
            for response in chat(message, history, model, system_msg):
                ai_response = response
                new_history[-1] = {"role": "assistant", "content": ai_response}
                yield new_history, ""
        except Exception as e:
            new_history[-1] = {"role": "assistant", "content": f"Error: {str(e)}"}
            yield new_history, ""

    refresh_btn.click(refresh_models, outputs=model_dropdown)
    clear_btn.click(clear_chat, outputs=[chatbot, msg_input])
    
    send_btn.click(
        send_message,
        inputs=[msg_input, chatbot, model_dropdown, system_msg_input],
        outputs=[chatbot, msg_input]
    )
    
    msg_input.submit(
        send_message,
        inputs=[msg_input, chatbot, model_dropdown, system_msg_input],
        outputs=[chatbot, msg_input]
    )

if __name__ == "__main__":
    demo.launch(share=False, show_error=True)
