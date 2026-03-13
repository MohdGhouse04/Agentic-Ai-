from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinance
from phi.tools.duckduckgo_search import DuckDuckGoSearch

##web search agent 
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    models=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGoSearch()],
    instructions=["Allways include source"],
    show_tools_calls=True,
    markdown=True,
    
    )
##financial agent

financial_agent = Agent(
    name="Financial AI Agent", 
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinance(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use the tools to get the data"],
    show_tools_calls=True,
    markdown=True,
    )   
multi_ai_agent = Agent(
    team=[web_search_agent, financial_agent],
    instructions=["Always include source","Use table to display the data"],
    show_tools_calls=True,
    markdown=True,
)   

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVIDA ",stream=True)