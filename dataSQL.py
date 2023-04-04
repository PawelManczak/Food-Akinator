from sqlalchemy import create_engine, Column, Integer, Boolean, String
from sqlalchemy.orm import declarative_base, sessionmaker

#to use this file you can call dh.serializeData(Dish) in main or serialize(self, Dish) in data.py
#to see results open https://sqliteonline.com/
#and in the left top corner choose file dishes.db, it is in the same folder as this file

def initialize():
    engine = create_engine('sqlite:///dishes.db')
    Session = sessionmaker(bind=engine)

    # Define the model
    Base = declarative_base()

    class DishModel(Base):
        __tablename__ = 'dishes'
        name = Column(String, primary_key=True)  # Add this line to define the "name" column
        sweet = Column(Boolean)
        sour = Column(Boolean)
        spicy = Column(Boolean)
        salty = Column(Boolean)
        umami = Column(Boolean)
        bitter = Column(Boolean)
        cheese = Column(Boolean)
        gluten_free = Column(Boolean)
        vegetarian = Column(Boolean)
        vegan = Column(Boolean)
        organic = Column(Boolean)
        cuisineAmerican = Column(Boolean)
        cuisineChinese = Column(Boolean)
        cuisineFrench = Column(Boolean)
        cuisineGreek = Column(Boolean)
        cuisineIndian = Column(Boolean)
        cuisineItalian = Column(Boolean)
        cuisineJapanese = Column(Boolean)
        cuisineKorean = Column(Boolean)
        cuisineMexican = Column(Boolean)
        cuisineMiddle_Eastern = Column(Boolean)
        cuisineRussian = Column(Boolean)
        cuisineThai = Column(Boolean)
        cuisineVietnamese = Column(Boolean)
        cuisineOther = Column(Boolean)
        fruity = Column(Boolean)
        nutty= Column(Boolean)
        herbal= Column(Boolean)
        floral= Column(Boolean)
        earthy= Column(Boolean)
        cheesy= Column(Boolean)
        creamy= Column(Boolean)
        smoky= Column(Boolean)
        savory= Column(Boolean)

    return engine, Session, Base, DishModel
def serialize(data_handler, Dish):

    # Set up the database connection
    engine, Session, Base, DishModel = initialize()

    Base.metadata.create_all(engine)
    session = Session()

    # Iterate over the dishes and add them to the database
    for name, dish in zip(data_handler.names, data_handler.dishes):
        existing_dish = session.query(DishModel).filter_by(name=name).first()
        if existing_dish:
            print(f"Dish {name} already exists in the database. Skipping.")
        else:
            print(f"Adding dish {name} to database")  # Add this line to check if the loop is executing
            dish_model = DishModel(name=name, **dict(zip(Dish.get_dish_variable_names(), dish)))
            session.add(dish_model)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()

def deserialize(data_handler, Dish):
    engine, session, Base, DishModel = initialize()
    Session = sessionmaker(bind=engine)
    # create a session object
    session = Session()


    for dish_model in session.query(DishModel).all():
        dish = Dish(
            sweet=dish_model.sweet,
            sour=dish_model.sour,
            spicy=dish_model.spicy,
            salty=dish_model.salty,
            umami=dish_model.umami,
            bitter=dish_model.bitter,
            cheese=dish_model.cheese,
            vegetarian=dish_model.vegetarian,
            cuisineAmerican=dish_model.cuisineAmerican,
            cuisineIndian=dish_model.cuisineIndian,
            cuisineItalian=dish_model.cuisineItalian,
            cuisineJapanese=dish_model.cuisineJapanese,
            cuisineMexican=dish_model.cuisineMexican,
            fish=dish_model.fish,
            tomato=dish_model.tomato,
            mostlyMeet=dish_model.mostlyMeet,
            pasta=dish_model.pasta
        )
        data_handler.add_dish(dish_model.name, dish)
        # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()