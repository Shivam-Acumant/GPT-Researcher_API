# GPT-Researcher API

This project wraps the open source [GPT-Researcher](https://docs.gptr.dev/) into a REST API. It exposes a `/research` endpoint that accepts atleast four inputs:

- **research_topic**: The main research query.
- **summary_type**: Type of report (e.g., "research_report").
- **tone**: The tone for the final report.
- **document_source**: Source type ("web", "local", or "hybrid").

- **report_format**, **source_urls**, **document_urls**, **documents**: are optional inputs.

## Setup

1. Clone the repository and navigate into the project directory:
   ```bash
   git clone <repo-url>
   cd GPT-Researcher_API
   ```

2. Create a Virtual Environment and Activate It (Optional but Recommended):
   ```bash
   python -m venv env
   .\env\Scripts\activate
   ```

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set Your Environment Variables:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   TAVILY_API_KEY=your_tavily_api_key
   AZURE_CONNECTION_STRING=your_azure_storage_connection_string
   AZURE_CONTAINER_NAME=your_azure_storage_container_name
   ```

## Run the API

1. Start the server by running:
   ```bash
   uvicorn app.main:app --reload
   ```

2. The API endpoint will be available at:
   ```bash
   http://localhost:8000/research
   ```

## Test the API via Postman

**Send a POST request to 'http://localhost:8000/research' with a JSON body similar to:**
```bash
{
  "research_topic": "Your Research Topic",
  "report_type": "research_report(short-summary)/ resource_report/ outline_report/ detailed_report/ detailed_report/ subtopic_report",
  "tone": "formal/ objective/ analytical/ persuasive/ informative/ explanatory/ descriptive/ critical/ comparative/ speculative/ reflective/ narrative/ humorous/ optimistic/ pessimistic",
  "report_source": "web/ local/ hybrid(web+local)/ azure"
}

```