from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo
from neomodel.properties import DateProperty, DateTimeFormatProperty, DateTimeProperty, FloatProperty
from neomodel.relationship import StructuredRel
from neomodel.relationship_manager import RelationshipFrom
from datetime import date

# Create your models here.
class Tattooparlor(StructuredNode):
    cvr = IntegerProperty(unique_index=True, required=True)
    name = StringProperty(index=True, required=True)
    phonenumber = IntegerProperty(index=True, required=True)
    adress = StringProperty(index=True, required=True)
    email = StringProperty(index=True, required=True)

class Customer(StructuredNode):
    cpr = IntegerProperty(unique_index=True, required=True)
    name = StringProperty(index=True, required=True)
    email = StringProperty(index=True, required=True)
    phonenumber = IntegerProperty(index=True, required=True)
    #registered = DateTimeFormatProperty(required=True, format='%YYYY-%MM-%DD')

class Appointment(StructuredNode):
    idappointment = UniqueIdProperty()
    date=StringProperty(required=True, index=True)
    time=StringProperty(required=True, index=True)
    sessionlenght=IntegerProperty(index=True, default=1)

    #Relationships
    customer = RelationshipFrom(Customer, 'HAS_AN')
    tatooparlor = RelationshipFrom(Tattooparlor, 'HOLDS_AN')
     
    
class Artist(StructuredNode):
    cpr = IntegerProperty(unique_index=True, required=True)
    name = StringProperty(index=True, required=True)
    phonenumber = IntegerProperty(index=True, required=True)
    email = StringProperty(index=True, required=True)
    price = IntegerProperty(index=True, required=True)
    
    #Relationships
    tattooparlor = RelationshipTo(Tattooparlor, 'WORKS_IN')
    customer = RelationshipTo(Customer, 'HAS_AN')


class Ink(StructuredNode):
    batchnumber = IntegerProperty(unique_index=True, required=True)
    brand = StringProperty(index=True, required=True)
    colorcode = StringProperty(index=True, required=True)
    experationdate = StringProperty(required=True)
    price = FloatProperty(index=True, required=True)

    #Relationships
    tattooparlor = RelationshipFrom(Tattooparlor, 'HAS')

class Producer(StructuredNode):
    cvr = IntegerProperty(unique_index=True, required=True)
    name = StringProperty(index=True, required=True)
    phonenumber = IntegerProperty(index=True, required=True)
    adress = StringProperty(index=True, required=True)

    #Relationships


class Supplier(StructuredNode):
    cvr = IntegerProperty(unique_index=True, required=True)
    name = StringProperty(index=True, required=True)
    phonenumber = IntegerProperty(index=True, required=True)
    adress = StringProperty(index=True, required=True)
    
    #Relationships
    producer = RelationshipTo(Producer, 'HAS_A')

class Tattoo(StructuredNode):
    idtattoo = UniqueIdProperty()
    description = StringProperty(index=True, required=True)
    placementonbody = StringProperty(index=True, required=True)

    #Relationships
    appointment = RelationshipTo(Appointment, 'HAS_A')
    ink = RelationshipTo(Ink, 'MADE_WITH')



