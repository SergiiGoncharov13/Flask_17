from sqlalchemy import create_engine, String, Float, Integer, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship, sessionmaker, DeclarativeBase
from typing import List

from configs import Config


# connection
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine, autoflush=False)


# create tables
class Base(DeclarativeBase):
    def create_db(self):
        Base.metadata.create_all(engine)

    def drop_db(self):
        Base.metadata.drop_all(engine)


class Product(Base):
    __tablename__='products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    description: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    image_filename: Mapped[str] = mapped_column(String(100), nullable=False)
    orders: Mapped[List['Orders']] = relationship('Orders', back_populates='product')


class Orders(Base):
    __tablename__='orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[str] = mapped_column(String(15), nullable=False)
    email: Mapped[str] = mapped_column(String(70), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'), nullable=False)
    product: Mapped['Product'] = relationship('Product', back_populates='orders')
    

def init_db():
    base = Base()
    base.create_db()

    with Session() as session:
        products = [
            Product(name='Nike Air Max', description='All day use', price=5500, image_filename='nike_air_max.png'),
            Product(name='Adidas ultraboost', description='The best boots in the world', price=7000, image_filename='adidas_ultraboost.png'),
            Product(name='Puma rsx', description='best use', price=7500, image_filename='puma_rsx.png')
        ]
        session.add_all(products)
        session.commit()


# create db, only ones
# init_db()

