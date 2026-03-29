# upfallProject
2nd Interview Project

# 요구사항

## 1. LLM Model Choice reason
### OpenAI(ChatGPT) -> ollama
### 이유 : 무료로 개발환경에서 사용할 수 있음. 개발 테스트 시 개발 비용에 대한 부담을 줄일 수 있음.
## 2. Lang Choice reason
### Python(FastAPI)
### 이유 : AI 관련하여 연동하기 쉬우며 빠르게 개발을 해야할 일이 필요할때 Python언어가 최선의 선택이라고 생각하여 선정.

# | 항목	기술 |
| :-:  | :-: |
| Language	| Python |
| Framework	| FastAPI |
| LLM	| Ollama (LLaMA3) |
| LLM Orchestration	| LangChain |
| Workflow	| LangGraph |
| Vector DB | FAISS |
| Embedding	| Ollama Embedding |
| Document | Loader	PyPDFLoader |

## 사용방법 :
# 1.source code git pull 
# 2.해당 dir 이동
# 3.pip install -r requirements.txt
# 4.uvicorn app.main:app --reload
# 5.[ollama download url]:(https://ollama.com/download/windows)
# 6.ollama run llama3
# 7.localhost:8000/docs 에서 api 실행 가능.
