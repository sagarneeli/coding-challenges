from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.orm.exc import NoResultFound

# Define the database engine (replace with your actual database details)
engine = create_engine(
    "your_database_connection_string"
)  # Example: 'mysql+mysqlconnector://user:password@host/database'

# Declarative base for ORM models
Base = declarative_base()


# User Model
class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    organizations = relationship(
        "Organization", secondary="UserOrganizations", back_populates="users"
    )


# Organization Model
class Organization(Base):
    __tablename__ = "Organizations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    users = relationship(
        "User", secondary="UserOrganizations", back_populates="organizations"
    )
    linodes = relationship("Linode", back_populates="organization")


# Linode Model
class Linode(Base):
    __tablename__ = "Linodes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    organization_id = Column(Integer, ForeignKey("Organizations.id"), nullable=False)
    ram_size = Column(Integer, default=512)
    disk_size = Column(Integer, default=2046)
    distribution = Column(String(255), default="Ubuntu")
    organization = relationship("Organization", back_populates="linodes")
    user = relationship(
        "User", secondary="LinodeUsers", back_populates="linodes"
    )  # Add relationship to User

    def __init__(
        self,
        organization_id,
        user_email,
        ram_size=512,
        disk_size=2046,
        distribution="Ubuntu",
        **kwargs,
    ):
        # Input Validation
        if not 64 <= ram_size <= 4096:
            raise ValueError("RAM size must be between 64 and 4096 MB")
        if not 256 <= disk_size <= 10240:
            raise ValueError("Disk size must be between 256 and 10240 MB")
        if distribution not in ["Ubuntu", "Debian", "CentOS", "Fedora"]:
            raise ValueError("Invalid distribution")

        # Check if the user belongs to the organization
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            user = session.query(User).filter_by(email=user_email).one()
            organization = (
                session.query(Organization).filter_by(id=organization_id).one()
            )
            if (user, organization) not in session.query(UserOrganizations).filter_by(
                user_id=user.id, organization_id=organization.id
            ).all():
                raise ValueError("User does not belong to the organization")
        except NoResultFound:
            raise ValueError("User or Organization not found")
        finally:
            session.close()

        # Initialize attributes
        super().__init__(
            organization_id=organization_id,
            ram_size=ram_size,
            disk_size=disk_size,
            distribution=distribution,
            **kwargs,
        )


# Association table for Linode and User (many-to-many)
LinodeUsers = Base.Table(
    "LinodeUsers",
    Base.Column("linode_id", ForeignKey("Linodes.id"), primary_key=True),
    Base.Column("user_id", ForeignKey("Users.id"), primary_key=True),
)

# Association table for User and Organization (many-to-many)
UserOrganizations = Base.Table(
    "UserOrganizations",
    Base.Column("user_id", ForeignKey("Users.id"), primary_key=True),
    Base.Column("organization_id", ForeignKey("Organizations.id"), primary_key=True),
)

# Create tables in the database
Base.metadata.create_all(engine)
