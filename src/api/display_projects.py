from fastapi import APIRouter
from ..administrator.app import gallery_app
from ..models.response_model import ResponseModel
from ..models.display_request_model import QueryModel
from utils.database_functions import DbFunctions
from ..processor.filtering_project import filter_project


class DisplayProjects:

    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(path="/projects", endpoint=self.project_controller,
                                  methods=["POST"], response_model=ResponseModel)

    @staticmethod
    async def project_controller(query: QueryModel):
        resp = filter_project(query.search_string)
        # resp = DbFunctions.find_all(database=gallery_app.db, collection_name="PROJECT_GALLERY",
        #                             projection={"_id": 0}, query={"Project.Title":{"$in":resp}})

        return {"response": resp, "message": "Success"}


projects = DisplayProjects()
