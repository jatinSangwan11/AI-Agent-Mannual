
def search_papers(query: str)-> list:
    """
        Here we will get the query from which we gonna return mock research papers
    """
    return [
        {
            "title": "ReAct: Synergizing Reasoning and Acting in Language Models",
            "summary": "Introduces ReAct, a framework that combines reasoning traces with actions."
        },
        {
            "title": "Generative Agents: Interactive Simulacra of Human Behavior",
            "summary": "Presents agents with memory, reflection, and planning capabilities."
        },
        {
            "title": "Voyager: An Open-Ended Embodied Agent",
            "summary": "An LLM-powered agent that continuously learns through interaction."
        }        
    ]

def summarize_paper(paper: dict) -> str:
    """
        return the summary of the paper
    """

    return f"{paper.get("title")}\nsummary is::: {paper.get("summary")}"