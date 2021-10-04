from flask import Flask
from flask import request
from flask import jsonify
import string
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

# @app.route('/users')
# def get_users():
#    return users


# @app.route('/users')
# def get_users():
#    search_username = request.args.get('name') #accessing the value of parameter 'name'
#    if search_username :
#       subdict = {'users_list' : []}
#       for user in users['users_list']:
#          if user['name'] == search_username:
#             subdict['users_list'].append(user)
#       return subdict
#    return users

# @app.route('/users/<id>')
# def get_user(id):
#    if id :
#       for user in users['users_list']:
#         if user['id'] == id:
#            return user
#       return ({})
#    return users

@app.route('/users', methods=['GET', 'POST'])#, 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      elif search_job:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      users['users_list'][-1]['id'] = create_id()
      resp = jsonify(success=True)
      resp.status_code = 201 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp
   # elif request.method == 'DELETE':
   #    delete_username = request.args.get('name')
   #    if delete_username:
   #       for user in users['users_list']:
   #          if user['name'] == delete_username:
   #             users['users_list'].remove(user)
   #       return users
   #    return users


# @app.route('/users/<name>', methods=['GET', 'DELETE'])
# def get_user(name):
#    if name :
#       for user in users['users_list']:
#         if user['name'] == name:
#            if request.method == 'GET':
#               return user
#            if request.method == 'DELETE':
#               users['users_list'].remove(user)
#             #   resp = jsonify(success=True)
#             #   resp.status_code = 204
#               return users
#       return users
#    return users

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           if request.method == 'GET':
              return user
           if request.method == 'DELETE':
              users['users_list'].remove(user)
              resp = jsonify(success=True)
              resp.status_code = 204
              return resp
      resp = jsonify({"User not found"}), 404
      return resp
   return users


def create_id():
   new_id = ""
   for i in range(0, 3):
      new_id += random.choice(string.ascii_lowercase)
   for i in range(0, 3):
      new_id += str(random.randint(0, 9))
   for user in users['users_list']:
      if user['id'] == new_id:
         new_id = ""
         create_id()
         break
      else:
         return new_id