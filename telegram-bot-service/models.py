from sqlalchemy import Column, Integer, String, DateTime, func
from orchestrator_bot.database import Base


class UserToken(Base):
    __tablename__ = "user_tokens"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)  # Telegram ID или что-то ещё
    service = Column(String, index=True)  # "github", "trello" и т.п.
    token = Column(String)

class ActionHistory(Base):
    __tablename__ = "action_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    action_type = Column(String)
    details = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())