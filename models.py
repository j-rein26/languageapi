from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from database import Base


class Functions(Base):
    __tablename__ = "functions"
    id = Column(Integer, primary_key=True, index=True)
    english = Column(String, nullable=False)
    turkish = Column(String, nullable=False)
    examples = Column(Text, nullable=True)

class Sequences(Base):
    __tablename__ = "sequences"
    id = Column(Integer, primary_key=True, index=True)
    english = Column(String, nullable=False)
    turkish = Column(String, nullable=False)
    examples = Column(Text, nullable=True)

class RelatedActions(Base):
    __tablename__ = "related_actions"
    id = Column(Integer, primary_key=True, index=True)
    english = Column(String, nullable=False)
    turkish = Column(String, nullable=False)
    examples = Column(Text, nullable=True)

class Operations(Base):
    __tablename__ = "operations"
    id = Column(Integer, primary_key=True, index=True)
    english = Column(String, nullable=False)
    turkish = Column(String, nullable=False)
    examples = Column(Text, nullable=True)

class Topics(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True, index=True)
    english = Column(String, nullable=False)
    turkish = Column(String, nullable=False)
    examples = Column(Text, nullable=True)

class Places(Base):
    __tablename__ = "places"
    id = Column(Integer, primary_key=True, index=True)
    english = Column(String, nullable=False)
    turkish = Column(String, nullable=False)
    examples = Column(Text, nullable=True)

class Proverbs(Base):
    __tablename__ = "proverbs"
    id = Column(Integer, primary_key=True, index=True)
    english = Column(String, nullable=False)
    turkish = Column(String, nullable=False)
    examples = Column(Text, nullable=True)