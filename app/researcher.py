import asyncio
from gpt_researcher.agent import GPTResearcher
# from dotenv import load_dotenv
# load_dotenv()
# import os
# api_key = os.environ["OPENAI_API_KEY"]
# print(api_key)
async def generate_report(query, report_type, tone, report_source, report_format, source_urls, document_urls, documents) -> str:
    """
    Generates a research report using GPT-Researcher.
    
    Parameters:
      - research_topic: The main research query.
      - summary_type: The type of report (e.g. "research_report", "resource_report", "outline_report").
      - tone: The desired tone of the report (e.g. "formal and objective").
      - document_source: The document source ("web", "local", or "hybrid").
      
    Returns:
      - A research report as a string.
    """
    
    researcher = GPTResearcher(
        query=query,
        report_type=report_type,
        report_source=report_source,
        tone=tone,
        config_path=None,
        report_format=report_format,
        source_urls=source_urls,
        document_urls=document_urls,
        documents=documents,
    )
    
    # Run the research process (first conduct research then write the report)
    await researcher.conduct_research()
    report = await researcher.write_report()
    return report
