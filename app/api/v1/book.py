

from app.libs.redprint import Redprint

api = Redprint('book')
@api.route('/v1/book/get')
def get_book():
    pass
