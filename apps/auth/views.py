from sanic.views import HTTPMethodView
from sanic.response import json
import apps
from bson import ObjectId


class RegisterAPI(HTTPMethodView):
    """
    name, email, mobile, password, registered_on
    """

    async def get(self, request):
        user = apps.db.notification.find_all()
        return json(user)


class TestAPI(HTTPMethodView):
    async def get(self, request):
        return json({"hello": "2eeee"})

    async def post(self, request):
        data = request.json

        inserted = await apps.db.movie.insert_one(data)

        res = {
            "data": inserted,
            "status": "Ok"
        }
        return json(res, status=201)
