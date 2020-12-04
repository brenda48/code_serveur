from typing import Tuple

from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
CORS(app)


class EvenOddAPI(Resource):
    """
    API REST GET, PUT et DELETE pour une expedition client
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def get(value: int) -> Tuple[str, int]:
        """
        ## URL
        `GET /even_odd/<int:value>`
        ## Paramètres (URL)
        aucun
        ## Description
        Vérifier que lvaleur envoyés est pair ou impair
        """
        print(value)
        if value % 2 == 0:
            result = 'Pair'
        else:
            result = 'Impair'
        print(result)
        return result, 200


api.add_resource(EvenOddAPI, '/even_odd/<int:value>')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
