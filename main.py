from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin:admin@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    __tablename__ = 'todolist'
    id = db. Column(db.Integer, nullable = False, primary_key = True)
    item_name = db. Column(db.String(100), nullable = False)
    is_done = db.Column(db.Boolean, nullable = False, default = False)



    def __repr__(self):
        return "<Item %r>" % self.item_name


CORS(app)

@app.route('/')
def index():
    return jsonify({"message":"ToDo List"})

@cross_origin()
@app.route('/additem', methods = ['POST'])
def create_item():
    item_data = request.get_json()

    item_name = item_data['item_name']
    #is_done = item_data['is_done']

    item = Item(item_name = item_name)
    db.session.add(item)
    db.session.commit()

    return jsonify({"success": True,"response":"Item added"})

@app.route('/getitems', methods = ['GET'])
def getitems():
     todolist = []
     items = Item.query.all()
     for item in items:
          results = {
                    "id":item.id,
                    "item_name":item.item_name,
                    "is_done":item.is_done }
          todolist.append(results)

     return jsonify(
            {
                "success": True,
                "ToDoList": todolist
            }
        )

@app.route("/getdone/<int:id>", methods = ["PATCH"])
def update_item(id):
    item = Item.query.get(id)

    if item is None:
        abort(404)
    else:
        item.is_done = True
        db.session.add(item)
        db.session.commit()
        return jsonify({"success": True, "response": "Item is done!"})


@app.route("/delete/<int:id>", methods = ["PATCH"])
def delete_item(id):
    item = Item.query.get(id)
    if item is None:
        abort(404)
    else:
        db.session.delete(item)
        db.session.commit()
        return jsonify({"success": True, "response": "Item is deleted!"})

if __name__ == '__main__':
  app.run(debug = True)
