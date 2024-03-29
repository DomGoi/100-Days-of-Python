from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice, random
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        column_names = self.__table__.columns.keys()
        return {column: getattr(self, column) for column in column_names}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def random_cafe_def():
    random_cafe  = db.session.execute((db.select(Cafe)).order_by(db.sql.func.random()).limit(1)).scalar()

    return jsonify(Cafe={
        "id":random_cafe.id,
        "name":random_cafe.name,
        "map_url":random_cafe.map_url,
        "img_url":random_cafe.img_url,
        "location":random_cafe.location,
        "seats":random_cafe.seats,
        "has_toilet":random_cafe.has_toilet,
        "has_wifi":random_cafe.has_wifi,
        "has_sockets":random_cafe.has_sockets,
        "can_take_calls":random_cafe.can_take_calls,
        "coffee_price":random_cafe.coffee_price
    })
# HTTP GET - Read Record

@app.route("/all")
def all_cafes_def():
    all_cafes=Cafe.query.all()
    kawy=[k.to_dict() for k in all_cafes]
    return jsonify(kawy=kawy)

@app.route("/search")
def search_cafe():
    location=request.args.get("loc",'').strip().title()
    if location:
        results = db.session.execute(db.select(Cafe).filter(Cafe.location.like(f'%{location}%'))).scalars()
        cafes = results.all()
        if cafes:
            return jsonify(lokacje=[k.to_dict() for k in cafes])

        else:
            return jsonify(error="Sorry we don't have this place in our database")

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe=Cafe(
        name=request.form.get("name"),
        map_url= request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=bool(request.form.get("coffee_price"))
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})




# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    coffee_shop=Cafe.query.get_or_404(cafe_id)

    new_price=float(request.args.get("new_price",'').strip())
    coffee_shop.coffee_price=new_price
    db.session.commit()

    return jsonify({"message": "Coffee price updated successfully", "new_coffee_price": coffee_shop.coffee_price})


API_KEY="TopSecretAPIKey"


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def deleting_coffe_shop(cafe_id):
    apikey = request.args.get("api_key")
    if apikey == API_KEY:
        cafe = Cafe.query.get_or_404(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": f"Successfully deleted the {cafe.name} from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
