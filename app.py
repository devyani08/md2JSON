import streamlit as st
import json
import re

# Function to extract recommendations from Markdown content
def extract_recommendations(md_content):
    # Updated regex to match COR and LOE values more flexibly
    pattern = r"\|\s*([\d\w]+)\s*\|\s*([\w-]+)\s*\|\s*(.*?)\s*\|"
    matches = re.findall(pattern, md_content)

    recommendationss = []
    for cor, loe, recommendations in matches:
        recommendationss.append({
            "recommendation_content": recommendationss.strip(),
            "recommendation_class": cor.strip(),
            "rating": loe.strip()
        })
    
    return recommendationss

# Function to generate JSON chunks
def generate_json_chunks(recommendationss):
    base_json = {
        "title": "Distal Radius Fracture Rehabilitation",
        "subCategory": [],
        "guide_title": "Distal Radius Fracture Rehabilitation",
        "stage": ["Rehabilitation"],
        "disease": ["Fracture"],
        "rationales": [],
        "references": [],
        "specialty": ["orthopedics"]
    }
    
    json_chunks = []
    for rec in recommendationss:
        chunk = base_json.copy()
        chunk.update(rec)
        json_chunks.append(chunk)
    
    return json_chunks

# Streamlit app
st.title("Markdown to JSON Converter")

uploaded_file = st.file_uploader("Upload a Markdown (.md) file", type=["md"])

if uploaded_file is not None:
    # Read the file content
    md_content = uploaded_file.read().decode("utf-8")
    
    # Extract recommendations from the Markdown content
    recommendationss = extract_recommendations(md_content)
    
    if recommendationss:
        # Generate JSON chunks
        json_chunks = generate_json_chunks(recommendationss)
        
        # Display the JSON chunks
        st.write("Generated JSON:")
        st.json(json_chunks)
        
        # Option to download JSON file
        json_output = json.dumps(json_chunks, indent=2)
        st.download_button(
            label="Download JSON",
            data=json_output,
            file_name="output.json",
            mime="application/json"
        )
    else:
        st.warning("No recommendations found in the uploaded file. Please check the file format.")
