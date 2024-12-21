from flask import Blueprint, request, jsonify
from .models import db, User, Court

bp = Blueprint('routes', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({"id": user.id, "username": user.username, "email": user.email})

@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get_or_404(id)
    user.username = data['username']
    user.email = data['email']
    user.password = data['password']
    db.session.commit()
    return jsonify({"message": "User updated successfully"})

@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})

@bp.route('/courts', methods=['POST'])
def create_court():
    data = request.get_json()
    new_court = Court(user_id=data['user_id'], sport=data['sport'], num=data['num'])
    db.session.add(new_court)
    db.session.commit()
    return jsonify({"message": "Court created successfully"}), 201

@bp.route('/courts/<int:id>', methods=['GET'])
def get_court(id):
    court = Court.query.get_or_404(id)
    return jsonify({"id": court.id, "user_id": court.user_id, "reserved": court.reserved, "sport": court.sport, "num": court.num})

@bp.route('/courts/<int:id>', methods=['PUT'])
def update_court(id):
    data = request.get_json()
    court = Court.query.get_or_404(id)
    court.user_id = data['user_id']
    court.sport = data['sport']
    court.num = data['num']
    db.session.commit()
    return jsonify({"message": "Court updated successfully"})

@bp.route('/courts/<int:id>', methods=['DELETE'])
def delete_court(id):
    court = Court.query.get_or_404(id)
    db.session.delete(court)
    db.session.commit()
    return jsonify({"message": "Court deleted successfully"})
