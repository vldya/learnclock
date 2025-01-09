from routes.tasks import router as task_router
from routes.ping import router as ping_router
from routes.users import router as user_router
from routes.auth import router as auth_router

routers = [task_router, ping_router, user_router, auth_router]

