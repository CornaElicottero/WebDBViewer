from typing import Optional, List

import strawberry
from sqlalchemy import or_, and_

from backend.sql_app import database, models as db_models


@strawberry.type
class Employees:
    employee_id: int
    employee_fio: str
    employee_position: str
    employee_phone_number: str


@strawberry.type
class Manufacturers:
    manufacturer_id: int
    manufacturer_name: str


@strawberry.type
class Models:
    model_id: int
    manufacturer_id: Manufacturers
    model_name: str


@strawberry.type
class Divisions:
    division_id: int
    division_mid_name: str
    division_code: str
    division_min_name: str
    division_full_name: str


@strawberry.type
class Locality:
    locality_id: int
    locality_name: str


@strawberry.type
class Streets:
    street_id: int
    street_name: str


@strawberry.type
class Subdivisions:
    subdivision_id: int
    subdivision_name: str


@strawberry.type
class NetworkMasks:
    mask_id: int
    mask: str


@strawberry.type
class VCSSystems:
    codec_id: int
    model: Models
    serial_number: str
    inventory_number: str
    start_year: str
    division: Divisions
    location: Locality
    street: Streets
    room: str
    used_by: Subdivisions
    e164: str
    h323id: str
    on_service: bool
    ip: str
    mask: NetworkMasks
    gateway: str
    building_number: str
    spisan: bool


@strawberry.type
class ResponsibleForCodecs:
    codec_id: VCSSystems
    employee_id: Employees


