# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 29, 2024 14:05:49
# Database: sqlite:////tmp/tmp.ZcdmnfVPnO/WalkiesR-Us/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Administrator(SAFRSBaseX, Base):
    """
    description: Represents a business administrator who can view records.
    """
    __tablename__ = 'administrator'
    _s_collection_name = 'Administrator'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class Feedback(SAFRSBaseX, Base):
    """
    description: Stores feedback from owners or walkers about the service.
    """
    __tablename__ = 'feedback'
    _s_collection_name = 'Feedback'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    user_type = Column(String(13), nullable=False)
    user_id = Column(Integer, nullable=False)
    feedback_text = Column(String, nullable=False)
    feedback_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class Notification(SAFRSBaseX, Base):
    """
    description: Manages notifications sent to owners and walkers.
    """
    __tablename__ = 'notification'
    _s_collection_name = 'Notification'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    recipient_type = Column(String(6), nullable=False)
    recipient_id = Column(Integer, nullable=False)
    message = Column(String, nullable=False)
    sent_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class Owner(SAFRSBaseX, Base):
    """
    description: Represents a dog owner who registers and can request walks.
    """
    __tablename__ = 'owner'
    _s_collection_name = 'Owner'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    DogList : Mapped[List["Dog"]] = relationship(back_populates="owner")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="owner")
    WalkRequestList : Mapped[List["WalkRequest"]] = relationship(back_populates="owner")



class SystemLog(SAFRSBaseX, Base):
    """
    description: Logs actions and events in the system for auditing.
    """
    __tablename__ = 'system_log'
    _s_collection_name = 'SystemLog'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    action_desc = Column(String, nullable=False)
    timestamp = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class Walker(SAFRSBaseX, Base):
    """
    description: Represents a dog walker who can self-register and provide availability.
    """
    __tablename__ = 'walker'
    _s_collection_name = 'Walker'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    max_dogs_per_walk = Column(Integer, nullable=False)
    morning_available = Column(Boolean)
    afternoon_available = Column(Boolean)

    # parent relationships (access parent)

    # child relationships (access children)
    DogSizePriceHistoryList : Mapped[List["DogSizePriceHistory"]] = relationship(back_populates="walker")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="walker")
    WalkRequestList : Mapped[List["WalkRequest"]] = relationship(back_populates="walker")
    WalkerAvailabilityList : Mapped[List["WalkerAvailability"]] = relationship(back_populates="walker")
    WalkerHistoryList : Mapped[List["WalkerHistory"]] = relationship(back_populates="walker")
    WalkerPriceList : Mapped[List["WalkerPrice"]] = relationship(back_populates="walker")



class Dog(SAFRSBaseX, Base):
    """
    description: Represents a dog belonging to an owner.
    """
    __tablename__ = 'dog'
    _s_collection_name = 'Dog'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey('owner.id'), nullable=False)
    name = Column(String, nullable=False)
    breed = Column(String)
    size = Column(String(6), nullable=False)
    notes = Column(String)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("DogList"))

    # child relationships (access children)
    WalkRequestDogList : Mapped[List["WalkRequestDog"]] = relationship(back_populates="dog")



class DogSizePriceHistory(SAFRSBaseX, Base):
    """
    description: Maintains a history of price changes for dog sizes.
    """
    __tablename__ = 'dog_size_price_history'
    _s_collection_name = 'DogSizePriceHistory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walker_id = Column(ForeignKey('walker.id'), nullable=False)
    dog_size = Column(String(6), nullable=False)
    price = Column(Float, nullable=False)
    effective_date = Column(DateTime)

    # parent relationships (access parent)
    walker : Mapped["Walker"] = relationship(back_populates=("DogSizePriceHistoryList"))

    # child relationships (access children)



class Review(SAFRSBaseX, Base):
    """
    description: Stores reviews for walkers provided by owners.
    """
    __tablename__ = 'review'
    _s_collection_name = 'Review'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walker_id = Column(ForeignKey('walker.id'), nullable=False)
    owner_id = Column(ForeignKey('owner.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comments = Column(String)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("ReviewList"))
    walker : Mapped["Walker"] = relationship(back_populates=("ReviewList"))

    # child relationships (access children)



class WalkRequest(SAFRSBaseX, Base):
    """
    description: Records requests made by owners to walk their dogs.
    """
    __tablename__ = 'walk_request'
    _s_collection_name = 'WalkRequest'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey('owner.id'), nullable=False)
    walker_id = Column(ForeignKey('walker.id'), nullable=False)
    request_date = Column(DateTime)
    status = Column(String(9), nullable=False)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("WalkRequestList"))
    walker : Mapped["Walker"] = relationship(back_populates=("WalkRequestList"))

    # child relationships (access children)
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="walk_request")
    WalkRequestDogList : Mapped[List["WalkRequestDog"]] = relationship(back_populates="walk_request")



class WalkerAvailability(SAFRSBaseX, Base):
    """
    description: Represents the days a walker is available.
    """
    __tablename__ = 'walker_availability'
    _s_collection_name = 'WalkerAvailability'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walker_id = Column(ForeignKey('walker.id'), nullable=False)
    day_of_week = Column(String(3), nullable=False)

    # parent relationships (access parent)
    walker : Mapped["Walker"] = relationship(back_populates=("WalkerAvailabilityList"))

    # child relationships (access children)



class WalkerHistory(SAFRSBaseX, Base):
    """
    description: Tracks the walking history of a walker.
    """
    __tablename__ = 'walker_history'
    _s_collection_name = 'WalkerHistory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walker_id = Column(ForeignKey('walker.id'), nullable=False)
    walk_date = Column(DateTime)
    number_of_dogs = Column(Integer, nullable=False)

    # parent relationships (access parent)
    walker : Mapped["Walker"] = relationship(back_populates=("WalkerHistoryList"))

    # child relationships (access children)



class WalkerPrice(SAFRSBaseX, Base):
    """
    description: Stores pricing details for different dog sizes by each walker.
    """
    __tablename__ = 'walker_price'
    _s_collection_name = 'WalkerPrice'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walker_id = Column(ForeignKey('walker.id'), nullable=False)
    dog_size = Column(String(6), nullable=False)
    price = Column(Float, nullable=False)

    # parent relationships (access parent)
    walker : Mapped["Walker"] = relationship(back_populates=("WalkerPriceList"))

    # child relationships (access children)



class Payment(SAFRSBaseX, Base):
    """
    description: Represents payments made to walkers after a walk is completed.
    """
    __tablename__ = 'payment'
    _s_collection_name = 'Payment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walk_request_id = Column(ForeignKey('walk_request.id'), nullable=False)
    payment_date = Column(DateTime)
    amount = Column(Float, nullable=False)

    # parent relationships (access parent)
    walk_request : Mapped["WalkRequest"] = relationship(back_populates=("PaymentList"))

    # child relationships (access children)



class WalkRequestDog(SAFRSBaseX, Base):
    """
    description: Associates dogs with walk requests.
    """
    __tablename__ = 'walk_request_dog'
    _s_collection_name = 'WalkRequestDog'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walk_request_id = Column(ForeignKey('walk_request.id'), nullable=False)
    dog_id = Column(ForeignKey('dog.id'), nullable=False)

    # parent relationships (access parent)
    dog : Mapped["Dog"] = relationship(back_populates=("WalkRequestDogList"))
    walk_request : Mapped["WalkRequest"] = relationship(back_populates=("WalkRequestDogList"))

    # child relationships (access children)
