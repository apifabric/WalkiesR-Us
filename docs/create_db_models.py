# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Walker(Base):
    """description: Represents a dog walker who can self-register and provide availability."""
    __tablename__ = 'walker'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    max_dogs_per_walk = Column(Integer, nullable=False)
    morning_available = Column(Boolean, default=False)
    afternoon_available = Column(Boolean, default=False)

class WalkerAvailability(Base):
    """description: Represents the days a walker is available."""
    __tablename__ = 'walker_availability'

    id = Column(Integer, primary_key=True)
    walker_id = Column(Integer, ForeignKey('walker.id'), nullable=False)
    day_of_week = Column(Enum('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'), nullable=False)

class WalkerPrice(Base):
    """description: Stores pricing details for different dog sizes by each walker."""
    __tablename__ = 'walker_price'

    id = Column(Integer, primary_key=True)
    walker_id = Column(Integer, ForeignKey('walker.id'), nullable=False)
    dog_size = Column(Enum('small', 'medium', 'large'), nullable=False)
    price = Column(Float, nullable=False)

class Owner(Base):
    """description: Represents a dog owner who registers and can request walks."""
    __tablename__ = 'owner'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Dog(Base):
    """description: Represents a dog belonging to an owner."""
    __tablename__ = 'dog'
    
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('owner.id'), nullable=False)
    name = Column(String, nullable=False)
    breed = Column(String, nullable=True)
    size = Column(Enum('small', 'medium', 'large'), nullable=False)
    notes = Column(String, nullable=True)

class WalkRequest(Base):
    """description: Records requests made by owners to walk their dogs."""
    __tablename__ = 'walk_request'
    
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('owner.id'), nullable=False)
    walker_id = Column(Integer, ForeignKey('walker.id'), nullable=False)
    request_date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(Enum('pending', 'approved', 'completed'), nullable=False)

class WalkRequestDog(Base):
    """description: Associates dogs with walk requests."""
    __tablename__ = 'walk_request_dog'
    
    id = Column(Integer, primary_key=True)
    walk_request_id = Column(Integer, ForeignKey('walk_request.id'), nullable=False)
    dog_id = Column(Integer, ForeignKey('dog.id'), nullable=False)

class Payment(Base):
    """description: Represents payments made to walkers after a walk is completed."""
    __tablename__ = 'payment'
    
    id = Column(Integer, primary_key=True)
    walk_request_id = Column(Integer, ForeignKey('walk_request.id'), nullable=False)
    payment_date = Column(DateTime, default=datetime.datetime.utcnow)
    amount = Column(Float, nullable=False)

class Administrator(Base):
    """description: Represents a business administrator who can view records."""
    __tablename__ = 'administrator'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

class SystemLog(Base):
    """description: Logs actions and events in the system for auditing."""
    __tablename__ = 'system_log'
    
    id = Column(Integer, primary_key=True)
    action_desc = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class Feedback(Base):
    """description: Stores feedback from owners or walkers about the service."""
    __tablename__ = 'feedback'
    
    id = Column(Integer, primary_key=True)
    user_type = Column(Enum('walker', 'owner', 'administrator'), nullable=False)
    user_id = Column(Integer, nullable=False)
    feedback_text = Column(String, nullable=False)
    feedback_date = Column(DateTime, default=datetime.datetime.utcnow)

class Notification(Base):
    """description: Manages notifications sent to owners and walkers."""
    __tablename__ = 'notification'
    
    id = Column(Integer, primary_key=True)
    recipient_type = Column(Enum('walker', 'owner'), nullable=False)
    recipient_id = Column(Integer, nullable=False)
    message = Column(String, nullable=False)
    sent_date = Column(DateTime, default=datetime.datetime.utcnow)

class Review(Base):
    """description: Stores reviews for walkers provided by owners."""
    __tablename__ = 'review'
    
    id = Column(Integer, primary_key=True)
    walker_id = Column(Integer, ForeignKey('walker.id'), nullable=False)
    owner_id = Column(Integer, ForeignKey('owner.id'), nullable=False)
    rating = Column(Integer, nullable=False)  # rating out of 5
    comments = Column(String, nullable=True)

