from flask import Flask, render_template, abort
from peewee import *
import datetime

app = Flask(__name__)
db = SqliteDatabase(':memory:')

class BaseModel(Model):
    class Meta:
        database = db

class Example(BaseModel):
    data = CharField()
    
    def __repr__(self):
        return self.data
    
class Contact(BaseModel):
    firstname = CharField()
    lastname = CharField()
    email = CharField(unique=True)
    notes = TextField(default="")
    is_active = BooleanField(default=True)
    created_on = DateTimeField(default=datetime.datetime.now)
    
    def __repr__(self):
        return self.email
    
def init_database():
    db.connect()
    db.create_tables([Example, Contact], safe=True)
    #Example.create(data="This is first.")
    #Example.create(data="This is second.")
    try:
        Contact.create(firstname="Aaron", lastname="Aardvark", email="aardvark@aaron.net")
        Contact.create(firstname="Billy", lastname="Batson", email="batson@beta.net")
    except Exception as e:
        print e

def get_object_or_404(cls, object_id):
    try:
        object = cls.get(cls.id==object_id)
        return object
    except:
        abort(404)
        
def get_object_or_none(cls, object_id):
    try:
        object = cls.get(cls.id==object_id)
    except:
        object = None
    return object
        
@app.route('/contact/<int:contact_id>')
def contact_view(contact_id):
    contact = get_object_or_404(Contact, contact_id)
    return render_template('contact_view.html', contact=contact)

@app.route('/contact_edit/<int:contact_id>')
def contact_edit(contact_id):
    contact = get_object_or_404(Contact, contact_id)
    return render_template('contact_edit.html', contact=contact)

@app.route('/contact_edit_alt/<int:contact_id>')
def contact_edit_alt(contact_id):
    contact = get_object_or_404(Contact, contact_id)
    return render_template('contact_edit_alt.html', contact=contact)

@app.route('/')
def index():
    return render_template('test_edit.html')

if __name__ == '__main__':
    init_database()
    app.run(debug=False)
    
    