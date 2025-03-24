from sqlalchemy import create_engine, String, Float, Integer, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship, sessionmaker, DeclarativeBase



engine = create_engine('sqlite:///flask_images.db')
Session = sessionmaker(bind=engine, autocommit=False)


class Base(DeclarativeBase):
    pass


class UserFiles(Base):
    __tablename__ = 'users_images'
    id : Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str] = mapped_column(String(70), nullable=False, unique=True)
    file_description: Mapped[str] = mapped_column(String(255), nullable=False)



def create_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    create_db()

