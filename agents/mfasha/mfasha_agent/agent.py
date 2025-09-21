from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import BaseTool, FunctionTool
from google.genai import types
from mfasha_agent.contants import INSTRUCTIONS
from mfasha_agent.tools.seleniumBase import SeleniumBaseTools

requirements_breakdown_agent = Agent(
    name="requirements_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions about the time and weather in a city."),
    instruction=(INSTRUCTIONS["requirements_agent"]),
    generate_content_config=types.GenerateContentConfig(temperature=0.2),
    output_key="requirements_breakdown"
)


seleniumBaseTool = SeleniumBaseTools('https://urubutopay.rw')

get_body_tool = FunctionTool(
    # BaseTool(name="get_body", doc = "Returns the HTML <body> content of the current page."),
    func=seleniumBaseTool.get_body_content_page_source
)

click_xpath_tool = FunctionTool(
    # name="click_xpath",
    func=seleniumBaseTool.click_xpath,
    # description="Clicks an element on the page using its XPath."
)

close_browser_tool = FunctionTool(
    # name="close_browser",
    func=seleniumBaseTool.close,
    # description="Closes the browser session."
)

automation_development_agent = Agent(
    name="automation_developer_agent",
    model="gemini-2.0-flash",
    description="Agent to develop the automation script.",
    instruction=(INSTRUCTIONS["automation_agent"]),
    output_key="automation_script",
    tools=[get_body_tool, click_xpath_tool, close_browser_tool]
)

root_agent = SequentialAgent(
    name="AutomationDevelopmentSystem",
    description="A simple system that researches, creates, and enhances automation scripts",
    sub_agents=[requirements_breakdown_agent, automation_development_agent],
)
