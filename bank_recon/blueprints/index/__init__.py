from flask import Blueprint

bp = Blueprint('index', __name__)


@bp.route("/")
def home():
    return "This is working."
