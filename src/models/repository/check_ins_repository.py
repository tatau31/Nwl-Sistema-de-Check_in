from src.models.settings.connection import db_connection_handler
from src.models.entitites.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError
from src.errors.error_types.http_conflict import HttpClonflictError


class CheckInRepository:
    def insert_check_in(self, attendee_id):
        with db_connection_handler as database:
            try:
                check_in = (
                    CheckIns(
                        attendeeId=attendee_id
                    )
                )
                database.session.add(check_in)
                database.session.commit()
                return attendee_id
            except IntegrityError:
                raise HttpClonflictError('Check In  ja cadastrado!')
            except Exception as exception:
                database.session.rollback()
                raise exception