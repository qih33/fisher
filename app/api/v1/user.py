

from app.libs.redprint import Redprint

api = Redprint('user')
@api.route('/v1/user/get')
def get_user():
    pass
