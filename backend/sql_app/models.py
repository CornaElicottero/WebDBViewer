from sqlalchemy import CHAR, Column, VARCHAR, INTEGER, ForeignKey, BOOLEAN
from sqlalchemy.orm import relationship

from backend.sql_app.database import Base, engine, SessionLocal


class Employees(Base):
    __tablename__ = "employees"
    __table_args__ = {'extend_existing': True}
    employee_id = Column(INTEGER, primary_key=True, nullable=False, index=True)
    employee_fio = Column(VARCHAR, nullable=False)
    employee_position = Column(VARCHAR, nullable=False)
    employee_phone_number = Column(VARCHAR, nullable=False)

class ResponsibleForCodecs(Base):
    __tablename__ = "responsible_for_codecs"
    __table_args__ = {'extend_existing': True}
    responsible_for_codecs_id = Column(INTEGER, primary_key=True, nullable=False, index=True)
    codec_id = Column(ForeignKey("vcs_systems.codec_id"))
    employee_id = Column(ForeignKey("employees.employee_id"))


class Manufacturers(Base):
    __tablename__ = "manufacturers"
    __table_args__ = {'extend_existing': True}
    manufacturer_id = Column(INTEGER, primary_key=True, nullable=True, index=True)
    manufacturer_name = Column(VARCHAR, nullable=False)


class Divisions(Base):
    __tablename__ = "divisions"
    __table_args__ = {'extend_existing': True}
    division_id = Column(INTEGER, primary_key=True, nullable=False, index=True)
    division_mid_name = Column(VARCHAR, nullable=False)
    division_code = Column(VARCHAR, nullable=False)
    division_min_name = Column(VARCHAR, nullable=False)
    division_full_name = Column(VARCHAR, nullable=False)


class Locality(Base):
    __tablename__ = "locality"
    __table_args__ = {'extend_existing': True}
    locality_id = Column(INTEGER, primary_key=True, nullable=False, index=True)
    locality_name = Column(VARCHAR, nullable=False)


class Streets(Base):
    __tablename__ = "streets"
    __table_args__ = {'extend_existing': True}
    street_id = Column(INTEGER, primary_key=True, nullable=False, index=True)
    street_name = Column(VARCHAR, nullable=False)


class Subdivisions(Base):
    __tablename__ = "subdivisions"
    __table_args__ = {'extend_existing': True}
    subdivision_id = Column(INTEGER, primary_key=True, nullable=False, index=True)
    subdivision_name = Column(VARCHAR, nullable=False)


class NetworkMasks(Base):
    __tablename__ = "network_masks"
    __table_args__ = {'extend_existing': True}
    mask_id = Column(INTEGER, primary_key=True, nullable=False, index=True)
    mask = Column(VARCHAR, nullable=False)

class Models(Base):
    __tablename__ = "models"
    __table_args__ = {'extend_existing': True}
    model_id = Column(INTEGER, primary_key=True, nullable=False, index=True)
    manufacturer_id = Column(ForeignKey("manufacturers.manufacturer_id"))
    model_name = Column(VARCHAR, nullable=False)

    manufacturer = relationship(Manufacturers, backref="models")


class VCSSystems(Base):
    __tablename__ = "vcs_systems"
    __table_args__ = {'extend_existing': True}
    codec_id = Column(INTEGER, primary_key=True, nullable=False, index=True)
    model = Column(ForeignKey("models.model_id"))
    serial_number = Column(VARCHAR, nullable=False)
    inventory_number = Column(VARCHAR, nullable=False)
    start_year = Column(VARCHAR, nullable=False)
    division = Column(ForeignKey("divisions.division_id"))
    location = Column(ForeignKey("locality.locality_id"))
    street = Column(ForeignKey("streets.street_id"))
    room = Column(VARCHAR, nullable=False)
    used_by = Column(ForeignKey("subdivisions.subdivision_id"))
    e164 = Column(VARCHAR, nullable=False)
    h323id = Column(VARCHAR, nullable=False)
    on_service = Column(BOOLEAN, nullable=False)
    ip = Column(VARCHAR, nullable=False)
    mask = Column(ForeignKey("network_masks.mask_id"))
    gateway = Column(VARCHAR, nullable=False)
    building_number = Column(VARCHAR, nullable=False)
    spisan = Column(BOOLEAN, nullable=False)

    models = relationship(Models, backref="vcs_systems")
    divisions = relationship(Divisions, backref="vcs_systems")
    locality = relationship(Locality, backref="vcs_systems")
    streets = relationship(Streets, backref="vcs_systems")
    subdivisions = relationship(Subdivisions, backref="vcs_systems")
    network_masks = relationship(NetworkMasks, backref="vcs_systems")

if __name__ == "__main__":
    # Base.metadata.create_all(bind=engine)
    Session = SessionLocal()
    new_employee = Employees(
        employee_fio="Кизириди Игорь Георгиевич",
        employee_position="Директор интернета",
        employee_phone_number="88005553535"
    )
    Session.add(new_employee)
    new_manufacturer = Manufacturers(
        manufacturer_name="Zamzung"
    )
    Session.add(new_manufacturer)
    new_model = Models(
        model_name="Galaxy G3",
        manufacturer_id=1
    )
    Session.add(new_model)
    new_division = Divisions(
        division_mid_name="ЧД",
        division_code="123321",
        division_min_name="ООО ЧД",
        division_full_name="ООО ЛТД ЧД"
    )
    Session.add(new_division)
    new_locality = Locality(
        locality_name="Сургут"
    )
    Session.add(new_locality)
    new_street = Streets(
        street_name="Чехова"
    )
    Session.add(new_street)
    new_subdivision = Subdivisions(
        subdivision_name="ИСИТ"
    )
    Session.add(new_subdivision)
    new_network_masks = NetworkMasks(
        mask="123.123.123.123"
    )
    Session.add(new_network_masks)
    new_vcs_systems = VCSSystems(
        model=1,
        serial_number="1234АЫА",
        inventory_number="1243124",
        start_year="123412",
        division=1,
        location=1,
        street=1,
        room="14dfasf",
        used_by=1,
        e164="124",
        h323id="wad1d31",
        on_service=True,
        ip="123.0.0.1",
        mask=1,
        gateway="124.421",
        building_number="213421",
        spisan=False
    )
    Session.add(new_vcs_systems)
    Session.commit()