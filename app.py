import streamlit as st
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer #type: ignore

# ✅ Initialize Streamlit App
st.title("🗣️ AI Debate Assistant - LLaMA-2-7B")
st.write("Optimized for Mac M2 with Metal (MPS)")

# ✅ Use Apple Metal Backend (MPS)
device = "mps" if torch.backends.mps.is_available() else "cpu"

# ✅ Load Model (Optimized for MPS)
MODEL_NAME = "debate_model_finetuned"

@st.cache_resource  # ✅ Cache model & tokenizer separately
def load_model():
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME, torch_dtype=torch.float16
    ).to(device)
    return model

@st.cache_resource
def load_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token
    return tokenizer

model = load_model()
tokenizer = load_tokenizer()

# ✅ User Input for Debate Topic
debate_topic = st.text_input("Enter Debate Topic:", "Should AI replace human teachers?")
debate_position = st.radio("Select Your Position:", ["Pro", "Con"])
debate_stage = st.radio("Select Debate Stage:", ["Opening", "Counterargument", "Rebuttal"])

# ✅ Generate Argument
if st.button("Generate Argument"):
    with st.spinner("Generating argument... ⏳"):
        prompt = f"Debate Topic: {debate_topic}\nPosition: {debate_position}\nStage: {debate_stage}\nArgument:\n"
        inputs = tokenizer(prompt, return_tensors="pt", padding=True).to(device)

        with torch.no_grad():
            output_ids = model.generate(
                inputs.input_ids,
                attention_mask=inputs.attention_mask,
                max_new_tokens=100,  # ✅ Reduce token limit for MPS stability
                pad_token_id=tokenizer.eos_token_id
            )

        generated_text = tokenizer.decode(output_ids[0].cpu(), skip_special_tokens=True)
        st.subheader("💡 Generated Argument:")
        st.write(generated_text)

        # ✅ Feedback for RL Fine-Tuning
        feedback = st.radio("Was this response good?", ["Yes", "No"])
        if feedback == "No":
            st.write("💡 We'll improve future responses!")



