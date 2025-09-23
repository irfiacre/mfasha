from google.adk.agents import Agent, SequentialAgent
from google.adk.planners import BuiltInPlanner
from google.genai import types
from mfasha_agent.prompts import INSTRUCTIONS
from mfasha_agent.tools.tools import start_browser_session_tool, get_body_tool, add_text_to_input_tool, click_xpath_tool, \
    close_browser_tool, click_enter_tool, scroll_tool

requirements_breakdown_agent = Agent(
    name="requirements_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions about the time and weather in a city."),
    instruction=(INSTRUCTIONS["requirements_agent"]),
    generate_content_config=types.GenerateContentConfig(temperature=0.2),
    output_key="requirements_breakdown"
)

requirements_review_agent = Agent(
    name="reviewer_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions about the time and weather in a city."),
    instruction=(INSTRUCTIONS["requirements_agent"]),
    generate_content_config=types.GenerateContentConfig(temperature=0.2),
    output_key="final_testcases"
)

automation_development_agent = Agent(
    name="automation_developer_agent",
    model="gemini-2.0-flash",
    description="Agent to develop the automation script.",
    instruction=(INSTRUCTIONS["automation_agent"]),
    output_key="automation_script",
    # planner=BuiltInPlanner(
    #     thinking_config=types.ThinkingConfig(include_thoughts=True)
    # ),
    tools=[
        start_browser_session_tool,
        get_body_tool,
        add_text_to_input_tool,
        click_xpath_tool,
        scroll_tool,
        click_enter_tool,
        close_browser_tool
    ]
)

root_agent = SequentialAgent(
    name="AutomationDevelopmentSystem",
    description="A simple system that researches, creates, and enhances automation scripts",
    sub_agents=[requirements_breakdown_agent, requirements_review_agent, automation_development_agent],
)
