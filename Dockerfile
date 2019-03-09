FROM python:alpine

COPY runaction.py /runaction.py
RUN chmod +x /runaction.py
RUN python3 -m pip install PyGithub

ENTRYPOINT ["python3", "/runaction.py"]

LABEL "name"="action-accesscontrol"
LABEL "maintainer"="Ludeeus <ludeeus@gmail.com>"
LABEL "version"="0.0.1"
LABEL "com.github.actions.name"="action-accesscontrol"
LABEL "com.github.actions.description"="Check if the invoker has access defined access level."
LABEL "com.github.actions.icon"="lock"
LABEL "com.github.actions.color"="red"
