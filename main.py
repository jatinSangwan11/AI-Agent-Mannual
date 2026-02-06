from state import initial_state
from controller import run_agent
from llm import MockLLM


def main():
    goal = "Find 3 recent AI agent research papers and summarize them."
    state = initial_state(goal)
    
    print("main.py loaded")

    llm = MockLLM()
    final_state = run_agent(state, llm)

    print("\n=== AGENT STATUS ===")
    print(final_state["status"])

    print("\n=== RESULTS ===")
    for r in final_state["results"]:
        print("-", r)


if __name__ == "__main__":       # checks that this is the entry point and here the __name__ is a variable we have with every file 
    main()
