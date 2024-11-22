from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class B_size(Base):
    __tablename__ = "size_table"
    b_size: Mapped[str] = mapped_column(primary_key=True)
    help: Mapped["Common_table"] = mapped_column(ForeignKey("common.help"))

    def __repr__(self) -> str:
        return f"B_size(b_size={self.b_size!r}, help={self.help!r})"

class Common_table(Base):
    __tablename__ = "common"
    help: Mapped[str] = mapped_column(primary_key=True)
    b_size: Mapped["B_size"] = mapped_column(ForeignKey("size_table.b_size"))

    def __repr__(self) -> str:
        return f"Common(help={self.help!r}, b_size={self.b_size!r})"