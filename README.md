## Create Virtual Environment
```
Python -m venv venv
```

## Activate environment
```
source venv/bin/activate
```

## Install google-adk
```
pip install google-adk
```

## Create Agent project
You will need to create the following project structure:
```
parent_folder/
    multi_tool_agent/
        __init__.py
        agent.py
        .env
```

inside __init__.py, write below code
```
from . import agent
```

## Create agent.py and start writing the code

For running any agent > get into the folder and run the code ```adk web```
