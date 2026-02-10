import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

class AIAnalyzer:
    def __init__(self):
        
        self.llm = ChatOpenAI(
            model="gpt-4o", 
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0 # For debugging and logs, you don't want the AI to be "creative";
        )

        self.output_parser = StrOutputParser()

    def analyze_stack_trace(self, log_content):
        """Processes the log and returns a structured fix suggestion."""
        print("AI Engine: Analyzing stack trace for Root Cause...")

        # Instructing the AI on persona and output format
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
            # We truncate the log if it's too long to save on token costs
            response = chain.invoke({"logs": log_content[:2000]})
            return response
        except Exception as e:
            return f"AI Analysis failed: {str(e)}"

if __name__ == "__main__":
    # Independent Test Run
    test_log = "local.ERROR: Column not found: 1054 Unknown column 'user_id' in 'field list'"
    analyzer = AIAnalyzer()
    print("\n--- AI FIX SUGGESTION ---")
    print(analyzer.analyze_stack_trace(test_log))