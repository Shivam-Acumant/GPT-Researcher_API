import uvicorn
import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from app.researcher import generate_report

app = FastAPI(title="GPT-Researcher ")

class ResearchRequest(BaseModel):
    research_topic: str
    report_type: str   # e.g. "research_report(short-summary)", "resource_report", "outline_report", "detailed_report", "detailed_report", "subtopic_report"
    tone: str           # e.g. "formal, objective, analytical, persuasive, informative, explanatory, descriptive, critical, comparative, speculative, reflective, narrative, humorous, optimistic, pessimistic"
    report_source: str  # "web", "local", "hybrid(web+local)" or "azure"
    report_format: Optional[str] = "markdown"
    source_urls: Optional[List[str]]=None
    document_urls: Optional[List[str]]=None
    documents: Optional[list]=None

@app.post("/research", response_model=dict)
async def research_endpoint(request: ResearchRequest):
    try:
        print("API got a Post request")
    
        query = request.research_topic if request.research_topic else None
        report_type = request.report_type if request.report_type else None
        tone = request.tone if request.tone else None
        report_source = request.report_source if request.report_source else None
        report_format = request.report_format if request.report_format else "markdown"
        source_urls = request.source_urls if request.source_urls else None
        document_urls = request.document_urls if request.document_urls else None
        documents = request.documents if request.documents else None
        
        report = await generate_report(
            query, report_type, tone, report_source, report_format, source_urls, document_urls, documents
        )
        return {"report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# If you want to run the app directly (e.g. python -m uvicorn app.main:app --reload)
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
