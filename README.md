# upfallProject
# 2nd Interview Project

## 1. LLM Model Choice reason
#### OpenAI(ChatGPT) -> ollama
#### 선정 이유 : 
#### 1. 무료로 개발환경에서 사용할 수 있음. 
#### 2.개발 테스트 시 개발 비용에 대한 부담을 줄일 수 있음. 
#### 3. 로컬 환경에서 실행 가능. 
#### 4. 빠른 테스트 및 개발 가능
## 2. Lang Choice reason
#### Python(FastAPI)
#### 선정 이유 : 
#### 1. AI 관련하여 연동이 쉬움. 
#### 2. 빠른 개발 가능 
#### 3. LangChain, LangGraph 등 주요 라이브러리 지원

## 프로젝트 구조
```
app/ 
├── main.py 
├── core/ 
│ └── config.py 
├── agent/ 
│ ├── graph.py 
│ └── nodes.py 
├── retriever/ 
│ ├── loader.py 
│ ├── embedding.py 
│ └── vectorstore.py 
├── routers/ 
│ ├── routes.py 
│ ├── ask.py 
│ └── upload.py 
├── data/ 
│ └── sample.pdf
```

## 기술 스택
| 항목|	기술 |
| :-:  | :-: |
| Language| Python |
| Framework| FastAPI |
| LLM	| Ollama (LLaMA3) |
| LLM Orchestration	| LangChain |
| Workflow	| LangGraph |
| Vector DB | FAISS |
| Embedding	| Ollama Embedding |
| Document | Loader	PyPDFLoader |

## 실행 방법 :
#### 1.source code git pull 
#### 2.해당 dir 이동
#### 3.pip install -r requirements.txt
#### 4.uvicorn app.main:app --reload
#### 5.상위dir에 .env 생성 후 DOWN_LOAD_URL=app/data/ 코드 입력.
#### 6.[ollama download url]:(https://ollama.com/download/windows)
#### 7.ollama run llama3
#### 8.localhost:8000/docs 에서 api 실행 가능.
#### PDF내 content를 기반으로 대답.
#### POST localhost:8000/ask 요청 { "question": " Improvement of independent agency capabilities?" }


