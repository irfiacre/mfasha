from google.adk.tools import FunctionTool

from mfasha_agent.tools.seleniumBase import SeleniumBaseTools


seleniumBaseTool = SeleniumBaseTools('https://youtube.com')

start_browser_session_tool = FunctionTool(func=seleniumBaseTool.start_browser_session)

get_body_tool = FunctionTool(func=seleniumBaseTool.get_body_content_page_source)
click_xpath_tool = FunctionTool(func=seleniumBaseTool.click_xpath)
add_text_to_input_tool = FunctionTool(func=seleniumBaseTool.add_text_to_input)
scroll_tool = FunctionTool(func=seleniumBaseTool.scroll)
click_enter_tool = FunctionTool(func=seleniumBaseTool.click_enter)

close_browser_tool = FunctionTool(func=seleniumBaseTool.close)
