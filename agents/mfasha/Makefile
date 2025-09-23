install:
	cd ${PWD}/mfasha_agent
# 	Should add how to setup the environment for both frontend & backend.

dev:
	make dev-backend & make dev-frontend

dev-backend:
	source venv/bin/activate && adk api_server --allow_origins="*"

dev-frontend:
	cd ${PWD}/nextjs && npm run dev
