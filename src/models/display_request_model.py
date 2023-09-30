from pydantic import BaseModel


class QueryModel(BaseModel):
    search_string: str