@strawberry.type
class Query:
    @strawberry.field
    def employees(self, employee_id: Optional[int] = None,
                  employee_fio: Optional[str] = None,
                  employee_position: Optional[str] = None,
                  employee_phone_number: Optional[str] = None,
                  employee_universal: Optional[str] = None) -> List[Employees]:
        db = database.SessionLocal()
        query = db.query(db_models.Employees)
        filters = []
        if employee_universal is not None:
            filters.append(db_models.Employees.employee_fio.like(f"%{employee_universal}%"))
            filters.append(db_models.Employees.employee_position.like(f"%{employee_universal}%"))
            filters.append(db_models.Employees.employee_phone_number.like(f"%{employee_universal}%"))
            return query.filter(or_(*filters))
        else:
            if employee_id is not None:
                filters.append(db_models.Employees.employee_id == employee_id)
            if employee_fio is not None:
                filters.append(db_models.Employees.employee_fio.like(f"%{employee_fio}%"))
            if employee_position is not None:
                filters.append(db_models.Employees.employee_position.like(f"%{employee_position}%"))
            if employee_phone_number is not None:
                filters.append(db_models.Employees.employee_phone_number(f"%{employee_phone_number}%"))
        if filters:
            query = query.filter(and_(*filters))
        return query.all()

    @strawberry.field
    def manufacturers(self, manufacturer_id: Optional[int] = None,
                      manufacturer_name: Optional[str] = None,
                      manufacturer_universal: Optional[str] = None) -> List[Manufacturers]:
        db = database.SessionLocal()
        query = db.query(db_models.Manufacturers)
        filters = []
        if manufacturer_universal is not None:
            filters.append(db_models.Manufacturers.manufacturer_name.like(f"%{manufacturer_universal}%"))
            return query.filter(or_(*filters))
        else:
            if manufacturer_id is not None:
                filters.append(db_models.Manufacturers.manufacturer_id == manufacturer_id)
            if manufacturer_name is not None:
                filters.append(db_models.Manufacturers.manufacturer_name.like(f"%{manufacturer_name}%"))
        if filters:
            query = query.filter(and_(*filters))
        return query.all()

    @strawberry.field
    def models(self, model_name: Optional[str] = None,
               model_id: Optional[int] = None,
               manufacturer_name: Optional[str] = None,
               models_universal: Optional[str] = None) -> List[Models]:
        db = database.SessionLocal()
        query = db.query(db_models.Models).join(db_models.Manufacturers)
        filters = []
        if models_universal is not None:
            filters.append(db_models.Models.model_name.like(f"%{models_universal}%"))
            filters.append(db_models.Models.model_name.like(f"%{models_universal}%"))
            query = query.filter(or_(*filters))
        else:
            if model_name is not None:
                filters.append(db_models.Models.model_name.like(f"%{model_name}%"))
            if model_id is not None:
                filters.append(db_models.Models.model_id == model_id)
            if manufacturer_name is not None:
                filters.append(db_models.Models.model_name.like(f"%{model_name}%"))
            if filters:
                query = query.filter(and_(*filters))

        results = query.all()

        models = [
            Models(
                model_id=result.model_id,
                manufacturer_id=Manufacturers(
                    manufacturer_id=result.manufacturer.manufacturer_id,
                    manufacturer_name=result.manufacturer.manufacturer_name
                ),
                model_name=result.model_name
            )
            for result in results
        ]

        return models

    @strawberry.field
    def divisions(self, division_id: Optional[int] = None,
                  division_mid_name: Optional[str] = None,
                  division_code: Optional[str] = None,
                  division_min_name: Optional[str] = None,
                  division_full_name: Optional[str] = None,
                  divisions_universal: Optional[str] = None) -> List[Divisions]:
        db = database.SessionLocal()
        query = db.query(db_models.Divisions)
        filters = []
        if divisions_universal is not None:
            filters.append(db_models.Divisions.division_mid_name.like(f"%{divisions_universal}%"))
            filters.append(db_models.Divisions.division_min_name.like(f"%{divisions_universal}%"))
            filters.append(db_models.Divisions.division_full_name.like(f"%{divisions_universal}%"))
            filters.append(db_models.Divisions.division_code.like(f"%{divisions_universal}%"))
            return query.filter(or_(*filters))
        else:
            if division_id is not None:
                filters.append(db_models.Divisions.division_id == division_id)
            if division_mid_name is not None:
                filters.append(db_models.Divisions.division_mid_name.like(f"%{division_mid_name}%"))
            if division_min_name is not None:
                filters.append(db_models.Divisions.division_min_name.like(f"%{division_min_name}%"))
            if division_full_name is not None:
                filters.append(db_models.Divisions.division_full_name.like(f"%{division_full_name}%"))
            if division_code is not None:
                filters.append(db_models.Divisions.division_code.like(f"%{division_code}%"))
        if filters:
            query = query.filter(and_(*filters))
        return query.all()

    @strawberry.field
    def locality(self, locality_id: Optional[int] = None,
                 locality_name: Optional[str] = None,
                 locality_universal: Optional[str] = None) -> List[Locality]:
        db = database.SessionLocal()
        query = db.query(db_models.Locality)
        filters = []
        if locality_universal is not None:
            filters.append(db_models.Locality.locality_name.like(f"%{locality_universal}%"))
            return query.filter(or_(*filters))
        else:
            if locality_id is not None:
                filters.append(db_models.Locality.locality_id == locality_id)
            if locality_name is not None:
                filters.append(db_models.Locality.locality_name.like(f"%{locality_name}%"))
        if filters:
            query = query.filter(and_(*filters))
        return query.all()

    @strawberry.field
    def streets(self, street_id: Optional[int] = None,
                street_name: Optional[str] = None,
                streets_universal: Optional[str] = None) -> List[Streets]:
        db = database.SessionLocal()
        query = db.query(db_models.Streets)
        filters = []
        if streets_universal is not None:
            filters.append(db_models.Streets.street_name.like(f"%{streets_universal}%"))
            return query.filter(or_(*filters))
        else:
            if street_id is not None:
                filters.append(db_models.Streets.street_id == street_id)
            if street_name is not None:
                filters.append(db_models.Streets.street_name.like(f"%{street_name}%"))
        if filters:
            query = query.filter(and_(*filters))
        return query.all()

    @strawberry.field
    def subdivisions(self, subdivision_id: Optional[int] = None,
                     subdivision_name: Optional[str] = None,
                     subdivisions_universal: Optional[str] = None) -> List[Subdivisions]:
        db = database.SessionLocal()
        query = db.query(db_models.Subdivisions)
        filters = []
        if subdivisions_universal is not None:
            filters.append(db_models.Subdivisions.subdivision_name.like(f"%{subdivisions_universal}%"))
            return query.filter(or_(*filters))
        else:
            if subdivision_id is not None:
                filters.append(db_models.Subdivisions.subdivision_id == subdivision_id)
            if subdivision_name is not None:
                filters.append(db_models.Subdivisions.subdivision_name.like(f"%{subdivision_name}%"))
        if filters:
            query = query.filter(and_(*filters))
        return query.all()

    @strawberry.field
    def network_masks(self, mask_id: Optional[int] = None,
                      mask: Optional[str] = None,
                      network_masks_universal: Optional[str] = None) -> List[NetworkMasks]:
        db = database.SessionLocal()
        query = db.query(db_models.NetworkMasks)
        filters = []
        if network_masks_universal is not None:
            filters.append(db_models.NetworkMasks.mask_name.like(f"%{network_masks_universal}%"))
            return query.filter(or_(*filters))
        else:
            if mask_id is not None:
                filters.append(db_models.NetworkMasks.mask_id == mask_id)
            if mask is not None:
                filters.append(db_models.NetworkMasks.mask_name.like(f"%{mask}%"))
        if filters:
            query = query.filter(and_(*filters))
        return query.all()

    @strawberry.field
    def vcs_systems(self, codec_id: Optional[int] = None,
                    serial_number: Optional[str] = None,
                    model_name: Optional[str] = None,
                    manufacturer_name: Optional[str] = None,
                    inventory_number: Optional[str] = None,
                    start_year: Optional[str] = None,
                    division_mid_name: Optional[str] = None,
                    division_code: Optional[str] = None,
                    division_min_name: Optional[str] = None,
                    division_full_name: Optional[str] = None,
                    locality_name: Optional[str] = None,
                    street_name: Optional[str] = None,
                    room: Optional[str] = None,
                    subdivision_name: Optional[str] = None,
                    e164: Optional[str] = None,
                    h323id: Optional[str] = None,
                    ip: Optional[str] = None,
                    mask: Optional[str] = None,
                    gateway: Optional[str] = None,
                    building_number: Optional[str] = None,
                    vcs_systems_universal: Optional[str] = None) -> List[VCSSystems]:
        db = database.SessionLocal()
        query = db.query(db_models.VCSSystems)\
            .join(db_models.Models)\
            .join(db_models.Manufacturers)\
            .join(db_models.Divisions)\
            .join(db_models.Streets)\
            .join(db_models.Locality)\
            .join(db_models.Subdivisions)\
            .join(db_models.NetworkMasks)
        filters = []
        if vcs_systems_universal is not None:
            filters.append(db_models.Models.model_name.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.Manufacturers.manufacturer_name.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.VCSSystems.serial_number.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.VCSSystems.inventory_number.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.VCSSystems.start_year.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.Divisions.division_mid_name.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.Divisions.division_min_name.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.Divisions.division_full_name.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.Divisions.division_code.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.Locality.locality_name.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.Streets.street_name.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.Subdivisions.subdivision_name.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.NetworkMasks.mask.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.VCSSystems.room.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.VCSSystems.e164.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.VCSSystems.h323id.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.VCSSystems.ip.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.VCSSystems.gateway.like(f"%{vcs_systems_universal}%"))
            filters.append(db_models.VCSSystems.building_number.like(f"%{vcs_systems_universal}%"))
            query = query.filter(or_(*filters))
        else:
            if codec_id is not None:
                filters.append(db_models.VCSSystems.codec_id == codec_id)
            if model_name is not None:
                filters.append(db_models.Models.model_name.like(f"%{model_name}%"))
            if manufacturer_name is not None:
                filters.append(db_models.Manufacturers.manufacturer_name.like(f"%{manufacturer_name}%"))
            if serial_number is not None:
                filters.append(db_models.VCSSystems.serial_number.like(f"%{serial_number}%"))
            if inventory_number is not None:
                filters.append(db_models.VCSSystems.inventory_number.like(f"%{inventory_number}%"))
            if start_year is not None:
                filters.append(db_models.VCSSystems.start_year.like(f"%{start_year}%"))
            if division_mid_name is not None:
                filters.append(db_models.Divisions.division_mid_name.like(f"%{division_mid_name}%"))
            if division_min_name is not None:
                filters.append(db_models.Divisions.division_min_name.like(f"%{division_min_name}%"))
            if division_full_name is not None:
                filters.append(db_models.Divisions.division_full_name.like(f"%{division_full_name}%"))
            if division_code is not None:
                filters.append(db_models.Divisions.division_code.like(f"%{division_code}%"))
            if locality_name is not None:
                filters.append(db_models.Locality.locality_name.like(f"%{locality_name}%"))
            if street_name is not None:
                filters.append(db_models.Streets.street_name.like(f"%{street_name}%"))
            if subdivision_name is not None:
                filters.append(db_models.Subdivisions.subdivision_name.like(f"%{subdivision_name}%"))
            if mask is not None:
                filters.append(db_models.NetworkMasks.mask.like(f"%{mask}%"))
            if room is not None:
                filters.append(db_models.VCSSystems.room.like(f"%{room}%"))
            if e164 is not None:
                filters.append(db_models.VCSSystems.e164.like(f"%{e164}%"))
            if h323id is not None:
                filters.append(db_models.VCSSystems.h323id.like(f"%{h323id}%"))
            if ip is not None:
                filters.append(db_models.VCSSystems.ip.like(f"%{ip}%"))
            if gateway is not None:
                filters.append(db_models.VCSSystems.gateway.like(f"%{gateway}%"))
            if building_number is not None:
                filters.append(db_models.VCSSystems.building_number.like(f"%{building_number}%"))
            if filters:
                query = query.filter(and_(*filters))

        results = query.all()

        vsc_systems = [
            VCSSystems(
                codec_id=result.codec_id,
                model=Models(
                    model_id=result.models.model_id,
                    model_name=result.models.model_name,
                    manufacturer_id=Manufacturers(
                        manufacturer_id=result.models.manufacturer.manufacturer_id,
                        manufacturer_name=result.models.manufacturer.manufacturer_name
                    )
                ),
                serial_number=result.serial_number,
                inventory_number=result.inventory_number,
                start_year=result.start_year,
                division=Divisions(
                    division_id=result.divisions.division_id,
                    division_mid_name=result.divisions.division_mid_name,
                    division_code=result.divisions.division_code,
                    division_min_name=result.divisions.division_min_name,
                    division_full_name=result.divisions.division_full_name
                ),
                location=Locality(
                    locality_id=result.locality.locality_id,
                    locality_name=result.locality.locality_name
                ),
                street=Streets(
                    street_id=result.streets.street_id,
                    street_name=result.streets.street_name
                ),
                room=result.room,
                used_by=Subdivisions(
                    subdivision_id=result.subdivisions.subdivision_id,
                    subdivision_name=result.subdivisions.subdivision_name
                ),
                e164=result.e164,
                h323id=result.h323id,
                on_service=result.on_service,
                ip=result.ip,
                mask=NetworkMasks(
                    mask_id=result.network_masks.mask_id,
                    mask=result.network_masks.mask
                ),
                gateway=result.gateway,
                building_number=result.building_number,
                spisan=result.spisan
            )
            for result in results
        ]

        return vsc_systems
