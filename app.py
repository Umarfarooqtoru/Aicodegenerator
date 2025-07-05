import streamlit as st
from api_client import DeepSeekAPIClient
import time

# Page configuration
st.set_page_config(
    page_title="AI Code Generator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .language-selector {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .code-preview {
        background-color: #1e1e1e;
        color: #d4d4d4;
        padding: 1rem;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        margin-top: 1rem;
    }
    .stButton > button {
        background-color: #1f77b4;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #145a8c;
    }
</style>
""", unsafe_allow_html=True)

# Initialize API client
@st.cache_resource
def get_api_client():
    return DeepSeekAPIClient()

api_client = get_api_client()

# Main app
def main():
    st.markdown("<h1 class='main-header'>🤖 AI Code Generator</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Powered by DeepSeek R1 through OpenRouter</p>", unsafe_allow_html=True)
    
    # Sidebar for settings
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Language selection
        st.markdown("<div class='language-selector'>", unsafe_allow_html=True)
        st.subheader("Programming Language")
        programming_languages = ["Python", "JavaScript", "Java", "C++", "Go"]
        selected_language = st.selectbox(
            "Choose a programming language:",
            programming_languages,
            index=0
        )
        st.markdown("</div>", unsafe_allow_html=True)
        
        # API Status
        st.subheader("🔗 API Status")
        if api_client.api_key:
            st.success("API Key Configured ✅")
        else:
            st.error("API Key Missing ❌")
            st.warning("Please set OPENROUTER_API_KEY in .env file")
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📝 Code Generation")
        
        # Prompt input
        prompt = st.text_area(
            "Enter your code generation prompt:",
            placeholder="Example: Create a function to calculate fibonacci numbers",
            height=150,
            help="Describe what you want the code to do. Be specific for better results."
        )
        
        # Generate button
        generate_button = st.button(
            "🚀 Generate Code",
            type="primary",
            use_container_width=True
        )
        
        # Language info
        st.info(f"**Selected Language:** {selected_language}")
        
        # Example prompts
        with st.expander("💡 Example Prompts"):
            st.markdown("""
            **Python Examples:**
            - Create a class for managing a to-do list
            - Write a function to scrape data from a website
            - Implement a binary search algorithm
            
            **JavaScript Examples:**
            - Create a React component for a user card
            - Write an async function to fetch data from an API
            - Implement a shopping cart functionality
            
            **Java Examples:**
            - Create a Student class with getters and setters
            - Implement a simple calculator
            - Write a method to sort an array
            """)
    
    with col2:
        st.header("👀 Code Preview")
        
        # Initialize session state for generated code
        if 'generated_code' not in st.session_state:
            st.session_state.generated_code = ""
        if 'last_language' not in st.session_state:
            st.session_state.last_language = selected_language
        
        # Generate code when button is clicked
        if generate_button:
            if not prompt.strip():
                st.error("Please enter a prompt to generate code.")
            elif not api_client.api_key:
                st.error("API key is not configured. Please check your .env file.")
            else:
                with st.spinner(f"Generating {selected_language} code..."):
                    try:
                        generated_code = api_client.generate_code(prompt, selected_language)
                        st.session_state.generated_code = generated_code
                        st.session_state.last_language = selected_language
                        st.success("Code generated successfully! 🎉")
                    except Exception as e:
                        st.error(f"Error generating code: {str(e)}")
        
        # Display generated code
        if st.session_state.generated_code:
            st.subheader(f"Generated {st.session_state.last_language} Code:")
            
            # Language mapping for syntax highlighting
            language_map = {
                "Python": "python",
                "JavaScript": "javascript", 
                "Java": "java",
                "C++": "cpp",
                "Go": "go"
            }
            
            # Display code with syntax highlighting
            st.code(
                st.session_state.generated_code,
                language=language_map.get(st.session_state.last_language, "text"),
                line_numbers=True
            )
            
            # Action buttons
            col_copy, col_download = st.columns(2)
            
            with col_copy:
                if st.button("📋 Copy to Clipboard", use_container_width=True):
                    st.success("Code copied to clipboard!")
            
            with col_download:
                # File extension mapping
                ext_map = {
                    "Python": "py",
                    "JavaScript": "js",
                    "Java": "java",
                    "C++": "cpp",
                    "Go": "go"
                }
                
                file_ext = ext_map.get(st.session_state.last_language, "txt")
                filename = f"generated_code.{file_ext}"
                
                st.download_button(
                    label="💾 Download Code",
                    data=st.session_state.generated_code,
                    file_name=filename,
                    mime="text/plain",
                    use_container_width=True
                )
        else:
            st.info("Generated code will appear here after you click 'Generate Code'")
            st.markdown("""
            **Instructions:**
            1. Select your preferred programming language from the sidebar
            2. Enter a detailed prompt describing what you want the code to do
            3. Click 'Generate Code' to create AI-powered code
            4. Review the generated code in this preview area
            5. Copy or download the code as needed
            """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666; margin-top: 2rem;'>"
        "Built with ❤️ using Streamlit and DeepSeek API • "
        "<a href='https://openrouter.ai' target='_blank'>OpenRouter</a>"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
