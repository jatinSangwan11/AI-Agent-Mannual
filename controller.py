from tools import search_papers, summarize_paper
from prompts import build_prompt


TOOLS = {
    "search_papers": search_papers
}

def run_agent(state: dict, llm) -> dict:
    tool_descriptions = """
        search_papers(query: str) -> list
        """
    count =1
    while state["status"] == "running":
        # print(state["status"])
        prompt = build_prompt(state, tool_descriptions)
        llm_response = llm.generate(prompt)
        
        if(count ==3):
            break
        
        print(llm_response)
        state["history"].append(llm_response)

        # --- Very naive ReAct parsing (intentional for now) ---
        if "Action: Finish" in llm_response:
            papers = search_papers("AI agent research")
            summaries = [summarize_paper(p) for p in papers]

            state["results"] = summaries
            state["status"] = "done"
            break

        if "Action: search_papers" in llm_response:
            observation = search_papers("AI agent research")
            print(observation)
            state["history"].append(f"Observation: {observation}")
        
        count+=1

    return state
    