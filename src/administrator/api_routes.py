from ..api.display_projects import projects


class ApiRoutes:

    def __init__(self, app):
        app.include_router(projects.router, prefix="/api/v1", tags=["All Projects"])
