from .start_handler import router as start_router
from .commands_handler import router as commands_router
from .callback_handler import router as callback_router
from .error_handler import router as error_router
from .github_handler import router as github_router
from .trello_handler import router as trello_router
from .ci_cd_handler import router as ci_cd_router  

routers = [
    start_router,
    commands_router,
    callback_router,
    error_router,
    github_router,
    trello_router,
    ci_cd_router,  
]

