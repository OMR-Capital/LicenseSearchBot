from odetam.async_model import AsyncDetaModel


class MessagesPackage(AsyncDetaModel):
    chat_id: int
    messages_ids: list[int]

    class Config:
        table_name = 'messages_packages'