class WalkerHistory(Base):
    """description: Tracks the walking history of a walker."""
    __tablename__ = 'walker_history'

    id = Column(Integer, primary_key=True)
    walker_id = Column(Integer, ForeignKey('walker.id'), nullable=False)
    walk_date = Column(DateTime, default=datetime.datetime.utcnow)
    number_of_dogs = Column(Integer, nullable=False)

class DogSizePriceHistory(Base):
    """description: Maintains a history of price changes for dog sizes."""
    __tablename__ = 'dog_size_price_history'

    id = Column(Integer, primary_key=True)
    walker_id = Column(Integer, ForeignKey('walker.id'), nullable=False)
    dog_size = Column(Enum('small', 'medium', 'large'), nullable=False)
    price = Column(Float, nullable=False)
    effective_date = Column(DateTime, default=datetime.datetime.utcnow)

# Below would be the code block where we set up the SQLite database and create sample data

# Create the database and tables
from sqlalchemy import create_engine
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

# Insert sample data
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Sample data creation
walker1 = Walker(name="Alice Smith", postal_code="12345", phone="555-1234", email="alice@example.com", max_dogs_per_walk=5, morning_available=True)
walker2 = Walker(name="Bob Johnson", postal_code="54321", phone="555-5678", email="bob@example.com", max_dogs_per_walk=4, afternoon_available=True)

session.add(walker1)
session.add(walker2)
session.commit()

walker_availability1 = WalkerAvailability(walker_id=walker1.id, day_of_week='Mon')
walker_availability2 = WalkerAvailability(walker_id=walker1.id, day_of_week='Wed')

session.add(walker_availability1)
session.add(walker_availability2)
session.commit()

walker_price1 = WalkerPrice(walker_id=walker1.id, dog_size='small', price=15.0)
walker_price2 = WalkerPrice(walker_id=walker1.id, dog_size='medium', price=20.0)

session.add(walker_price1)
session.add(walker_price2)
session.commit()

owner1 = Owner(name="Charlie Brown", address="123 Elm St", phone="555-2233", email="charlie@example.com")
owner2 = Owner(name="Lucy van Pelt", address="456 Oak St", phone="555-3344", email="lucy@example.com")

session.add(owner1)
session.add(owner2)
session.commit()

dog1 = Dog(owner_id=owner1.id, name="Snoopy", breed="Beagle", size="medium")
dog2 = Dog(owner_id=owner1.id, name="Woodstock", breed="Unknown", size="small")

session.add(dog1)
session.add(dog2)
session.commit()

walk_request1 = WalkRequest(owner_id=owner1.id, walker_id=walker1.id, status='pending')
walk_request2 = WalkRequest(owner_id=owner1.id, walker_id=walker2.id, status='completed')

session.add(walk_request1)
session.add(walk_request2)
session.commit()

walk_request_dog1 = WalkRequestDog(walk_request_id=walk_request1.id, dog_id=dog1.id)
walk_request_dog2 = WalkRequestDog(walk_request_id=walk_request2.id, dog_id=dog2.id)

session.add(walk_request_dog1)
session.add(walk_request_dog2)
session.commit()

payment1 = Payment(walk_request_id=walk_request2.id, amount=20.0)

session.add(payment1)
session.commit()

admin1 = Administrator(name="Admin User", email="admin@example.com")

session.add(admin1)
session.commit()

system_log1 = SystemLog(action_desc="Initial setup and sample data added")

session.add(system_log1)
session.commit()

feedback1 = Feedback(user_type='owner', user_id=owner1.id, feedback_text="Great service!")
feedback2 = Feedback(user_type='walker', user_id=walker1.id, feedback_text="Enjoyed walking the dogs!")

session.add(feedback1)
session.add(feedback2)
session.commit()

notification1 = Notification(recipient_type='owner', recipient_id=owner1.id, message="Your walk request has been approved.")
notification2 = Notification(recipient_type='walker', recipient_id=walker1.id, message="You have a new walk request.")

session.add(notification1)
session.add(notification2)
session.commit()

review1 = Review(walker_id=walker1.id, owner_id=owner1.id, rating=5, comments="Excellent walker!")

session.add(review1)
session.commit()

walker_history1 = WalkerHistory(walker_id=walker1.id, number_of_dogs=2)

session.add(walker_history1)
session.commit()

dog_size_price_history1 = DogSizePriceHistory(walker_id=walker1.id, dog_size='medium', price=18.0)

session.add(dog_size_price_history1)
session.commit()

session.close()
