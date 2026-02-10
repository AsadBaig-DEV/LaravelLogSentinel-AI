import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

class AIAnalyzer:
  def __init__(self, provider=None):
    self.provider = provider or os.getenv("AI_PROVIDER", "gemini").lower()
    self.llm = self._initialize_llm()
    self.output_parser = StrOutputParser()

  def _initialize_llm(self):
    if self.provider == "openai":
      print("AI Engine: Initializing OpenAI (GPT-4o)...")
      return ChatOpenAI(
        model="gpt-4o",
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0
      )
    elif self.provider == "gemini":
      print("AI Engine: Initializing GEMINI (1.5 Flash)...")
      return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0
      )
    else:
      raise ValueError(f"Unsupported AI provider: {self.provider}")
    
  def analyze_stack_trace(self, log_content):
    """Processes the log using the selected provider and returns a fix."""
    prompt = ChatPromptTemplate.from_messages([
      ("system", (
        "You are an Expert Laravel and Database Architect. "
        "Analyze the provided error log. Provide a 2-line 'Root Cause' "
        "and a 3-bullet point 'Fix Recommendation'. "
        "Keep it technical and concise for a Senior Developer."
      )),
      ("user", "Here is the Laravel log entry:\n\n{logs}")
    ])

    chain = prompt | self.llm | self.output_parser
    try:
      response = chain.invoke({"logs": log_content[:2000]})
      return response
    except Exception as e:
      return f"{self.provider.capitalize()} Analysis failed: {str(e)}"

if __name__ == "__main__":
  test_log = "local.ERROR: Call to a member function getClientOriginalExtension() on null"

  analyzer = AIAnalyzer()
  print(f"\n--- {analyzer.provider.upper()} FIX SUGGESTION ---")
  print(analyzer.analyze_stack_trace(test_log))