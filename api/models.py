from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.session import Base


class Reminder(Base):
    __tablename__ = 'reminders'
    id = Column(Integer, primary_key=True)
    time = Column(Integer, unique=True, comment='Time in seconds')


class Closer(Base):
    __tablename__ = 'closers'
    id = Column(Integer, primary_key=True)
    time = Column(Integer, unique=True, comment='Time in seconds')


class User(Base):
    __tablename__ = 'users'
    telegram_id = Column(BigInteger, nullable=False, primary_key=True)
    created_at = Column(DateTime)
    reminder_id = Column(Integer, ForeignKey('reminders.id'))
    reminder = relationship('Reminder')
    closer_id = Column(Integer, ForeignKey('closers.id'))
    closer = relationship('Closer')
    is_active = Column(Boolean, default=True)


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    telegram_id = Column(BigInteger, nullable=True)


class TimeSlot(Base):
    __tablename__ = 'time_slots'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, nullable=False, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category')
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    is_auto = Column(Boolean, default=True)
