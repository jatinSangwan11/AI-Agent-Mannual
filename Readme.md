# 🧠 AI Agent From Scratch (No Frameworks)

This project demonstrates how to **build an AI agent from first principles**, without using LangChain, LangGraph, CrewAI, MCP, or any other agent framework.

The goal is **deep understanding** of agent architecture, control flow, and failure modes — not shortcuts.

---

## 🎯 Problem Statement

> **“Find 3 recent AI agent research papers and summarize them.”**

The agent:
- Receives a goal
- Reasons step-by-step using an LLM (ReAct-style)
- Decides which tool to call
- Executes tools via a controller (orchestrator)
- Maintains explicit state
- Terminates only when it emits `Action: Finish`

---

## 🧩 What This Project Is (and Is Not)

### ✅ This project **is**:
- A **manual implementation** of an AI agent loop
- Explicit orchestration and state management
- Deterministic and debuggable
- Framework-independent
- Designed for learning and extension

### ❌ This project is **not**:
- An autonomous system that runs forever
- A wrapper around LangChain/LangGraph
- A production-ready agent
- A “prompt-only” demo

---

## 🏗️ Core Architecture

```text
User Goal
   ↓
Agent Controller (Orchestrator)
   ↓
LLM (Reasoning Only)
   ↓
Action Selection (ReAct)
   ↓
Tool Execution
   ↓
Observation
   ↓
State Update
   ↓
Repeat until Action: Finish
